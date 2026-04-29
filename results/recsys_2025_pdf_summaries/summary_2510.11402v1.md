### Main Idea
- **Problem:** Cold-start recommender systems, particularly those using generative methods supervised by pre-trained collaborative filtering (CF) models, inherit and even amplify popularity bias, leading to unfair item exposure and reduced recommendation quality for new items.
- **Motivation:** CF models are prone to popularity bias, which means they tend to over-recommend popular items and neglect less popular ones. When generative cold-start models learn from these biased CF models, they also learn to predict popularity based on content features. This leads to certain cold items being predicted as very popular, even without user interaction data, resulting in an imbalanced and unfair distribution of recommendations.
- **Solution:** The paper proposes a simple post-processing mitigation approach that balances the distribution of predictions across items by rescaling the magnitudes of learned item representations. This method uses embedding magnitude as a proxy for predicted popularity and adjusts the magnitude distribution to reduce the influence of overexposed items.

### Technologies
- **Datasets:** Microlens (micro-video), Clothing, and Electronics Amazon E-commerce subsets from the MMRec toolbox. The datasets include user-item interaction data and item content features (text, image, video).
- **Models:**
    - **Generative Cold-Start Models:** Heater (mixture-of-experts), GAR (generative-adversarial training), GoRec (conditional variational autoencoder). These models generate synthetic ID embeddings for cold items based on content features, using a pre-trained CF model for supervision.
    - **Pre-trained CF Model:** FREEDOM (multimodal recommender that leverages item content features).
    - **Baseline Model:** KNN (non-parametric, calculates preference scores by content similarity).
- **Evaluation Metrics:**
    - **User-Oriented:** NDCG@k and Recall@k
    - **Item-Oriented (Fairness):** Max-Min Opportunity (measured with Mean Discounted Gain - MDG@k). The paper focuses on MDG-Min80% (bottom 80% of items), MDG-Max5% (top 5% of items), and MDG-All (overall item performance).
    - **Exposure Unfairness:** Gini-Diversity (measures distributional equality in item prediction counts).
- **Experimental Setup:** The datasets are split into warm and cold item sets, with warm items used to train the CF model and cold items used to evaluate the cold-start models. Hyperparameters are tuned to maximize cold validation set accuracy.
- **Novelty:** Post-processing method to mitigate bias by scaling the magnitudes of output item representations. It differs from previous methods by leveraging embedding magnitude as a proxy for predicted popularity. Unlike other methods it normalizes towards a mean, impacting both the smaller and larger vector magnitudes in opposite directions. The influence of the scaling is controlled by hyperparameter alpha.

### Results
- **Popularity Bias Inheritance:** Generative cold-start models inherit popularity bias from the supervisory warm model. They tend to overexpose certain items due to content similarity with popular training items.
- **Performance of Magnitude Scaling:** The proposed post-processing method (magnitude scaling) significantly improves prediction diversity (Gini-Diversity) across all datasets and models. It balances the distribution of prediction counts.
- **Impact on Item Fairness:** Magnitude scaling provides statistically significant improvements to low-end item accuracy (MDG-Min80%) while slightly reducing top-end MDG. The overall impact on MDG-All is positive.
- **Impact on User Accuracy:** The cost to user accuracy (NDCG@k, Recall@k) is small. It typically stays consistent or improves slightly for Clothing and Microlens, and decreases slightly for Electronics (less than 10%).
- **KNN Baseline:** The baseline KNN method often outperforms the cold-start models in both accuracy and fairness, suggesting that content similarity-based inference is less vulnerable to predictive biases based on interaction history.