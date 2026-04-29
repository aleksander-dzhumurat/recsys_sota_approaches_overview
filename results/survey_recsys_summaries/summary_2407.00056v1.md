# Summary of 2407.00056v1.md

**Token Usage**: Input: 13561, Output: 793, Total: 14354

---

### Main Idea
- The paper addresses the problem of live streaming gifting prediction, which is crucial for enhancing user experience and increasing streamer revenue on platforms like Kuaishou.
- Existing methods struggle to capture the real-time content changes in live streams using limited categorical information and face sparsity issues in gifting behaviors, making it difficult to model user preferences accurately.
- The authors propose MMBee, a method based on real-time Multi-Modal Fusion and Behavior Expansion. MMBee leverages a Multi-modal Fusion Module with Learnable Query (MFQ) to process dynamic content and a Graph-guided Interest Expansion (GIE) approach to alleviate data sparsity by learning user and streamer representations on large-scale gifting graphs.

### Technologies
- **Multi-modal Fusion Module with Learnable Query (MFQ):** This module processes visual frames, text comments, and speech from live streaming segments. It uses orthogonal projection to maximize complementarity between modalities and learnable query tokens to extract streamer-aware content patterns.
- **Graph-guided Interest Expansion (GIE):** This approach constructs User-to-Author (U2A) and Author-to-Author (A2A) graphs based on gifting history. It uses graph contrastive learning (GraphCL) for graph node representation pre-training and metapath-based behavior expansion to enrich sparse behavior sequences.
- **Graph Construction:** The U2A graph represents the correlation between users and authors based on donation history, while the A2A graph represents the interdependence among authors using Swing similarity.
- **Metapath-guided Neighbors:** The paper defines metapaths like 𝑈𝑠𝑒𝑟 → 𝐴𝑢𝑡ℎ𝑜𝑟 → 𝐴𝑢𝑡ℎ𝑜𝑟 to capture specific structural relations between objects and expands the behavior sequence of users and authors using these metapaths.
- **Training and Inference Infrastructure:** The model is trained on Kuaishou's large-scale distributed training system using real-time preprocessed logs. The metapath-guided neighbors are pre-computed and stored in a Graph Behavior Offline Storage for efficient online access.
- The foundational model used for GTR (Gift-Through-Rate) prediction is SIM (Search-based Interest Model), chosen for its industry adoption, online efficiency, and effectiveness.
- Datasets: Kuaishou internal dataset (3 billion user interaction logs), TikTok, and MovieLens. Evaluation metrics: AUC, UAUC, GAUC, Recall@10, Precision@10, and NDCG@10.

### Results
- MMBee achieves significant performance improvements on both the Kuaishou real-world streaming dataset and public datasets (TikTok and MovieLens).
- On the Kuaishou dataset, MMBee shows improvements of 0.1646% in AUC, 1.1439% in UAUC, and 1.2057% in GAUC compared to the SIM baseline.
- Online A/B tests on Kuaishou's live streaming main page demonstrate a 2.862% increase in NGU (Number of users who sent gifts) and a 4.775% increase in NGC (the total number of gifts sent).
- Ablation studies highlight the importance of both the MFQ module and the GIE module, with visual modality being the most influential.
- Visualization of learnable query representations shows distinct clustering of authors based on content type (e.g., chatting vs. gaming).
- The online response time of MMBee is only about 1 ms more than the baseline system, showing its efficiency in a real-world deployment.
- MMBee has been deployed on the live-streaming recommendation system of Kuaishou, serving millions of active users every day and bringing considerable revenue increments for the platform.
