# Summary of 2504.01489v1.md

**Token Usage**: Input: 14281, Output: 511, Total: 14792

---

### Main Idea
- The paper addresses the problem of user interest shifts in sequential recommendation systems. Existing models trained on static historical data struggle to adapt to these shifts, leading to performance degradation during testing.
- The motivation is that real-world user behavior is dynamic, influenced by factors like time and context, which current models fail to capture effectively.
- The proposed solution, T 2 ARec, is a novel test-time training (TTT) based sequential recommendation model that uses a state space model (SSM) and two novel alignment modules to capture temporal dynamics and user interest shifts.

### Technologies
- **State Space Model (SSM)**: Used as the backbone to model user interest state transitions. Specifically Mamba-2 architecture.
- **Test-Time Training (TTT)**: The model adapts to new data during the testing phase by updating its parameters through self-supervised learning.
- **Time Interval Alignment Loss**: Aligns absolute time intervals with model-adaptive learning intervals to capture temporal dynamics. This loss incorporates both relative and absolute timestamps.  A pairwise loss is used, computed within smaller blocks to reduce computational complexity.
- **Interest State Alignment Loss**: Models the dynamic evolution of user interest patterns by transforming the input sequence into a final state, applying forward and backward state updates to generate a reconstructed state, and aligning it with the original state.
- **Datasets**: ML-1M, Amazon Prime Pantry, and Zhihu-1M are used for evaluation.
- **Evaluation Metrics**: Recall@10, MRR@10, and NDCG@10.

### Results
- T 2 ARec outperforms several baseline models (Caser, GRU4Rec, BERT4Rec, SASRec, Mamba4Rec, TiM4Rec, TTT4Rec) on all three datasets.
- Ablation studies demonstrate the effectiveness of both the time interval alignment loss and the interest state alignment loss. Removing either loss significantly degrades performance.
- Analysis of test-time throughput shows that T 2 ARec has a slightly lower throughput than models that don't use test-time training, but the performance gains outweigh this drawback.
- Experiments validate that T 2 ARec is more effective at mitigating user interest shifts compared to existing methods, especially when the shifts are more pronounced.
- Sensitivity analysis of the self-supervised loss weights shows that both losses significantly impact performance, with the interest state alignment loss having a slightly greater effect.
