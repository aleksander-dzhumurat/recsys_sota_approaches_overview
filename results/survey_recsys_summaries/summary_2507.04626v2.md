# Summary of 2507.04626v2.md

**Token Usage**: Input: 13622, Output: 802, Total: 14424

---

### Main Idea
- **Problem:** The paper addresses the challenge of effectively modeling user preferences from heterogeneous behaviors across multiple domains for open-domain recommendation using Large Language Models (LLMs). Existing methods struggle with poor generalization, inability to compress noisy interactions, and the domain seesaw phenomenon (where improvements in one domain lead to decline in others).
- **Motivation and Significance:** Leveraging LLMs for recommendation has shown potential, but modeling user preferences across diverse domains remains a key challenge. Accurately capturing these preferences from noisy, heterogeneous interactions is crucial for delivering personalized recommendations in open-domain scenarios.
- **Proposed Approach:** The paper proposes a Heterogeneous User Modeling (HUM) method that incorporates a compression enhancer and a robustness enhancer for LLM-based recommendation. The compression enhancer compresses heterogeneous behaviors into a tailored token using a customized prompt and a masking mechanism. The robustness enhancer introduces a domain importance score to mitigate the domain seesaw phenomenon.

### Technologies
- **Model Architecture:** A Large Language Model (LLM) is used as the base model, specifically Qwen2.5-1.5b.
- **Compression Enhancer:**
    - *Compression Prompt:* A customized prompt "Compress the following description about the user or item into the last token:" guides the LLM to compress user interactions.
    - *User Token:* A special token "[USER]" is inserted after the user input to serve as a designated aggregation anchor for user representation.
    - *Masking Mechanism:* Randomly masks a portion of target-domain items in the user history to encourage the model to leverage context from other domains.
- **Robustness Enhancer:**
    - *Domain Importance Score:* Quantifies each domain's importance based on empirical risk (average training loss per domain) to guide the model toward a more balanced optimization.
    - *Domain Smoothing:* Incorporates prior information into the domain importance estimation using a regulating factor and KL divergence to ensure training stability.
- **Training and Optimization:**
    - *Parameter-efficient fine-tuning:* LoRA (Low-Rank Adaptation) is used to fine-tune the LLM.
    - *Contrastive Learning:* A contrastive objective is used to improve the model's discriminative ability between the target item and its similar items.
- **Datasets:** Amazon review datasets from six domains ('Scientific', 'Office', 'Books', 'CDs', 'Auto', 'Tools') were used. Also, generalization was tested on 'Instruments', 'Games', 'Arts' and 'Sports' domains.
- **Evaluation Metrics:** Recall@K and NDCG@K (K=5, 10) were used.

### Results
- **Overall Performance:** HUM outperforms existing heterogeneous user modeling methods (ID-based and semantic-based) across six domains, demonstrating effectiveness in modeling user heterogeneity.
- **Ablation Study:** Removing the compression prompt, user token, or masking mechanism individually decreases performance, highlighting the contribution of each component.
- **Compression Effectiveness:** HUM shows a substantial improvement over LLM-Rec, especially on sequences with multi-domain interactions, validating HUM's strong performance under domain-level heterogeneity and its ability to compress heterogeneous user sequences and capture users' diverse preferences.
- **Robustness:** The domain importance score improves performance across domains, confirming its role as an effective regularizer that promotes balanced optimization.
- **Noise Resistance:** HUM consistently outperforms LLM-Rec-Qwen even under a high level of noise, demonstrating its strong resistance against random noise.
- **Generalization:** HUM achieves the best performance across domains, demonstrating strong generalization.
- **Scalability:** HUMconsistently outperforms LLM-Rec across all levels of heterogeneity, demonstrating its ability to handle diverse user interactions.
- **Mask Ratio effect:** Moderately increasing mask ratio improves the performance. However, excessively increasing mask ratio may inversely hurt the performance.
