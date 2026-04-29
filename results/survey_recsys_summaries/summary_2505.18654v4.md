# Summary of 2505.18654v4.md

**Token Usage**: Input: 9031, Output: 586, Total: 9617

---

### Main Idea

- The paper introduces Meituan Generative Recommendation (MTGR), a novel industrial-scale generative recommendation framework designed to effectively scale ranking models while retaining the benefits of traditional Deep Learning Recommendation Models (DLRM).
- MTGR addresses the limitations of DLRM in handling exponential user behavior growth and high training/inference costs by adopting a Generative Recommendation Model (GRM) approach with user-level compression.
- The key innovation lies in maintaining the inputs consistent with DLRM, including well-designed cross features, while reorganizing the features by converting user and candidate features into different tokens. This approach allows for efficient model scaling without sacrificing performance, which is a common problem when scaling GRMs and ignoring cross features.

### Technologies

- **Architecture**: MTGR employs a Hierarchical Sequential Transduction Units (HSTU) architecture similar to [23] for modeling user behavior sequences.
- **Group-Layer Normalization (GLN)**: A novel normalization technique is proposed to normalize different types of tokens separately, which enables better modeling of multiple heterogeneous information simultaneously
- **Dynamic Masking**: A dynamic masking strategy with full-attention, auto-regressive and visibility only to itself is used to prevent information leakage and improve performance.
- **Training Framework**: The training framework is built on TorchRec and optimized for computational efficiency, including dynamic hash tables for embedding management, dynamic sequence balancing, embedding ID de-duplication, automatic table merging, mixed precision training, and operator fusion.
- **Dataset**: A large, real-world industrial-scale recommendation system dataset from Meituan is used, containing rich cross features and long user behavior sequences.
- **Evaluation Metrics**: Offline evaluations use AUC and GAUC for CTR and CTCVR prediction. Online evaluations use PV_CTR and UV_CTCVR.

### Results

- MTGR achieves 65x FLOPs for single-sample forward inference compared to the DLRM model, indicating a significant increase in computational complexity.
- Offline experiments demonstrate that MTGR outperforms DLRM baselines, with improvements of up to 0.8956% in CTR AUC and 1.4656% in CTCVR GAUC.
- Online A/B testing on the Meituan platform shows that MTGR increases conversion volumes by 1.22% and CTR by 1.31%.
- The optimized training framework improves training throughput by 1.6x - 2.4x compared to TorchRec while maintaining good scalability over 100 GPUs.
- Inference costs are reduced by 12% compared to DLRM due to MTGR's sub-linear scaling with the number of candidates.
- Ablation studies confirm the importance of cross features, GLN, and dynamic masking in achieving optimal performance.
