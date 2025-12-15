import numpy as np

class RandomAgent:
    def __init__(self, action_space):
        self.action_space = action_space

    def select_action(self, obs):
        return self.action_space.sample()
    
    def update(self, obs, action, reward, next_obs, done):
        pass   # RandomAgent 不學習，所以不做任何事
