# Model Overview

Sources:
- `sources/survey_of_recommender_systems.md` — Zou & Sun, 2025 ("A Survey of Real-World Recommender Systems")
- `sources/RecSys_2025_findings.md` — ACM RecSys 2025, Prague (arXiv preprints found 2026-04-27)

---

## Generative / Foundation Models

| Model | Reference | Description |
|---|---|---|
| OneRec | [26] | Unify retrieve & rank with generative recommender; iterative preference alignment (Kuaishou) |
| 360Brew | [34] | Decoder-only foundation model for personalized ranking and recommendation |
| MTGR | [42] | Industrial-scale generative recommendation framework (Meituan) |
| PinRec | [3] | Outcome-conditioned multi-token generative retrieval at industry scale (Pinterest) |
| Actions Speak Louder | [169] | Trillion-parameter sequential transducers for generative recommendations |

## Sequential & CTR Models

| Model | Reference | Description |
|---|---|---|
| TWIN-V2 | [123] | Ultra-long user behavior sequence modeling via divide-and-conquer (Kuaishou) |
| SASRec | [63] | Sequential recommendation; referenced for popularity-bias mitigation |
| PLE (Progressive Layered Extraction) | [130] | Multi-task learning model for personalized recommendations |
| DPAN | [25] | Dynamic Preference-based and Attribute-aware Network for relevant recommendations |
| ATBRG | [33] | Adaptive Target-Behavior Relational Graph Network for recommendation |
| Diag-LinUCB | §4.1.4 | Real-time bandit system for million-scale queries per second (video) |

## Graph Neural Network Models

| Model | Reference | Description |
|---|---|---|
| M2GRL | [137] | Multi-task Multi-view Graph Representation Learning; trained on 57B samples (Taobao) |
| M2GNN | [46] | Metapath and Multi-interest Aggregated Graph Neural Network for cross-domain rec |
| MMGCL | [58] | Meta Knowledge-Enhanced Multi-view Graph Contrastive Learning |
| Gemini | [156] | Heterogeneous graph information fusing framework for online recommendations (Taobao) |
| STGIN | [91] | Spatial-Temporal Graph Interaction Network for large-scale POI recommendation |

## Cross-Domain / Transfer Models

| Model | Reference | Description |
|---|---|---|
| DDCDR | [2] | Disentangle-based Distillation Framework for Cross-Domain Recommendation |
| EXIT | [48] | EXplicit Interest Transfer Framework for Cross-Domain Recommendation |
| M5 | [186] | Multi-Modal Multi-Interest Multi-Scenario Matching for OTT recommendation |

## LLM-Augmented Models

| Model | Reference | Description |
|---|---|---|
| ReLand | [132] | Integrates LLM insights into industrial recommenders |
| LARR | [135] | LLM-Aided Real-time Scene Recommendation |

## Multi-Task / Multi-Objective Models

| Model | Reference | Description |
|---|---|---|
| GradCraft | [5] | Holistic gradient crafting for multi-task recommendations |
| STAN | [76] | Stage-Adaptive Network for multi-task recommendation |
| MLoRA | [163] | Multi-domain Low-Rank Adaptive Network for CTR prediction |

## Cold-Start Models

| Model | Reference | Description |
|---|---|---|
| PURS | [75] | Personalized Unexpected Recommender System for improving user satisfaction |
| BOSS | [45] | Bilateral Occupational-Suitability-Aware Recommender for online recruitment |

## Retrieval / Embedding Models

| Model | Reference | Description |
|---|---|---|
| ItemSage | [6] | Product embeddings for shopping recommendations (Pinterest) |
| RUEL | [147] | Retrieval-Augmented User Representation with Edge browser logs |

## Audio / Playlist Models

| Model | Reference | Description |
|---|---|---|
| Hydrus | [168] | Personalized Quality of Experience in short-form video services |

## Efficiency / Compression Models

| Model | Reference | Description |
|---|---|---|
| Shark | [171] | Lightweight model compression for large-scale recommenders |
| GreenSeq | [116] | Automatic green network design for sequential recommendation |
| AutoGroup | [87] | Automatic feature grouping for modelling high-order feature interactions in CTR |
| AutoOpt | [79] | Automatic hyperparameter scheduling and optimization for deep CTR prediction |

## Bandit / Reinforcement Learning Models

| Model | Reference | Description |
|---|---|---|
| RPAF | [127] | Reinforcement Prediction-Allocation Framework for cache allocation in large-scale RecSys |
| Reloop | [12] | Self-correction continual learning loop for recommender systems |

## Other Named Systems

| Model | Reference | Description |
|---|---|---|
| BOLT | [100] | Automated deep learning framework for training and deploying search & recommendation models |
| SAR-Net | [119] | Scenario-Aware Ranking Network for personalized fair recommendation (travel) |
| SASNet | [190] | Stage-Aware Sequential Matching for online travel recommendation |
| MODEM | [73] | Shared-account video recommendation decoupling (large screen devices) |
| WG4Rec | [122] | Word Graph for news recommendation |
| NxtPost | [114] | User-to-post recommendations in Facebook Groups |
| CausCF | [154] | Causal Collaborative Filtering for recommendation effect estimation |
| MIC | [104] | Model-agnostic Integrated Cross-channel Recommender |
| Mirror | [189] | Multi-view Reciprocal Recommender System for online recruitment |
| MMBee | [27] | Live streaming gift-sending recommendations via multi-modal fusion |
| SEMI | [70] | Sequential Multi-modal Information Transfer network for e-commerce micro-video |
| CEC | [69] | Causality Enhanced Conversion model |
| SLH-BIA | [108] | Short-Long Hawkes Process for Buy-It-Again recommendations at scale |

---

## RecSys 2025 — Generative & Retrieval Models

| Model | arXiv | Description |
|---|---|---|
| GRACE | 2507.14758 | Generative Recommendation via Journey-Aware Sparse Attention on Chain-of-Thought Tokenization (Walmart Global Tech) |
| GenSAR | 2504.05730 | Unifying Balanced Search and Recommendation with Generative Retrieval (Renmin University) |
| Prompt-to-Slate | 2408.06883 | Diffusion models for prompt-conditioned slate generation (Spotify) |
| PinFM | — | Foundation Model for User Activity Sequences at Pinterest *(ACM-only)* |

## RecSys 2025 — Sequential & LLM-based Models

| Model | arXiv | Description |
|---|---|---|
| LONGER | 2505.04421 | Scaling Up Long Sequence Modeling in Industrial Recommenders (ByteDance) |
| MoRE | 2409.06377 | Mixture of Reflectors Framework for LLM-Based Sequential Recommendation (Renmin University) |
| LLM-RecG | 2501.19232 | Semantic Bias-Aware Framework for Zero-Shot Sequential Recommendation (UIUC) |
| USB-Rec | 2509.20381 | Framework for Improving Conversational Recommendation Capability of LLMs |
| LANCE | — | Exploration and Reflection for LLM-based Textual Attacks on News Recommender Systems *(ACM-only)* |
| Lasso | — | LLM-based User Simulator for Cross-Domain Recommendation (Sichuan University) *(ACM-only)* |
| R4ec | — | Reasoning, Reflection, and Refinement Framework for Recommendation Systems (Kuaishou) *(ACM-only)* |

## RecSys 2025 — Graph Models

| Model | arXiv | Description |
|---|---|---|
| NLGCL | 2507.07522 | Naturally Existing Neighbor Layers Graph Contrastive Learning for Recommendation (HKU) |
| HGIB | 2507.15395 | Hierarchical Graph Information Bottleneck for Multi-Behavior Recommendation (CUHK) |

## RecSys 2025 — Multi-Task & Multi-Objective Models

| Model | arXiv | Description |
|---|---|---|
| Paragon | 2410.10639 | Parameter Generation for Controllable Multi-Task Recommendation (Renmin University) |

## RecSys 2025 — Multimodal Models

| Model | arXiv | Description |
|---|---|---|
| VL-CLIP | 2507.17080 | Multimodal Recommendations via Visual Grounding and LLM-Augmented CLIP Embeddings (Walmart Global Tech) |

## RecSys 2025 — Embedding & Efficiency Models

| Model | arXiv | Description |
|---|---|---|
| LEAF | — | Lightweight, Efficient, Adaptive and Flexible Embedding for Large-Scale Recommendation (USC) *(ACM-only)* |
| MDSBR | — | Multimodal Denoising for Session-based Recommendation *(ACM-only)* |

## RecSys 2025 — Other Named Models

| Model | arXiv | Description |
|---|---|---|
| IP2 | — | Entity-Guided Interest Probing for Personalized News Recommendation *(ACM-only)* |
| RecPS | — | Privacy Risk Scoring for Recommender Systems (UMBC) *(ACM-only)* |
