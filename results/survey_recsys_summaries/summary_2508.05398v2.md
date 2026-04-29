# Summary of 2508.05398v2.md

**Token Usage**: Input: 12450, Output: 1064, Total: 13514

---

### Main Idea
- The paper addresses the problem of bias in offline evaluation of recommender systems, specifically focusing on exposure bias (users only interact with items they see) and sampling bias (evaluating on a subset of items).
- The motivation is that offline evaluation is crucial when online testing is impractical, but these biases can lead to unreliable model comparisons and misleading conclusions about true user preferences.
- The paper proposes a framework to systematically analyze how different combinations of logging (simulating exposure bias) and sampling strategies affect the reliability of offline evaluation. It uses a fully observed dataset as ground truth to assess common sampling strategies across four dimensions: resolution, fidelity, robustness, and predictive power.

### Technologies
- **Dataset**: KuaiRec, a large-scale dataset of user interactions with short-form videos, is used. Crucially, the test split contains complete interaction histories, allowing for a fully observed ground-truth preference matrix.
- **Logging Strategies (Exposure Bias Simulation)**:
    - Uniform: Items are exposed to users uniformly at random.
    - Popularity-biased: Items are exposed with probabilities proportional to their global popularity.
    - Positivity-biased: Items are exposed with probabilities proportional to their positive feedback count.
    - Sparsity levels varying from 0% to 95% are applied to each logging strategy.
- **Sampling Strategies**:
    - Full: Uses all available non-positives (no sampling).
    - Exposed: Uses all exposed non-positives for each user.
    - Random@N: Samples N non-positives uniformly at random.
    - Popularity@N: Samples N non-positive items based on their popularity rank using Zipf's law.
    - Positivity@N: Samples N non-positive items weighted by their estimated relevance scores following Zipf's law.
    - WTD@N: Samples N non-positives weighted based on empirical exposure distributions.
    - WTDH@N: Heuristic version of WTD with uniform exposure assumptions.
    - Skew@N: Samples N non-positives based on empirical popularity distributions.
    - N is varied across {1, 2, 5, 10, 20, 50, 100, 200, 500, 1000}.
- **Recommender Models**:
    - ALS (Alternating Least Squares)
    - BPR (Bayesian Personalized Ranking)
    - LightFM (with collaborative and content-based variants)
    - SAR-Cosine (Item-based collaborative filtering using cosine similarity)
    - SAR-Jaccard (Item-based collaborative filtering using Jaccard index)
    - Popularity (Non-personalized baseline)
    - Random (Naive baseline)
- **Evaluation Metrics**:
    - Precision@K, Recall@K, nDCG@K (K = 5, 10, 50, 100)
- **Meta-Evaluation Metrics**:
    - Tie rate: Fraction of tied recommender model pairs in each evaluation scenario.
    - Kendall's Tau: Degree of ranking agreement across pairs of evaluation scenarios.
- **Framework/Libraries**:
    - Microsoft Recommenders framework (v1.2.0)
    - Hyperopt (for hyperparameter optimization)
    - Ray Tune (for parallelized evaluations)

### Results
- **Resolution (Q1)**: Tie rates are high in too small or too large samples. Samplers like Skew, Popularity, and Positivity yield lower tie rates (better resolution) under high sparsity and biased exposure. The Full sampler often yields lower resolution as sparsity increases. Samplers with small to moderate size exhibit stronger resolution.
- **Fidelity (Q2)**: Fidelity improves with sample size.  WTD and WTDH achieve near-maximum fidelity at moderate sparsity (10%-50%) with N ≥ 200.  Skew's effectiveness declines more rapidly as sparsity increases. Fidelity is not guaranteed by sample size alone but depends on how well the sampling strategy captures the structure and information present in the original data.
- **Robustness (Q3)**: Most sampling strategies are affected by exposure bias. WTD, and WTDH retain high agreement between biased and unbiased samples, especially with the Uniform logger. Popularity and Positivity show limited gains, particularly under high sparsity.
- **Predictive Power (Q4)**:  Skew, WTD, and WTDH achieve strong alignment with ground truth even under moderate to high sparsity. Random yielded results comparable to those of weighted methods. Popularity and Positivity samplers exhibit much lower predictive power, especially in biased or sparse regimes.

In summary, the paper finds that the choice of sampling strategy significantly impacts offline evaluation reliability. Bias-aware strategies are generally more robust and predictive, but no single strategy excels across all dimensions. The study emphasizes the need to carefully design sampling strategies, considering the interplay between logging bias, sparsity, and sampling methodology.
