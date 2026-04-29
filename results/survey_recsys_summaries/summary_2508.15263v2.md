# Summary of 2508.15263v2.md

**Token Usage**: Input: 16753, Output: 948, Total: 17701

---

### Main Idea
- The paper addresses the problem of approximate unlearning in session-based recommendation systems. It aims to remove the influence of specific training samples (user-item interaction sessions) from a recommender system without fully retraining the model. This is crucial for complying with data protection regulations (GDPR, CCPA, PIPL) and for practical purposes like removing outdated preferences or noisy data. The authors argue that directly applying gradient ascent (GA) for unlearning in this context is challenging due to performance degradation and the failure to consider the sequential order of unlearning samples. The paper proposes CAU (Curriculum Approximate Unlearning), a framework that tackles these challenges by formulating unlearning as a multi-objective optimization problem and by using a curriculum-based sequence to process unlearning batches.
- The motivation stems from the increasing importance of data privacy and the need for recommender systems to adapt to user requests for data removal efficiently. Existing unlearning methods are either inefficient (exact unlearning requires retraining) or not well-suited for the sequential nature of session-based recommendation.
- The proposed solution, CAU, balances unlearning efficacy with performance retention by using a Pareto-optimal solver for multi-objective optimization. It also addresses the sample order issue by quantifying unlearning difficulty (gradient and embedding difficulty) and employing hard-sampling and soft-sampling strategies to prioritize easier samples.

### Technologies
- **Gradient Ascent (GA)**: Used as the core technique for approximate unlearning, applying opposite gradients to the target unlearning samples to reduce their influence.
- **Multi-Objective Optimization**: Formulates unlearning as a multi-objective problem to balance unlearning efficacy, retaining normal recommendation performance, and maintaining consistency with the original model, employing Pareto-optimality.
- **Pareto-Optimality Solver (MGDA)**: A multiple gradient descent algorithm is used to find a stable solution that balances the trade-offs between conflicting objectives. It seeks a convex combination of gradients from all objectives such that their weighted sum forms a common descent direction.
- **Curriculum Learning**: A strategy to process unlearning samples in a specific order, from easier to harder, based on difficulty metrics.
- **Gradient Unlearning Difficulty**: A metric to quantify the difficulty of unlearning based on the cosine similarity between the gradient of the unlearning loss and the sum of gradients of the normal and KL losses.
- **Embedding Unlearning Difficulty**: A metric based on the dot product between the session state representation and the embedding of the item to be forgotten, capturing the semantic proximity between session states and target items.
- **Hard-Sampling**: A deterministic approach to curriculum learning where samples are strictly ordered based on their difficulty rankings, processing easier samples first.
- **Soft-Sampling**: A stochastic approach to curriculum learning where samples are drawn with probabilities based on their difficulty scores, gradually shifting the distribution towards harder samples.
- **Benchmark Datasets**: MovieLens-1M, Amazon Beauty, and Amazon Games datasets are used for experiments.
- **Evaluation Metrics**: Recall@K, NDCG@K, Hit_u@K, and a combined U-score are used to evaluate recommendation performance and unlearning effectiveness.
- **Baseline Models**: GRU4Rec, SASRec, and BERT4Rec are used as the backbone session-based recommendation models.

### Results
- CAU demonstrates superior unlearning efficiency and effectiveness while maintaining high recommendation accuracy compared to baseline methods (Retrain, SISA, SRU).
- CAU achieves performance close to the Original model (without unlearning) with a stable performance drop controlled within 8%, indicating effective performance preservation.
- CAU consistently achieves the best performance regarding the U-score, maintaining recommendation accuracy close to Original while attaining a lower Hit_u score than Retrain.
- Soft-sampling is generally more effective than hard-sampling due to the increased robustness that soft-sampling provides throughout the unlearning procedure.
- CAU achieves a speedup of approximately 13x over Retrain and 3x over SISA and SRU in terms of unlearning time, highlighting the efficiency of the proposed approximate unlearning method.
- Ablation studies confirm the importance of each component of CAU (Pareto-optimality solver, Curriculum Unlearning, Recommendation Loss) for achieving optimal performance.
- Smaller unlearning batch sizes lead to higher U-scores but may increase training time, revealing a trade-off between unlearning effectiveness and efficiency.
- CAU exhibits stability and robustness under varying amounts of unlearning data due to the contributions of the Pareto-optimality solver and sampling strategy.
