# Summary of 2309.08939v1.md

**Token Usage**: Input: 9240, Output: 743, Total: 9983

---

### Main Idea
- The paper addresses the challenge of jointly training multi-domain models for search and recommendation (S&R) systems, especially in scenarios where data is imbalanced, items are heterogeneous, and negative transfer can occur.
- The authors propose a novel Search and Recommendation Multi-Domain Foundation model (S&R Foundation) that leverages Large Language Models (LLMs) to extract domain-invariant text features, helping to mitigate these issues.
- The core idea is to use these domain-invariant text features, in conjunction with other features and a domain-adaptive multi-task learning approach, to improve the performance of S&R systems, particularly in cold start situations.

### Technologies
- **Large Language Models (LLMs)**: Used to extract domain-invariant text features from queries and items. Examples include BERT, GPT, and ChatGLM.
- **Aspect Gating Fusion**: A novel fusion mechanism to combine ID features, domain-invariant text features from LLMs, and task-specific sparse features. Different strategies are used: Mean-Gating, [CLS]-Gating, and Domain-Gating
- **Domain Adaptive Multi-Task (DA-MTL) Module**:  This module addresses domain shift by mapping inputs from multiple domains into a common vector space using domain embeddings and domain-specific linear transformations. Jensen-Shannon Divergence (JS) and Maximum Mean Discrepancy (MMD) are compared as divergence metrics. Multi-gate Mixture of Experts (MMoE) are used.
- **User-Query-Item Encoding Module:** Extracts user, query, and item representations, including ID embeddings, token-level text embeddings, and sparse feature embeddings.
- **Datasets:** Experiments were conducted on real-world datasets from Alipay Search Ranking and Query Recommendation, consisting of 7 industrial datasets.
- **Evaluation Metrics:** Click-Through Rate (CTR) prediction and query-item relevance prediction. AUC is used to compare performance. Also, Page View Click Through Rate (PVCTR) is used for online A/B testing.

### Results
- The S&R Multi-Domain Foundation model, particularly when combined with the MMoE-DA-JS configuration, achieved state-of-the-art (SOTA) performance compared to other multi-domain and multi-task models on several tasks (Task 4, 5, 6, 7). Specifically, MMoE-DA-JS achieved AUC improvement of +0.0404, +0.0192, +0.0297, +0.0131 respectively.
- Experiments showed that Domain-Gating achieves the best AUC performance (+0.0139 absolute gain over mean-pooling)
- The use of domain-invariant text features extracted by LLMs, along with the Aspect Gating Fusion network, improved performance compared to methods without token embeddings or randomly initialized embeddings. Freezing pretrained parameters in level 𝐿 0 and 𝐿 1 achieves better performance than other split methods (+0.0043 absolute gain in AUC)
- Supervised fine-tuning (SFT) of the S&R Foundation model in cold start scenarios outperformed training single-domain models on tasks such as Service Card Recommendation (+0.0216 AUC) and Content Query Recommendation (+0.0279 AUC).
- Online A/B testing in the Service Card Recommendation scenario demonstrated a +17.54% relative gain in PVCTR over the baseline single-domain model, confirming the effectiveness of the approach in real-world deployments.
