# Summary of 2502.10648v3.md

**Token Usage**: Input: 23612, Output: 827, Total: 24439

---

### Main Idea
- The paper introduces LLM-Lasso, a novel framework that uses large language models (LLMs) to guide feature selection in Lasso ℓ1 regression. Unlike traditional methods that rely solely on numerical data, LLM-Lasso incorporates domain-specific knowledge extracted from natural language, optionally enhanced through a retrieval-augmented generation (RAG) pipeline, to seamlessly integrate data-driven modeling with contextual insights.
- The motivation is to augment traditional Lasso regression with task-specific expert knowledge in a systematic, scalable, and robust way, addressing the limitations of existing LLM-based feature selection methods that are vulnerable to hallucinations and lack robustness. The significance lies in enhancing model accuracy and interpretability, especially in high-stakes domains like biomedicine where precision is critical.
- LLM-Lasso generates penalty factors for each feature using an LLM, which are then converted into weights for the Lasso penalty using a simple, tunable model. A cross-validation step ensures that LLM-Lasso never performs worse than standard Lasso, regardless of the LLM's generation quality.

### Technologies
- **Core Model:** Lasso regression with LLM-informed penalty factors. The objective function is enhanced by assigning penalty factors to each coefficient in the ℓ1 penalty.
- **LLMs:** Black-box access to LLMs such as GPT-4o, GPT-3.5, DeepSeek-R1, LLaMA-3, and Qwen to generate penalty factors or importance scores for predictors. Different prompting strategies (Bayesian, ReLU, adversarial, empirically-calibrated) are employed.
- **RAG Pipeline:** Optional retrieval-augmented generation to extract domain-specific knowledge via LLMs. Includes a retrieval component that extracts relevant information from external knowledge sources (e.g., OMIM database) using semantic similarity search and a generation component where an LLM generates context-aware responses.
- **Cross-Validation:** k-fold cross-validation to tune the model's reliance on LLM knowledge. A family of transformations, T, is applied to the LLM-generated penalty factors, and the transformation τ* is chosen based on cross-validation loss.
- **Transformation Families:** Includes the inverse importance family (1 / Vη) and a ReLU-based family of penalty transformations. Simulations are used to find the better form of penalty factors.
- **Datasets:** Evaluation across various biomedical case studies, including lymphoma (unpublished) and lung cancer (public). Small-scale experiments use public datasets (Bank, Diabetes, Glioma, Wine Quality, Spotify 2024).
- **Evaluation Metrics:** Misclassification rate, AUROC (Area Under the Receiver Operating Characteristic curve), recall@k for RAG performance.

### Results
- LLM-Lasso consistently outperforms standard Lasso and existing feature selection baselines across various datasets.
- Metadata improves Lasso performance, evident in large-scale experiments where LLM-generated penalty factors boost Lasso's performance.
- LLM-Lasso is more robust than comparable LLM-driven methods. In adversarial simulations with corrupted gene names, LLM-Lasso's accuracy remains comparable to Lasso, while LLM-Score performs worse than random feature selection.
- LLM-Lasso is competitive in a broad variety of settings, matching or often outperforming baselines in both large- and small-scale experiments.
- RAG LLM-Lasso outperforms both baselines and plain LLM-Lasso, achieving lower misclassification rates with fewer selected genes. Larger and more powerful models generally perform better, especially with RAG.
- In the clinically relevant problem of classifying FL and DLBCL, several genes with high feature contributions have relevance in cancer genomics and hematology/oncology, especially in the GPT-4o LLM-Lasso heatmap. Genes like AICDA, BCL2, and BCL6, implicated in the transformation of FL to DLBCL, are consistently selected by RAG LLM-Lasso.
