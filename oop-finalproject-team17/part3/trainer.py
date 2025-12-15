# trainer.py
import numpy as np

import matplotlib.pyplot as plt


class Trainer:
    def __init__(self, env, agent, episodes=500, max_steps=200, ma_window=50):
        self.env = env
        self.agent = agent
        self.episodes = episodes
        self.max_steps = max_steps
        self.ma_window = ma_window  # running moving average window

    def train(self):
        rewards = []
        success_count = 0
        moving_avg = []

        for ep in range(1, self.episodes + 1):
            obs, _ = self.env.reset()
            obs = obs.tolist()

            total_reward = 0
            done = False
            steps = 0
            reached_target = False

            while not done and steps < self.max_steps:
                action = self.agent.select_action(obs)
                next_obs, reward, terminated, truncated, _ = self.env.step(action)
                next_obs = next_obs.tolist()

                if hasattr(self.agent, "update"):
                    self.agent.update(obs, action, reward, next_obs, terminated)
                #self.agent.update(obs, action, reward, next_obs, terminated)

                total_reward += reward
                obs = next_obs
                done = terminated or truncated
                steps += 1

                if terminated:
                    reached_target = True

            rewards.append(total_reward)
            if reached_target:
                success_count += 1

            # running average
            window = rewards[-self.ma_window:]
            moving_avg.append(np.mean(window))

            if ep % 20 == 0:
                print(f"Episode {ep}/{self.episodes} - reward={total_reward:.2f} "
                    f"- success={reached_target} - MA({self.ma_window})={moving_avg[-1]:.3f}")

        success_rate = success_count / self.episodes

        print("\n========== Training Summary ==========")
        print(f"Total Episodes: {self.episodes}")
        print(f"Success Count:  {success_count}")
        print(f"Success Rate:   {success_rate:.3f}")
        print(f"Avg Reward:     {np.mean(rewards):.3f}")
        print("======================================\n")

        # 產生三種圖
        self.plot_reward_curve(rewards, moving_avg)
        #self.plot_policy_map(self.agent)
        #self.plot_qtable_heatmap(self.agent)
        # 只有 Q-learning 類 agent 才畫 policy / Q-table
        if hasattr(self.agent, "encode") and hasattr(self.agent, "q"):
            self.plot_policy_map(self.agent)
            self.plot_qtable_heatmap(self.agent)


        return rewards, success_rate, moving_avg


    def plot_reward_curve(self, rewards, moving_avg):
        plt.figure(figsize=(10,5))
        plt.plot(rewards, label="Reward", alpha=0.4)
        plt.plot(moving_avg, label=f"Moving Avg ({self.ma_window})", linewidth=2)
        plt.title("Training Reward Curve")
        plt.xlabel("Episode")
        plt.ylabel("Reward")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("reward_curve.png")
        plt.close()
        print("Saved: reward_curve.png")


    def plot_policy_map(self, agent):
        # 使用固定 target 位置：例如 (grid_rows-1, grid_cols-1)
        tr, tc = self.env.unwrapped.warehouse_robot.target_pos

        arrow = {0: "←", 1: "↓", 2: "→", 3: "↑"}

        grid = []
        for r in range(self.env.unwrapped.grid_rows):
            row = []
            for c in range(self.env.unwrapped.grid_cols):
                s = agent.encode([r, c, tr, tc])
                best_a = int(np.argmax(agent.q[s]))
                row.append(arrow[best_a])
            grid.append(row)

        # 輸出成圖片
        plt.figure(figsize=(5,4))
        plt.imshow(np.zeros((self.env.unwrapped.grid_rows, self.env.unwrapped.grid_cols)), cmap="gray_r")
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                plt.text(c, r, grid[r][c], ha="center", va="center", fontsize=20)
        plt.title("Policy Map (Best Action per Cell)")
        plt.axis("off")
        plt.savefig("policy_map.png")
        plt.close()
        print("Saved: policy_map.png")

    def plot_qtable_heatmap(self, agent):
        tr, tc = self.env.unwrapped.warehouse_robot.target_pos

        vals = np.zeros((self.env.unwrapped.grid_rows, self.env.unwrapped.grid_cols))
        for r in range(self.env.unwrapped.grid_rows):
            for c in range(self.env.unwrapped.grid_cols):
                s = agent.encode([r, c, tr, tc])
                vals[r,c] = np.max(agent.q[s])  # 每個 state 的最佳 Q-value

        plt.figure(figsize=(6,5))
        plt.imshow(vals, cmap="viridis")
        plt.colorbar(label="Max Q-value")
        plt.title("Q-table Heatmap (max Q per state)")
        plt.xlabel("Column")
        plt.ylabel("Row")
        plt.tight_layout()
        plt.savefig("qtable_heatmap.png")
        plt.close()
        print("Saved: qtable_heatmap.png")

