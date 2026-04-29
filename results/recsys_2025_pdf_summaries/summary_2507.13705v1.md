### Main Idea
- The paper investigates how Large Language Models (LLMs) perform as joint decision-makers and explanation generators in Group Recommender Systems (GRS). It aims to contextualize LLM-generated group recommendations by comparing them with recommendations derived from established social choice-based aggregation strategies (Additive Utilitarian, Approval Voting, Least Misery, and Most Pleasure).
- The motivation stems from the increasing use of LLMs in recommendation systems, particularly in group settings, where aggregating individual preferences is a complex task.  The significance lies in evaluating the consistency and reliability of LLMs as both recommenders and explainers in GRS, ensuring transparency and explainability.
- The approach involves generating fictitious group scenarios, prompting several LLMs to produce recommendations and explanations, and then comparing the LLM outputs with the results of social choice-based aggregation strategies. The study also examines the impact of group preference structures (uniform vs. divergent) and the number of items on LLM performance.

### Technologies
- **LLMs:** Llama3.1 (8B), Mistral NeMo (12B), Gemma3 (12B), and Phi4 (14B) were used to generate group recommendations and explanations.  Ollama was used to run LLMs and the Langchain python package was used to load and prompt the included models.
- **Social Choice-Based Aggregation Strategies:** Additive Utilitarian (ADD), Approval Voting (APP), Least Misery (LMS), and Most Pleasure (MPL) were implemented as baselines for comparison.
- **Evaluation Metric:** NDCG@10 was used to measure the similarity between LLM-generated recommendations and those produced by the aggregation strategies.
- **Group Structure Analysis:** Euclidean distance was used to calculate within-group user distance, classifying groups as either uniform or divergent based on a threshold derived from the normal distribution of distances.
- **Explanation Categorization:** A rule-based fuzzy string matching approach, using the RapidFuzz library with Levenshtein distance, was employed to categorize LLM-generated explanations into predefined categories (e.g., averaging ratings, user similarity).
- **Experimental Setup:**  Randomized, fictitious group scenarios were created with four users and varying numbers of items (25, 50, or 75) rated on a scale of 0-100.

### Results
- LLM-generated recommendations often resembled those produced by the Additive Utilitarian (ADD) aggregation strategy. Gemma3 was an exception, with recommendations more closely aligning with the Most Pleasure (MPL) strategy.
- LLM-generated explanations frequently referred to averaging ratings, aligning with the ADD strategy. However, many explanations also mentioned "undefined popularity" metrics or thresholds, indicating a lack of transparency.
- Group structure (uniform vs. divergent preferences) had a limited impact on LLM performance. LLMs performed slightly better on uniform groups.
- Increasing the number of items led to a decrease in NDCG@10 scores and an increase in the frequency of LLM explanations referencing user/item similarity and diversity, suggesting a shift from simple averaging to more complex aggregation methods.
- LLMs tended to combine multiple approaches rather than consistently applying a single social choice-based strategy.  The choice of approach seemed to be influenced by the number of available items.
