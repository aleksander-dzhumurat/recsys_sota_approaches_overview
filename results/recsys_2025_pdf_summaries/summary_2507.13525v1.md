### Main Idea
- The research investigates the effectiveness of different prompt engineering techniques for Large Language Model (LLM)-based recommendation systems in a single-user, personalized setting.
- It addresses the limitations of traditional recommendation methods (e.g., collaborative filtering) in cold-start and cross-domain scenarios, where LLMs offer potential advantages through natural language understanding and generation.
- The study aims to provide practical guidance on selecting prompts and LLMs based on the balance between accuracy and cost for personalized recommendation.

### Technologies
- **LLMs**: Experiments were conducted using 12 LLMs from OpenAI, Meta, AWS, Microsoft, and Anthropic, categorized into low-cost (e.g., gpt-4o-mini, llama3.3-70b), high-cost (e.g., claude-3.7-sonnet), and reasoning models (e.g., o3-mini).
- **Datasets**: Eight publicly available datasets were used, including Yelp, MIND, Food, and five Amazon Review categories (Music, Movies, Groceries, Clothes, Books).
- **Prompt Engineering**: Twenty-three different prompt types were compared, including baseline prompts, rephrasing prompts, step-back prompts, and prompts inspired by NLP techniques like chain-of-thought reasoning.
- **Evaluation Metrics**: Recommendation accuracy was evaluated using nDCG@3 and Hit@3. Inference cost was measured in USD per 1,600 users.
- **Statistical Analysis**: Hypothesis testing (Wilcoxon signed-rank test) and linear mixed-effects models (LMEM) were used to evaluate the performance of different prompts while controlling for factors like LLM, user, and evaluation metric.
- **Meta-Prompting**: Techniques like Self-Refine and Self-Consistency were applied to refine LLM outputs based on initial reasoning.

### Results
- For cost-efficient LLMs (e.g., gpt-4.1-mini, llama3.3-70b), prompts that rephrase instructions, consider background knowledge (Step-Back), or facilitate reasoning (ReAct) were particularly effective.
- Commonly used NLP prompting styles like step-by-step reasoning and role-playing often led to lower accuracy.
- For high-performance LLMs (e.g., claude-3.7-sonnet), simpler prompts often outperformed more complex ones, while reducing cost.
- Reasoning models (e.g., o3) showed relatively strong performance but did not exceed the accuracy of claude-3.7-sonnet and had higher inference costs. Adding more reasoning steps did not always improve performance.
- The combination of claude-3.7-sonnet with Step-Back achieved the highest accuracy, but the difference compared to the baseline was minimal. gpt-4.1-mini or llama3.3-70b with Rephrase, ReAct, or Step-Back offered a cost-efficient alternative with about 90% of the accuracy at less than one-fifth of the cost.
- Guidelines were provided for applying the findings to new LLMs, prompt methods, or datasets, emphasizing the importance of recording ranking metrics and inference costs, and checking inference logs for incomplete rankings.
