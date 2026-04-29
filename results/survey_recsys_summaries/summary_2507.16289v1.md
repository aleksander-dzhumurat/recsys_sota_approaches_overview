# Summary of 2507.16289v1.md

**Token Usage**: Input: 17345, Output: 855, Total: 18200

---

### Main Idea
- The paper addresses the problem of inconsistent and unreliable evaluation protocols in sequential recommender systems (SRS). It argues that widely used leave-one-out (LOO) splits suffer from temporal leakage and unrealistic test horizons, while global temporal splits (GTS) lack standardized target selection and validation schemes.
- The motivation is that current evaluation practices can lead to inflated offline performance and poor real-world relevance, hindering the development of effective SRS models.
- The proposed solution is a systematic comparison of different GTS variants tailored to next-item prediction (NIP), including various target selection strategies (Last, First, Successive, Random, All) and validation schemes (Global Temporal, User-Based, Last Training Item). The paper aims to identify splitting strategies that are better aligned with real-world scenarios and provide reproducible, fair comparisons of SRS models.

### Technologies
- **Data Splitting Strategies**:
    - Leave-One-Out (LOO) Split: The traditional approach of holding out the last item for each user.
    - Global Temporal Split (GTS): Splitting data based on a global timepoint to prevent data leakage. Explored with various target selection options:
        - Last: The user's last interaction in the holdout sequence.
        - First: The user's first interaction in the holdout sequence.
        - Successive: Each interaction in the holdout sequence is treated as a separate target.
        - Random: A randomly sampled interaction from the holdout sequence.
        - All: Bundles all of a user's holdout items as a single ground-truth set.
    - Validation splitting strategies: Global Temporal (GT), Last Training Item (LTI), and User-Based (UB) validation.
- **Datasets**:
    - Amazon Reviews (Beauty, Sports)
    - MovieLens-1M (ML-1M) and MovieLens-20M (ML-20M)
    - BeerAdvocate (BeerAdv)
    - Diginetica 2
    - YooChoose
    - Zvuk
- **Evaluation Metrics**:
    - Normalized Discounted Cumulative Gain (NDCG@K)
    - Mean Reciprocal Rank (MRR@K)
    - HitRate (HR@K)
- **Baselines**:
    - SASRec+ (an adaptation of the original PyTorch implementation that employs full cross-entropy loss)
    - BERT4Rec (using the Transformers library)
    - GRU4Rec (with full CE loss)
    - SeqKNN (sequential item-based kNN)
- **Implementation Details**:
    - Wide ranges for each model's hyperparameters (hidden sizes, self-attention blocks, attention heads, masking probability, GRU layers, dropout rates).
    - Adam optimizer with a learning rate of 10^-3.
    - Trained on NVIDIA H100 GPUs with 80GB HBM3 memory.
- **Statistical Analysis**:
    - Kendall and Spearman rank correlation coefficients.
    - Paired Student's t-test (mentioned for its limitations).

### Results
- LOO splits, while maximizing the number of test users, can lead to temporal leakage and unrealistic test periods.
- GTS with "First" target exhibits lower correlation due to time-gap distributions between interactions, and GTS "All" target shows task mismatch.
- GTS with "Last" and "Random" targets correlate strongly with the more comprehensive "Successive" evaluation, making them viable alternatives.
- Choice of data splitting strategy for SRS significantly impacts evaluation metrics and model rankings. The most reliable validation strategy under GTS is the matching global temporal validation.
- Retraining models on combined training and validation data is important for optimal deployment performance, especially with global temporal validation, and does not substantially alter the relative ranking of models.
- The paper provides recommendations for reporting splitting strategy details, including target item selection and input sequence building.
- The code is publicly available at: https://github.com/monkey0head/time-to-split
