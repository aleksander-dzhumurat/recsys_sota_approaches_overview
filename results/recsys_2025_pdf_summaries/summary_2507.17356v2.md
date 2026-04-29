### Main Idea
- The paper addresses the limitation of existing recommender systems based on the ACT-R cognitive architecture, which primarily focus on recommending previously listened tracks and struggle with new track recommendations.
- The paper posits that even unseen tracks should have some activation based on a higher-level representation of similar music. The goal is to improve music recommendation by incorporating audio features to predict ACT-R-like activation for new tracks, allowing the model to recommend both familiar and novel content.
- The proposed solution involves a model called REACTA (Recommendations from Embeddings with ACT-R and Audio features) that leverages audio information to predict ACT-R-like activation of new tracks and integrates them into the recommendation scoring process.

### Technologies
- **ACT-R (Adaptive Control of Thought-Rational)**: A cognitive architecture used as a foundation for modeling user behavior and memory access.
- **SVD-based embeddings**: Used for representing tracks based on their co-occurrences in music collections.
- **Audio embeddings**: Used to represent tracks based on their audio features.
- **Feedforward Neural Networks**: Two-layer networks are used to project audio embeddings into a vector space compatible with SVD embeddings and to predict ACT-R weights based on audio features and session embeddings.
- **PISA (Psychology-Informed Session embedding using ACT-R)**: A Transformer-based model used for session embedding, incorporating ACT-R activation into attention mechanisms.
- **Transformer**: Used to model short-term preferences by processing sequences of past sessions.
- **Multi-task learning**: Used to optimize model parameters by minimizing a loss function that considers both positive and negative examples of next-session tracks.
- **Evaluation Metrics**: NDCG, Recall, RepBias, and PopBias are used to evaluate the model's performance. Repetition and Exploration focused variants of NDCG and Recall are also used.
- **Dataset**: A proprietary dataset from Deezer, consisting of nearly 900 million time-stamped listening events from over 4 million users.
- **Negative Sampling**: Uniform negative sampling (REACTA-U) and popularity-based negative sampling (REACTA-P) strategies are used.

### Results
- REACTA demonstrates competitive performance, particularly excelling on exploration-focused metrics.
- REACTA-P achieves a top NDCG Exp (exploration) of 3.30%, indicating its strength in recommending unheard tracks and contributing to music discovery.
- REACTA effectively balances familiar and novel tracks in each session, closely matching ground-truth repetition ratios, with RepBias as low as 0.09%.
- Popularity-based negative sampling reduces the model's susceptibility to popularity bias.
- The model's main limitation is the computational cost of calculating ACT-R activation over a large catalog, which is planned to be addressed in future work using approximate activation methods.
