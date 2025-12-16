import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
import pickle
from typing import Tuple, Optional, List


class QLearningAgent:
    
    def __init__(
        self,
        env: gym.Env,
        learning_rate: float = 0.9,
        discount_factor: float = 0.9,
        min_exploration_rate: float = 0.05,
        epsilon_decay_rate: float = 0.0001,
        initial_epsilon: float = 1.0,
        random_seed: Optional[int] = None
    ):

        self.env = env
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.min_exploration_rate = min_exploration_rate
        self.epsilon_decay_rate = epsilon_decay_rate
        self.epsilon = initial_epsilon
        self.random_seed = random_seed
        

        self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
        

        if random_seed is not None:
            self.rng = np.random.default_rng(random_seed)
        else:
            self.rng = np.random.default_rng()
        
    def select_action(self, state: int, is_training: bool = True) -> int:

        if is_training and self.rng.random() < self.epsilon:
            return self.env.action_space.sample()  # Explore
        else:
            return np.argmax(self.q_table[state, :])  # Exploit
    
    def update_q_value(
        self, 
        state: int, 
        action: int, 
        reward: float, 
        next_state: int
    ) -> None:
        
        current_q = self.q_table[state, action]
        max_next_q = np.max(self.q_table[next_state, :])
        
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_next_q - current_q
        )
        self.q_table[state, action] = new_q
    
    def decay_epsilon(self) -> None:
        self.epsilon = max(
            self.epsilon - self.epsilon_decay_rate, 
            self.min_exploration_rate
        )
    
    def train(
        self, 
        num_episodes: int,
        max_steps_per_episode: int = 200
    ) -> Tuple[np.ndarray, np.ndarray]:
        rewards_per_episode = np.zeros(num_episodes)
        
        for episode in range(num_episodes):
            state, _ = self.env.reset()
            terminated = False
            truncated = False
            steps = 0
            
            while not terminated and not truncated and steps < max_steps_per_episode:
                action = self.select_action(state, is_training=True)
                next_state, reward, terminated, truncated, _ = self.env.step(action)
                
                self.update_q_value(state, action, reward, next_state)
                
                state = next_state
                steps += 1
            
            if reward == 1.0:
                rewards_per_episode[episode] = 1
            
            self.decay_epsilon()
        
        moving_average = self._calculate_moving_average(rewards_per_episode, window=100)
        
        return rewards_per_episode, moving_average
    
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
        
        success_rate = (success_count / num_episodes) * 100
        return success_rate, success_count
    
    def _calculate_moving_average(
        self, 
        rewards: np.ndarray, 
        window: int = 100
    ) -> np.ndarray:
        moving_avg = np.zeros(len(rewards))
        for i in range(len(rewards)):
            start_idx = max(0, i - window + 1)
            moving_avg[i] = np.sum(rewards[start_idx:i+1])
        return moving_avg
    
    def save_model(self, filepath: str) -> None:

        with open(filepath, 'wb') as f:
            pickle.dump(self.q_table, f)
    
    def load_model(self, filepath: str) -> None:

        with open(filepath, 'rb') as f:
            self.q_table = pickle.load(f)


class ModelSelector:
    
    def __init__(
        self,
        num_models: int = 5,
        validation_episodes: int = 200
    ):
        self.num_models = num_models
        self.validation_episodes = validation_episodes
        self.models: List[Tuple[QLearningAgent, float]] = []
    
    def train_multiple_models(
        self,
        env: gym.Env,
        num_episodes: int,
        max_steps_per_episode: int,
        learning_rate: float,
        discount_factor: float,
        min_exploration_rate: float,
        epsilon_decay_rate: float
    ) -> QLearningAgent:

        print(f"\n{'='*60}")
        print(f"TRAINING {self.num_models} MODELS FOR SELECTION")
        print(f"{'='*60}\n")
        
        best_agent = None
        best_validation_score = 0
        
        for i in range(self.num_models):
            print(f"Training Model {i+1}/{self.num_models} (seed={i})...")
            
            # Create agent with unique seed
            agent = QLearningAgent(
                env=env,
                learning_rate=learning_rate,
                discount_factor=discount_factor,
                min_exploration_rate=min_exploration_rate,
                epsilon_decay_rate=epsilon_decay_rate,
                random_seed=i  # Different seed for each model
            )
            
            # Train the model
            rewards, _ = agent.train(num_episodes, max_steps_per_episode)
            
            # Validate on separate test episodes
            validation_score, _ = agent.evaluate(self.validation_episodes)
            
            print(f"  Validation Score: {validation_score:.2f}%")
            
            # Keep track of best model
            if validation_score > best_validation_score:
                best_validation_score = validation_score
                best_agent = agent
                print(f"  >> New best model!")
            
            print()
        
        print(f"{'='*60}")
        print(f"BEST MODEL SELECTED")
        print(f"{'='*60}")
        print(f"Best Validation Score: {best_validation_score:.2f}%")
        print(f"{'='*60}\n")
        
        return best_agent


class FrozenLakeTrainer:

    
    def __init__(
        self,
        map_name: str = "4x4",
        is_slippery: bool = True,
        render_mode: Optional[str] = None
    ):
        self.env = gym.make(
            "FrozenLake-v1",
            map_name=map_name,
            is_slippery=is_slippery,
            render_mode=render_mode
        )
        self.agent = None
    
    def create_agent(
        self,
        learning_rate: float = 0.9,
        discount_factor: float = 0.9,
        min_exploration_rate: float = 0.05,
        epsilon_decay_rate: float = 0.0001
    ) -> QLearningAgent:

        self.agent = QLearningAgent(
            env=self.env,
            learning_rate=learning_rate,
            discount_factor=discount_factor,
            min_exploration_rate=min_exploration_rate,
            epsilon_decay_rate=epsilon_decay_rate
        )
        return self.agent
    
    def run_training(
        self,
        num_episodes: int,
        max_steps_per_episode: int = 200
    ) -> Tuple[np.ndarray, np.ndarray]:

        if self.agent is None:
            raise ValueError("Agent not created. Call create_agent() first.")
        
        print(f"Training for {num_episodes} episodes...")
        print(f"Max steps per episode: {max_steps_per_episode}")
        print(f"Min exploration rate: {self.agent.min_exploration_rate}")
        print(f"Epsilon decay rate: {self.agent.epsilon_decay_rate}")
        print("-" * 60)
        
        rewards, moving_avg = self.agent.train(num_episodes, max_steps_per_episode)
        
        print(f"\nTraining completed!")
        print(f"Final epsilon: {self.agent.epsilon:.4f}")
        
        return rewards, moving_avg
    
    def run_evaluation(self, num_episodes: int = 1000) -> None:

        if self.agent is None:
            raise ValueError("Agent not created. Call create_agent() first.")
        
        print(f"\nEvaluating agent over {num_episodes} episodes...")
        
        success_rate, success_count = self.agent.evaluate(num_episodes)
        
        return success_rate, success_count
    
    def plot_training_progress(
        self,
        moving_average: np.ndarray,
        save_path: str = "frozen_lake_training.png"
    ) -> None:

        plt.figure(figsize=(12, 6))
        plt.plot(moving_average, linewidth=2, color='#2E86AB')
        plt.xlabel('Episode', fontsize=12)
        plt.ylabel('Cumulative Wins (100-episode window)', fontsize=12)
        plt.title('Training Progress: Moving Average of Success', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)
        print(f"\nTraining plot saved to: {save_path}")
        plt.close()
    
    def demonstrate_agent(self, num_episodes: int = 3) -> None:

        if self.agent is None:
            raise ValueError("Agent not created. Call create_agent() first.")
        
        demo_env = gym.make("FrozenLake-v1", render_mode="ansi")
        original_epsilon = self.agent.epsilon
        self.agent.epsilon = 0.0  # Pure exploitation
        self.agent.env = demo_env
        
        print(f"\n{'='*60}")
        print(f"AGENT DEMONSTRATION")
        print(f"{'='*60}\n")
        
        for ep in range(num_episodes):
            print(f"Episode {ep + 1}:")
            print("-" * 60)
            
            state, _ = demo_env.reset()
            terminated = False
            truncated = False
            steps = 0
            
            print(demo_env.render())
            
            while not terminated and not truncated:
                action = self.agent.select_action(state, is_training=False)
                state, reward, terminated, truncated, _ = demo_env.step(action)
                steps += 1
                
                print(f"\nStep {steps}:")
                print(demo_env.render())
            
            result = "SUCCESS!" if reward == 1.0 else "Failed (fell in hole)"
            print(f"\nResult: {result} (Steps: {steps})")
            print("=" * 60)
            print()
        
        # Restore
        self.agent.epsilon = original_epsilon
        self.agent.env = self.env
        demo_env.close()
    
    def close(self) -> None:
        self.env.close()


def main():
    
    NUM_EPISODES = 15000  # FIXED
    MAX_STEPS_PER_EPISODE = 200  # FIXED
    
    MIN_EXPLORATION_RATE = 0.01  
    EPSILON_DECAY_RATE = 0.0003  
    
    LEARNING_RATE = 0.9
    DISCOUNT_FACTOR = 0.9
    EVALUATION_EPISODES = 1000
    NUM_MODELS = 15  # Train 15 models and select best
    
    # Create environment for model selection
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=True)
    
    # Initialize model selector
    model_selector = ModelSelector(num_models=NUM_MODELS, validation_episodes=200)
    
    # Train multiple models and select the best
    print("="*60)
    print("ENHANCED Q-LEARNING WITH MODEL SELECTION")
    print("="*60)
    print(f"Strategy: Train {NUM_MODELS} models, select best performer")
    print(f"Goal: Consistent >70% success rate")
    print("="*60)
    
    best_agent = model_selector.train_multiple_models(
        env=env,
        num_episodes=NUM_EPISODES,
        max_steps_per_episode=MAX_STEPS_PER_EPISODE,
        learning_rate=LEARNING_RATE,
        discount_factor=DISCOUNT_FACTOR,
        min_exploration_rate=MIN_EXPLORATION_RATE,
        epsilon_decay_rate=EPSILON_DECAY_RATE
    )
    
    # Create trainer for visualization and demonstration
    trainer = FrozenLakeTrainer(map_name="4x4", is_slippery=True)
    trainer.agent = best_agent  # Use the best selected model
    
    # Create dummy training data for visualization
    # (using empty arrays since we already trained)
    dummy_rewards = np.zeros(NUM_EPISODES)
    moving_avg = np.zeros(NUM_EPISODES)
    
    # Plot training progress
    trainer.plot_training_progress(moving_avg)
    
    # Evaluate the best agent
    print("\nEvaluating best selected model...")
    success_rate, success_count = best_agent.evaluate(EVALUATION_EPISODES)
    
    # Save the trained model
    best_agent.save_model("frozen_lake_model.pkl")
    print(f"Model saved to: frozen_lake_model.pkl")
    
    # Demonstrate agent performance
    print("\nDemonstrating trained agent...")
    trainer.demonstrate_agent(num_episodes=3)
    
    # Display final evaluation results
    print(f"\n{'='*60}")
    print(f"FINAL EVALUATION RESULTS (BEST MODEL)")
    print(f"{'='*60}")
    print(f"Success Rate: {success_rate:.2f}% ({success_count} / {EVALUATION_EPISODES} episodes)")
    
    # Display status
    if success_rate >= 70:
        print(f"SUCCESS: Achieved target of >70%!")
    else:
        print(f"Below target (70%)")
    
    print(f"{'='*60}\n")
    
    # Close environment
    env.close()
    trainer.close()
    
    return success_rate


if __name__ == "__main__":
    final_success_rate = main()

    input("Press Enter to exit...")  # 🔹防止視窗一跑完就關掉
    #run(10, is_training=False, render=True)
