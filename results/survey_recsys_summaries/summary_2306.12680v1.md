# Summary of 2306.12680v1.md

**Token Usage**: Input: 33864, Output: 784, Total: 34648

---

### Main Idea
- This survey paper comprehensively summarizes the latest advancements in recommender systems. The objective is to provide an overview of the current state-of-the-art and highlight recent trends. It starts with a taxonomy of recommender systems, including personalized and group recommenders, then delves into knowledge-based systems. The survey also analyzes robustness, data bias, and fairness issues, summarizing evaluation metrics. Finally, it provides insights into the latest trends and new directions for future research.

### Technologies
- **Taxonomy of Recommender Systems:** Personalized, Group, Collaborative Filtering, Content-Based, Knowledge-Based, Hybrid methods.
- **Collaborative Filtering (CF):** Memory-based CF (Pearson Correlation Coefficient, Cosine Similarity, Mean Squared Difference, Proximity Impact Popularity, Jaccard Similarity, Proximity Significance Singularity, embedding techniques like 'prefs2vec', graph-based methods, anchor vectors), Model-based CF (Convolutional Neural Networks, Long Short-Term Memory, Recurrent Neural Networks, AutoEncoders, Multi-Layer Perceptron, Neural Collaborative Filtering, Neural Network Matrix Factorization, Factorization Machines, Graph Neural Networks).
- **Context-Aware CF:** Pre-filtering, Post-filtering, Contextual Modeling, sensor data analysis, latent context embedding, hierarchical models.
- **Content-Based RS:** Text data analysis, word embeddings, open knowledge graphs, Heterogeneous Information Networks (HIN), Bayesian models.
- **Knowledge-Based RS:** Utilizes domain knowledge, knowledge graphs (YAGO, Freebase, DBpedia, NELL, Wikidata, Bio2RDF, Knowlife, Satori), knowledge graph embedding (TransE, TransH, TransR, TransD, DistMult).
- **Group Recommender Systems:** Memory-based, Model-based, Preference Aggregation (majority-based, consensus-based, borderline strategies), deep learning, attention mechanisms.
- **Bundled Recommendations:** Beam Generation Network (BGN), BasConv, BundleBert (Bunt), Multi-View Intent Separation Graph Network (MIDGN), BRUCE model.
- **Robustness Techniques:** Adversarial training, model distillation.
- **Debiasing Techniques:** Score calibration losses, propensity scores,query-based bias estimation, self-supervised learning.
- **Evaluation Metrics:** Rating Based Indicators (RMSE, MAE), Item Based Indicators (Precision, Recall, F-Measure, MAP@k, MAR@k, NDCG, NDPM), Similarity metrics (PCC, COS, MSD, PIP, Jaccard, PSS, NHSM).
- **Datasets**: MovieLens.

### Results
- The survey presents a comprehensive overview of recommender systems, covering categorization, implementation, and evaluation metrics.
- Memory-based CF is simple and accurate in small-scale scenarios but faces scalability challenges with large datasets.
- Model-based CF leverages neural networks and factorization machines to improve prediction accuracy and handle sparse data.
- Integration of external knowledge and context enhances recommender system performance.
- Graph Neural Networks have been widely used in recommender systems.
- The two combined models which are based on the collaborative filtering algorithm of graph neural networks, achieve the best results. The neighborhood-enhanced contrastive learning method, integrated into the collaborative filtering algorithm, can alleviate the 'catastrophic forgetting' issue and avoids cold starts, producing slightly better outcomes than the combined incremental graph convolution methods.
- Robustness, data bias, and fairness are critical challenges addressed with adversarial training, debiasing techniques, and meta-learning approaches.
- The choice of evaluation metrics depends on the type of recommender system and the desired outcome.
- Future trends include the use of Generative Pre-Training (GPT) technology to enhance conversational recommendation systems.
