# Summary of 2508.12665v2.md

**Token Usage**: Input: 11355, Output: 768, Total: 12123

---

### Main Idea
- The paper addresses the problem of accurate watch time prediction in short-video platforms, which is crucial for enhancing user engagement.
- It identifies two key challenges: coarse-grained skewness due to quick-skips and fine-grained diversity arising from various user-video interaction patterns.
- The proposed solution is an Exponential Gaussian Mixture Network (EGMN) that assumes watch time follows an Exponential Gaussian Mixture (EGM) distribution, where the exponential component models skewness and the Gaussian components capture diversity.

### Technologies
- **EGM Distribution:** A mixture distribution composed of one exponential distribution to capture coarse-grained skewness (quick-skips) and K Gaussian distributions to capture fine-grained diversity (user-video interaction patterns).
- **EGMN Model:** A neural network architecture designed to parameterize the EGM distribution. It consists of:
    - A **hidden representation encoder**: Takes user features, video features, and contextual information and encodes them into a shared hidden representation. This encoder can be any standard backbone used in recommender systems (e.g., DCN, DIN, SENet, Transformer).
    - A **mixture parameter generator**: Uses the hidden representation to estimate the parameters of each distribution component (exponential rate, Gaussian means and variances, and mixture weights).  Softplus activation ensures positivity for rate, mean, and variance, while softmax ensures mixture weights sum to one.
- **Loss Functions:** A combination of three loss functions is used to optimize the model:
    - **Maximum Likelihood Estimation (MLE) Loss**: Maximizes the likelihood of observed watch times under the EGM distribution.
    - **Entropy Maximization Loss**: Prevents the model from collapsing into a single component by maximizing the entropy of the mixture weights.
    - **Regression Loss**: Incorporates a regression loss between the expected value of the EGM distribution and the actual watch time.
- **Datasets:**
    - **Indust**: A real-world industrial dataset from Xiaohongshu.
    - **KuaiRec**: A public dataset from the KuaiShou mobile app.
    - **WeChat**: A public dataset from WeChat Channels.
    - **CIKM**: A public dataset from the CIKM16 Cup Competition.
- **Evaluation Metrics:**
    - **MAE (Mean Absolute Error)**: Measures the average absolute error between predicted and actual watch times.
    - **XAUC**: Measures the consistency between predicted and ground truth order of watch time values (ranking performance).
    - **KL Divergence**: Used online to measure the divergence between the predicted and actual watch time distributions.

### Results
- Offline experiments on four datasets show that EGMN outperforms state-of-the-art methods, achieving an average improvement of 14.11% in MAE and 7.76% in XAUC.
- Online A/B tests on Xiaohongshu App demonstrate a significant improvement (+0.681%) in user watch time compared to a baseline (CREAD).
- EGMN shows a significant improvement (+0.189%) in video views, indicating better alignment with user interests.
- EGMN reduces the KL divergence by nearly 20% compared to CREAD, demonstrating a closer approximation to the ground-truth distribution.
- Ablation studies validate the contribution of each component (exponential and Gaussian) in the EGM distribution and each loss function (MLE, entropy, and regression).
- EGMN demonstrates the ability to recognize quick-skipping behaviors more effectively than other models.
- EGMN exhibits excellent distribution-fitting ability across coarse-to-fine-grained levels, capturing complex patterns within watch time distributions.
