# Summary of 2308.13246v1.md

**Token Usage**: Input: 5079, Output: 725, Total: 5804

---

### Main Idea
- The paper addresses the problem of stochastic rewards in model-free Reinforcement Learning (RL)-based recommender systems. Unlike traditional RL environments with deterministic rewards, recommender systems often face the issue where user feedback on the same item varies over time due to unobserved factors. This stochasticity significantly degrades the performance and sample efficiency of existing RL methods.
- The motivation is to improve the performance and training efficiency of RL-based recommender systems by mitigating the negative impact of stochastic user feedback.
- The paper proposes two Stochastic Reward Stabilization (SRS) frameworks: SRS and SRS with Shared Representation (SRS2). These frameworks replace the direct stochastic reward with an estimated reward predicted by a supervised model, effectively stabilizing the reward signal and improving learning.

### Technologies
- **Model-free RL Methods:** The paper focuses on enhancing model-free RL approaches, which are categorized into value-based, policy-based, and actor-critic methods. Examples include DRN, DQN-att(EDRR), REINFORCE, URL, DDPG, and DRR-att(EDRR).
- **Stochastic Reward Stabilization (SRS):** This is the core technique, involving replacing the stochastic reward with its conditional expectation estimated via a supervised reward estimation model.
- **SRS with Shared Representation (SRS2):** An extension of SRS, where the reward estimation model and the RL model share a common embedding layer for user and item representations. This leverages auxiliary training to accelerate representation learning.
- **Reward Estimation Model:** The paper employs a myopic DIN (Deep Interest Network) model as the supervised reward estimation model, co-trained with the RL model.
- **Experimental Environments:** The methods are evaluated in two environments:
    - **Virtual Taobao:** A publicly available recommendation simulator where stochastic and deterministic rewards are explicitly controlled.
    - **Industrial-level Recommender System:** A real-world coupon recommendation task with over 1 billion users.
- **Evaluation Metrics:**
    - **Average Cumulative Reward:** Used in the simulation environment to measure the number of purchases per session.
    - **Sample Efficiency:** Measured by the number of training samples needed to reach a satisfactory performance threshold.
    - **User Return:** The average number of times a user returns to the coupon recommendation scenario.
    - **User Payment:** The average number of payments with coupon redemption for each user.

### Results
- The empirical study on Virtual Taobao demonstrates that model-free RL methods trained with stochastic rewards suffer from slower convergence and lower final performance compared to those trained with deterministic rewards.
- Combining existing RL methods with SRS consistently achieves higher rewards and lower variance in the learning process, indicating the effectiveness and model-agnostic nature of the framework.
- SRS and SRS2 significantly improve the sample efficiency of RL-based recommender systems, with SRS2 achieving at least a 2x speedup in training compared to state-of-the-art models in actor-critic and policy-based approaches.
- In the live experiment on a real-world coupon recommendation task, DQN-att(EDRR) equipped with SRS2 achieves a +3.16% relative improvement on user return and a +0.89% improvement on user payments compared to a myopic DIN method.
- The results highlight the detrimental effect of stochastic rewards in RL-based recommender systems and demonstrate that the proposed SRS and SRS2 frameworks effectively mitigate this issue, leading to improved performance and sample efficiency in both simulated and real-world environments.
