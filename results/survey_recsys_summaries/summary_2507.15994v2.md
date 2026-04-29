# Summary of 2507.15994v2.md

**Token Usage**: Input: 14700, Output: 644, Total: 15344

---

### Main Idea

- The paper addresses the challenge of scaling transformer models for recommender systems, which is difficult due to large item catalogs and dynamic user preferences. While large transformer models have shown success in NLP, computer vision, and speech, scaling them for recommender systems, especially in terms of encoder capacity, remains relatively unexplored. The paper aims to bridge this gap.
- The authors hypothesize that the scaling potential of early fusion rankers is limited by specialized network layers and propose that sequential recommenders, despite lacking structural limitations, have encoders that are too small. They introduce a novel autoregressive framework called ARGUS (Auto Regressive Generative User Sequential framework) that scales recommender transformers to one billion parameters.
- ARGUS uses a two-stage training approach: (1) pre-training with a dual objective of next-item prediction and feedback prediction, and (2) efficient fine-tuning that transforms the encoder into a two-tower architecture. This allows for offline inference and provides features for downstream models.

### Technologies

- **Model Architecture:** Transformer encoder-based sequential recommender system.
- **Training Objective:** Combines next-item prediction and feedback prediction. Next-item prediction is optimized using logQ-corrected sampled softmax with mixed negative sampling.
- **Pre-training:** Autoregressive learning on user histories. Input consists of context-item-feedback triplets.
- **Fine-tuning:** Converts the large transformer encoder into a two-tower architecture for efficient offline inference. Impression-aware, one-pass fine-tuning with pairwise ranking objective.
- **Hardware:** PyTorch 2.x with Distributed Data Parallel (DDP) across 64-256 A100 80GB GPUs.
- **Datasets:** A large-scale (300B user-item interactions) proprietary dataset sampled from a music-streaming platform, including ItemID, ArtistID, implicit and explicit feedback signals, and contextual features.
- **Evaluation Metrics:** Normalized entropy for feedback and next-item prediction during pre-training; Pairwise accuracy uplift relative to a production ranker during fine-tuning.
- **Baselines:** Production ranking model (gradient-boosted decision tree ensemble), and HSTU (a previously proposed encoder architecture).

### Results

- The paper demonstrates that ARGUS scales effectively, with consistent improvements in performance as model size increases (from 3.2M to 1B parameters). Feedback prediction entropy improves by 3-7%, next-item entropy drops by over 10%, and pairwise accuracy uplift increases from +1.35% to +2.66%.
- The proposed two-stage training pipeline (pre-training and fine-tuning) is essential for optimal performance.
- Increasing context length improves recommendation quality, yielding comparable gains to scaling model size.
- Deployment on a large-scale music platform yielded significant improvements in online A/B tests: +2.26% in total listening time and +6.37% in like likelihood, representing the largest improvement in recommendation quality reported for any deep learning-based system on the platform.
