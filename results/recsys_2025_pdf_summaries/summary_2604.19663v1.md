### Main Idea
- The paper addresses the lack of standardized evaluation protocols for counterfactual explanations (CEs) in recommender systems.
- It highlights the problem that existing CE methods are evaluated using heterogeneous protocols, datasets, and metrics, hindering reproducibility and fair comparison.
- The paper proposes a unified benchmarking framework to systematically reproduce, re-implement, and re-evaluate state-of-the-art CE methods for recommender systems, covering both native explainers and graph-based explainers. The framework is designed to assess explainers along three dimensions: explanation format (implicit vs. explicit), evaluation level (item-level vs. list-level), and perturbation scope (user interaction vectors vs. user-item interaction graphs).

### Technologies
- The study involves re-implementing and evaluating eleven state-of-the-art CE methods: LIME-RS, SHAP, PRINCE, ACCENT, LXR, GREASE, CF-GNNExplainer, CF2, CLEAR, UNR-Explainer, and C2Explainer.
- The unified benchmarking framework includes evaluation criteria such as effectiveness (Positive Perturbation, Negative Perturbation, Probability of Necessity - Single, Probability of Necessity - Ranking), explanation sparsity (Gini Index, #Perturb), and computational complexity (inference time).
- Experiments are conducted on three real-world datasets: Amazon Fashion, ML1M, and Yahoo.
- Six representative recommender models are used: MF, VAE, DiffRec, LightGCN, GFormer, and SimGCL.
- The implementation is done in PyTorch, and hyperparameter tuning is performed using Optuna.

### Results
- The study found that the trade-off between effectiveness and sparsity depends strongly on the specific CE method and evaluation setting, particularly under the explicit format.
- Explainer performance remains largely consistent across item-level and list-level evaluations.
- Several graph-based explainers exhibit notable scalability limitations on large recommender graphs.
- LXR exhibits a clear advantage in both effectiveness and sparsity under the implicit format.
- GREASE achieves strong performance on Amazon but degrades substantially on ML1M and Yahoo. CF2 and C2Explainer achieve the highest effectiveness overall, but require extremely large perturbation sets.
- Restricting perturbations to k-hop subgraphs can effectively reduce the search space while preserving explanation quality for certain methods.
- Pretraining-based methods (LXR and CLEAR) exhibit minimal inference time but can have scalability issues due to memory overhead.
- The study challenges earlier conclusions about the robustness and practicality of CE generation methods and provides a reproducible reference point for future work, with code available at https://github.com/L2R-UET/CFExpRec.
