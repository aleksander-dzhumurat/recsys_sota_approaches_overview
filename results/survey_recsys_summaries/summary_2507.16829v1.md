# Summary of 2507.16829v1.md

**Token Usage**: Input: 16222, Output: 599, Total: 16821

---

### Main Idea

-   The paper addresses the growing problem of unwanted content being recommended by online platforms, which leads to decreased user satisfaction and broader societal issues like misinformation.
-   Current mitigation strategies, like user feedback mechanisms, are often ineffective. The paper proposes a novel, model-agnostic, post-hoc method based on conformal risk control to provably limit the amount of unwanted content in personalized recommendations.
-   The method filters potentially unsafe items and replaces them with previously consumed, safe content, all while respecting a user-defined risk level. A key aspect is leveraging implicit feedback on consumed items to expand the recommendation set, mitigating a common limitation of conformal risk control.

### Technologies

-   **Conformal Risk Control**: A framework for uncertainty quantification that provides distribution-free, finite-sample guarantees on controlling a general loss function (risk). It is used to determine a threshold to filter potentially harmful items.
-   **KuaiRand Dataset**: A real-world dataset from a short-form video-sharing platform with user interaction signals, including negative feedback (e.g., "Do not recommend," "Report" buttons), and watch time.
-   **Risk Metric:** The fraction of unwanted content in the recommendations, defined as the proportion of items flagged by the user after being presented in the recommendations.
-   **Two-Stage Recommender System:**
    -   Stage 1: Filters items using the conformal risk control procedure.
    -   Stage 2: Re-ranks the filtered items using a model trained to predict watch-time.
-   **Ranking Models:** LightGCL, GFormer, SiReN, and SIGFormer (graph-based and sign-aware methods).
-   **Re-ranking Model:** Neural Collaborative Filtering (NCF).
-   **Evaluation Metrics:** Recall@k, nDCG@k, and empirical risk (fraction of unwanted content).

### Results

-   The proposed method provably reduces unwanted content in recommendations with minimal performance degradation.  It ensures that the empirical reduction of unwanted content is equal to or better than the desired target.
-   Replacing potentially unwanted items with safer ones (previously consumed and not flagged) is more effective than simply removing items, which degrades performance significantly.
-   Sign-aware models (SiReN and SIGFormer) tend to require more item replacements than unsigned models (LightGCL and GFormer) to achieve the same level of risk control, potentially due to the sparsity of negative feedback data.
-   Filtering replacement items based on their initial watch time is crucial for maintaining risk control guarantees. Stricter filtering reduces the pool of candidate items but restores risk control.
-   The risk control procedure is biased toward high-reporting users; low-reporting users experience a greater reduction in unwanted content at lower risk values, suggesting that the global threshold is influenced disproportionately by high-reporting users.
