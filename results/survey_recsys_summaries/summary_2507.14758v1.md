# Summary of 2507.14758v1.md

**Token Usage**: Input: 12613, Output: 724, Total: 13337

---

### Main Idea

- **Problem:** Existing generative models for multi-behavior recommendation systems (MBRS) suffer from a lack of explicit information for token reasoning, high computational costs due to full attention over long tokenized sequences, and limited multi-scale modeling of user history.
- **Motivation:** Improving the performance and efficiency of MBRS by incorporating explicit knowledge and reducing computational complexity can lead to better user personalization and scalability.
- **Proposed Solution:** GRACE (Generative Recommendation via journey-aware sparse Attention on Chain-of-thought tokEnization) is a novel generative framework. It introduces a hybrid Chain-of-Thought (CoT) tokenization method that incorporates explicit attributes from product knowledge graphs (PKGs) over semantic tokens. It also features a Journey-Aware Sparse Attention (JSA) mechanism that selectively attends to compressed, intra-, inter-, and current-context segments of the tokenized sequence.

### Technologies

- **Hybrid Chain-of-Thought (CoT) Tokenization:**
  - Combines semantic tokens (derived from item descriptions using RQ-VAE and K-means) with explicit attributes from PKGs (e.g., category, brand, price).
  - PKG traversal forms a Chain-of-Thought path, mimicking a user's decision-making process.
- **Journey-Aware Sparse Attention (JSA):**
  - Divides the attention process into four scopes: compression over journey blocks, selection of top-N intra-journey blocks, inter-journey traversal through coarse-grained tokens, and a truncated window for current-context modeling.
  - A trainable sparse attention mechanism is tailored for multi-behavior recommendation.
- **Encoder-Decoder Architecture:**
  - Utilizes an encoder-decoder structure similar to previous generative models.
  - The encoder learns rich contexts from item information, and the decoder predicts the target behavior-item pair tokens.
- **Datasets:**
  - Real-world user behavior data from Walmart.com for Home and Electronics categories.
  - Includes click, add-to-cart (ATC), like, and remove-from-cart behaviors.
- **Evaluation Metrics:**
  - Recall@K (HR@K) and Normalized Discounted Cumulative Gain (NDCG@K) with K=5 and 10.
  - Evaluated on target behavior item prediction, behavior-specific item prediction, and behavior-item prediction tasks.

### Results

- GRACE outperforms state-of-the-art baselines on two real-world datasets.
- Significant improvements on the Home domain: +106.9% HR@10 and +106.7% NDCG@10 over the best baseline (MBGen).
- Improvements on the Electronics domain: +22.1% HR@10 over MBGen.
- JSA reduces attention computation by up to 48% with long sequences.
- Ablation studies show the importance of both CoT tokenization and each component of the JSA mechanism.
- Sensitivity analysis shows optimal hyperparameter values for the window size in current-journey attention, the number of top blocks for intra-journey attention, and the beam width during inference.
- GRACE shows improvements in multi-behavior recommendation across Add-to-cart, Click, Like, and Remove-from-cart behaviors.
- Co-occurrence heatmaps show CoT tokenization narrows the effective search space during item generation, improving decoding efficiency.
