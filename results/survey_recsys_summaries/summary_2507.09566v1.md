# Summary of 2507.09566v1.md

**Token Usage**: Input: 4787, Output: 698, Total: 5485

---

### Main Idea
- The paper addresses the critical challenge of bridging the gap between offline metrics and online Key Performance Indicators (KPIs) in large-scale recommender systems, particularly within the e-commerce domain. It is motivated by the need for industry practitioners to efficiently identify offline metrics that reliably predict real-world performance, enabling data-driven decisions and accelerated optimization cycles. The proposed solution leverages recent advances in Pareto front approximation to simultaneously split traffic into multiple test groups, each with distinct offline metrics, while serving all groups through a single scalable model.

### Technologies
- **Pareto Front Approximation**: Used to model trade-offs between multiple objectives during inference with a single model. It involves sampling a preference vector from a Dirichlet distribution during training and scalarizing objective losses.
- **MultiTRON**: A session-based Transformer architecture with three layers and a hidden size of 256, used as the neural backbone for the recommender system.
- **Offline Metrics**:
    - `Recall@20`: Measures the click prediction performance.
    - `Order Density at 20 (OD@20)`: A novel metric defined as the empirical probability that a clicked item is ordered, given it is ranked within the top 20 positions. It estimates the post-click conversion rate.
    - `Recall@20 · OD@20`: A product metric capturing the joint effectiveness of generating clicks and subsequent orders, serving as an offline proxy for units sold.
- **Online KPIs**:
    - Click-Through Rate (CTR)
    - Post-Click Conversion Rate (CVR)
    - Units Sold
- **Loss Functions**:
    - Sampled Softmax Loss (for predicting item clicks)
    - Binary Cross-Entropy Loss (for predicting whether an item is ordered)
    - Auxiliary Distortion Loss (artificially induces a trade-off with the primary loss to extend the strategy to single-objective systems)
- **Statistical Analysis**: Logistic regression with the Wald test is used to test the significance of the relationship between offline metrics and online KPIs.
- **Experimental Setup**: A large-scale online experiment on the OTTO e-commerce platform, involving session-based recommender systems, was conducted. The traffic was randomly split into five distinct groups.
- **Dataset**: User sessions from the OTTO e-commerce platform, modeled as sequences of user-item interactions.

### Results
- The online experiment validated the proposed strategy, identifying statistically significant relationships between offline metrics and online KPIs.
- `Recall@20` was found to be a significant positive predictor for CTR.
- `OD@20` was found to be a significant positive predictor for CVR.
- `Recall@20 · OD@20` was found to be a significant positive predictor for units sold.
- `Recall@20` was found to be a significant negative predictor for CVR.
- Sacrificing `OD@20` to increase `Recall@20` resulted in a more efficient strategy for driving units sold.
- A 1% increase in `Recall@20` led to a 0.9% increase in CTR, while reducing CVR by only 0.2%.
- The paper highlights that Pareto front approximation techniques offer a promising direction for bridging the offline-to-online evaluation gap.
