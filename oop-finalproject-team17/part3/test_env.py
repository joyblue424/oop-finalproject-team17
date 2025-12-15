import gymnasium as gym
import oop_project_env  # noqa: F401  # 只為了註冊 env

env = gym.make("warehouse-robot-v0")

obs, info = env.reset()
print("Initial obs:", obs)

for i in range(5):
    obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
    print(f"Step {i} | obs={obs} | reward={reward} | done={terminated or truncated}")
