# Summary of 2202.02698v1.md

**Token Usage**: Input: 10444, Output: 607, Total: 11051

---

### Main Idea
- The paper addresses the problem of click-through rate (CTR) prediction in online advertising, where existing methods struggle with sparse user behavior data and limited interest exploration.
- The authors propose that current methods fail to capture the true motivations behind user clicks and are biased towards popular or similar items, hindering diversity in recommendations.
- They introduce a novel framework called Triangle Graph Interest Network (TGIN) that leverages triangles in item-item co-occurrence graphs as basic units of user interests. TGIN aims to capture implicit user interests, promote diversity, and improve CTR prediction accuracy.

### Technologies
- **Triangle Graph Interest Network (TGIN)**: The proposed framework.
- **Item-Item Co-occurrence Graph**:  An undirected graph where nodes represent items and edges represent co-occurrence in user behavior sequences. Edge weights indicate co-occurrence frequency. Constructed using a sliding window approach on user behavior sequences.
- **Triangles**:  Triplets of items in the co-occurrence graph where all three items are connected.  Used as the fundamental unit of user interest.  k-Order Triangles are defined based on the shortest distance of the triangle's nodes to a given item.
- **Bloom Filters**: Used to efficiently check for edges during triangle extraction.
- **Determinantal Point Processes (DPP)**:  Used to select a diverse and relevant set of triangles. DPP kernel matrix is constructed based on triangle relevance scores (inner and outer weights) and triangle feature vectors (average of node features).
- **Attention Mechanism**:  Used to determine user preferences for different interest units (triangles) and to fuse multi-level interests represented by triangles of different orders. Position-aware attention is used for user behavior modeling.
- **Multi-Head Self-Attention**: Used to aggregate information among multiple triangles for each item.
- **Auxiliary Loss**: Used to supervise better item representation learning.
- **Datasets**: Public datasets (Amazon Books and Electronics) and an industrial dataset from Alibaba's online display advertising system.
- **Evaluation Metric**: Area Under the Curve (AUC).

### Results
- TGIN significantly outperforms state-of-the-art baselines on both public and industrial datasets in terms of AUC.
- Ablation studies demonstrate the effectiveness of modeling triangles as basic units of user interests and the contribution of the auxiliary loss.
- Diversity analysis shows that TGIN with diversity-based triangle sampling achieves higher item diversity compared to weight-based sampling methods.
- Online A/B testing in AliExpress's merchant advertising system showed improvements in UV L-P (3.62%), L-GMV (3.16%), and commission earn per user (3.20%).
- TGIN's efficiency is comparable to, if not better than, popular sequential models like DIN, GIN, MIMN, DIEN, and DMIN. The average response time is about 30 milliseconds.
