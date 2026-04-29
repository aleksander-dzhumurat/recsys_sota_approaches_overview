# Summary of 2508.21334v1.md

**Token Usage**: Input: 16612, Output: 768, Total: 17380

---

### Main Idea
- This paper addresses the lack of empirical understanding regarding the relationship between group and individual fairness in recommender systems (RSs).
- It is motivated by the need for responsible AI development, where RS fairness evaluation is crucial to prevent systematic disadvantages for users. Prior work has discussed potential conflicts between group and individual fairness but lacked empirical studies on how these conflicts manifest in RS fairness evaluation.
- The paper aims to fill this gap by conducting a comprehensive comparison of evaluation measures applicable to both group and individual fairness. The core approach is to evaluate user-side group and individual fairness using the same families of measures across multiple datasets, allowing for a direct comparison of fairness scores.

### Technologies
- **Datasets:** ML-1M, JobRec, and LFM-1B datasets are used. These datasets were preprocessed, filtering users and items based on interaction counts and removing minors.
- **User Grouping:** Users are grouped based on sensitive attributes like gender, age, occupation (ML-1M), degree, years of experience, major (JobRec), and gender, age, country (LFM-1B). Intersectional groups are formed by combining these attributes.
- **LLM-based Recommenders (LLMRecs):** Four open-source LLMs, Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, GLM-4-9B-chat, and Ministral-8B-Instruct-2410, are utilized as recommenders with in-context learning (ICL).
- **Prompt Engineering:** Two prompt types are used: Sensitive (S) prompts including interaction history and sensitive attributes, and Non-Sensitive (NS) prompts including only interaction history.
- **Evaluation Metrics:**
    - **Recommendation Effectiveness (Eff):** Mean Hit Rate (HR), MRR, P@k, and NDCG@k.
    - **Group Fairness:** Min, Range, SD, MAD, Gini, CV, FStat, KL, GCE, and Atkinson Index (Atk).  Between-group and within-group versions of these measures are also computed.
    - **Individual Fairness:** SD, Gini, and Atk.
- **Implementation Details:** The experiments are carried out with vllm and RecLM-eval. Fuzzy string matching with a TF-IDF ngram similarity threshold of 0.75 is used to evaluate LLMRecs. Kendall's 𝜏 is used to assess agreement between fairness measures.

### Results
- Group fairness measures often mask unfairness within groups and between individuals.
- No individual fairness measure consistently provides equivalent rankings to group fairness measures, indicating that individual fairness measures cannot reliably proxy for group fairness.
- Fairness worsens as more attributes are used for grouping, emphasizing the importance of considering intersectionality.
- Recommendations can be relatively fair for intersectional groups but much less fair for individuals. Individual fairness scores are consistently worse than group fairness scores.
- Within-group unfairness is almost as high as individual unfairness and consistently higher than between-group unfairness, regardless of how users are grouped.
- Including sensitive attributes in the prompt has little effect on effectiveness/fairness. An exception to this is Ministral-8B for LFM-1B, which may be due to the LLM's relatively high gender bias.
- For Atk/Gini, the fairest model for intersectional groups and for individual users are always the same, but this is not the case for SD. Thus, if sensitive attribute information is missing, Atkind /Giniind can estimate which model is the fairest for intersectional groups.
