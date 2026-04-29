# Summary of 2403.13574v2.md

**Token Usage**: Input: 15351, Output: 768, Total: 16119

---

### Main Idea

- **Primary Research Objective:** The paper addresses the problem of improving video and comment recommendations on online video platforms by leveraging user interaction histories with both videos and comments.
- **Motivation and Significance:** Existing recommender systems primarily focus on video interactions, neglecting the valuable information contained in comment content and user-comment interactions. Since a significant portion of users actively engage with comments, incorporating this data can enhance recommendation quality and user engagement. The paper aims to create a unified framework that models both videos and comments.
- **Proposed Approach (LSVCR):** The authors propose a novel framework called LSVCR (Leveraging Sequential Recommendation with Large Language Models for Joint Video and Comment Recommendation). LSVCR combines a conventional sequential recommendation (SR) model (retained in deployment) for efficient user preference modeling with a supplemental large language model (LLM) recommender (discarded in deployment) to capture underlying user preferences from heterogeneous interaction behaviors. A two-stage training paradigm, personalized preference alignment and recommendation-oriented fine-tuning, is used to integrate the strengths of both components.

### Technologies

- **Sequential Recommendation (SR) Model:** This serves as the recommendation backbone for efficient user preference modeling. It encodes video and comment interaction sequences using Transformer layers. The specific architecture of the SR model is not explicitly specified, but it uses multi-head attention for cross-fusion of video and comment sequence representations. Additive attention is used to extract user video preferences, while a query-based attention mechanism, using the current video's title embedding as the query, extracts user comment preferences.
- **Large Language Model (LLM) Recommender:** This model acts as a supplement to enhance the semantics of the SR model. It's not used in deployment due to computational cost. The paper utilizes ChatGLM3 as the LLM backbone and performs low-rank adaptation based on LoRA. The LLM is used to generate textual instructions from user interaction histories to leverage its semantic understanding and knowledge reasoning capabilities.
- **Training Paradigm:**
    - **Personalized Preference Alignment:** This stage aligns the preference representations of the SR model with the LLM recommender using contrastive learning losses. This involves sequential-supplemental preference contrast and video-comment preference contrast. The goal is to enhance the semantics of the SR model. Comment diversification augmentation is also applied to ensure input consistency across components.
    - **Recommendation-Oriented Fine-Tuning:** This stage discards the LLM recommender and fine-tunes the alignment-enhanced SR model for specific video and comment recommendation tasks. Video ID embeddings are incorporated to enhance performance, and an ID-text regularization loss is introduced.
- **Dataset and Metrics:**
    - A large-scale industrial dataset from the KuaiShou platform consisting of user interaction logs with videos and comments.
    - Evaluation metrics: Recall@K, NDCG@K, and MRR (K=5, 10).

### Results

- **Offline Evaluation:** LSVCR demonstrated significant improvements compared to various competitive baselines for both video and comment recommendation tasks.
- **Online A/B Testing:** Deployed on the KuaiShou platform, LSVCR achieved a cumulative gain of 4.13% in comment watch time and a 1.36% gain in interaction number. This indicates the practical benefits of the approach in a real-world industrial recommender system.  The gains in comment watch time are especially notable.
- **Ablation studies** showed the contribution of various components, with removing the alignment stage hurting performance the most.
- **Generalization:** LSVCR's core techniques were shown to be generalizable to item recommendation tasks in the Amazon dataset.
