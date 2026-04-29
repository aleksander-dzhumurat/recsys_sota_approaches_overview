### Main Idea
- The paper addresses the cold start problem in sequential recommender systems, where new items with few or no interactions cannot be effectively recommended.
- The motivation is that cold start items hinder recommendation diversity, overall performance, and model deployment lifetime. Content-based approaches are used to generate initial embeddings but suffer from a distribution gap and potential drift.
- The proposed solution is to use a small, trainable "delta" vector to adjust frozen content-based embeddings, allowing the model to adapt while staying close to the original semantic structure.

### Technologies
- **Model:** SASRec (Self-Attentive Sequential Recommendation) is used as the base sequential recommendation model.
- **Embeddings:**  E5 encoder is used for text-based content embeddings. Precomputed audio embeddings were used for the Zvuk dataset. Principal Component Analysis (PCA) is applied to reduce the dimensionality of content-based embeddings.
- **Datasets:** Amazon-M2 (e-commerce, textual descriptions), Beauty (e-commerce, textual descriptions), and Zvuk (music streaming, audio representations).
- **Evaluation Metrics:** Normalized Discounted Cumulative Gain (NDCG@10) and Hit Rate (HR@10). Evaluated separately for warm and cold items.
- **Optimization:** Adam optimizer with a learning rate of 1e-3. Full cross-entropy loss is used.
- **Implementation:** Experiments are performed with a batch size of 128. SASRec is configured with two transformer blocks, a single attention head, and a dropout rate of 0.3. The embedding dimension is set to 128 for Beauty and Zvuk, and to 64 for Amazon-M2. The maximum input sequence length is limited to 128 for Zvuk, and to 64 for Amazon-M2 and Beauty.
- **Novelty:** Introduction of the trainable delta on top of frozen content embeddings with a bounded norm.

### Results
- The proposed trainable delta approach consistently improves performance on cold items across all three datasets compared to content-based baselines and SASRec with content initialization.
- Warm-item performance remains stable or slightly improves, demonstrating the robustness of the method.
- The norm of the trainable delta vector (𝛿 max) is a key hyperparameter; values in the range of 0.3 to 0.6 provide a good trade-off between flexibility and proximity to the original content embedding.
- Using content-based initialization, especially with the trainable delta, significantly improves recommendation quality when cold items are present in user input sequences.
- The trainable delta approach shows improvements for rare items, with performance converging to standard SASRec levels as item frequency increases.
- A limitation is the additional training cost due to maintaining a second embedding vector.
