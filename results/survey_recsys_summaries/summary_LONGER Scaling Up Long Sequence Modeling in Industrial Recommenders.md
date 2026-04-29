# Summary of LONGER Scaling Up Long Sequence Modeling in Industrial Recommenders.md

**Token Usage**: Input: 10194, Output: 754, Total: 10948

---

### Main Idea

- The paper addresses the challenge of modeling ultra-long user behavior sequences in industrial recommendation systems, which is crucial for capturing both long- and short-term preferences. Existing methods rely on two-stage retrieval or indirect modeling, leading to inconsistency and inefficiency.
- The motivation is that fully modeling long sequences improves recommendation accuracy, diversity, and mitigates the information cocoon effect. Scaling laws from large language models (LLMs) suggest performance improvements with increased model size, data, and computation, guiding innovations in recommendation systems. The paper aims to pioneer an end-to-end ultra-long sequence modeling paradigm.
- The proposed solution is LONGER (Long-sequence Optimized traNsformer for GPU-Efficient Recommenders), a transformer-based framework optimized for GPU efficiency. It incorporates global tokens to stabilize attention, a token merge module with lightweight InnerTransformers and hybrid attention to reduce quadratic complexity, and engineering optimizations for training and serving.

### Technologies

- **Model Architecture**: LONGER incorporates Global Tokens (target item representation, user ID embedding), a Token Merge module with InnerTransformers, and hybrid attention mechanisms (cross-causal and self-causal attention).
- **Algorithms/Models**: The model utilizes a Transformer architecture with modifications.  The attention mechanism is hybrid, combining cross-attention for initial feature extraction and self-attention for deeper relationship learning.
- **Frameworks**: TensorFlow is used, modified with custom gradient implementations for recomputation.
- **Datasets**: The model is trained and evaluated on a billion-scale industrial dataset from Douyin Ads, comprising 5.2 billion samples with user demographics, behavior sequences, and candidate ad items.
- **Evaluation Metrics**: The model is evaluated using AUC (Area Under the ROC Curve) and LogLoss for offline experiments, and ADSS/ADVV for advertising and Order/U and GMV/U for e-commerce in online A/B testing.
- **Experimental Setup**: Experiments are conducted on a 48xA100s GPU cluster.
- **Novel Contributions**:
    - End-to-end ultra-long sequence modeling within computational constraints.
    - Global tokens for stabilizing attention and enhancing feature interactions.
    - Token merge module with InnerTransformers for efficient sequence compression.
    - Hybrid attention mechanism for capturing both local and global dependencies.
    - Training and serving framework optimized for GPU efficiency with mixed-precision training, activation recomputation, and KV cache serving.

### Results

- LONGER consistently outperforms strong baselines in offline experiments, achieving an AUC of 0.85290 and a LogLoss of 0.47103, representing a relative improvement of 1.57% in AUC compared to the base model and a 0.21% improvement compared to the most competitive model.
- Ablation studies demonstrate that the TokenMerge module and InnerTrans contribute to reduced FLOPs and improved performance. The hybrid attention design improves performance while reducing computational cost.
- Online A/B tests on Douyin Ads show improvements in ADSS and ADVV across Live Streaming, Short Video, and Mall formats. On Douyin E-Commerce, improvements are seen in Order/U and GMV/U for both Live Streaming and Short Video content formats.
- Scaling analysis shows that increasing sequence length, model parameters, and FLOPs generally improve performance, following power-law trends.
- The KV caching mechanism improves inference efficiency, reducing throughput degradation from -40% to -6.8% in online serving.
- The paper mentions future work includes investigating more efficient sequence modeling techniques and improving cross-domain behavior modeling.
