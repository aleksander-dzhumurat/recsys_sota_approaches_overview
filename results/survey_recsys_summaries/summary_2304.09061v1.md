# Summary of 2304.09061v1.md

**Token Usage**: Input: 13817, Output: 650, Total: 14467

---

### Main Idea

- The paper addresses the challenge of Automatic Playlist Continuation (APC) in large-scale music streaming services. APC involves recommending songs to extend user-created playlists while preserving their musical characteristics and matching user preferences.
- The core problem is the discrepancy between complex APC models proposed in research and the scalability requirements of industrial applications that need to select recommendations from millions of songs in real-time.
- The paper introduces a general framework called Represent-Then-Aggregate (RTA) to build scalable and effective APC models suitable for large-scale industrial applications. The framework decomposes APC models into song representation learning and playlist-level sequence modeling.

### Technologies

- **Represent-Then-Aggregate (RTA) Framework:** A two-stage approach involving learning song representations (embedding vectors) offline and aggregating them online to form playlist representations. This enables scalability by pre-computing song representations and minimizing online operations dependent on dataset size.
- **Song Representation Learning:**
    -  Direct song embeddings (e.g., from matrix factorization).
    -  Factorization Machines (FM): representing songs using metadata embeddings (artist, album, etc.).
    -  Neural Networks (NN): processing metadata using attention mechanisms.
- **Playlist-Level Aggregation:**
    -  Averaging song embeddings (AVG).
    -  Gated Convolutional Neural Networks (CNN).
    -  Gated Recurrent Units (GRU).
    -  Transformer Decoders.
- **Similarity Function:** Inner product between playlist and song embeddings to estimate the relevance score.
- **Datasets:** Spotify's Million Playlist Dataset (MPD) was used for offline experiments, and a private dataset of 25 million playlists was used for online A/B testing on Deezer.
- **Evaluation Metrics:** Precision, Recall, Normalized Discounted Cumulative Gain (NDCG), R-Precision, Clicks, Coverage, Popularity bias, Training time, Inference time.
- **Baselines:** SKNN, VSKNN, STAN, and VSTAN session-based nearest neighbor approaches.
- **Implementation Details:** Python, stochastic gradient descent, Optuna library for hyperparameter tuning, single CPU machine with 25 GB of RAM and a Tesla P100 GPU accelerator.

### Results

- RTA framework enables the integration of complex sequence modeling techniques (e.g., Transformers) into large-scale APC systems.
- Transformer-based models generally outperform other approaches in accuracy-oriented metrics, especially ranking quality (NDCG, Clicks), while maintaining reasonable popularity and coverage scores.
- RTA models achieve significantly faster inference times (less than 10 milliseconds per playlist) compared to baselines (around 500 milliseconds), making them suitable for real-time recommendation in production environments.
- An online A/B test on Deezer demonstrated that the RTA-based MF-Transformer model improved the Add-To-Playlist rate by 70% compared to the existing production system (collaborative filtering based).
- The successful deployment of the MF-Transformer model on Deezer highlights the practical impact and industrial relevance of the RTA framework.
