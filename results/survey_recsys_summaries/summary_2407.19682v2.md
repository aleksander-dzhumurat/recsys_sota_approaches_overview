# Summary of 2407.19682v2.md

**Token Usage**: Input: 15611, Output: 1010, Total: 16621

---

### Main Idea
- The paper addresses the challenge of optimizing multiple objectives simultaneously in recommender systems using multi-task learning.
- Existing multi-task learning methods often overlook the specific characteristics of recommendation scenarios, leading to suboptimal gradient balancing. The paper argues that achieving both appropriate magnitude balance and global direction balance in gradients is crucial for effective multi-task optimization in recommender systems.
- The paper proposes GradCraft, a novel methodology that dynamically adjusts gradient magnitudes to achieve magnitude balance and then employs projections to eliminate gradient conflicts in directions, thus ensuring global direction balance.

### Technologies
- **GradCraft:** A dynamic gradient balancing method for multi-task optimization in recommender systems. It comprises two main steps:
  - **Magnitude Adjustment:** Dynamically aligns gradient norms across all tasks based on the maximum norm, preventing excessive norm differences and dominance by certain tasks. The adjustment involves a hyperparameter τ to control the closeness to the maximum norm, using the formula:  ˆ𝑔𝑖 = 𝑔𝑖 * (∥𝑔𝑖∥ + τ * max𝑗 ∥𝑔𝑗∥) / ∥𝑔𝑖∥, where  ˆ𝑔𝑖 is the adjusted gradient, 𝑔𝑖 is the original gradient, and max𝑗 ∥𝑔𝑗∥ is the maximum gradient norm among all tasks.
  - **Direction Projection:** Applies projections to eliminate gradient conflicts in directions while considering all conflicting tasks concurrently. It requires a certain level of positive similarity (controlled by hyperparameter ε) to facilitate positive knowledge transfer across tasks.  The deconflicted gradient ˜𝑔𝑖 is computed as ˜𝑔𝑖 = ˆ𝑔𝑖 − 𝐺 ⊤ 𝑖 𝒘, where 𝐺𝑖 is a matrix of conflicting gradients and 𝒘 is a weight vector solved in closed form.
- **PLE (Progressive Layered Extraction):** Used as the backbone recommender model for experiments. It consists of shared and task-specific experts (DeepFM), gate networks, and tower networks. DeepFM combines Factorization Machine (FM) with Multi-Layer Perceptron (MLP).
- **Datasets:**
  - **Wechat:** A public short video dataset with 19,997 users and 59,322 items.
  - **Kuaishou:** A real-world short video recommendation dataset with 8,516 users and 62,699 items.
- **Evaluation Metrics:** AUC (Area Under the Curve) and GAUC (Group AUC) are used to measure recommendation accuracy. The paper primarily focuses on the average performance across all tasks (AV-A, AV-G) and the relative improvement compared to the Single-task baseline (RI-A, RI-G).
- **Baselines:** Single, EW (Equal Weighting), UC (Uncertainty-based weighting), DWA (Dynamic Weight Averaging), MGDA (Multi-Gradient Descent Algorithm), PCGrad (Projected Conflictive Gradients), GradVac (Gradient Vaccine), CAGrad, IMTL, and DBMTL. A variant of PCGrad named PCGrad+ (incorporating magnitude balance) is also used.
- **Optimizer:** Adam optimizer with grid search to find optimal hyperparameters (learning rate, mini-batch size, L2 regularization).
- Implementation details: The hidden layer configuration for the MLP is set to 256 × 128 × 64. The tower network is implemented as an MLP with a hidden layer configuration of 32 × 16. The gate network structure is based on a linear layer with Softmax [41] serving as the activation function. The embedding size is consistently set to 16 for all user and video features.

### Results
- GradCraft consistently outperforms all baseline methods on both the Wechat and Kuaishou datasets, demonstrating superior performance in terms of AV-A, AV-G, RI-A, and RI-G.
- Ablation studies confirm the importance of both the magnitude adjustment (controlled by τ) and direction projection (controlled by ε) components of GradCraft. Setting τ or ε to extreme values degrades performance.
- GradCraft's performance scales well with an increasing number of tasks, indicating its suitability for complex recommendation scenarios.
- Online A/B testing on the Kuaishou platform shows significant improvements in key business metrics, including average watch time (+0.505%), effective video views (+0.950%), and video sharing (+1.746%).
- Parameter sensitivity analysis shows that GradCraft achieves optimal performance with τ around 0.1 and ε around 1e-10. The performance remains stable within the ranges of τ ∈ [0, 0.3] and ε ∈ [1e-12, 1e-9].
