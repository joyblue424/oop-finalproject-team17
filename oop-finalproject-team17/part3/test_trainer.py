import gymnasium as gym
import oop_project_env  # register

from agent_qlearning import QLearningAgent
from trainer import Trainer

env = gym.make("warehouse-robot-v0", render_mode="human")

agent = QLearningAgent(
    grid_rows=4,
    grid_cols=5,
    n_actions=env.action_space.n
)

trainer = Trainer(env, agent, episodes=300)

result = trainer.train()
print("Training finished. Total success episodes:", result)
