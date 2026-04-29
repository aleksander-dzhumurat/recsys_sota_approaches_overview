# Summary of 2507.13622v1.md

**Token Usage**: Input: 12157, Output: 799, Total: 12956

---

### Main Idea
- **Core Concept**: The paper addresses the problem of personalized news recommendation by proposing a novel method (IP2) that explicitly models entity-guided reading interest at both intra-news and inter-news levels, aligning with the observed three-step news selection behavior: scanning, title reading, and clicking.
- **Motivation and Significance**: Current news recommendation methods often overlook the unique role played by entities in guiding user interest. This research emphasizes that entities are crucial in the news selection process, especially during the initial scanning and title reading phases, and aims to improve recommendation accuracy by effectively leveraging entity information.
- **Proposed Approach**: IP2 uses a Transformer-based entity encoder with signature entity-title contrastive pre-training to capture intra-news entity interest and a dual-tower user encoder with cross-attention to capture inter-news entity and semantic-guided reading preferences. This approach mimics how users scan for entities and subsequently make click decisions based on title reading influenced by those entities.

### Technologies
- **Transformer-based Entity Encoder**: A Transformer-based encoder aggregates mentioned entities in a news title into a signature entity representation, capturing the contextual importance of each entity.
- **Signature Entity-Title Contrastive Pre-training**: A self-supervised learning approach is used to initialize entity embeddings with proper meanings by contrasting signature entities with news titles. The contrastive learning includes losses for title-title similarity, entity-entity similarity, and entity-title similarity.
- **Dual-Tower User Encoder**: Two parallel attention towers capture inter-news reading interest from both the title (semantic) and entity aspects.
- **Cross-Attention Mechanism**: A cross-attention mechanism between the two towers calibrates title reading interest using inter-news entity interest, aligning with real-world behavior.
- **Learnable Aggregation Layer**: Adjusts the importance of entity guidance in news recommendations, allowing for personalized weighting of entity and semantic information.
- **Datasets**: MIND (small and large versions) and Adressa1week are used for experimental evaluation.
- **Evaluation Metrics**: AUC, MRR, nDCG@5, and nDCG@10 are used to measure the performance of the recommendation system.
- **Baselines**: Several state-of-the-art neural and knowledge-aware news recommendation methods, including NRMS, GERL, HieRec, PLM-NR, UNBERT, DIGAT, PUNR, TDNR-C2, DKN, KRED, UaG, GREP, FUM, PerCoNet, and GLORY, are used for comparison.

### Results
- **State-of-the-Art Performance**: IP2 achieves state-of-the-art performance on both MIND and Adressa1week datasets, outperforming all compared baseline methods.
- **Ablation Studies**: Ablation experiments demonstrate that all proposed components (intra-news entity interest probing, inter-news entity guidance, and learnable aggregation) are necessary to improve the performance.
- **Contrastive Pre-training Effectiveness**: The signature entity-title contrastive pre-training is shown to be effective in initializing entity embeddings and probing intra-news entity focus, outperforming setups that use TransE-Wikidata embeddings.
- **Impact of Model Size**: Larger PLMs generally lead to better performance, while the size of the SEE has an optimal point (L=2), beyond which performance declines, possibly due to overfitting.
- **Real-World Case Study**: A case study illustrates IP2's effectiveness in capturing real-world user interest and balancing entity and semantic information for more accurate recommendations.
- **Key Insights**: The study highlights the importance of fine-grained entity guidance at both intra-news and inter-news levels, as well as the capability of language models to understand entities and enhance recommendation systems through contrastive pre-training.
