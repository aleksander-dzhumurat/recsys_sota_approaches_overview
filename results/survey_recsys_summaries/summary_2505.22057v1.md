# Summary of 2505.22057v1.md

**Token Usage**: Input: 18829, Output: 812, Total: 19641

---

### Main Idea
- Recommender systems often suffer from noisy interactions (accidental clicks, popularity bias). Existing methods filter interactions based on assumed user intent, ignoring that 'noisy' interactions can aid training while 'clean' interactions may be unhelpful. The paper proposes Shapley Value-driven Valuation (SVV), a framework to evaluate interactions based on their objective impact on model training, quantifying each interaction's value by its contribution to reducing training loss using Shapley values. SVV highlights high-value interactions while downplaying low-value ones for effective data pruning, shifting denoising from heuristic filtering to principled model-driven valuation.
- The motivation is to address the limitations of existing denoising methods that rely on subjective intent assumptions and heuristic rules to identify noisy interactions. The significance lies in improving recommendation accuracy and robustness by focusing on the training utility of interactions rather than relying solely on user intent.
- The proposed approach is to use Shapley values to quantify the contribution of each user-item interaction to the reduction of training loss. A real-time Shapley value estimation method (FastSHAP) is used to mitigate the high computational cost of exact Shapley value calculation. The framework includes a simulated noise protocol to examine the performance of various denoising approaches systematically.

### Technologies
- **Shapley Value-driven Valuation (SVV)**: A framework for evaluating user-item interactions based on their objective impact on model training.
- **Shapley values**: A concept from cooperative game theory used to assess the contribution of each interaction to the overall model performance.
- **FastSHAP**: A real-time Shapley value estimation method used to mitigate the high computational cost of exact Shapley value calculation.
- **Denoising Autoencoder (DAE)**: Used as the base recommendation model. The DAE masks and reconstructs user-item interaction data. The code normalizes and adjusts the model's outputs by leveraging additive efficient normalization, inspired by prior works like [25,39].
- **Simulated noise injection protocol**: A method for injecting simulated noise into the dataset to validate the impact of noise and establish a verifiable ground truth. Specifically, the process randomly selects a fraction 'k' % of interacted items for non-interacted items to flip their interaction labels from 0 to 1, thereby artificially injecting noise. This enables the objective evaluation of denoising methods. The chosen 'k' hyperparameter was set to 20, as it was determined that the value of 'k' had no effect on the main experimental conclusions.
- **Datasets**: Ta Feng, Amazon (CDs and Vinyl, Video Games, Movies and TV).
- **Evaluation Metrics**: Recall@K, NDCG@K.

### Results
- SVV outperforms existing denoising methods in both accuracy and robustness on four real-world datasets. SVV consistently achieves the best performance across all datasets and evaluation metrics, with an average improvement of 3.72% over the DAE base model and an even greater improvement of 4.63% on the Games dataset. The implementation of Shapley values provides an efficient and interpretable means to identify and prune low-quality interactions, enhancing recommendation accuracy and robustness.
- SVV more accurately identifies high-contribution interactions and mitigates the adverse effects of low-quality interactions, including instances of different noise types (random, popular, unpopular item injections).
- Analysis demonstrates that SVV can preserve training-critical interactions and offer interpretable noise assessment. In particular, the evaluation based on Shapley values offers an efficient and interpretable means to identify and prune low-quality interactions.
- A case study is provided to showcase how SVV distinguishes user-preferred items from those truly valuable for training, revealing that some positive feedback may have little learning utility.
- The limitations or future work are mentioned as: Extending SVV to dynamic settings and exploring scalable variants to further enhance its applicability in evolving recommendation environments.
