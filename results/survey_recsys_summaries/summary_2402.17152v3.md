# Summary of 2402.17152v3.md

**Token Usage**: Input: 32218, Output: 752, Total: 32970

---

### Main Idea
- **Problem:** Deep Learning Recommendation Models (DLRMs) struggle to scale effectively with increasing computational resources despite being trained on vast datasets with numerous features. This is a significant limitation in industrial recommendation systems.
- **Proposed Solution:** The paper introduces Generative Recommenders (GRs), a new paradigm that reformulates recommendation as a sequential transduction task within a generative modeling framework. GRs use a novel architecture called Hierarchical Sequential Transduction Units (HSTU) designed to handle high cardinality, non-stationary streaming recommendation data.
- **Motivation and Significance:** Inspired by the success of Transformers in language and vision, the authors revisit fundamental design choices in recommendation systems. By treating user actions as a new modality in generative modeling, GRs aim to improve both efficiency and model quality in large-scale recommendation tasks. The empirical demonstration of scaling laws in recommendation systems, similar to those observed in LLMs, is a key contribution.

### Technologies
- **Generative Recommenders (GRs):** A new paradigm replacing DLRMs by sequentializing and unifying the heterogeneous feature space in DLRMs.
- **Hierarchical Sequential Transduction Units (HSTU):** A novel sequential transduction architecture designed for large, non-stationary vocabularies. HSTU modifies the attention mechanism for large, non-stationary vocabulary and exploits characteristics of recommendation datasets. HSTU consists of Pointwise Projection, Spatial Aggregation (Pointwise Aggregated Attention Mechanism), and Pointwise Transformation.
- **M-FALCON (Microbatched-Fast Attention Leveraging Cacheable OperatioNs):** A new algorithm that amortizes computational costs via micro-batching to serve complex GR models with the same inference budget as traditional DLRMs. This algorithm handles candidates in parallel by modifying attention masks and biases.
- **Stochastic Length (SL):** An algorithm that increases the sparsity of user history sequences by leveraging the temporal repetitiveness of user behaviors. This reduces the computational cost of attention mechanisms.
- **Rowwise AdamW Optimizers:** Used to alleviate memory pressure associated with large vocabulary embeddings by placing optimizer states on DRAM.
- **Datasets:** Evaluated on synthetic datasets, public datasets (MovieLens, Amazon Reviews), and deployments on a large internet platform with billions of daily active users.
- **Evaluation Metrics:** NDCG, Hit Rate, Normalized Entropy (NE), log perplexity.

### Results
- **Performance Improvements:** HSTU outperforms baselines (including FlashAttention2-based Transformers and SASRec) over synthetic and public datasets by up to 65.8% in NDCG.
- **Efficiency Gains:** HSTU is 5.3x to 15.2x faster than FlashAttention2-based Transformers on 8192 length sequences. M-FALCON enables serving 285x more complex GR models while achieving 1.50x-2.99x speedups with the same inference budget.
- **Online A/B Tests:** HSTU-based Generative Recommenders with 1.5 trillion parameters improve metrics in online A/B tests by 12.4% and have been deployed on multiple surfaces of a large internet platform.
- **Scaling Laws:** The model quality of Generative Recommenders empirically scales as a power-law of training compute across three orders of magnitude, up to GPT-3/LLaMa-2 scale.
- **Ablation Studies:** Ablation studies validate the effectiveness of pointwise attention and relative attention biases in HSTU.
- **Sparsity:** Stochastic Length can significantly sparsify user history sequences without compromising model quality.
