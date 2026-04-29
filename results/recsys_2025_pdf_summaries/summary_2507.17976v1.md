### Main Idea
- The paper introduces the task of Supervised Conversational Performance Prediction in Conversational Image Recommendation systems.  The goal is to predict whether a conversation will fail to retrieve the user's target item.  This addresses the problem that current systems assume the target item is always in the catalog, leading to user frustration when it's not. The paper differentiates between "system failure" (item exists but isn't retrieved) and "catalogue failure" (item doesn't exist in the catalog).  The inspiration comes from Query Performance Prediction (QPP) used in search engines.
- The motivation stems from the real-world scenario where users may not always find their desired item even after multiple turns of interaction with a Conversational Recommendation System (CRS). This can lead to frustration and a poor user experience. Current systems often assume that the target item exists within the catalog, and failure to retrieve it is attributed to the system's inability to find it. However, the item may simply be unavailable in the catalog.
- The proposed approach involves using predictors for conversational performance that detect conversation failures, using multi-turn semantic information contained in the embedded representations of retrieved image items.  Specifically, an AutoEncoder-based predictor is proposed to learn a compressed representation of top-retrieved items and use classification labels to predict the outcome. A shrinkage-based predictor is also introduced as a baseline.

### Technologies
- **Datasets:** Shoes and FashionIQ Dresses datasets, containing relative critiques per candidate-target pair.
- **User Simulator:** Show, Attend, and Tell user simulator is used to train an EGE CRS model.
- **EGE CRS Model:** This model uses historical feedback and recommendations.
- **AutoEncoder (AE) Predictor:** This model learns a compressed representation of retrieved items from multiple turns using Mean Squared Error (MSE) as the reconstruction loss. A softmax function and Cross-Entropy Loss are added for classification. Adam optimizer with a learning rate of 0.01 is used.
- **Coherence-based QPP Predictors:** Autocorrelation (AC), Network metrics (WAND), Reciprocal Volume (RV), and A-pairRatio.
- **L1-based Regularized Predictor:** A shrinkage factor 𝜆 is added to existing coherence-based predictors, regularized with L1 to maintain important information from various turns. Lasso Regression is adapted with 𝜆 = 0.1.
- **Evaluation Metrics:** Classification accuracy. McNemar's test is used for statistical significance.
- **Experimental Setup:** 70% of conversations used for training, and 30% for testing.
- Top 100 item representations of all turns up to *k*-1 are used to predict *k*.

### Results
- In the base scenario (target item exists), the AE-based classifier shows higher accuracy, especially for the Dresses dataset. This indicates the utility of AE in predicting conversational failures when the target item is present.
- In the missing target scenario (catalogue failure), all classifiers show a reduction in accuracy, indicating the increased difficulty of predicting catalogue failures compared to system failures.
- The L1-based variant of predictors shows a noticeable increase in accuracy for both datasets compared to the corresponding RF-variant, especially in the missing target scenario.
- Multi-turn predictors (using features from multiple turns) generally outperform single-turn predictors.
- Feeding the entire set of top-ranked items for training the AE is more useful than using only the top-ranked item.
- For the Dresses dataset, the accuracy peaks at turns 2-3 and then decreases, which suggests that as the user gives uninformative feedback, predictions become less accurate.
