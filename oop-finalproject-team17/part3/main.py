# main.py
import gymnasium as gym

# 必須先 import 才會 register environment
import oop_project_env

from agent_random import RandomAgent
from agent_qlearning import QLearningAgent
from trainer import Trainer


def create_agent(choice, env):
    """function to create agent"""
    if choice == "1":
        print("Using RandomAgent...")
        return RandomAgent(env.action_space)

    elif choice == "2":
        print("Using QLearningAgent...")
        return QLearningAgent(
            grid_rows=env.unwrapped.grid_rows,
            grid_cols=env.unwrapped.grid_cols,
            n_actions=env.action_space.n,
            alpha=0.2,
            gamma=0.95,
            epsilon=1.0,
            epsilon_min=0.05,
            epsilon_decay=0.995,
        )
    else:
        raise ValueError("Invalid agent choice")
    

def main():

    # =========================
    # Choose Agent
    # =========================
    print("Choose agent:")
    print("1. Random Agent")
    print("2. Q-Learning Agent")

    choice = input("Your choice: ").strip()

    # =========================
    # 1. TRAIN (no rendering)
    # =========================
    train_env = gym.make("warehouse-robot-v0")   

    #agent = RandomAgent(train_env.action_space)
    agent = create_agent(choice, train_env)

    ''''
    agent = QLearningAgent(
        grid_rows=train_env.unwrapped.grid_rows,
        grid_cols=train_env.unwrapped.grid_cols,
        n_actions=train_env.action_space.n,
        alpha=0.2,
        gamma=0.95,
        epsilon=1.0,
        epsilon_min=0.05,
        epsilon_decay=0.995,
    )
    '''
    trainer = Trainer(train_env, agent, episodes=1000)

    # 接 train() 回傳值
    rewards, success_rate, moving_avg = trainer.train()


    print("\nTraining finished!")
    print("First 10 episode rewards:", rewards[:10])
    print(f"Final Success Rate: {success_rate:.2f}")

    # =========================
    # 2. TEST (with rendering)
    # =========================
    print("\nNow testing the learned agent...")
    test_episodes = 10
    test_env = gym.make("warehouse-robot-v0", render_mode="human")

    # 測試時用 greedy policy
    #agent.set_eval_mode(True)
    if hasattr(agent, "set_eval_mode"):
        agent.set_eval_mode(True)


    for ep in range(test_episodes):

        obs, _ = test_env.reset()
        obs = obs.astype(int).tolist()
        done = False
        steps = 0
        max_test_steps = 30


        while not done and steps < max_test_steps:
            action = agent.select_action(obs)
            next_obs, reward, terminated, truncated, _ = test_env.step(action)
            next_obs = next_obs.astype(int).tolist()

            obs = next_obs
            done = terminated or truncated
            steps += 1


        print("Press ESC to quit...")

        waiting = True
        import pygame
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # 下一個 episode
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:  # 結束
                        print("Testing aborted by user.")
                        #agent.set_eval_mode(False)
                        if hasattr(agent, "set_eval_mode"):
                            agent.set_eval_mode(False)
                        pygame.quit()
                        exit()

        # 清掉測試結束後的殘餘事件
        pygame.event.clear()

    #agent.set_eval_mode(False)  # 還原 epsilon
    if hasattr(agent, "set_eval_mode"):
        agent.set_eval_mode(False)
    print("\nTesting completed.")

if __name__ == "__main__":
    main()
