import numpy as np


class QLearningAgent:

    def __init__(self, grid_rows, grid_cols, n_actions,
                 alpha=0.2, gamma=0.95, epsilon=1.0, epsilon_min=0.05, epsilon_decay=0.995):

        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.n_actions = n_actions

        # obs = [r, c, tr, tc] 各 0~4
        # 所以最多 state = 5*5*5*5 = 625
        self.state_count = grid_rows * grid_cols * grid_rows * grid_cols

        self.q = np.zeros((self.state_count, n_actions), dtype=float)

        self.alpha = alpha
        self.gamma = gamma

        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

    # 將 obs 映射為離散 state index
    def encode(self, obs):
        r, c, tr, tc = obs
        # 把 (r,c) 當一個 index、(tr,tc) 當一個 index，再組起來
        pos_idx = r * self.grid_cols + c                    # 0 ~ (R*C-1)
        tgt_idx = tr * self.grid_cols + tc                  # 0 ~ (R*C-1)
        return pos_idx * (self.grid_rows * self.grid_cols) + tgt_idx

    def select_action(self, obs):
        s = self.encode(obs)

        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)

        # exploitation
        return int(np.argmax(self.q[s]))

    def update(self, obs, action, reward, next_obs, done):
        s = self.encode(obs)
        ns = self.encode(next_obs)

        best_next_q = np.max(self.q[ns])
        target = reward if done else reward + self.gamma * best_next_q

        self.q[s, action] += self.alpha * (target - self.q[s, action])

        # epsilon decay
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    # 測試時方便把 epsilon 設為 0（純 greedy）
    def set_eval_mode(self, eval_mode: bool):
        if eval_mode:
            self._old_epsilon = self.epsilon
            self.epsilon = 0.0
        else:
            if hasattr(self, "_old_epsilon"):
                self.epsilon = self._old_epsilon