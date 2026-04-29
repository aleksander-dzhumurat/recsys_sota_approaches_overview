# Summary of 2110.06475v2.md

**Token Usage**: Input: 16199, Output: 919, Total: 17118

---

### Main Idea
- The paper addresses the challenges of providing personalized travel recommendations across different scenarios within Alibaba's travel marketing platform (Fliggy, Taobao, Alipay). Two key issues are highlighted: the **Multi-Scenario Modeling Issue**, arising from diverse data distributions across scenarios, making it difficult to train a unified model, and the **Data Fairness Issue**, stemming from manual intervention during promotion periods, which biases the training data and degrades ranking model performance.
- The motivation is to improve the click-through rate (CTR) and overall performance of the recommendation system by effectively handling scenario diversity and intervention bias. The significance lies in the platform's scale, serving hundreds of travel scenarios, and the need for fair and accurate recommendations.
- The paper proposes a novel **Scenario-Aware Ranking Network (SAR-Net)** to tackle these issues. SAR-Net learns cross-scenario user interests via attention mechanisms, extracts scenario-specific features, and employs debiasing expert networks to mitigate intervention bias. A **Fairness Coefficient (FC)** is introduced to reweigh samples during training, further addressing the data fairness problem.

### Technologies
- **SAR-Net Architecture**: The network is based on a multi-expert network, consisting of scenario-specific and scenario-shared experts. It includes a Cross-Scenario Behavior Extract Layer, a Scenario-Specific Transform Layer, and a Mixture of Debias Experts.
- **Attention Mechanisms**: Two attention modules are used to extract user's cross-scenario interest, considering scenario features and item features. These modules modulate user behavior features to capture relevant interests across scenarios.
- **Scenario-Specific Linear Transformation**: A linear transformation layer is used to strengthen important information for each scenario. It uses an element-wise operation to leverage differences and commonalities between scenarios.
- **Debias Expert Networks**: The expert networks are divided into Bias Net and Main Net to alleviate the influence of intervention bias. The Bias Net predicts the degree of intervention bias, and the Main Net predicts the click-through rate.
- **Fairness Coefficient (FC)**: The FC measures the importance of individual samples, representing the degree of intervention for different items. It's used as a weight in the loss function and as a feature in the bias-expert net. The formula is presented for calculating FC based on PV(i,s) and F(i,s) where PV(i,s) represents the number of samples from item i in scenario s and F(i,s) represents the sum of predicted values by SAR-Net for all samples from item i in scenario s.
- **Multi-Scenario Gating Module**: A gating module fuses the outputs of scenario-specific and scenario-shared experts into a final prediction.
- **Loss Function**: A binary cross-entropy loss function is used, incorporating the Fairness Coefficient to weigh samples according to their intervention degree.
- **Datasets**: The experiments used Alibaba's production data, including user click behaviors across 20 scenarios. The training dataset covers over 80 million users and 1.55 million travel items.
- **Evaluation Metrics**: AUC (Area Under the ROC Curve) and RelaImpr (Relative Improvement) were used for offline evaluation. Real CTR was used for online A/B testing.
- **Competitors**: The SAR-Net was compared with multi-task learning models (HPS, Cross-Stitch, MMOE, CGC, PLE) and single-scenario models (Wide&Deep, PNN, DIN).

### Results
- Offline experiments showed that SAR-Net consistently outperformed the competitor models, demonstrating its effectiveness in multi-scenario CTR prediction. SAR-Net achieved superior performance across all scenarios compared to single-scenario and mix-scenario methods.
- Ablation studies demonstrated the importance of each component in SAR-Net: the attention mechanism, the Bias Net and Bias Adapting Loss, and the Scenario-Specific Transform Layer.
- Online A/B testing showed that SAR-Net outperformed the base model (MMOE) consistently in terms of real CTR. This led to the SAR-Net being deployed in the Alibaba online travel marketing platform, serving hundreds of travel scenarios. The deployment resulted in a 5% increase in CTR.
- Further analysis showed that SAR-Net made the exposure ratio of each category more even, achieved consistent improvements in all categories, and the improvements were more obvious on categories with smaller traffic, demonstrating the effectiveness of the method in mitigating intervention bias.
