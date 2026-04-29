# Summary of 2507.09969v1.md

**Token Usage**: Input: 14546, Output: 696, Total: 15242

---

### Main Idea

- **Problem:** The paper addresses the challenge of incorporating graph knowledge into the ranking stage of recommender systems (RecSys), where rich contextual information is available. While graph neural networks (GNNs) have proven effective in the retrieval stage, their application in ranking is limited by the substantial computational cost of repeatedly retrieving neighborhood information from billions of items in distributed systems.
- **Motivation:**  Improving the ranking quality in RecSys is crucial for enhancing user experience in various online applications like e-commerce, advertising, and social media. Integrating graph knowledge, which captures user-item relationships, has the potential to enhance ranking models. However, the high computational overhead associated with GNNs during training makes them impractical for real-world deployment.
- **Proposed Approach:** The authors propose a non-parametric strategy that utilizes graph convolution for re-ranking only during test time. This strategy circumvents the computational overhead of graph convolution during training. It involves constructing a graph-based similarity matrix, retrieving candidate users/items, forming augmented user-item pairs, and aggregating the predictions using a weighted fusion.

### Technologies

- **Ranking Models:**  Click-Through Rate (CTR) models, specifically DCN (Deep & Cross Network) and DCNV2, are used as baseline ranking models.
- **Graph Neural Networks (GNNs):** Graph convolution is used to incorporate graph knowledge at test time.  A linear message passing mechanism inspired by LightGCN is adapted.
- **Graph Construction:** User-item interaction bipartite graphs are constructed to represent user-item relationships.  Similarity matrices are created based on co-purchase relationships.
- **Similarity Calculation:**  Cosine similarity is used to quantify the relationship between users and items.
- **Test-Time Augmentation:** The core technology is a non-parametric graph convolution strategy applied only at test time.
- **Datasets:** Experiments are conducted on four benchmark datasets: Yelp2018, Amazon-Books, MovieLens-1M, and Anime, representing varying levels of data sparsity.
- **Evaluation Metrics:**  Recall@K and NDCG@K are used to evaluate the ranking performance.
- **Implementation:** The experiments are implemented using Recbole, a unified framework for recommendation algorithms, and conducted on an NVIDIA RTX 3090 GPU.

### Results

- **Performance Improvement:** The proposed test-time augmentation strategy consistently improves the ranking performance of various baseline models across the four datasets.  The average improvement is 8.1% in terms of NDCG and Recall metrics.
- **Efficiency:**  The strategy introduces minimal additional computational overhead.  The inference-time cost is negligible, with an average overhead of only 0.5%.
- **Comparison with Graph-Enhanced Training:**  The proposed strategy achieves performance comparable to a naive graph-enhanced ranking framework (where GNNs are used during training) but with significantly reduced computational cost (less than 2% extra time overall compared to the 480% overhead of graph-enhanced training).
- **Impact of Neighborhood Size:** The optimal number of neighbor candidates (nk) varies depending on the dataset sparsity. Larger values of nk tend to be more suitable for sparse datasets, while smaller values are more appropriate for dense datasets.
- **Robustness:** The strategy demonstrates stable improvements across various ranking models, indicating its general applicability and robustness.
