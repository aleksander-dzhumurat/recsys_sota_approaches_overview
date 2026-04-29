# Summary of 2508.03703v2.md

**Token Usage**: Input: 12642, Output: 606, Total: 13248

---

### Main Idea
- This paper investigates the privacy vulnerabilities of Large Language Model (LLM)-empowered recommender systems (RecSys) by demonstrating that they are susceptible to inversion attacks.
- The study highlights the potential for adversaries to reconstruct user prompts containing sensitive information (personal preferences, interaction history, demographics) by exploiting the output logits of recommendation models. This poses a significant privacy risk to both users and the RecSys providers.
- The authors propose an optimized inversion framework that leverages a vec2text engine combined with a similarity-guided refinement procedure to reconstruct the original prompts.

### Technologies
- **LLM-empowered RecSys Models:** The study uses two representative LLM-based recommendation models, TallRec (fine-tuned LLaMA-7B) and CoLLM (LoRA-tuned Qwen-7B with collaborative embeddings).
- **Inversion Attack Framework:**
    - **Projection Network:** Converts the logits into fixed-size embeddings.
    - **Inversion Model:** Uses a vec2text encoder-decoder model (T5-base) to map the embeddings back to possible textual prompts.
    - **Similarity-Guided Refinement:** Employs beam search to generate candidate prompts and iteratively selects the one whose logits have the highest cosine similarity to the ground truth until convergence.
- **Datasets:**
    - MovieLens (ML-1M, ML-25M, ML-32M) and Amazon Books Reviews datasets are used for training and evaluating the RecSys models and for constructing synthetic datasets for the inversion models.
    - Synthetic datasets (InvInst_movie, InvInst_book) are constructed using a pipeline that incorporates diverse prompt templates across five representative recommendation tasks.
- **Evaluation Metrics:** BLEU, ROUGE-L, Token-level F1, ItemMatch (proportion of recovered ground-truth items), and ProfileMatch (accuracy of recovering user age and gender).

### Results
- The proposed inversion framework demonstrates a strong ability to reconstruct prompts across both movie and book domains, with text similarity metrics exceeding 51% and up to 85% on the TallRec-based movie recommendation model.
- The model achieves high-fidelity recovery of sensitive user profiles, with ProfileMatch scores reaching 83.3%-87.0%.
- The effectiveness of the attack depends on domain alignment between the training data of the inversion model and the target RecSys. Models trained on domain-aligned data achieve substantial gains in reconstruction performance.
- Similarity-Guided Refinement further enhances performance by improving the accuracy of prompt reconstruction.
- The study reveals that prompt leakage is largely insensitive to the recommender's performance, as the logits continue to encode specific details of the input regardless of the overall performance of the RecSys.
- The limitations of the attack include performance degradation as prompt length increases due to the constraint of reconstructing more tokens from a fixed-size probability vector.
