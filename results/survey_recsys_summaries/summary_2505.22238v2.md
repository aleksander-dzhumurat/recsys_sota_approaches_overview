# Summary of 2505.22238v2.md

**Token Usage**: Input: 9703, Output: 689, Total: 10392

---

### Main Idea
- The paper introduces Yambda-5B, a large-scale, publicly available dataset of music listening interactions sourced from Yandex.Music. The dataset aims to address the limitations of existing datasets used in recommender systems research by providing data at an industrial scale.
- The motivation stems from the gap between academic research and real-world industrial scenarios, where models trained on smaller datasets often lose efficacy when scaled up. The significance lies in providing a resource that enables researchers to validate model scaling hypotheses, develop methods for extreme data sparsity, and improve reproducibility in recommender systems research.
- The core of the work involves the collection, preprocessing, and release of the Yambda-5B dataset. It includes 4.79 billion user-item interactions from 1 million users across 9.39 million tracks. A key innovation is the "is_organic" flag, which distinguishes organic user actions from recommendation-driven events. The authors also introduce a Global Temporal Split (GTS) based evaluation protocol for benchmarking recommendation algorithms.

### Technologies
- **Dataset**: Yambda-5B, comprising 4.79 billion listening events, likes, dislikes, unlikes, and undislikes from 1 million users across 9.39 million tracks. Includes two subsampled versions: Yambda-500M and Yambda-50M.
- **Data Format**: Apache Parquet, available in both flat (tabular) and sequential formats. Includes user and track anonymization, numerical identifiers, and relational mappings.
- **Evaluation Protocol**: Global Temporal Split (GTS) scheme with a 30-minute gap between the training and test sets to avoid data leakage.
- **Audio Embeddings**: Neural embeddings derived from a convolutional neural network trained in a contrastive manner on audio spectrograms.
- **Baseline Algorithms**:
    - MostPop (overall item popularity)
    - DecayPop (time-decayed variant of MostPop)
    - ItemKNN (neighborhood-based collaborative filtering)
    - iALS (matrix factorization for implicit feedback)
    - BPR (pairwise ranking optimization)
    - SANSA (scalable EASE framework)
    - SASRec (transformer-based sequential model)
- **Evaluation Metrics**: NDCG@k, Recall@k, and Coverage@k, where k ∈ {10, 100}.
- **Hyperparameter Tuning**: OPTUNA framework.

### Results
- The paper presents benchmark results for the listed baseline algorithms on the Yambda-50M, Yambda-500M, and Yambda-5B datasets, evaluating performance under two feedback setups: "Listen +" (implicit feedback) and "Like" (explicit feedback).
- ItemKNN and SASRec consistently performed well in the "Listen +" scenario across all dataset scales, whereas DecayPop showed superior performance in the "Like" scenario.
- The evaluation framework highlighted the degraded performance of conventional collaborative filtering methods (e.g., Matrix Factorization) in scenarios requiring real-time interaction processing, underscoring the need for sequence-aware architectures like Transformers.
- The authors suggest future work focusing on enhanced temporal evaluation protocols, multi-modal recommendation paradigms leveraging audio embeddings and track metadata, and comprehensive analysis of behavioral differences between organic and recommendation-driven interactions.
