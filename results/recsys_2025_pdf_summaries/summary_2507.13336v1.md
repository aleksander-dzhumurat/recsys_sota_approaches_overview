### Main Idea
- **Problem**: Current graph contrastive learning methods in recommender systems (RecSys) suffer from "Ineffective Optimization" due to the decoupled design of recommendation supervision and self-supervised contrastive signals. This leads to redundant graph convolutions, conflicting gradients from separate loss functions, and unstable multi-task training, resulting in performance degradation and inefficiency.
- **Motivation**: To address the limitations of existing methods by creating a more streamlined and efficient approach.
- **Proposed Solution**: The paper introduces Supervised Graph Contrastive Learning for Recommendation (SGCL), a novel framework that incorporates a unique supervised graph contrastive learning loss. This loss integrates user-item interaction supervision directly within the self-supervised loss, merging supervised and self-supervised contrastive learning tasks into a single optimization objective.  This eliminates redundant graph convolutions and extensive hyperparameter tuning.

### Technologies
- **Supervised Graph Contrastive Learning (SGCL)**: A novel framework that combines the training of recommendation and unsupervised contrastive losses into a cohesive supervised contrastive learning loss.
- **Light Graph Convolution**: Used for aggregating connected neighbors' representations.
- **Supervised Graph Contrastive Loss**:  A loss function that integrates user-item interaction supervision signal directly within the self-supervised loss, thereby merging supervised and self-supervised contrastive learning tasks into a single optimization objective
- **Datasets**: Amazon Beauty and Toys-and-Games datasets (5-core filtering).
- **Evaluation Metrics**: Recall@20, Recall@50, NDCG@20, NDCG@50.
- **Baselines**: BiasMF, NeuMF, NGCF, LightGCN, NCL, SGL, LightGCL, SimGCL.
- **Implementation Details**: Batch size = 1024, embedding size = 64, temperature 𝜏 = 0.2.
- **Open Source**: The SGCL framework is available as an open-source resource.

### Results
- **Performance**: SGCL achieves the highest NDCG and Recall scores across all datasets compared to state-of-the-art methods, demonstrating superior efficacy in recommendation tasks.
- **Efficiency**: SGCL demonstrates extreme efficiency, running for the fewest epochs and having the lowest total training time across all datasets.
- **Convergence**: SGCL achieves high and stable Recall levels within the first 30 training epochs, converging much faster than LightGCN and SGL.
- **Trade-off**: SGCL exhibits the most competitive performance while being much faster than other graph contrastive recommendation baselines.
- **Time Complexity Analysis**:  The paper provides a time complexity analysis comparing SGCL with LightGCN and SGL, showing SGCL's efficiency in normalization of the adjacency matrix, graph convolution, and loss computation.
