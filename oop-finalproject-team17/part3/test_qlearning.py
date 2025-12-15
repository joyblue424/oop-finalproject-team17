import gymnasium as gym
import oop_project_env   # 註冊環境用
from agent_qlearning import QLearningAgent

env = gym.make("warehouse-robot-v0", render_mode="human")

agent = QLearningAgent(
    grid_rows=4,
    grid_cols=5,
    n_actions=env.action_space.n,
)

episodes = 200
rewards = []

for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    total = 0

    while not done:
        action = agent.select_action(obs)
        next_obs, reward, terminated, truncated, _ = env.step(action)

        agent.update(obs, action, reward, next_obs, terminated or truncated)

        obs = next_obs
        total += reward
        done = terminated or truncated

    rewards.append(total)

print("=== QLearningAgent Test ===")
print("First 20 episode rewards:", rewards[:20])
print("Last 20 episode rewards:", rewards[-20:])
print("Total success episodes:", sum(rewards))
