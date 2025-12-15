import gymnasium as gym
import oop_project_env  # noqa: F401

from agent_random import RandomAgent

env = gym.make("warehouse-robot-v0", render_mode="human")
agent = RandomAgent(env.action_space)

obs, info = env.reset()
print("=== Testing RandomAgent ===")

for step in range(30):
    action = agent.select_action(obs)
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"Step {step} | action={action} | reward={reward}")

    if terminated or truncated:
        print("Reached target, reset.")
        obs, info = env.reset()
