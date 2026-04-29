# Summary of 2506.15267v1.md

**Token Usage**: Input: 4895, Output: 745, Total: 5640

---

### Main Idea
- The paper addresses the item cold-start problem in online recommendation systems, specifically for short video platforms like Douyin. The cold-start problem hinders the promotion of new items due to a lack of historical interaction data.
- The motivation is to enable high-quality new items to gain traction, provide feedback to inspire creators, and improve the fairness, interaction, and diversity of recommendations, ultimately leading to long-term creator retention.
- The paper introduces "Next-User Retrieval," a novel framework that uses a generative next-user modeling approach, inspired by lookalike modeling, to enhance cold-start recommendations. The system aims to identify and leverage relationships between users who have interacted with similar items to predict the next potential user to interact with a cold-start item.

### Technologies
- **Transformer-based Model:** The core of the proposed system is a transformer-based model designed to capture unidirectional relationships among recently interacted users. It's used to generate the next potential user most likely to interact with the item.
- **Sequential UID Embeddings:** The system leverages interaction sequences (likes, comments) to represent users who interact with the item.
- **Prefix Prompt Embeddings:** Item features (ID, category) are used as prefix prompts to enhance the sequential user modeling. This addresses the limitations of relying solely on sequence information, especially for items with limited interactions.
- **Learnable [CLS] Token:** A learnable [CLS] token is introduced to bridge the feature domain gap between the sequential user embeddings and the real requesting user features.
- **Causal Attention:** Causal attention is used to model the unidirectional relationship of sequential users, ensuring that the generation of each token is conditioned on preceding tokens.
- **Loss Functions:** Three loss functions are combined for model training:
    - **Contrastive Loss:** Transforms the discrete item prediction into item representation learning, increasing the similarity between generated and ground-truth user embeddings and decreasing similarity with randomly sampled embeddings.
    - **Cross-Entropy Loss:** Leverages samples that were exposed but not interacted with, to improve model performance by considering relatively high-quality non-interaction samples.
    - **Auxiliary Loss:** Enhances UID representation learning by supervising the generation of the next UID.
- **HNSW (Hierarchical Navigable Small World) Algorithm:** The generated user embeddings are integrated into Douyin's retrieval system, which uses HNSW for efficient approximate nearest neighbor search.
- **Real-time Exposure-Grained Feature System:** A feature system to process sequential user interactions in real-time, considering storage and latency constraints in a high-traffic environment.

### Results
- The proposed Next-User Retrieval method was evaluated through both offline experiments and online A/B tests within Douyin's short-video recommendation system.
- **Offline Results:** Showed that the Next-User Retrieval model outperformed traditional lookalike methods and other variants in terms of Recall@Top20 and Recall@Top50.
- **Online Results:** Demonstrated significant improvements in Douyin, including:
    - +0.0142% increase in daily active users.
    - +0.1144% increase in publications.
    - +7.0515% increase in interactions.
- The online A/B tests confirmed that Next-User Retrieval effectively enhances the recommendation system, leading to increased user activity and content creation.
- The method has been successfully integrated into Douyin's main recommendation system, showcasing its practical applicability and scalability in a large-scale environment with over 600 million daily active users.
