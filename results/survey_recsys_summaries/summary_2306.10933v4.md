# Summary of 2306.10933v4.md

**Token Usage**: Input: 18878, Output: 1019, Total: 19897

---

### Main Idea

- **Problem:** Existing recommender systems (RSs) are limited by their insulated nature, trained and deployed within specific domains, restricting access to valuable open-world knowledge. Simply using Large Language Models (LLMs) for recommendation does not achieve optimal results due to accuracy, latency and compositionality issues.
- **Motivation:** Integrating external knowledge, like user preference reasoning and item factual knowledge, can significantly enhance the accuracy and generalization of recommender systems, leading to better user experiences.
- **Solution:** The paper proposes KAR (Knowledge Augmented Recommendation), a framework that bridges classical recommender systems and open-world knowledge by leveraging LLMs to generate both reasoning knowledge on user preferences (inferred from behavior) and factual knowledge on items (obtained from the web). KAR uses factorization prompting to elicit accurate reasoning and a hybrid-expert adaptor to transform generated knowledge into augmented vectors compatible with recommendation tasks, pre-storing the knowledge for efficient inference.

### Technologies

- **Factorization Prompting:** Decomposes complex preference reasoning into key factors to generate reasoning knowledge about users and factual knowledge about items, alleviating the compositional gap issue of LLMs. LLMs and experts collaborate to define the scenario-specific factors for different recommendation scenarios.
- **Knowledge Reasoning and Generation:** Uses prompts tailored to extract reasoning and factual knowledge from LLMs.
    - **Preference Reasoning Prompt:** Constructed using user profile, behavior history, and scenario-specific factors, enabling LLMs to analyze preferences from different facets.
    - **Item Factual Prompt:** Uses item descriptions and scenario-specific factors to guide LLMs in providing external knowledge to align user preferences.
- **Knowledge Adaptation:** Converts textual knowledge into compact representations suitable for recommendations.
    - **Knowledge Encoder:** Uses models like BERT or ChatGLM to encode generated text into dense vectors. Average pooling is used for aggregation.
    - **Hybrid-Expert Adaptor:** Transforms representations from the semantic space to the recommendation space. The module uses shared and dedicated experts (MLPs) to capture common and specific aspects of reasoning and factual knowledge. Gating networks determine expert weights.
- **Knowledge Utilization:** Integrates augmented vectors into recommendation models as additional input features, allowing the models to leverage both domain and open-world knowledge.
- **Evaluation Metrics:** AUC and LogLoss for CTR prediction; NDCG@K and MAP@K for reranking.
- **Backbone Models:** Experiments were conducted using DCNv2, DCNv1, DeepFM, FiBiNet, AutoInt, FiGNN, xDeepFM, DIEN, and DIN for CTR prediction. DLCM, PRM, SetRank, and MIR are used for reranking.
- **Baselines:** P5, UniSRec, VQRec, TALLRec, and LLM2DIN are used as baselines.
- **Datasets:** MovieLens-1M and Amazon-Books datasets.

### Results

- **Performance Improvement:** KAR significantly outperformed state-of-the-art baselines across various tasks, consistently improving AUC and LogLoss on CTR prediction and MAP/NDCG on reranking tasks. Using KAR improves the AUC of the selected 9 representative CTR models on two datasets by about 1-1.5%. KAR achieves an improvement of 5.71% in MAP@7 and 4.71% in NDCG@7 with PRM as the backbone for reranking on the Amazon-Books dataset.
- **Comparison with PLM-based Baselines:** KAR outperforms models using pretrained language models, demonstrating that KAR's approach to incorporating reasoning and factual knowledge is more effective. KAR outperformed the strongest baseline, TALLRec, by 0.91% in AUC and 1.27% in LogLoss on the Amazon-Books dataset with DIN as the backbone model.
- **Knowledge Source Comparison:** LLM-derived knowledge provided greater improvements compared to knowledge graphs (KGs), likely due to LLMs incorporating reasoning knowledge.
- **Online A/B Testing:** Deployment on Huawei's news and music recommendation platforms showed a 7% improvement on Recall metric and a 1.7% increase in song play count, respectively.
- **Ablation Studies:** Both reasoning and factual knowledge improve performance, with reasoning knowledge having a more substantial impact, even achieving a synergistic effect when combined (1+1>2).
- **Efficiency:** KAR, with preprocessing and prestoring techniques, achieves inference speeds comparable to original backbone models, addressing the latency issues associated with directly using LLMs. KAR inference time is nearly the same as the base DIN model with the augmented vectors prestored.
- **Privacy Considerations:** KAR ensures the privacy of users by leveraging LLMs' reasoning ability and factual knowledge without finetuning LLMs and avoids displaying harmful or misleading content generated by LLMs while enabling us to utilize filtering mechanisms commonly used in traditional RSs to screen out potential harmful item recommendations.
