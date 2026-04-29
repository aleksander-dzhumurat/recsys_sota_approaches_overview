# Summary of 2405.11764v2.md

**Token Usage**: Input: 12651, Output: 934, Total: 13585

---

### Main Idea
- **Primary Research Objective**: The paper addresses the problem of user fatigue in sequential recommendation systems, which occurs when users become tired of seeing recommendations that are too similar to content they've recently interacted with.
- **Motivation and Significance**: User fatigue can negatively impact user experience and platform activity. Existing recommendation systems often overlook this factor, focusing primarily on accurately capturing user interests without considering the potential for overexposure to similar content. The paper argues that understanding and mitigating user fatigue is crucial for enhancing user satisfaction and engagement.
- **Proposed Approach**: The paper introduces FRec (Fatigue-aware Recommendation), a model that integrates user fatigue into the interest learning process. FRec addresses three main challenges: (1) obtaining fine-grained features to support fatigue modeling, (2) capturing the complex influence of fatigue on both long-term and short-term user interests, and (3) obtaining explicit signals of user fatigue for model training.

### Technologies
- **Multi-Interest Extraction**: The model uses a self-attention mechanism to extract multiple interest representations from the user's historical interaction sequence. This allows for a more nuanced understanding of user preferences beyond a single, generalized interest profile.
- **Interest-Aware Similarity Matrix (ISM)**: FRec constructs an ISM to measure the similarity between the target item and historical items with respect to each user interest. This matrix is based on the projection distance between item embeddings in a latent space, providing a fine-grained measure of similarity compared to traditional item-level or category-level features.
- **Fatigue-Enhanced Multi-Interest Fusion**: The model utilizes cross networks to capture complex non-linear dependencies between target-historical item similarity and user fatigue. These cross networks are applied to the ISM to model how fatigue influences long-term user interests, adaptively adjusting the importance of different sub-interests.
- **Fatigue-Gated Recurrent Unit (FRU)**: A novel FRU, built upon the GRU architecture, is introduced to model the influence of temporal user fatigue on short-term interest learning. The FRU incorporates extracted fatigue representations as additional inputs to the update and reset gates, allowing the model to dynamically adjust short-term interest evolution based on the user's level of fatigue.
- **Sequence Augmentation and Contrastive Learning**: To address the lack of explicit fatigue signals, the paper proposes a sequence augmentation technique. This involves replacing items in the user's historical sequence with the target item, creating counterfactual scenarios where users are likely to experience increased fatigue. Contrastive learning is then used to train the model to predict fatigue levels based on the original and augmented sequences, providing supervision for representation learning.
- **Datasets**: The model was evaluated on two public datasets (Kuaishou and Taobao) and one large-scale industrial dataset collected from Kuaishou.
- **Evaluation Metrics**: Performance was evaluated using standard recommendation metrics, including AUC, GAUC, HR@k, NDCG@k, and MRR.

### Results
- **Improved Recommendation Accuracy**: FRec consistently outperformed state-of-the-art recommendation models on both public and industrial datasets. Specifically, FRec achieved improvements in AUC and GAUC of up to 0.026 and 0.019, respectively, compared to existing methods.
- **Effectiveness of Key Modules**: Ablation studies demonstrated the necessity of each proposed module for modeling user fatigue. Removing any of the key components (fatigue-enhanced fusion, FRU, cross networks, or contrastive learning) resulted in a decrease in performance.
- **User Fatigue Reduction**: Online experiments on Kuaishou showed that FRec can significantly improve key online metrics, including app usage, number of videos played, and diversity of video consumption. Furthermore, FRec reduced the "concentration" of similar videos in consecutive exposures, indicating a decrease in perceived user fatigue.
- **Online EVTR Improvement**: Online experiments showed that FRec improved Effective View-Through Rate (EVTR) compared to the baseline, especially when users have consumed many similar videos, suggesting reduction in fatigue.
- **Adaptability to User Interests**:  A case study presented recommendations by baseline vs FRec, showing the system could recommend better diverse videos compared to the baseline.
- **Proxy Measurement**: A proxy measurement was created to analyze effectiveness when fatigue played a high role in the decision, with results showing FRec performed better.
- **Hyperparameter Sensitivity**: Experiments showed that there was sensitivity to key hyperparameters like Kernel size and Truncated threshold.
