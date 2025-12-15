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

[image1]: reward_curve_random.png

[image2]: oop-finalproject-team17/part3/policy_map.png

[image3]: oop-finalproject-team17/part3/qtable_heatmap.png

[image4]: reward_curve.png

[image5]: dependencies.png