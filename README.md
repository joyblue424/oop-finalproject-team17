README.md  
B123245025 李君潔 B123245026 黃昱憙 B123040060 陳泉龍

## **Project Overview**

* Gymnasium v1.2.2  
* Part1 Code  
* Part2 Code  
* Part3 Code


## **How To Run**

**Part1:** 

\# Train the agent  
python mountain\_car.py \--train \--episodes 5000

\# Render and visualize performance  
python mountain\_car.py \--render \--episodes 10

**Part2:**

python frozen\_lake.py

**Part3:**

Open Command Prompt terminal 

.venv\\Scripts\\activate  
cd part3  
python main.py

It will show a menu to choose like:

Choose agent:  
1\. Random Agent  
2\. Q-Learning Agent  
Your choice: 

Explanation of output:  
—————————————————————————————————————

Output Format:

Each line of output consists of four items separated by dashes. N denotes the episodes trained so far.   
Episode N/1000   –   reward \= X   –   success=True   –   MA(50) \= Y

A total of 1000 episodes will be run for training, with 20 episodes per round.

—————————————————————————————————————

In every episode, if the agent reaches the goal, it will receive a reward of \+1. At the same time, to encourage the agent to reach the goal as quick as possible, every step it takes will deduct 0.01 of the reward, hence obtaining the following algorithm: 

reward \= 1 \- 0.01 \* steps

Reward will be in the range of 0 to 1.5. A high reward means the agent’s learnt strategy takes the relatively shorter path to the goal.

---

Success is defined as the following:

	True: The agent successfully reaches the goal.

	False: The agent did not reach the goal after the maximum amount of steps taken.

---

MA(50) denotes the moving average of reward in the recent 50 episodes. If the value continues to rise, it means the agent is improving. 

---

We provide three visual graphs with the output.

(1) Policy Map(only for Q-learning): A visual representation of the best action per cell. Each arrow corresponds to its respective grid on the map.

(2) Q-table Heatmap(only for Q-learning): A value landscape of the best Q-value in the Q-table of each grid on the map. Yellow symbolizes high confidence that the grid is close to the goal and has a clear best route. Blue symbolizes the opposite.

(3) Graph of Training Reward Curve: A visualization of how the reward curve and the moving average change as training goes on.

---

You will see an output like that:

1. Random

Episode 20/1000 \- reward=1.18 \- success=True \- MA(50)=0.956  
Episode 40/1000 \- reward=0.84 \- success=True \- MA(50)=0.891  
Episode 60/1000 \- reward=1.11 \- success=True \- MA(50)=0.865  
Episode 80/1000 \- reward=1.29 \- success=True \- MA(50)=0.793  
Episode 100/1000 \- reward=1.12 \- success=True \- MA(50)=0.912  
Episode 120/1000 \- reward=1.10 \- success=True \- MA(50)=0.878  
Episode 140/1000 \- reward=1.10 \- success=True \- MA(50)=0.919  
Episode 160/1000 \- reward=0.52 \- success=True \- MA(50)=0.971  
Episode 180/1000 \- reward=1.02 \- success=True \- MA(50)=0.921  
Episode 200/1000 \- reward=1.07 \- success=True \- MA(50)=0.915  
Episode 220/1000 \- reward=0.64 \- success=True \- MA(50)=0.876  
Episode 240/1000 \- reward=0.99 \- success=True \- MA(50)=0.917  
Episode 260/1000 \- reward=1.26 \- success=True \- MA(50)=0.892  
Episode 280/1000 \- reward=0.91 \- success=True \- MA(50)=0.970  
Episode 300/1000 \- reward=1.06 \- success=True \- MA(50)=0.940  
Episode 320/1000 \- reward=0.84 \- success=True \- MA(50)=0.901  
Episode 340/1000 \- reward=1.08 \- success=True \- MA(50)=1.017  
Episode 360/1000 \- reward=0.79 \- success=True \- MA(50)=0.947  
Episode 380/1000 \- reward=0.98 \- success=True \- MA(50)=0.852  
Episode 400/1000 \- reward=1.25 \- success=True \- MA(50)=0.858  
Episode 420/1000 \- reward=1.17 \- success=True \- MA(50)=0.945  
Episode 440/1000 \- reward=1.06 \- success=True \- MA(50)=0.999  
Episode 460/1000 \- reward=1.02 \- success=True \- MA(50)=1.008  
Episode 480/1000 \- reward=-1.60 \- success=False \- MA(50)=0.920  
Episode 500/1000 \- reward=0.96 \- success=True \- MA(50)=0.892  
Episode 520/1000 \- reward=1.33 \- success=True \- MA(50)=0.885  
Episode 540/1000 \- reward=1.19 \- success=True \- MA(50)=0.889  
Episode 560/1000 \- reward=1.17 \- success=True \- MA(50)=0.841  
Episode 580/1000 \- reward=0.62 \- success=True \- MA(50)=0.874  
Episode 600/1000 \- reward=1.02 \- success=True \- MA(50)=0.858  
Episode 620/1000 \- reward=1.07 \- success=True \- MA(50)=0.803  
Episode 640/1000 \- reward=0.98 \- success=True \- MA(50)=0.853  
Episode 660/1000 \- reward=1.17 \- success=True \- MA(50)=0.996  
Episode 680/1000 \- reward=0.06 \- success=True \- MA(50)=0.949  
Episode 700/1000 \- reward=0.83 \- success=True \- MA(50)=0.987  
Episode 720/1000 \- reward=1.23 \- success=True \- MA(50)=0.937  
Episode 740/1000 \- reward=0.70 \- success=True \- MA(50)=0.962  
Episode 760/1000 \- reward=1.01 \- success=True \- MA(50)=0.945  
Episode 780/1000 \- reward=1.14 \- success=True \- MA(50)=0.919  
Episode 800/1000 \- reward=0.98 \- success=True \- MA(50)=0.978  
Episode 820/1000 \- reward=0.83 \- success=True \- MA(50)=0.936  
Episode 840/1000 \- reward=0.05 \- success=True \- MA(50)=0.822  
Episode 860/1000 \- reward=0.98 \- success=True \- MA(50)=0.839  
Episode 880/1000 \- reward=1.06 \- success=True \- MA(50)=0.899  
Episode 900/1000 \- reward=1.16 \- success=True \- MA(50)=0.961  
Episode 920/1000 \- reward=1.27 \- success=True \- MA(50)=0.951  
Episode 940/1000 \- reward=1.21 \- success=True \- MA(50)=0.930  
Episode 960/1000 \- reward=1.06 \- success=True \- MA(50)=0.980  
Episode 980/1000 \- reward=0.95 \- success=True \- MA(50)=0.980  
Episode 1000/1000 \- reward=1.32 \- success=True \- MA(50)=0.927

\========== Training Summary \==========  
Total Episodes: 1000  
Success Count:  986  
Success Rate:   0.986  
Avg Reward:     0.915  
\======================================

Saved: reward\_curve.png

Training finished\!  
First 10 episode rewards: \[1.54, 0.5900000000000004, 1.07, 1.2200000000000004, 1.06, 1.27, 1.12, 0.14, 0.8700000000000003, 0.9500000000000001\]  
Final Success Rate: 0.99

Now testing the learned agent...  
R \_ \_ \_ \_   
\_ \_ \_ T \_   
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.DOWN  
\_ \_ \_ \_ \_   
R \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.DOWN  
\_ \_ \_ \_ \_   
\_ \_ \_ T \_  
R \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ R \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.UP  
\_ \_ \_ \_ \_   
\_ R \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.UP  
\_ R \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.DOWN  
\_ \_ \_ \_ \_   
\_ R \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
\_ \_ \_ \_ \_   
R \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
\_ \_ \_ \_ \_   
R \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.UP  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.UP  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ R \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.UP  
R \_ \_ \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ R \_ \_ \_  
\_ \_ \_ T \_   
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ R \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ \_ R \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.UP  
\_ \_ \_ R \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.LEFT  
\_ \_ R \_ \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ \_ R \_   
\_ \_ \_ T \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_

RobotAction.DOWN  
\_ \_ \_ \_ \_   
\_ \_ \_ R \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ \_  
![][image1]

2. Q-learning

Episode 20/1000 \- reward=1.16 \- success=True \- MA(50)=1.175  
Episode 40/1000 \- reward=1.18 \- success=True \- MA(50)=1.205  
Episode 60/1000 \- reward=1.18 \- success=True \- MA(50)=1.262  
Episode 80/1000 \- reward=1.45 \- success=True \- MA(50)=1.309  
Episode 100/1000 \- reward=1.54 \- success=True \- MA(50)=1.344  
Episode 120/1000 \- reward=1.54 \- success=True \- MA(50)=1.345  
Episode 140/1000 \- reward=1.17 \- success=True \- MA(50)=1.313  
Episode 160/1000 \- reward=1.45 \- success=True \- MA(50)=1.315  
Episode 180/1000 \- reward=1.36 \- success=True \- MA(50)=1.296  
Episode 200/1000 \- reward=1.34 \- success=True \- MA(50)=1.318  
Episode 220/1000 \- reward=1.25 \- success=True \- MA(50)=1.313  
Episode 240/1000 \- reward=1.27 \- success=True \- MA(50)=1.310  
Episode 260/1000 \- reward=1.09 \- success=True \- MA(50)=1.310  
Episode 280/1000 \- reward=1.18 \- success=True \- MA(50)=1.317  
Episode 300/1000 \- reward=1.18 \- success=True \- MA(50)=1.290  
Episode 320/1000 \- reward=1.36 \- success=True \- MA(50)=1.275  
Episode 340/1000 \- reward=1.45 \- success=True \- MA(50)=1.300  
Episode 360/1000 \- reward=1.54 \- success=True \- MA(50)=1.335  
Episode 380/1000 \- reward=1.45 \- success=True \- MA(50)=1.331  
Episode 400/1000 \- reward=1.18 \- success=True \- MA(50)=1.320  
Episode 420/1000 \- reward=1.09 \- success=True \- MA(50)=1.301  
Episode 440/1000 \- reward=1.45 \- success=True \- MA(50)=1.304  
Episode 460/1000 \- reward=1.36 \- success=True \- MA(50)=1.322  
Episode 480/1000 \- reward=1.36 \- success=True \- MA(50)=1.316  
Episode 500/1000 \- reward=1.09 \- success=True \- MA(50)=1.311  
Episode 520/1000 \- reward=1.27 \- success=True \- MA(50)=1.285  
Episode 540/1000 \- reward=1.34 \- success=True \- MA(50)=1.284  
Episode 560/1000 \- reward=1.54 \- success=True \- MA(50)=1.286  
Episode 580/1000 \- reward=1.45 \- success=True \- MA(50)=1.315  
Episode 600/1000 \- reward=1.27 \- success=True \- MA(50)=1.318  
Episode 620/1000 \- reward=1.09 \- success=True \- MA(50)=1.309  
Episode 640/1000 \- reward=1.25 \- success=True \- MA(50)=1.309  
Episode 660/1000 \- reward=1.36 \- success=True \- MA(50)=1.314  
Episode 680/1000 \- reward=1.36 \- success=True \- MA(50)=1.336  
Episode 700/1000 \- reward=1.27 \- success=True \- MA(50)=1.344  
Episode 720/1000 \- reward=1.26 \- success=True \- MA(50)=1.327  
Episode 740/1000 \- reward=1.27 \- success=True \- MA(50)=1.318  
Episode 760/1000 \- reward=1.27 \- success=True \- MA(50)=1.275  
Episode 780/1000 \- reward=1.16 \- success=True \- MA(50)=1.263  
Episode 800/1000 \- reward=1.36 \- success=True \- MA(50)=1.285  
Episode 820/1000 \- reward=1.54 \- success=True \- MA(50)=1.299  
Episode 840/1000 \- reward=1.54 \- success=True \- MA(50)=1.312  
Episode 860/1000 \- reward=1.27 \- success=True \- MA(50)=1.321  
Episode 880/1000 \- reward=1.27 \- success=True \- MA(50)=1.316  
Episode 900/1000 \- reward=1.27 \- success=True \- MA(50)=1.306  
Episode 920/1000 \- reward=1.27 \- success=True \- MA(50)=1.325  
Episode 940/1000 \- reward=1.27 \- success=True \- MA(50)=1.287  
Episode 960/1000 \- reward=1.45 \- success=True \- MA(50)=1.277  
Episode 980/1000 \- reward=1.54 \- success=True \- MA(50)=1.269  
Episode 1000/1000 \- reward=1.27 \- success=True \- MA(50)=1.310

\========== Training Summary \==========  
Total Episodes: 1000  
Success Count:  1000  
Success Rate:   1.000  
Avg Reward:     1.306  
\======================================

Saved: reward\_curve.png  
Saved: policy\_map.png  
Saved: qtable\_heatmap.png

Training finished\!  
First 10 episode rewards: \[0.8000000000000003, 1.2000000000000002, 0.6100000000000008, 1.1700000000000002, 1.27, 1.08, 1.34, 1.21, 1.27, 1.33\]  
Final Success Rate: 1.00

Now testing the learned agent...

R \_ \_ \_ \_  
\_ \_ \_ \_ \_  
\_ \_ \_ \_ T  
\_ \_ \_ \_ \_

RobotAction.DOWN  
\_ \_ \_ \_ \_   
R \_ \_ \_ \_  
\_ \_ \_ \_ T  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ \_ \_ \_   
\_ R \_ \_ \_  
\_ \_ \_ \_ T  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ \_ \_ \_   
\_ \_ R \_ \_  
\_ \_ \_ \_ T  
\_ \_ \_ \_ \_

RobotAction.DOWN  
\_ \_ \_ \_ \_   
\_ \_ \_ \_ \_  
\_ \_ R \_ T  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ \_ \_ \_   
\_ \_ \_ \_ \_  
\_ \_ \_ R T  
\_ \_ \_ \_ \_

RobotAction.RIGHT  
\_ \_ \_ \_ \_   
\_ \_ \_ \_ \_  
\_ \_ \_ \_ R  
\_ \_ \_ \_ \_

Press ESC to quit...  
Testing aborted by user.  
![][image2]  
![][image3]  
![][image4]

## **Project Dependencies**

![][image5]        

**Contribution lists**    
B123245025 李君潔: Part1, Part2, Report  
B123245026 黃昱憙: Part1, Part3, Report  
B123040060 陳泉龍: Part1, Part2, Presenter

[image1]: oop-finalproject-team17/part3/reward_curve.png

[image2]: oop-finalproject-team17/part3/policy_map.png

[image3]: oop-finalproject-team17/part3/qtable_heatmap.png

[image4]: reward_curve.png

[image5]: <data:image/png;base64,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>
