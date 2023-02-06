Deep Q-Net (DQN)
===========
| Contents:
| `1. Data`_
| `2. Agent`_
| `3. Evaluation`_

1.	Data
---------
Bitcoin Data of 2989 day:

- Basic Info:
   tic(currency),date,high,low,open,close,
- technical Factors: 
   adjcp(adjusted close), open (relative open price to t-1), zhigh, zlow, zadjcp, zclose, zd_5 (5-day moving average), zd_10, zd_15, zd_20, zd_25, zd_30.
- Train-Validation-Test Split:0.8,0.1,0.1.
      Train: BTC 2393 days. Validation: 300 days. Test: 298 days

2.	Agent
------------
DQN:
^^^^^^^^^
Use Multi-layer Perceptron (MLP) as Q-net to approximate the function of action value Q_value.

Update Process:
^^^^^^^^^^^^^^^^
- Update Process
      *Q(s,a)<-- Q(s,a)+α(Rt+1+γV(St+1)-V(St))*
      
      *TD Target: Rt+1+γV(St+1)*

      *TD Error：Rt+1+γV(St+1)-V(St)*  
 
 - where 
   
   Q(s,a) is the action-value function,
         
   Rt is the reward at timestep t,
 
   γ is the discount factor,
      
   V(St) is the expected return for State at timestep t.

- Optimizer: Adam 
- Loss: MSE(Q_values-Q_labels), where *Q_labels=Ri+γ * Q_next * (1-done)*.

Alogrithm ::

Initialize network and replay buffer
for t in timestep:
   Act At, get reward Rt, update state St+1
   Store <St,At,Rt,St+1> to Replay Buffer
   If enough samples in Replay Buffer:
      take N samples <Si,Ai,Ri,Si+1>
   Caculate TD-target yi= Ri + γ Maxa Q(St+1, A)
   Minimize Loss function L = sum i to N (yi-Q(Si))^2
   Update Q-net
End for 

Replay Buffer:
^^^^^^^^^^^^^^^
Put <State,Action,Reward,Next_Q> in the memory replay buffer. 

-	Random Sampling satisfies the Markov Property.
-	Increase Data Efficiency since each sample could be used multiple times.

3.	Evaluation
--------------
Profit Margin:  *LastDayAsset/FirstDayAsset-1* * *100%*

Risk Criteria 

