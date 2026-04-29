# Summary of 1907.05171v2.md

**Token Usage**: Input: 11357, Output: 740, Total: 12097

---

### Main Idea
- The paper addresses the problem of inconsistent feature usage between offline training and online serving in e-commerce recommendation systems. It proposes Privileged Features Distillation (PFD) to leverage "privileged features" which are discriminative but only available during training (e.g., post-click features for CVR prediction). The core idea is to train a teacher model with privileged features and a student model without them, then transfer knowledge from the teacher to the student via distillation.
- The motivation stems from the fact that strict feature consistency between training and serving neglects potentially valuable features. PFD aims to bridge this gap and improve prediction accuracy without increasing online serving latency.
- The proposed approach involves training a teacher model that utilizes both regular and privileged features, and a student model that uses only regular features. The knowledge from the teacher model (soft labels) is distilled to the student model. During online serving, only the student model is used, maintaining consistency and efficiency.

### Technologies
- **Privileged Features Distillation (PFD)**: The main technique for transferring knowledge from a teacher model (with privileged features) to a student model (without privileged features).
- **Model Distillation (MD)**: Used in conjunction with PFD (PFD+MD) to further improve performance by having a more complex teacher model.
- **Deep Neural Networks (DNNs)**: Used as the base models for both teacher and student, specifically Multi-Layer Perceptrons (MLPs).  For CTR prediction, an inner product model is used for efficiency, while DNNs are used for the teacher in PFD+MD.
- **Self-Attention Mechanism**: Employed to model user behavior sequences, incorporating both item embeddings and features describing user behavior on particular items. Multi-head self-attention is used.
- **Cascaded Learning Framework**:  The recommendation system uses a cascaded approach with candidate generation, coarse-grained ranking (CTR prediction), and fine-grained ranking (CVR prediction). PFD is applied in the ranking stages.
- **Evaluation Metrics**: Area Under the Curve (AUC) is used to evaluate the performance of CTR and CVR prediction. Online A/B tests are used to evaluate click and conversion metrics.
- **Training Details**: Models are trained in a parameter server system with asynchronous Adagrad optimizer.  A warm-up scheme is used for the distillation loss. Training the teacher and student models synchronously while sharing common input components is a key optimization.
- **Loss Functions**: Log-loss for teacher and student, Cross-entropy for distillation loss.
- **Datasets**: Large-scale traffic logs from Taobao recommendations, including CTR and CVR datasets, are used for experiments.

### Results
- Significant improvements were achieved on both CTR and CVR prediction tasks by using PFD.
- For CTR prediction, PFD improved AUC compared to the baseline and LUPI (Learning Using Privileged Information). PFD+MD further improved AUC.  Online A/B tests showed a +5.0% improvement in the click metric.
- For CVR prediction, PFD improved AUC compared to the baseline, MTL (Multi-Task Learning), and LUPI. Online A/B tests showed a +2.3% improvement in the conversion metric.
- PFD, with or without MD, was shown to be robust to the choice of the hyperparameter λ.
- Training the teacher and student synchronously while sharing common input components was found to be effective, achieving comparable or better performance with minimal increase in training time. Sharing user ID embedding had a positive effect.

