# Summary of 2407.16357v2.md

**Token Usage**: Input: 10941, Output: 907, Total: 11848

---

### Main Idea
- The paper addresses the challenge of modeling extremely long-term user behavior sequences (up to 10^6 interactions) for Click-Through Rate (CTR) prediction in large-scale recommendation systems, specifically within the Kuaishou short-video platform.
- The motivation stems from the limitation of existing methods (like SIM and TWIN) that struggle to fully capture user interests across their entire app usage lifecycle due to length restrictions in the General Search Unit (GSU). Modeling the full life-cycle behaviors promises enhanced user experience and commercial gains.
- The proposed solution, TWIN-V2, enhances the original TWIN model by employing a divide-and-conquer approach. It compresses life-cycle behaviors offline using hierarchical clustering, creating "virtual items" that represent clusters of similar interactions. Online, it uses a cluster-aware target attention mechanism to extract multi-faceted long-term user interests, improving recommendation accuracy and diversity.

### Technologies
- **Hierarchical Clustering**:  Used offline to group similar items in user behavior sequences into clusters. K-means is used within the hierarchical clustering process.  The number of clusters adapts dynamically to the number of items in each group. Algorithm 1 details the process which involves splitting the historical behaviors into M different groups based on the proportion of time they were played by the user, then recursively clustering life-cycle historical behaviors of each group until the number of items in each cluster does not exceed 𝛾.
- **Cluster Representation**:  A "virtual item" represents each cluster, using the average of numerical features and the closest item to the centroid for categorical features.
- **Cluster-aware Target Attention**:  This mechanism is used in both the GSU and ESU stages. The attention scores are reweighted based on the size of the corresponding cluster, giving more weight to clusters with more items, which signify stronger user preferences.
- **Two-Stage Approach (GSU and ESU)**: In the online stage, the GSU retrieves the top 100 clusters related to the target item. The ESU then extracts long-term interests from these retrieved clusters. Both use the cluster-aware target attention.
- **Datasets**: A multi-billion-scale industrial dataset from Kuaishou, comprising user interaction data over five consecutive days. It includes user, video, and sample data. User history covers a maximum length of 100,000 interactions.
- **Evaluation Metrics**: AUC (Area Under the ROC Curve) and GAUC (Group AUC) are used to evaluate model performance.
- **Implementation**:  The model utilizes the same item and user features as in Kuaishou's industrial context. TWIN-V2 limits user history to 100,000 items for clustering, compressing it to about 10% of its original size. Other models are limited to 10,000 behaviors for GSU input. The batch size is 8192, and the learning rate is 5e-6 for Adam.

### Results
- TWIN-V2 significantly outperforms SOTA baselines, including Avg-Pooling, DIN, SIM variants, ETA, SDIM, and the original TWIN model. TWIN-V2 achieves an improvement of 0.0013 in AUC and 0.0024 in GAUC compared to TWIN.
- GAUC shows a higher relative improvement than AUC, indicating that TWIN-V2 performs better across various user types and specific subsets, especially highly active users.
- Ablation studies demonstrate the effectiveness of both the adaptive hierarchical clustering method and the cluster-aware target attention mechanism.  Adaptive clustering achieves higher cluster accuracy and shorter running time. Omitting cluster size reweighting leads to performance decline.
- Online A/B tests at Kuaishou show that TWIN-V2 leads to improved watch time (+0.672% to +0.800% depending on the scenario) and diversity of recommended results (+0.005% to +0.740%).
- The model has been successfully deployed at Kuaishou, serving approximately 400 million daily active users. The system compresses historical behavior to 10% of its original length, leading to a 90% reduction in storage costs.
