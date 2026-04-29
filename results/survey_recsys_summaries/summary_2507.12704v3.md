# Summary of 2507.12704v3.md

**Token Usage**: Input: 12309, Output: 1058, Total: 13367

---

### Main Idea

- **Problem:** Recommender systems on large platforms need to understand user activity sequences to provide relevant content. Existing models are either too expensive to apply across multiple applications or lack the ability to effectively incorporate user activity history, candidate item features, and new items at scale. There is a need for a foundational model that is scalable, cost-effective, and capable of capturing interactions between user sequences and other features, while also generalizing to unseen items.
- **Motivation and Significance:** Building a large, foundational model for user activity sequences can enhance predictive performance and user engagement across various applications within a large visual discovery platform. This approach addresses the limitations of training standalone models for each application, which can be prohibitively expensive and slow down experimentation.
- **Proposed Solution:** The authors propose PinFM, a foundational model for user activity understanding. PinFM involves pretraining a large Transformer model (20B+ parameters) with extensive user activity data and then fine-tuning it for specific downstream recommender system applications. Innovative techniques, such as the Deduplicated Cross-Attention Transformer (DCAT) and int4 quantization, are used to address challenges related to cost, latency, and the ability to handle new items.

### Technologies

- **Model Architecture:** GPT2-based decoder-only transformer with Pre-LN. The use of causal attention allows for significant optimizations to the attention mechanism.
- **Pretraining:** Pretrained on two years of user activity data, focusing on categorical features like item IDs and action types rather than high-dimensional item embeddings. Training objectives include next token prediction loss, multi-token loss, and future-token loss. InfoNCE-based loss is used due to the large vocabulary size.
- **Fine-tuning:** Integrated with existing downstream ranking models (DLRM, DCN) for the Home Feed and Related Items Feed. The candidate item is incorporated into the input sequence in two ways: late fusion and early fusion. Optional sequence losses (L_ntl, L_mtl) are added in the fine-tuning stage. The learning rate of the pretrained module is set to be around 1/10 of the ranking model learning rate.
- **Infrastructure:**
    -   **Deduplicated Cross-Attention Transformer (DCAT):** An optimization that separates transformer computation into context and crossing components, storing the context component's keys and values as KV cache. Triton kernels are used to implement DCAT.
    -   **Embedding Quantization:** Post-training quantization (PTQ) using FBGEMM, converting 32-dim fp16 vectors to 32 int4 + 1 fp16 scale value + 1 fp16 bias value, and then performed bitpacking to fp32.
    -   **Serving Infrastructure:** The large ID embedding table is served on a separate CPU cluster from the GPU inference host.
-   **Data:**
    -   Pretraining dataset: 2 years of user activity history.
    -   Fine-tuning data: 3 weeks of Home Feed (HF) and Related Items (I2I) data.
-   **Evaluation Metrics:**
    -   HIT@3: Measures the performance of a ranking model by assessing whether the top three recommended items received the corresponding user action.
-   **Cold-start Item Handling:** Candidate item ID randomization and dropout on module outputs for fresh items.

### Results

- **Efficiency Improvements:** DCAT improved serving throughput by 600% and training throughput by 200%. Using length 256 sequences increased the throughput by an additional 25%. Int4 quantization reduced the embedding table size to 31.25% of its original size with negligible GPU forward pass latency overhead and a 7% reduction in overall inference API call latency.
- **Offline Experiments:**
    - Input Sequence Construction: The most complex variant, PinFM-GraphSAGE-LT, performed the best. There is a trade-off between metric improvements and model complexity.
    - Cold Start: The cold start remediation techniques boosted the save metric on items fresher than 28 days from around -4% to 17%.
    - Losses: Save metric keeps increasing as more losses are added, Hide metric improves when L_mtl is added but deteriorates when L_ftl is added.
    - Fine-tuning: Fine-tuning is critical for good performance.
    - Vocabulary Size: Steadily increase in model performance as embedding vocabulary size is scaled.
- **Online A/B Tests:**  PinFM was deployed on the Home Feed and Related Items Feed. Significant improvements were seen in sitewide saves (+1.20% for HF, +0.72% for I2I) and surface saves (+2.60% for HF, +2.09% for I2I). Increased feed diversity for both HF and I2I was also observed. In Home Feed, Fresh Saves increased 5.70% and Related Items Feed had a Fresh Saves drop of -0.82% (within acceptable range).

