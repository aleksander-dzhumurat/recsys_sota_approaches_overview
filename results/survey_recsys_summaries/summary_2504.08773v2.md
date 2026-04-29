# Summary of 2504.08773v2.md

**Token Usage**: Input: 9079, Output: 543, Total: 9622

---

### Main Idea
- The paper addresses the challenge of applying causal and counterfactual inference techniques, specifically off-policy evaluation, to recommender systems that use Thompson Sampling (TS) for action selection.
- The core problem is that existing off-policy estimators rely on action propensities (probabilities), which are not readily available under TS procedures because the action selection is based on a posterior distribution over reward model parameters rather than a fixed probability distribution over actions.
- The proposed solution is to derive exact and efficiently computable expressions for action propensities under TS for common parameter and outcome distributions, enabling the use of Inverse Propensity Scoring (IPS) based off-policy estimators in TS scenarios.

### Technologies
- **Thompson Sampling (TS)**: Used as the core action selection policy, leveraging a posterior distribution over reward model parameters to probabilistically select actions.
- **Importance Sampling (IPS)**: Employed as the foundation for off-policy estimators, requiring accurate action propensities to address the mismatch between the logging and target policies.
- **Beta-Bernoulli model**: Used for binary outcomes, modeling the probability of success with a Beta distribution.
- **(Multivariate) Normal distribution**: Used to model the posterior over model parameters in general machine learning models for reward estimation.
- **Multivariate Normal CDF**: Used to compute action propensities for Gaussian reward distributions.
- **Regularized Incomplete Beta Function**: Used for deriving analytical expressions for action propensities for Beta distributions.
- **Open Bandit Pipeline (OBP)**: Used as a platform for empirical validation and reproducible experiments.
- **Bayesian Logistic Regression**: Used to train a model for a TS policy in the experimental setup.
- **Synthetic Data**: Used to simulate realistic recommendation scenarios.

### Results
- The paper derives novel, exact expressions for action propensities under TS for common scenarios: (log)normal distributions for continuous outcomes and Beta distributions for binary outcomes.
- It demonstrates that these expressions can be efficiently computed, enabling the application of IPS-based off-policy estimators in TS settings.
- Empirical validation, using the Open Bandit Pipeline, confirms that the derived action propensities can be successfully applied to IPS-based estimators (traditional, self-normalized, and β-IPS) to obtain unbiased and consistent estimates of the average reward expected from deploying a TS-based policy.
- The results show that the IPS-based estimators converge to the true value as the sample size grows.
- The study opens up avenues for future work by broadening the situations where causal and counterfactual inference questions can be answered reliably in recommender systems that use Thompson Sampling.
