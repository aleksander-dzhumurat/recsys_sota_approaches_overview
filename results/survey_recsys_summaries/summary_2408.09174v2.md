# Summary of 2408.09174v2.md

**Token Usage**: Input: 16415, Output: 884, Total: 17299

---

### Main Idea

- The paper addresses the gap between academic benchmarks and real-world applications of large language models (LLMs) in handling tabular data. It argues that existing benchmarks don't adequately capture the complex reasoning required in industrial scenarios.
- The authors propose TableBench, a new, comprehensive, and complex benchmark for table question answering (TableQA) covering 18 subcategories within four major categories: fact-checking, numerical reasoning, data analysis, and visualization. The benchmark aims to evaluate LLMs' capabilities in realistic, complex scenarios.
- They also introduce TableInstruct, a large-scale instruction corpus designed to train LLMs for TableQA using three distinct reasoning methods: Textual Chain-of-Thought (TCoT), Symbolic Chain-of-Thought (SCoT), and Program-of-Thought (PoT). Based on this, they train TABLELLM, an open-source model, achieving performance comparable to GPT-3.5, which serves as a strong baseline.

### Technologies

- **TableBench Benchmark:** A dataset of 886 samples with 18 subcategories covering fact-checking, numerical reasoning, data analysis, and visualization tasks. Tables are selected based on topic and size with at least 8 rows and 5 columns, including a significant number of numerical values.
- **TableInstruct Corpus:** A training dataset of ~20,000 samples designed to instruct LLMs in TableQA. This is created by using seed questions, GPT-4 based question generation, manual annotation, and a question verification process.
- **Reasoning Methods:**
    - **Textual Chain-of-Thought (TCoT):** LLMs generate a series of intermediate textual steps to reach the final answer.
    - **Symbolic Chain-of-Thought (SCoT):** LLMs use Python-based instructions to facilitate logical reasoning, involving analyzing information, generating Python code, and simulating outcomes.
    - **Program-of-Thought (PoT):** LLMs generate executable code (Python) that is run to derive the final answer.
- **Evaluation Metrics:** ROUGE-L for assessing the quality of generated answers, pass@1 for evaluating chart generation accuracy, and Pearson Correlation Coefficient (PCC) for evaluating the consistency between automatic and human evaluations.
- **Models:** Evaluated 34 models, including open-source (Llama2, Llama3, CodeLlama, CodeQwen, Qwen, Mistral, Deepseek, StructLM, MAP-Neo, WizardLM) and proprietary LLMs (GPT-3.5, GPT-4, Qwen-Max, GLM-4, Yi-Large, Deepseek). TABLELLM is fine-tuned on CodeQwen, DeepSeekCoder, Llama3, and Qwen2.
- **Training Setup:** Supervised finetuning using a cosine annealing scheduler, Adam optimizer, batch size of 512, and maximum sequence length of 4096 on A100 GPUs.

### Results

- Extensive experiments on TableBench show that both open-source and proprietary LLMs still have significant room for improvement to meet real-world demands. Even GPT-4 achieves only a modest score compared to human performance.
- TABLELLM, trained on TableInstruct, demonstrates comparable performance to GPT-3.5.
- Analysis reveals that TCoT generally performs better, while PoT excels in numerical computations but is limited by code execution success rates. SCoT performs modestly due to its reliance on simulated outcomes.
- Most models performed well in fact-checking but struggled with numerical reasoning, data analysis, and visualization tasks. Small models struggle with chart generation, highlighting a need for strong coding capabilities.
- Experiments indicate that the ROUGE-L metric is effective in evaluating performance on TableBench, confirmed by high agreement with GPT-4 and human evaluations.
- Smaller-sized LLMs perform better with direct prompting (DP) than with reasoning-based methods due to insufficient coding capabilities and the complexity of iterative symbolic reasoning.
- TableInstruct data efficient; Llama-3-8B surpasses Qwen1.5-70B with fewer than 4,000 samples.