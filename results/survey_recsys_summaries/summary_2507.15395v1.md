# Summary of 2507.15395v1.md

**Token Usage**: Input: 15054, Output: 814, Total: 15868

---

### Main Idea

- **Problem:** Multi-behavior recommendation aims to improve prediction for a target behavior (e.g., purchase) by leveraging other user behaviors (e.g., views, add-to-cart). Existing methods face challenges due to distributional disparities across behaviors and negative transfer effects caused by noise in auxiliary behaviors. Distribution disparities lead to popularity bias from auxiliary behaviors and overfitting on sparse target behaviors. Noisy auxiliary behaviors (e.g., accidental clicks) can negatively impact target behavior prediction.
- **Motivation:** Overcoming data sparsity in target behaviors by effectively utilizing auxiliary behaviors is crucial for enhancing recommendation performance in real-world platforms where users interact in various ways.
- **Proposed Solution:** The paper proposes a novel model-agnostic Hierarchical Graph Information Bottleneck (HGIB) framework for multi-behavior recommendation. HGIB integrates the information bottleneck principle into a hierarchical model design to learn compact representations that preserve essential information for target behavior prediction while eliminating task-irrelevant redundancies. It also introduces a Graph Refinement Encoder (GRE) that dynamically prunes redundant edges through learnable edge dropout mechanisms to mitigate interaction noise.

### Technologies

- **Hierarchical Graph Information Bottleneck (HGIB) framework:** This is the core framework that integrates the information bottleneck principle with hierarchical model design. It learns robust representations by retaining information relevant to target behavior prediction while minimizing irrelevant noise.
- **Graph Refinement Encoder (GRE):** A component that explicitly removes noisy interactions from multi-behavior data by pruning redundant edges using a learnable edge dropout mechanism. This uses the Gumbel-softmax reparameterization trick for end-to-end learning. GRE uses LightGCN for graph aggregation.
- **Information Bottleneck (IB) Principle:** Used to formalize the trade-off between preserving predictive information about the target task and compressing irrelevant variations in intermediate representation. The objective is reformulated by deriving the lower bound of mutual information and employing HSIC for approximations.
- **Hilbert-Schmidt Independence Criterion (HSIC):** Used as an approximation for minimizing mutual information between representations at different encoder layers, encouraging compression of irrelevant information.
- **Target Attention (TA):** Used for aggregating the final representation.
- **LightGCN:** Used as a component in GRE for the graph aggregation process.
- **Datasets:** Taobao, Tmall, and Jdata (public e-commerce datasets) and two industrial datasets from WeChat (news and live-streaming recommendation).
- **Evaluation Metrics:** HR@K (Hit Ratio) and NDCG@K (Normalized Discounted Cumulative Gain) with K=10.
- **Optimization:** Adam optimizer with a learning rate of 5e-4.

### Results

- **Superior Performance:** HGIB consistently outperformed state-of-the-art multi-behavior recommendation methods on three public datasets and two industrial datasets.
- **Ablation Study:** Removing the loss terms related to preserving task-relevant information or compressing redundant information, or removing the GRE module, resulted in a decline in model performance, demonstrating the effectiveness of each component.
- **Compatibility:** HGIB demonstrated strong compatibility with other hierarchical multi-behavior methods like AutoDCS and MULE, leading to performance improvements when integrated as a framework.
- **Hyperparameter Sensitivity:** Optimal performance was achieved with moderate values for the hyperparameters controlling preservation and compression, with different datasets having slight variations in the best values.
- **Industrial Application:** HGIB showed significant performance gains on large-scale industrial datasets from WeChat for news and live-streaming recommendations. A 15-day online A/B test showed statistically significant improvements in Click-Through Rate (CTR) and Social Sharing Rate (SSR).
- **Information Abundance:** Embeddings learned by HGIB exhibit higher information abundance compared to baseline methods, indicating richer information capture and a more effective hierarchical funnel design. The information abundance decreases with increasing encoder levels, aligning with the goal of extracting task-relevant information while discarding redundant information.
