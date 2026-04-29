### Main Idea
- The paper addresses the issue of product-side fairness in bundle recommendation (BR) systems, where products and their suppliers may receive unequal exposure.
- It highlights the complexity of BR compared to traditional recommendation due to the need to consider both bundle-level and item-level exposure.
- The study aims to assess how current BR methods allocate exposure to bundles and individual items fairly, and to understand how exposure disparities arise. The research explores the impact of popularity bias and user interaction preferences on fairness in BR.

### Technologies
- **Datasets**: Youshu (books), NetEase (music playlists), iFashion (fashion outfits)
- **BR Methods**: CrossCBR, MultiCBR, EBRec, BunCa
- **Fairness Metrics**:
    - *Equal Opportunity*: Exposed Utility Ratio (EUR), Realized Utility Ratio (RUR), Expected Exposure Loss (EEL), Expected Exposure Relevance (EER)
    - *Statistical Parity*: Expected Exposure Disparity (EED), Demographic Parity (DP)
- **Evaluation Metrics**: Recall@K (R@K), Normalized Discounted Cumulative Gain@K (N@K)
- **User Grouping Strategy**: Users are grouped based on their interaction tendency (bundle-oriented, item-oriented, neutral) using a tendency score.
- **Geometric Browsing Model**: Used to compute exposure for fairness metrics.
- **Implementation Details**: Embedding dimension of 64, Xavier initialization, Adam optimizer, NVIDIA P100 and T4 GPUs.

### Results
- Exposure patterns differ significantly between bundles and items, suggesting the need for fairness interventions beyond bundle-level assumptions.
- Fairness assessments vary based on the metric used, highlighting the need for multi-faceted evaluation.
- Datasets with less uniform interaction distributions tend to result in less uniform exposure distributions in both bundles and items.
- BR methods generally decrease the uniformity of exposure compared to the input data, amplifying popularity bias.
- MultiCBR and BunCa perform well in terms of accuracy, while CrossCBR and EBRec are better for fairness at the bundle level, indicating a trade-off between accuracy and fairness.
- User behavior affects fairness outcomes: BR systems are fairer for users who interact more with bundles than individual items.