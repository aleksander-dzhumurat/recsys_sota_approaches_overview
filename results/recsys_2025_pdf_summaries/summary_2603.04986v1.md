### Main Idea
- The paper addresses the problem of exposure and selection bias in sequential recommendation (SR) systems caused by the absence of item exposure logs. Current SR models primarily rely on explicit user interactions (e.g., clicks or purchases) while ignoring items that were shown to the user but not interacted with (selection bias) or items that were never shown at all (exposure bias). This leads to a biased understanding of user preferences.
- The motivation is to improve the accuracy and fairness of SR by accounting for item exposure, especially in scenarios where exposure logs are unavailable. The significance lies in mitigating biases that can lead to suboptimal recommendations and reinforce existing popularity patterns.
- The proposed solution is Time-aware Inverse Propensity Scoring (TIPS), a novel framework designed as a plug-in for existing SR models. TIPS estimates item exposure distributions by constructing time-aware counterfactual examples, reweighting user interactions with time-sensitive propensity scores, and thereby approximating a counterfactual setting where all items have an equal chance of being exposed.

### Technologies
- **Structural Causal Model (SCM):** A causal model is used to explicitly represent the relationships between user preferences, item exposure, and user interactions.
- **Time-aware Inverse Propensity Scoring (TIPS):** A novel debiasing framework that incorporates temporal information into IPS.
- **Counterfactual Data Augmentation:** Generating synthetic interaction data by creating "what-if" scenarios. Three types of counterfactual samples are generated for each factual interaction: similar items, popular items, and the same item at a slightly different time.
- **Item and Time Embeddings:** Separate embedding lookup tables are maintained for interaction and exposure to disentangle user preferences and item exposure patterns. Time embeddings are created using a multi-layer perceptron (MLP) on normalized time intervals between interactions.
- **Cross-Attention Mechanism:** To incorporate exposure information into the interaction sequence, a cross-attention mechanism is used where the exposure embedding serves as the query and embeddings of historical interactions serve as the key and value.
- **Loss Functions:** Binary Cross-Entropy (BCE) loss is used to train the exposure estimation model, and Bayesian Personalized Ranking (BPR) loss is used for recommendation, both integrated into a final loss function controlled by a hyperparameter.
- **Backbone Models:** The TIPS framework is tested as a plug-in with three existing sequential recommendation models: Attention (a traditional sequential model), CVAE (a generative model), and DiffuRec (a generative model).
- **Datasets:** ML-1M, ML-10M, Music4All, and GoodReads.
- **Evaluation Metrics:** HR@K (Hit Ratio at K) and NDCG@K (Normalized Discounted Cumulative Gain at K).

### Results
- TIPS consistently improves recommendation performance when integrated with various backbone SR models. For example, incorporating TIPS (Attention+TIPS) achieved an average improvement of around 6% in HR@10 and 5% in NDCG@10.
- The performance improvement is more significant on large-scale datasets (Music4All and ML-10M), indicating that TIPS is more effective in diverse and complex recommendation scenarios.
- Ablation studies demonstrate the necessity of all components of the TIPS framework, including time-aware information, IPS, and exposure estimation.
- The inclusion of temporal information improves performance.
- The propensity scores computed by TIPS are more discriminative between positive and negative items compared to traditional IPS, suggesting that TIPS is better at mitigating exposure bias.
