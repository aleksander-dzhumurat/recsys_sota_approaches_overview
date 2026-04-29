# Summary of 2110.md

**Token Usage**: Input: 16103, Output: 924, Total: 17027

---

### Main Idea

- **Problem**: The paper addresses two key challenges in providing personalized recommendations on Alibaba's travel marketing platform, which serves diverse travel scenarios across multiple apps:
    - **Multi-Scenario Modeling Issue**:  The significantly different traffic characteristics (data scale, topic) across scenarios make it difficult to train a single, unified model that performs well in all scenarios.
    - **Data Fairness Issue**: Manual intervention to promote specific items during events like the Double-Eleven Shopping Festival introduces bias into the training data, leading to unfair ranking results and discrimination against disadvantaged items.
- **Motivation**: Accurate and fair recommendations are crucial for user satisfaction and business success in e-commerce. Addressing these issues can improve Click-Through Rate (CTR) and provide a more equitable experience for both users and merchants.
- **Proposed Solution**: The authors propose a novel Scenario-Aware Ranking Network (SAR-Net) to tackle these challenges. SAR-Net employs a multi-expert network architecture that learns cross-scenario user interests and mitigates intervention bias through a Fairness Coefficient.

### Technologies

- **SAR-Net Architecture**:
    - **Embedding Layer**: Maps input features (user profiles, user behavior, scenario context, target item, intervention bias) to low-dimensional vectors.
    - **Cross-Scenario Behavior Extract Layer**: Extracts user's cross-scenario interests using two attention modules that consider both scenario features and item features. This captures user interest transfer across different scenarios.
    - **Scenario-Specific Transform Layer**: Applies a linear transformation to strengthen important information for each scenario, leveraging differences and commonalities between scenarios.
    - **Mixture of Debias Experts**: A multi-expert network comprising scenario-specific and scenario-shared experts, each further divided into "Bias net" and "Main net." The Bias net helps to mitigate intervention bias and is removed during online deployment.
    - **Multi-Scenario Gating Module**: Fuses the outputs of the expert networks to produce the final predicted score.
- **Fairness Coefficient (FC)**: A metric proposed to measure the degree of intervention for each item in each scenario.  It is used to reweigh the prediction in the debias expert networks.
- **Loss Function**: Binary cross-entropy loss function, incorporating the Fairness Coefficient as a weight to emphasize less intervened samples during training.
- **Datasets**:
    - Offline Dataset: Alibaba production data containing user click behaviors from 20 scenarios over one month (80 million users, 1.55 million items).
- **Evaluation Metrics**:
    - AUC (Area Under the ROC Curve): Used to measure CTR prediction performance.
    - RelaImpr: Used to measure the relative improvement of a target model over a base model.
- **Competitors**:
    - Multi-Task Learning Models: HPS, Cross-Stitch, MMOE, CGC, PLE
    - Single-Scenario Models: Wide&Deep, PNN, DIN
- **Optimization**: Adam optimizer with a learning rate of 0.001.

### Results

- **Offline Evaluation**:
    - SAR-Net consistently outperforms both single-scenario and multi-task learning baselines in terms of AUC across various scenarios.
    - Ablation studies demonstrate the effectiveness of the Cross-Scenario Behavior Extract Layer, Bias Net with Bias Adapting Loss, and Scenario-Specific Transform Layer.
    - Explicit modeling of user interest transfer and extraction of scenario-specific information contribute to the improved performance.
- **Online A/B Test**:
    - Deployed on Alibaba's travel marketing platform, SAR-Net shows a consistent increase in real CTR compared to the base model (MMOE) over a seven-day period.
    - Analysis of performance across different categories reveals that SAR-Net makes the exposure ratio of each category more even, improves CTR across all categories, and shows more significant improvements for categories with smaller traffic.
- **Key Insights**:
    - SAR-Net effectively addresses the multi-scenario modeling and data fairness issues in recommender systems.
    - Learning user interest transfer across scenarios and extracting scenario-specific features are crucial for improved CTR prediction.
    - The Fairness Coefficient and Bias Net are effective in mitigating the impact of manual intervention on model training and ranking results.
- **Deployment**: SAR-Net has been deployed on Alibaba's online travel marketing platform, serving hundreds of travel scenarios and resulting in a 5% improvement in CTR.
