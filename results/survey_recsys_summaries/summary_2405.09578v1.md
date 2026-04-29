# Summary of 2405.09578v1.md

**Token Usage**: Input: 17429, Output: 1021, Total: 18450

---

### Main Idea

-   The research paper explores the feasibility of detecting dark matter (DM) by observing its heating effect on exoplanets in the inner regions of the Milky Way.
-   DM particles can be captured by exoplanets, and their subsequent annihilation deposits energy, increasing the exoplanet's temperature beyond what would be expected from standard formation and evolution models.
-   By measuring the temperatures, masses, ages, and locations of exoplanets, the researchers aim to infer the density profile of DM in the Milky Way, addressing the motivation to understand the spatial distribution of DM and test DM hypotheses. The work suggests that exoplanets may be superior probes to other celestial objects, such as nuclear-burning stars, neutron stars and white dwarfs [3-52], the Earth [5355], and other planets and moons [55-64]. Exoplanets can be superior probes to these other celestial objects in several ways [2, 65]. First, they have cooler cores while having relatively high escape velocities, allowing lighter DM particles to not evaporate and be retained in the system, providing a probe of sub-GeV mass DM. Second, they have large radii, allowing them to be detectable far into the inner Galaxy. Third, exoplanets are highly abundant, such that this signature can be probed throughout the Galaxy with potentially high statistics. This allows for a location-dependent probe of the DM density profile.
-   The proposed solution involves developing a Bayesian Hierarchical Model (BHM) to simultaneously infer exoplanet population parameters, individual object properties, and DM halo parameters from exoplanet data. This model accounts for the correlated uncertainties and variability within the exoplanet population, as well as measurement uncertainties.

### Technologies

-   **Bayesian Hierarchical Model (BHM)**: A statistical framework that takes exoplanet properties as input and infers population parameters, individual properties, and Galactic DM density profiles. The model accounts for correlated uncertainties and variability.
-   **gNFW DM Density Profile:** Generalized Navarro-Frenk-White halo profile to model the spatial distribution of dark matter.
-   **Pareto Distribution:** Used to model the initial mass function for the exoplanets.
-   **Exponential Distribution:** Used to model exoplanet spatial distribution within the galactic bulge.
-   **Maxwell-Boltzmann Distribution:** Used to model the velocity profile of dark matter particles.
-   **No-U-Turn Sampler (NUTS)**: A self-tuning variant of Hamiltonian Monte Carlo (HMC) used for sampling the high-dimensional posterior distribution in the Bayesian model.
-   **Pyro**: A probabilistic programming language used for implementing the NUTS sampler and the overall BHM.
-   **Mock Data**: Simulated exoplanet datasets generated with varying noise levels (1-20%) and sample sizes (10-200) to test the inference procedure. The range [1 , 20] % , where the optimistic (but unrealistic in the near future) value of 1% allows verification of the inference procedure, while a more realistic albeit still optimistic scenario is 20% uncertainty [70]. Additionally, we vary the number of observed exoplanets N from 10 to 200.
-   **Performance Metrics**: credible intervals, normalized bias, Bayes factor, and posterior distributions are used to evaluate performance of inferences.

### Results

-   Detection of around 100 exoplanets in the inner Galaxy can yield quantitative information on the galactic DM density profile, assuming 10% measurement uncertainty.
-   Even with as few as 10 exoplanets, meaningful sensitivities can be achieved if the DM density and inner slope are sufficiently large.
-   The study demonstrates that it is possible to achieve high accuracy in inferring the shape of the DM halo, both in the inner slope and in the normalization.
-   With 1% measurement uncertainties, observations of a sample of about 10 exoplanets can be sufficient for this task, depending on the underlying DM density and inner DM slope.
-   More realistic (but still optimistic) measurement uncertainties of about 10% require around 100 exoplanets for DM parameter inference.
-   The study identifies a systematic shift of the posteriors towards the middle of the prior range when the true values of the inner DM profile slope α are at the extremes of this range, particularly for larger noise levels and smaller numbers of exoplanets, which is called 'shrinkage'.
-   The mean estimate of α tends to be biased low, while that of the DM density at a Galactocentric radius of 1 kpc, C, tends to be biased high, explained by the anticorrelation between these parameters.
-   Future work should include observational selection effects using simulation-based inference (SBI) to handle complex probabilistic models for parameter inference and model selection.
