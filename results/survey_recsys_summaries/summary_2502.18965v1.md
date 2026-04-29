# Summary of 2502.18965v1.md

**Token Usage**: Input: 10582, Output: 845, Total: 11427

---

### Main Idea

-   **Primary Research Objective:** The paper addresses the limitations of cascade ranking recommender systems by introducing OneRec, a unified end-to-end generative model for single-stage recommendation.
-   **Motivation and Significance:** Cascade ranking systems suffer from independent optimization of each stage, limiting overall performance. Generative retrieval systems (GRs) offer a promising alternative, but their accuracy lags behind cascade rankers. OneRec aims to overcome these challenges by providing a more accurate and efficient single-stage generative approach.
-   **Proposed Approach/Solution:** OneRec employs an encoder-decoder architecture with sparse Mixture-of-Experts (MoE) for scaling model capacity. It uses a session-wise generation approach to capture contextual coherence and an Iterative Preference Alignment (IPA) module combined with Direct Preference Optimization (DPO) to enhance the quality of generated recommendations.

### Technologies

-   **Key Technical Components:**
    -   Encoder-decoder architecture based on the Transformer framework.
    -   Sparse Mixture-of-Experts (MoE) to scale model capacity efficiently.
    -   Residual K-Means quantization algorithm for semantic tokenization.
    -   Iterative Preference Alignment (IPA) module.
    -   Personalized reward model for self-hard negative sampling.
-   **Algorithms/Models/Frameworks:**
    -   Transformer-based encoder-decoder model (similar to T5).
    -   Direct Preference Optimization (DPO) and variants (IPO, cDPO, rDPO, CPO, simPO, S-DPO).
    -   Balanced K-means for codebook construction.
-   **Datasets/Evaluation Metrics/Experimental Setups:**
    -   Large-scale industry datasets from Kuaishou, a short video recommendation platform.
    -   Evaluation metrics: session watch time (swt), view probability (vtr), follow probability (wtr), and like probability (ltr).
    -   Offline experiments comparing OneRec with various baseline methods (SASRec, BERT4Rec, FDSA, TIGER, DPO variants).
    -   Online A/B testing on Kuaishou's main page with 1% traffic.
-   **Novel Technical Contributions/Innovations:**
    -   Unified end-to-end generative recommendation framework that surpasses traditional multi-stage ranking pipelines.
    -   Session-wise generation approach to model contextual information.
    -   Novel self-hard negative sample selection strategy based on a personalized reward model.
    -   Iterative Preference Alignment (IPA) strategy combined with DPO.

### Results

-   **Main Experimental Findings:** OneRec outperforms traditional pointwise and listwise methods, as well as other DPO variants, in offline experiments. Scaling model size consistently improves performance.
-   **Quantitative Results/Performance Improvements:**
    -   OneRec-1B achieves 1.78% higher maximum swt and 3.36% higher maximum ltr compared to TIGER-1B.
    -   OneRec-1B+IPA surpasses the base OneRec-1B by 4.04% in maximum swt and 5.43% in maximum ltr with only 1% DPO training ratio.
    -   Online A/B testing showed a 1.68% improvement in total watch time and a 6.56% improvement in average view duration when deployed on Kuaishou.
-   **Key Insights/Discoveries:**
    -   Session-wise modeling is advantageous for maintaining contextual coherence.
    -   A small ratio of DPO training yields substantial gains.
    -   IPA strategy is more effective than other DPO implementations.
    -   Scaling model capacity consistently improves accuracy.
-   **Limitations/Future Work:**
    -   The model exhibits limitations in interactive indicators (likes).
    -   Future work aims to enhance the model's capability in multi-objective modeling to provide a better user experience.
