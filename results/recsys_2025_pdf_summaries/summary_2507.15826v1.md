### Main Idea
- The paper addresses the challenge of integrating natural language interfaces into music recommender systems. Current approaches using Large Language Models (LLMs) are computationally expensive and have limitations in real-world deployment. Retrieval-based methods using smaller language models exist but often overlook multimodal item representations, long-term user preferences, and require complete model retraining.
- The authors propose JAM (Just Ask for Music), a lightweight framework that models user-query-item interactions as vector translations in a shared latent space. This is inspired by knowledge graph embedding methods. JAM aims to provide accurate recommendations by aggregating multimodal item features and capturing user's long-term tastes.
- The proposed solution involves modeling personalized recommendations by treating queries as translations from users to items, optimizing an equation of the form u + q ≈ t. It also explores various strategies to aggregate heterogeneous sources of item information.

### Technologies
- **JAM Framework**: A lightweight framework for natural language music recommendation.
- **Vector Translation**: Modeling user-query-item interactions as vector translations in a shared latent space, inspired by TransE.
- **Multimodal Item Feature Aggregation**:
    - Averaging (AvgMixing): Simple averaging of multimodal representations.
    - Cross-Attention (CrossMixing): Dynamically adjusting the weighting of modalities using cross-attention.
    - Sparse Mixture of Experts (MoEMixing): Combining representations from different modalities using Noisy Top-K gating.
- **ModernBert-base**: Text encoder used to obtain dense representations of queries.
- **User/Item Embeddings**: Collaborative filtering embeddings, audio embeddings (extracted via contrastive learning), and lyrics embeddings (created using multilingual-e5-base).
- **Loss Function**: BPR (Bayesian Personalized Ranking) loss.
- **Dataset**: JAMSessions, a new dataset of over 100k user-query-item triples with precomputed embeddings for users and items.
- **Evaluation Metrics**: Recall and Normalized Discounted Cumulative Gain (NDCG) at cut-off thresholds of 10 and 100.
- **Experimental Setup**: Experiments are based on real-world data from Deezer with a chronological split for training, validation, and testing. Models are trained for 50 epochs with AdamW optimizer and cosine annealing learning rate scheduler.
- **DeepSeek-R1-Distill-Qwen-7B**: LLM used to augment user queries by exploiting playlist title and descriptions.

### Results
- JAM variants outperform baseline models (TalkRec and TwoTower) in terms of Recall and NDCG at both 10 and 100 cut-off thresholds.
- CrossMixing consistently achieves the best performance among different multimodal aggregation strategies. AvgMixing is also effective, while MoEMixing shows a drop in accuracy, suggesting that all modalities contribute valuable information.
- Qualitative analysis demonstrates that modeling queries as translations in the user-item space enables personalized recommendations based on user preferences and query intent.
- The framework can deliver personalized music recommendations from natural language queries. A limitation arises with artist-specific requests due to data sparsity.
