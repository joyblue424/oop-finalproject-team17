# agent_base.py
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract Agent class defining the interface."""

    @abstractmethod
    def select_action(self, obs):
        """Return an action given the observation."""
        pass

    def update(self, obs, action, reward, next_obs, done):
        """Optional learning rule, overridden by RL agents."""
        pass
