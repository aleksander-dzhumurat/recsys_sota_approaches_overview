### Main Idea

- The paper investigates the zero-shot performance of Generalist Text Embedding Models (GTEs) in sequential recommendation and product search tasks.
- It challenges the common belief that task-specific fine-tuning is essential for achieving optimal performance with pre-trained language models (PLMs) in these domains.
- The central idea is that GTEs, pre-trained on large and diverse corpora, can achieve strong performance without any specialized adaptation. The authors attribute this to GTE's superior representational power, specifically their more uniform distribution of features across the embedding space.
- They also explore how dimensionality reduction techniques like PCA can further improve the performance and efficiency of these models.

### Technologies

- **Generalist Text Embedding Models (GTEs):** Models like NVEmbed-v2, GTE-Qwen2, KALM, mGTE, InstructOR XL, Sentence-T5 XXL, and Jasper. These models are trained on diverse corpora and tasks to produce rich, transferable representations. They leverage different transformer architectures, including encoder-based (e.g., BERT, Sentence-T5) and decoder-based (e.g., Qwen2) models.
- **Sequential Recommendation Models:** GRU4Rec, SASRec, and UniSRec were employed, along with adaptations to incorporate textual metadata.
- **Product Search Models:** The study compared the performance of GTEs with other text encoders like RoBERTa BASE, ColBERTv2, and BL a IR.
- **Datasets:** Amazon Reviews 2023 for both SR and PS, ESCI and Amazon-C4 for PS.
- **Evaluation Metrics:** Recall@k and nDCG@k were used to evaluate the performance of the models.
- **Dimensionality Reduction:** Principal Component Analysis (PCA) was used to estimate the effective dimensionality of the embeddings and to compress them by retaining only the most informative components. The concept of /u1D700-effective dimension was used to quantify space utilization.
- **Implementation Details**: Hugging Face Transformers library, RecBole framework

### Results

- **GTEs outperform traditional and fine-tuned models**: The experimental results demonstrated that GTEs outperformed traditional ID-based methods (GRU4Rec, SASRec) and task-specific fine-tuned models (BL a IR) in both sequential recommendation and product search tasks.
- **Competitive Performance against Closed-Source models:** Some GTEs (e.g., NVEmbed-v2, GTE-Qwen2) even surpassed the performance of closed-source models like OpenAI's text-embedding-3-large (t-emb-3).
- **Space Utilization Matters:** GTEs showed more uniform space utilization than fine-tuned models.
- **PCA Improves Specialized Models:** Compressing embedding dimensions using PCA, by focusing on the most informative directions, effectively reduces noise and improves the performance of specialized models like BL a IR.
- **Capacity Does Not Scale Linearly:** The study found that performance does not necessarily scale linearly with model capacity or dimensionality. Smaller GTEs (e.g., KALM) can sometimes outperform larger models.
- **Decoder-Based Architectures are Better:** Architecturally, decoder-style models (Jasper, GTE-Qwen2, NVEmbed-v2) outperformed encoder-based ones.
