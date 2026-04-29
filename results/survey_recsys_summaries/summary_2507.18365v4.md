# Summary of 2507.18365v4.md

**Token Usage**: Input: 10738, Output: 416, Total: 11154

---

### Main Idea
- The paper addresses the lack of methods for quantifying the privacy risk of Recommender Systems (RecSys) training data.
- The motivation is to enable privacy-aware RecSys model development and deployment, allowing users to make informed decisions about sharing sensitive interactions.
- The proposed solution is RecPS, a membership-inference attack (MIA)-based privacy scoring method to measure privacy risks at both the interaction and user levels. It is motivated and derived from differential privacy.

### Technologies
- **RecPS:** A privacy scoring method based on membership inference attacks (MIA).
- **RecLiRA:** A novel interaction-level MIA method based on likelihood-ratio attack (LiRA), designed for RecSys models.
- **Differential Privacy:** Used as a theoretical foundation for defining the privacy score based on the ratio between True Positive Rate (TPR) and False Positive Rate (FPR).
- **Recommender System Models:** Neural Collaborative Filtering (NCF) and Light Graph Convolution Network (LightGCN) are used for evaluation.
- **Datasets:** Amazon Digital Music (ADM), Amazon Beauty, and Movielens-1m (ml-1m) are used as benchmark datasets.
- **Evaluation Metrics:** Area Under the ROC Curve (AUC), TPR at low FPR, and Hit Ratio at top-k recommended items (HR@k).

### Results
- RecLiRA outperforms existing interaction-level MIA methods (MINER), achieving higher TPR in the low-FPR region.
- RecPS generates privacy scores at both the user and interaction levels, enabling finer-grained privacy-utility tradeoffs.
- Removing top-sensitive users' interactions significantly reduces model performance (HR@100).
- Selectively removing sensitive interactions based on privacy scores preserves better model utility compared to removing all interactions of sensitive users.
- The study observed a "privacy onion effect," where removing interactions or users affects the remaining interactions' and users' scores, but the effect is relatively small.
