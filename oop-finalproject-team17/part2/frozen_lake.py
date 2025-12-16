import gymnasium as gym
import numpy as np
import pickle
import matplotlib.pyplot as plt
from typing import Tuple, Optional


class EnhancedQLearningAgent:

    def __init__(
        self,
        env: gym.Env,
        learning_rate: float = 0.3,  
        discount_factor: float = 0.999,
        min_exploration_rate: float = 0.001,
        epsilon_decay_rate: float = 0.00015,  
        initial_epsilon: float = 1.0,
        random_seed: Optional[int] = None,
        optimistic_init: float = 7.0,  
        exploration_bonus_coef: float = 0.2,  
        temperature: float = 2.0  
    ):
        self.env = env
        self.learning_rate = learning_rate
        self.initial_lr = learning_rate
        self.discount_factor = discount_factor
        self.min_exploration_rate = min_exploration_rate
        self.epsilon_decay_rate = epsilon_decay_rate
        self.epsilon = initial_epsilon
        self.random_seed = random_seed
        self.exploration_bonus_coef = exploration_bonus_coef
        self.temperature = temperature
        self.initial_temp = temperature
        
        # OPTIMISTIC INITIALIZATION
        self.q_table = np.full((env.observation_space.n, env.action_space.n), optimistic_init)
        
        # COUNT-BASED EXPLORATION
        self.visit_counts = np.zeros((env.observation_space.n, env.action_space.n))
        self.state_visits = np.zeros(env.observation_space.n)

        if random_seed is not None:
            self.rng = np.random.default_rng(random_seed)
        else:
            self.rng = np.random.default_rng()
            
        self.n_rows = 8
        self.n_cols = 8
        self.max_distance = 14
        
    def get_manhattan_distance(self, state: int) -> int:
        row = state // self.n_cols
        col = state % self.n_cols
        return abs(7 - row) + abs(7 - col)

    def get_potential(self, state: int) -> float:
        dist = self.get_manhattan_distance(state)
        return 1.0 - (dist / self.max_distance)
    
    def get_exploration_bonus(self, state: int, action: int) -> float:
        # Enhanced UCB-style bonus.
        count = self.visit_counts[state, action]
        state_count = max(self.state_visits[state], 1)
        
        # UCB-inspired: bonus = c * sqrt(log(N(s)) / N(s,a))
        ucb_bonus = self.exploration_bonus_coef * np.sqrt(np.log(state_count + 1) / (count + 1))
        return ucb_bonus

    def select_action_softmax(self, state: int) -> int:
        #Softmax (Boltzmann) action selection.
        q_values = self.q_table[state, :]
        
        # Add small noise to break ties
        q_values = q_values + self.rng.normal(0, 0.01, size=4)
        
        # Softmax with temperature
        exp_q = np.exp((q_values - np.max(q_values)) / self.temperature)
        probs = exp_q / np.sum(exp_q)
        
        return self.rng.choice(4, p=probs)
    
    def select_action(self, state: int, is_training: bool = True, use_softmax: bool = False) -> int:
        if is_training:
            if use_softmax:
                return self.select_action_softmax(state)
            elif self.rng.random() < self.epsilon:
                return self.env.action_space.sample()
            else:
                return np.argmax(self.q_table[state, :])
        else:
            return np.argmax(self.q_table[state, :])
    
    def update(self, state: int, action: int, reward: float, next_state: int) -> None:
        self.visit_counts[state, action] += 1
        self.state_visits[state] += 1
        
        exploration_bonus = self.get_exploration_bonus(next_state, np.argmax(self.q_table[next_state, :]))
        
        current_q = self.q_table[state, action]
        max_next_q = np.max(self.q_table[next_state, :])
        
        target = reward + exploration_bonus + self.discount_factor * max_next_q
        self.q_table[state, action] = current_q + self.learning_rate * (target - current_q)
    
    def decay_epsilon(self) -> None:
        self.epsilon = max(self.epsilon - self.epsilon_decay_rate, self.min_exploration_rate)
    
    def decay_temperature(self) -> None:
        #Decay temperature for softmax.
        self.temperature = max(self.temperature * 0.9995, 0.1)
    
    def train(
        self, 
        num_episodes: int,
        max_steps_per_episode: int = 200,
        shaping_scale: float = 2.0,  
        step_penalty: float = -0.004,  
        polish_phase: bool = True
    ) -> Tuple[np.ndarray, np.ndarray]:
        # Train with polish phase.
        rewards_per_episode = np.zeros(num_episodes)
        
        for episode in range(num_episodes):
            # Adaptive learning rate
            progress = episode / num_episodes
            if progress > 0.7:
                self.learning_rate = self.initial_lr * 0.6
            elif progress > 0.9:
                self.learning_rate = self.initial_lr * 0.3
            
            state, _ = self.env.reset()
            terminated = False
            truncated = False
            steps = 0
            
            # Use softmax in first 30% of training
            use_softmax = (episode < num_episodes * 0.3)
            
            while not terminated and not truncated and steps < max_steps_per_episode:
                action = self.select_action(state, is_training=True, use_softmax=use_softmax)
                next_state, raw_reward, terminated, truncated, _ = self.env.step(action)
                
                # Strong reward shaping
                current_potential = self.get_potential(state)
                next_potential = self.get_potential(next_state)
                shaping = (self.discount_factor * next_potential - current_potential) * shaping_scale
                
                modified_reward = raw_reward + shaping + step_penalty
                self.update(state, action, modified_reward, next_state)
                
                state = next_state
                steps += 1
            
            if raw_reward == 1.0:
                rewards_per_episode[episode] = 1
            
            self.decay_epsilon()
            self.decay_temperature()
        
        # Calculate moving average
        moving_avg = self._calculate_moving_average(rewards_per_episode, window=100)
        
        return rewards_per_episode, moving_avg
    
    def polish(self, num_episodes: int, shaping_scale: float = 2.0, step_penalty: float = -0.004) -> Tuple[np.ndarray, np.ndarray]:
        """Polish phase: Fine-tune with minimal exploration (3,000 episodes)."""
        self.epsilon = 0.02  # Minimal exploration
        
        rewards_per_episode = np.zeros(num_episodes)
        
        for episode in range(num_episodes):
            state, _ = self.env.reset()
            terminated = False
            truncated = False
            steps = 0
            
            while not terminated and not truncated and steps < 200:
                action = self.select_action(state, is_training=True)
                next_state, raw_reward, terminated, truncated, _ = self.env.step(action)
                
                current_potential = self.get_potential(state)
                next_potential = self.get_potential(next_state)
                shaping = (self.discount_factor * next_potential - current_potential) * shaping_scale
                
                modified_reward = raw_reward + shaping + step_penalty
                self.update(state, action, modified_reward, next_state)
                
                state = next_state
                steps += 1
            
            if raw_reward == 1.0:
                rewards_per_episode[episode] = 1
        
        self.epsilon = 0.0  # Pure exploitation after polish
        moving_avg = self._calculate_moving_average(rewards_per_episode, window=100)
        
        return rewards_per_episode, moving_avg
    
    
    def evaluate(self, num_episodes: int = 1000) -> Tuple[float, int]:
        original_epsilon = self.epsilon
        self.epsilon = 0.0
        success_count = 0
        
        for _ in range(num_episodes):
            state, _ = self.env.reset()
            terminated = False
            truncated = False
            
            while not terminated and not truncated:
                action = self.select_action(state, is_training=False)
                state, reward, terminated, truncated, _ = self.env.step(action)
            
            if reward == 1.0:
                success_count += 1
        
        self.epsilon = original_epsilon
        return (success_count / num_episodes) * 100, success_count
    
    def _calculate_moving_average(self, rewards: np.ndarray, window: int = 100) -> np.ndarray:
        #Calculate moving average of rewards.
        moving_avg = np.zeros(len(rewards))
        for i in range(len(rewards)):
            start_idx = max(0, i - window + 1)
            moving_avg[i] = np.mean(rewards[start_idx:i+1])
        return moving_avg
    
    def save_model(self, filepath: str) -> None:
        with open(filepath, 'wb') as f:
            pickle.dump(self.q_table, f)
    
    def plot_training_progress(self, rewards: np.ndarray, moving_avg: np.ndarray, save_path: str = "training_progress.png") -> None:
        # Plot training progress with moving average.
        plt.figure(figsize=(12, 6))
        
        # Plot raw rewards (episodes where agent succeeded)
        episodes = np.arange(len(rewards))
        success_episodes = episodes[rewards == 1]
        
        # Plot moving average
        plt.plot(episodes, moving_avg * 100, 'b-', linewidth=2, label=f'Moving Average (window=100)')
        
        # Mark successful episodes
        plt.scatter(success_episodes, np.ones(len(success_episodes)) * 100, 
                   c='green', s=10, alpha=0.3, label='Success')
        
        plt.xlabel('Episode', fontsize=12)
        plt.ylabel('Success Rate (%)', fontsize=12)
        plt.title('Training Progress: 8x8 Frozen Lake', fontsize=14, fontweight='bold')
        plt.legend(loc='lower right', fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.ylim(-5, 105)
        
        # Add horizontal line at 70% target
        plt.axhline(y=70, color='r', linestyle='--', linewidth=1.5, label='Target (70%)', alpha=0.7)
        plt.legend(loc='lower right', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Training plot saved to: {save_path}")
        plt.close()


class EnhancedAgentTrainer:
    # Train 30 optimized agents.
    def __init__(self, env: gym.Env):
        self.env = env
    
    def _calculate_combined_moving_avg(self, rewards: np.ndarray, window: int = 100) -> np.ndarray:
        # Calculate moving average for combined training + polish rewards.
        moving_avg = np.zeros(len(rewards))
        for i in range(len(rewards)):
            start_idx = max(0, i - window + 1)
            moving_avg[i] = np.mean(rewards[start_idx:i+1])
        return moving_avg
    
    def train_and_select_best(
        self,
        num_agents: int = 30,
        num_episodes: int = 15000,
        validation_episodes: int = 500
    ) -> EnhancedQLearningAgent:
        print(f"\n{'='*60}")
        print(f"ENHANCED MODEL: TRAINING {num_agents} AGENTS")
        print(f"{'='*60}")
        print(f"Key Features:")
        print(f"  - Optimistic Initialization: 7.0")
        print(f"  - UCB-Based Exploration Bonus: 0.2")
        print(f"  - Softmax Action Selection (early phase)")
        print(f"  - Adaptive Learning Rate (0.3 → decay)")
        print(f"  - Strong Reward Shaping: 2.0")
        print(f"  - Training: 12,000 episodes")
        print(f"  - Polish Phase: 3,000 episodes")
        print(f"  - Total: 15,000 episodes")
        print(f"{'='*60}\n")
        
        best_agent = None
        best_score = 0
        best_rewards = None
        best_moving_avg = None
        
        for i in range(num_agents):
            agent = EnhancedQLearningAgent(
                env=self.env,
                learning_rate=0.3,
                epsilon_decay_rate=0.00015,
                optimistic_init=7.0,
                exploration_bonus_coef=0.2,
                temperature=2.0,
                random_seed=i
            )
            
            # Main training: 12,000 episodes
            rewards, moving_avg = agent.train(
                12000,  # 12k episodes
                max_steps_per_episode=200,
                shaping_scale=2.0,
                step_penalty=-0.004
            )
            
            # Polish phase: 3,000 episodes (total = 15,000)
            polish_rewards, polish_avg = agent.polish(
                3000,  # 3k episodes
                shaping_scale=2.0,
                step_penalty=-0.004
            )
            
            # Combine rewards for full training history
            all_rewards = np.concatenate([rewards, polish_rewards])
            
            score, _ = agent.evaluate(validation_episodes)
            
            print(f"Agent {i+1}/{num_agents}: {score:.2f}%", end="")
            
            if score > best_score:
                best_score = score
                best_agent = agent
                best_rewards = all_rewards  # Use combined 15k episodes
                best_moving_avg = self._calculate_combined_moving_avg(all_rewards)
                print(f" ★ NEW BEST!")
            else:
                print()
            
            if best_score >= 70.0:
                print(f"\n{'='*60}")
                print("★★★ TARGET >70% ACHIEVED! ★★★")
                print(f"{'='*60}\n")
                break
        
        print(f"\n{'='*60}")
        print("BEST AGENT SELECTED")
        print(f"{'='*60}")
        print(f"Best Validation: {best_score:.2f}%")
        print(f"{'='*60}\n")
        
        return best_agent, best_rewards, best_moving_avg


def main():
    print("="*60)
    print("ENHANCED Q-LEARNING AGENT")
    print("="*60)
    print("Algorithm Enhancements:")
    print("  • Optimistic Initialization: 7.0")
    print("  • UCB-Based Exploration Bonus: 0.2")
    print("  • Softmax Action Selection (early phase)")
    print("  • Adaptive Learning Rate (0.3 → decay)")
    print("  • Reward Shaping Coefficient: 2.0")
    print("  • Training: 12,000 + Polish: 3,000 = 15,000 total")
    print("  • Ensemble Size: 30 agents")
    print("="*60 + "\n")
    
    env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True)
    
    selector = EnhancedAgentTrainer(env)
    best_agent, rewards, moving_avg = selector.train_and_select_best(
        num_agents=30,
        num_episodes=15000,
        validation_episodes=500
    )
    
    # Plot training progress
    print("Generating training plot...")
    best_agent.plot_training_progress(rewards, moving_avg, "training_curve.png")
    
    print("Final Evaluation (1000 episodes)...")
    success_rate, success_count = best_agent.evaluate(1000)
    
    best_agent.save_model("frozen_lake_enhanced_8x8.pkl")
    
    print(f"\n{'='*60}")
    print("FINAL RESULTS (ENHANCED MODEL)")
    print(f"{'='*60}")
    print(f"Success Rate: {success_rate:.2f}% ({success_count}/1000)")
    
    if success_rate >= 70:
        print("★★★ SUCCESS: Target >70% ACHIEVED! ★★★")
    else:
        print(f"Result: {success_rate:.2f}%")
    
    print(f"Model saved: frozen_lake_enhanced_8x8.pkl")
    print(f"{'='*60}\n")
    
    env.close()
    return success_rate


if __name__ == "__main__":
    final_rate = main()

    input("Press Enter to exit...")  # 🔹防止視窗一跑完就關掉
    #run(10, is_training=False, render=True)
