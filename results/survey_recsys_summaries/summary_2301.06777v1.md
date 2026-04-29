# Summary of 2301.06777v1.md

**Token Usage**: Input: 3082, Output: 796, Total: 3878

---

### Main Idea
- The paper addresses the limitations of offline evaluations and the lack of side information in many recommender system studies based on self-attention models. It bridges the gap between academic research and real-world industry applications by presenting live experimental results from Zalando, a fashion industry leader.
- The core concept is to demonstrate that a single Transformer-based recommender system, trained on diverse types of user interactions with different entities (items, outfits, creators) and interaction types (clicks, purchases, wishlists), can be effectively reused across various fashion inspiration use-cases. This includes outfit ranking, outfit recommendation, and real-time personalized outfit generation, improving user retention and reducing complexity.
- The proposed solution involves a flexible and configurable recommender system that uses a Transformer architecture to model user interaction sequences and learn fashion compatibility. It integrates various data sources and features, addresses the cold-start problem, and mitigates feedback loops.

### Technologies
- **Transformer Architecture**: Utilizes standard Transformer encoders for recommendation use-cases (trained with causal language modeling) and encoder-decoder (sequence-to-sequence) Transformer architectures for personalized outfit generation.
- **Embeddings**: Represents each entity (item, outfit, creator) as a concatenation of learned embeddings corresponding to categorical features. Missing features are padded with 0s. Outfits are represented by averaging the embeddings of their constituent items. Interaction features are one-hot encoded and concatenated to the entity embedding.
- **Interaction Sequence Modeling**: Models each user as a sequence of interactions, incorporating different entities and interaction types. A target boolean mask is introduced to focus the loss function on specific entities (e.g., outfits).
- **Session Modeling**: Introduces temporal inputs in the form of interaction recency (number of days between the action timestamp and model training/serving timestamp) to model user sessions. Recency is discretized and concatenated with item features.
- **Filtering and Re-ranking Logic**: A flexible system design that follows the "inputs → scoring → filtering → re-ranking" framework, allowing for configurable filtering logic embedded in the backend. Re-ranking includes freshness rules (e.g., exponential age decay) and diversification heuristics (e.g., similarity-based diversification, multi-armed bandit sampling).
- **Backend Architecture**: Couples input data processing with the model to avoid duplication of serving and training logic, reduce network latencies, and decrease backend complexity. Entity data lives as a mapping on the same service as the model.

### Results
- **User Retention Improvement**: Live experiments demonstrated improvements in user retention of up to 30% compared to existing algorithms.
- **Outperformance of Baselines**: The Transformer-based recommender system outperformed baselines like Learning to Rank (LTR), CNN-embedding-based k-Nearest Neighbors (kNN), and Siamese Networks (SN) across different use-cases.
- **Significant Gains in User Engagement**: Achieved substantial increases in user engagement, with gains of up to +130.4% in cold-start scenarios and +28.5% overall in outfit catalog ranking compared to LTR. For style preview carousel ranking the increase was up to +39.7% in cold start and +23.9% overall. Get-the-look improved by 130% against the CNN-KNN.
- **Personalized Outfit Generation Improvements**: Showed improvements in user engagement (+5.79%) and retention (+11.20%) compared to Siamese Nets for personalized outfit generation. A fallback model consisting of a Transformer with single-embedding output further improved the results when dealing with undersupply due to business rule filtering.
- **Latency and Scalability Improvements**: The system achieved roughly twice as low p99 latency and scaled substantially better (roughly by a factor of 3) compared to an existing ranking system based on TensorFlow-ranking.
