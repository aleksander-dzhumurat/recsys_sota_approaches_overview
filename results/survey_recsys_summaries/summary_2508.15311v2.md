# Summary of 2508.15311v2.md

**Token Usage**: Input: 13472, Output: 670, Total: 14142

---

### Main Idea
- The paper addresses the challenges of modeling long-term user behaviors for Click-Through Rate (CTR) prediction, a crucial task in recommender systems and online advertising. Current two-stage models, while efficient, tend to limit the user's interest space by filtering behaviors from a single perspective, leading to suboptimal performance.
- The motivation is to overcome the limitations of existing two-stage models in capturing diverse user interests from long-term behavior sequences. The authors hypothesize that thoroughly exploring the user interest space can unlock the potential of long-term behaviors and improve CTR prediction.
- To address these challenges, the paper introduces DiffuMIN (Diffusion-driven Multi-Interest Network), a two-stage model that leverages a target-oriented multi-interest extraction method and a diffusion module to model long-term user behaviors and explore the user interest space thoroughly.

### Technologies
- **Orthogonal Multi-Interest Extractor (OMIE)**: This module disentangles and extracts multiple user interests by modeling the relationship between user behaviors and interest channels derived from the orthogonal decomposition of the target embedding. It involves behavior routing, channel filtering, and interest aggregation.
- **Diffusion Multi-Interest Generator (DMIG)**: Inspired by generative modeling, this module captures the distribution of users' multiple interests and generates augmented interests guided by contextual interests and interest channels. It employs a Transformer encoder as the backbone and utilizes self-attention and cross-attention mechanisms.
- **Contrastive Multi-Interest Calibrator (CMIC)**: This module leverages contrastive learning to ensure that the generated augmented interests align with a user's actual preferences, enhancing the distinguishability of interests among different users.
- **Transformer Encoder**: Utilized to model users' short-term behaviors and contextual interests.
- **Datasets**: Experiments were conducted on two public datasets (Alibaba, Ele.me) and one industrial dataset from Meituan.
- **Evaluation Metrics**: Offline experiments used Area Under Curve (AUC). Online A/B testing used Click-Through Rate (CTR) and Cost Per Mille (CPM).
- **Implementation Details**: The model was implemented in TensorFlow, using Adam as the optimizer.

### Results
- DiffuMIN achieved state-of-the-art (SOTA) performance on three real-world datasets, demonstrating its superiority over existing CTR models when modeling long-term user behaviors. Specifically, it shows RelaImpr of 5.80%, 13.96%, and 7.26% on the Industry, Alibaba, and Ele.me datasets, respectively.
- Ablation studies confirmed the contributions of individual modules within DiffuMIN, highlighting the importance of the target-oriented multi-interest extraction method, the diffusion module, and contrastive learning.
- Analysis of the OMIE module revealed that selecting an optimal number of channels and using the top-1 routing method are critical for performance.
- Comparisons with VAE-based models demonstrated the advantages of diffusion models in capturing complex distributions of user behavior and features.
- Online A/B testing in a live production environment showed a 1.52% increase in CTR and a 1.10% increase in CPM with DiffuMIN, indicating its practical effectiveness.
