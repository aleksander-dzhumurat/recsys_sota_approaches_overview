### Main Idea
- The paper addresses the challenge of personalized drug recommendation for complex clinical conditions like Parkinson's disease, where Large Language Models (LLMs) often struggle to capture the nuances of individual patient context. Existing Retrieval-Augmented Generation (RAG) methods are limited by either over-generalized guideline-based retrieval or majority bias in similar-patient retrieval.
- To overcome these limitations, the paper proposes PACE-RAG (Patient-Aware Contextual and Evidence-based Policy RAG), a novel framework that synthesizes individual patient context with the prescribing tendencies of similar cases to identify optimal prescriptions and generate explainable clinical summaries.
- PACE-RAG employs a four-stage reasoning process: Focus-Specific Retrieval, Prescribing Tendency Analysis, Policy-Driven Prescription Refinement, and Explainable Clinical Summary, to provide personalized and clinically grounded decision support.

### Technologies
- **Framework:** PACE-RAG, a four-stage RAG pipeline.
- **Focus-Specific Retrieval:** Retrieves similar patients using symptom-level keywords.
- **Prescribing Tendency Analysis:** Extracts treatment patterns from retrieved patient cohorts.
- **Policy-Driven Prescription Refinement:** Verifies the initial medication plan against the insights derived from the Prescribing Tendency Analysis, based on three policies (MAINTAIN, ADD, REMOVE).
- **Explainable Clinical Summary:** Synthesizes the decision trajectory into an interpretable report.
- **LLMs:** Llama-3.1-8B and Qwen3-8B as the backbone models.  Qwen2.5-14B, 32B and 72B also tested. MedGemma (4B) and HuatuoGPT-o1 (8B) also tested.
- **Datasets:** A real-world Parkinson's Disease dataset from Inje University Haeundae Paik Hospital (HPH) and the MIMIC-IV benchmark.
- **Evaluation Metrics:** F1 score, Accuracy, Precision, and Recall.  Drug Precision@k.
- **Baselines:** Zero-shot Baseline, Guideline RAG, TreatRAG, and MedReflect.
- **Implementation Details:**  SentenceTransformer (all-MiniLM-L6-v2) for embedding generation, FAISS for vector database, Google Translator API for translation (Korean to English).

### Results
- PACE-RAG achieved state-of-the-art performance on both the Parkinson's cohort and the MIMIC-IV benchmark, outperforming existing RAG methods and verification frameworks.
- On the Parkinson's cohort, PACE-RAG achieved F1 scores of 76.30% (Llama3.1-8B-Instruct) and 80.84% (Qwen3-8B).
- On the MIMIC-IV benchmark, PACE-RAG achieved F1 scores of 36.93% (Llama3.1-8B-Instruct) and 47.22% (Qwen3-8B).
- PACE-RAG consistently outperformed larger models such as Qwen2.5-72B when using Qwen3-8B, demonstrating superior reasoning efficiency.
- Blinded qualitative evaluation by Parkinson's specialists showed that PACE-RAG's reasoning is clinically meaningful and aligns with expert practitioners' intuitive reasoning.
- The study identifies limitations such as generalizability due to single-center data, computational latency, prompt engineering effort, and potential loss of linguistic nuance in translation. Future work includes multi-center validation, optimization of the pipeline, and exploration of multi-modal clinical signals.
