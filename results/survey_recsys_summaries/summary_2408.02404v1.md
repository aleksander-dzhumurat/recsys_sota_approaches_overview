# Summary of 2408.02404v1.md

**Token Usage**: Input: 10359, Output: 962, Total: 11321

---

### Main Idea

- The paper addresses the "seesaw dilemma" in graph collaborative filtering (GCF) for recommendation systems. This dilemma arises because not all user-item interactions are equally indicative of user interest.  Interactions can be categorized as "Interacted & Fascinated" (I&F) or "Interacted & Unfascinated" (I&U).  Training GCF models without distinguishing between these types of interactions can lead to recommendations of unfascinating items. Conversely, ignoring I&U interactions results in an incomplete representation of user intent, decreasing model accuracy.
- The motivation is to improve the user experience by recommending more fascinating items while reducing the recommendation of unfascinating items. Existing GCF models often fail to differentiate between these interaction types, leading to suboptimal recommendations.
- The proposed solution is Feedback Reciprocal Graph Collaborative Filtering (FRGCF). It partitions the user-item interaction graph into I&F and I&U subgraphs and then employs separate collaborative filtering on each.  Feedback-reciprocal contrastive learning connects the two subgraphs, enabling the I&F graph recommender to learn from the I&U graph without being negatively influenced by it. A macro-level feedback modeling scheme further alleviates data incompleteness.

### Technologies

- **Graph Collaborative Filtering (GCF):** Utilizes user-item interaction data represented as a graph for recommendation.  Specifically, graph neural networks (GNNs) are used to recursively aggregate neighbor representations.
- **Feedback-Partitioned Graph Collaborative Filtering:**  Divides the interaction graph into two subgraphs: I&F and I&U, based on user feedback (e.g., ratings, completion rates, page stay time).  Separate GCF models are trained on each subgraph.
- **Feedback-Reciprocal Contrastive Learning:**  Connects the I&F and I&U subgraphs using contrastive learning. This facilitates information exchange between the two graphs while mitigating the negative influence of I&U interactions on the I&F graph model. It models "impulsiveness" based on relationships within the I&F and I&U perspectives and constructs user-user, item-item, and user-item matrices to calculate this.
- **Macro-Level Feedback Modeling:**  Addresses the data incompleteness resulting from separate modeling of I&F and I&U graphs. K-means clustering is used to create macro-level representations (centroids) of users and items based on their embeddings. The model then infers the direction of GNN information propagation by averaging differences between results from GNN layers. It aggregates macro-level information to nodes in a way that produces results similar to those from GNNs.
- **Distance Regularization:** Jensen-Shannon divergence (JSD) is applied to regularize representations by increasing the disparity between probability distributions that govern the update directions of the respective GNNs, enhancing their expressiveness.
- **Loss Function:**  The overall objective function combines pairwise Bayesian Personalized Ranking (BPR) loss, feedback-reciprocal contrastive loss, macro-level feedback modeling loss, and distance regularization.
- **Datasets:** MovieLens, Douban, Beauty, KuaiRec (public benchmarks), and a billion-scale industrial dataset from Taobao.  Feedback (I&F vs. I&U) is determined by rating, completion rate, or page stay time.
- **Evaluation Metrics:** Recall@N and NDCG@N (N=20) are used for performance evaluation.

### Results

- FRGCF outperforms state-of-the-art GCF models on all evaluated datasets. Average improvements of 6.28% in Recall and 6.37% in NDCG were observed across the experimental datasets.  On the Taobao industrial dataset, FRGCF achieved 6.55% and 7.82% improvements in Recall and NDCG, respectively.
- Ablation studies demonstrated that each component of FRGCF (feedback-reciprocal contrastive learning, macro-level feedback modeling, and distance regularization) contributes positively to overall performance.
- Online A/B tests on Taobao's recommender system showed significant improvements with FRGCF in PCTR (+1.35%), UCTR (+0.91%), GMV (+1.61%), and Stay Time (+2.89%) compared to the baseline model, with only a slight increase in response time. This indicates that FRGCF is more effective at recommending items that fascinate users and encourages deeper engagement.
- Results show FRGCF recommends more fascinated items and fewer unfascinated items compared to baseline methods.
