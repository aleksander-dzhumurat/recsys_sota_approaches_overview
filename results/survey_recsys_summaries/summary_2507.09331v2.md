# Summary of 2507.09331v2.md

**Token Usage**: Input: 7636, Output: 647, Total: 8283

---

### Main Idea
- The paper addresses a bias in the standard logQ correction used in sampled softmax training for large-scale recommender systems. LogQ correction is a technique to mitigate bias introduced by using in-batch negatives during training, where popular items are over-penalized.
- The authors argue that the standard derivation of logQ correction is inconsistent because it treats the positive item in the softmax denominator as being sampled from the same distribution as the negative items, when in reality, the positive item is deterministically included. This inconsistency leads to systematic bias.
- They propose a corrected formulation of logQ correction that explicitly accounts for the deterministic inclusion of the positive item. This correction introduces a sample weight that reflects the model's uncertainty, defined as the probability of misclassifying the positive item.

### Technologies
- **Two-tower neural networks:** Used as the architecture for the retrieval stage of the recommender system, where user and item representations are generated independently.
- **Sampled Softmax:** Employed to approximate the full softmax loss function, which is computationally infeasible for large item catalogs.
- **In-batch negatives:** A negative sampling strategy where negative items are drawn from the current mini-batch.
- **LogQ correction:** A technique to mitigate the bias introduced by in-batch negative sampling. The paper presents both the standard and the improved version of logQ correction.
- **Importance Sampling:** Used in the derivation of both the standard and improved logQ corrections to adjust for the distribution mismatch between the true item distribution and the sampled distribution.
- **Count-min sketch:** Used in the industrial setup to approximate item frequencies for computing the logQ correction when the exact frequencies are not available.
- **Datasets:** MovieLens-1M and Steam (public datasets) and a large-scale proprietary music streaming dataset.
- **Evaluation Metrics:** Recall@k and NDCG@k are used to measure retrieval performance.
- **Baselines:** Binary Cross-Entropy (BCE), Generalized Binary Cross-Entropy (gBCE), Full Softmax Loss, sampled softmax with uniform negatives, sampled softmax with in-batch negatives, and mixed negative sampling (MNS).  gSASRec is used as the backbone model.

### Results
- The paper demonstrates that the proposed improved logQ correction consistently improves retrieval quality over the standard logQ correction on both public and proprietary datasets.
- On academic datasets (MovieLens-1M and Steam), the improved logQ correction achieves gains over the standard variant, particularly when combined with mixed negative sampling.
- In the industrial setup, the improved logQ correction shows a growing advantage over the standard variant as the value of *k* increases in Recall@k, indicating better performance in retrieving a large candidate pool for downstream ranking.
- The paper emphasizes the importance of the evaluation setup (leave-one-out vs. temporal split) and negative sampling strategy, showing that the proposed method is robust across different validation schemes and scales effectively to production settings.
- The results suggest that conclusions drawn from leave-one-out evaluation may not transfer well to more realistic, time-aware protocols.
