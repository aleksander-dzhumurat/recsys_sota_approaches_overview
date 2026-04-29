# Summary of 2410.16755v1.md

**Token Usage**: Input: 10481, Output: 1021, Total: 11502

---

### Main Idea

- **Problem:** Existing video recommendation systems often employ non-personalized modules, such as adjusting the distribution of videos with varying durations, which fail to cater to individual user preferences and real-time interests. Applying uplift modeling, a personalized technique successful in online marketing, to video recommendation faces challenges in designing treatments and capturing real-time user interests.
- **Motivation:** Personalizing video recommendation can enhance user experience by providing a more diverse and relevant range of videos, improving metrics such as watch time, app usage, and retention. Uplift modeling helps identify which users are most positively influenced by specific treatments.
- **Approach:** The paper proposes a Coarse-to-fine Dynamic Uplift Modeling (CDUM) framework. CDUM consists of two modules: Coarse-grained Preference Modeling (CPM) and Fine-grained Interest Capture (FIC). CPM models long-term user preferences using offline features and FIC captures real-time user interests using online contextual features. The combination of both modules enables dynamic targeting of specific user groups with effective treatments. The treatment is designed as adjusting the distribution of videos with varying durations.

### Technologies

- **Model Architecture:** CDUM is a two-module framework consisting of CPM and FIC.
    - **CPM (Coarse-grained Preference Modeling):** This module uses offline user features to model long-term preferences. It expands the treatment representation into guidance and indicator parts. The guidance filters and extracts information from user features, while the indicator enhances generalization across different treatments. A multi-treatment learning paradigm is used. It leverages a gating network with expert modules to predict the response of a user to a specific treatment. Huber loss is used for training.
    - **FIC (Fine-grained Interest Capture):** This module uses online real-time contextual features and request-level candidates to model users' current interests. It utilizes a Multi-Task Learning (MTL) module, similar to MMOE, to output real-time interest scores for videos with different durations. Huber loss is used for training. The ratio of long-play to short-play videos is used as the request-level label for training.
- **Treatment Design:** The treatment is designed as adjusting the distribution of videos with varying durations, based on the observation that increasing the exposure of short videos boosts commercialization metrics while enhancing long videos improves consumption metrics.
- **Datasets:**
    - **Public Datasets:** CRITEO and LAZADA are used for offline evaluation.
    - **Industrial Dataset:** A Kuaishou dataset, consisting of online user data collected before and during randomized controlled trials, is used. Features include user attributes, consumption information, and commercial attributes.
- **Evaluation Metrics:** Normalized Area Under the Uplift Curve (AUUC), normalized area under the qini curve (QINI), and uplift score at first ℎ percentile (LIFT@ ℎ ) are used for offline evaluation. APP usage time, watch time, Next day retention, and 7-day retention are used for online A/B testing.
- **Baselines:** S-Learner, T-Learner, BNN, TARNet, CFRNet, CEVAE, GANITE, DragonNet, FlexTENet, EUEN, DESCN, and EFIN are used as baselines for comparison in offline experiments. Multi-task models like Shared Bottom, MMOE, PLE, and MESI are used to replace CPM for effectiveness testing.
- **Implementation Details:** The model is implemented in TensorFlow using the Adam optimizer with a learning rate of 0.001. The batch size is 4096 and the embedding dimension is 32.

### Results

- **Offline Evaluation:** CDUM outperforms baseline uplift modeling methods on CRITEO and LAZADA datasets, demonstrating its effectiveness in uplift modeling. It also showed superior performance compared to multitask learning models on the Kuaishou dataset in a multi-treatment setting.
- **Ablation Studies:** Ablation studies on CPM showed that both the indicator embedding and the guidance embedding contribute to the model's performance.
- **Online A/B Testing:** Online A/B testing on the Kuaishou platform showed significant improvements in consumption metrics (APP usage time, watch time) and retention metrics (Next day retention, 7-day retention, Enter LT7/LT30, Slide LT7/LT30) compared to the online baseline. Specifically, significant improvements of 0.048% / 0.041% and 0.041% / 0.039% with respect to Enter LT7/LT30 and Silde LT7/LT30 respectively were observed.
- **Ablation of FIC:** Removing the FIC module resulted in performance degradation, highlighting its importance for online adjustment.
- **Deployment:** CDUM is deployed on the Kuaishou platform, serving hundreds of millions of users daily.
