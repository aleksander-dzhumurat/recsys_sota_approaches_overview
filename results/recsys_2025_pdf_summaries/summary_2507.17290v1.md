### Main Idea

- **Primary Research Objective:** To investigate whether Large Language Models (LLMs) can effectively simulate human users for serendipity evaluation in recommender systems, potentially combining the accuracy of user studies with the efficiency of proxy metrics. The study addresses the challenge of evaluating serendipity due to its subjective nature and the limitations of existing proxy metrics that don't fully align with user perceptions.
- **Motivation and Significance:** Serendipity enhances user satisfaction in recommender systems by mitigating information cocoon and filter bubble effects. The lack of effective and efficient evaluation methods hinders progress in serendipity-oriented research. LLMs have shown promise in user simulation and automatic assessment, motivating the investigation of their potential in serendipity evaluation.
- **Proposed Approach:** The study conducts a meta-evaluation framework, SerenEva, on two datasets from e-commerce and movie domains, comparing LLM performance against conventional proxy metrics and real user feedback. It explores the impact of auxiliary data and multi-LLM techniques on evaluation accuracy.

### Technologies

- **Key Technical Components:**
    - **Large Language Models (LLMs):**  LLaMA2 (7B, 13B), Qwen2.5 (7B, 14B, 72B), GPT-4. Used in zero-shot and few-shot settings.
    - **Conventional Proxy Metrics:** SOG, SNPR, PURS, DESR. Metrics based on relevance, diversity, unexpectedness, and user history used for comparison.
    - **SerenEva Framework:**  A meta-evaluation framework measuring the alignment between LLM evaluator ratings and human judgments using correlation and error metrics.  It evaluates the discrepancy between evaluation results from different methods (LLMs, proxy metrics) and real user feedback.
- **Algorithms, Models, and Frameworks:**
    - **Zero-shot and Few-shot Learning:** LLMs are used with basic prompting strategies and with a few examples to evaluate serendipity.
    - **Multi-LLM Techniques:** Score averaging used to combine predictions from multiple LLMs.
    - **Constrained Prompting:** Used to guide LLMs in providing serendipity ratings on a 5-point Likert scale.
- **Datasets, Evaluation Metrics, and Experimental Setups:**
    - **Datasets:** Taobao Serendipity (e-commerce) and Serendipity-2018 (MovieLens). User-study-validated datasets with serendipity ratings.
    - **Evaluation Metrics:** Pearson correlation coefficient, Mean Absolute Error (MAE), Root Mean Squared Error (RMSE). Used to compare LLM and proxy metric performance against user feedback.
    - **Experimental Setup:** User historical behavior data, auxiliary data (user demographics, item popularity, etc.), and different LLM configurations. Experiments conducted to address three research questions: (1) LLM performance vs. proxy metrics, (2) impact of auxiliary data, and (3) effectiveness of multi-LLM techniques.
- **Novel Technical Contributions or Innovations:**
    - The comprehensive meta-evaluation framework, SerenEva, measuring the alignment between LLM evaluators and human judgments using correlation and error metrics.
    - Systematic investigation of leveraging LLMs as evaluators for serendipity in recommender systems.
    - Exploration of auxiliary data and multi-LLM techniques to enhance LLMs' understanding of serendipity.

### Results

- **Main Experimental Findings:**
    - Zero-shot and few-shot LLMs achieved parity with or surpassed conventional proxy metrics.  LLMs like Qwen2.5-14B and GPT-4 outperformed proxy metrics by approximately 100% in Pearson correlation.
    - Incorporating auxiliary data, like user curiosity and item similarity, significantly enhanced LLM evaluation accuracy, with the optimal data depending on the domain. Curiosity was more beneficial in the Taobao dataset, while item popularity was crucial for Serendipity-2018.
    - Multi-LLM techniques with score averaging substantially improved evaluation performance and alignment with human judgments.
- **Quantitative Results, Performance Improvements, and Comparisons:**
    - The optimal evaluation by LLMs yielded a Pearson correlation coefficient of over 20% when compared to the results of the user study. Achieved 20.23% on Taobao and 21.51% on Serendipity-2018.
    - Multi-LLM ensembles showed performance improvements as the number of LLMs increased, indicating their ability to compensate for the limitations in knowledge and reasoning abilities inherent to a single LLM.
- **Key Insights or Discoveries:**
    - LLMs, when appropriately prompted, may serve as potentially reliable and reproducible evaluators that surpass conventional proxy metrics in accuracy.
    - The effectiveness of auxiliary data is domain-dependent.  Incorporating all available auxiliary data indiscriminately may not align with user study assessments.
    - Smaller parameter models can deliver high-quality outcomes in few-shot learning scenarios.
- **Limitations or Future Work:**
    - The LLaMA family models did not exhibit exceptional performance, especially on the Taobao dataset, possibly due to the dataset's focus on the Chinese community and the models' limited proficiency in processing Chinese.
    - Future work aims to explore more advanced LLM techniques and investigate the explainability of serendipity.
