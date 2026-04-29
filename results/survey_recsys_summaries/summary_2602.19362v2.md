# Summary of 2602.19362v2.md

**Token Usage**: Input: 10959, Output: 609, Total: 11568

---

### Main Idea
- The paper addresses the challenge of off-policy data in Reinforcement Learning (RL) post-training of Large Language Models (LLMs). Traditional RL methods assume on-policy data, which is often violated in distributed training architectures where the training and inference policies diverge.
- The authors argue that instead of trying to force off-policy data to appear on-policy (through techniques like importance sampling or modifying the inference engine), it's more effective to embrace off-policy learning directly.
- They propose a novel algorithm, Optimal Advantage-based Policy Optimization with Lagged Inference policy (OAPL), that is specifically designed for off-policy RL with LLMs. OAPL treats the mismatch between training and inference policies as a KL-regularized RL problem, enabling stable and efficient training.

### Technologies
- **Algorithm**: Optimal Advantage-based Policy Optimization with Lagged Inference policy (OAPL). This algorithm leverages the closed-form solution of KL-regularized RL to derive a squared regression objective, allowing training on rollouts from a lagged inference policy without on-policy sampling or importance weighting.
- **Base Models**: Qwen3-4B-Thinking-2507 (for math experiments) and DeepSeek-R1-Distill-Qwen-14B (for code generation experiments)
- **Frameworks**: HuggingFace models and vLLM.
- **Datasets**: Deepscaler (for math) and a custom-generated dataset based on DeepCoder's training data (for code).
- **Evaluation Metrics**: Pass@k (for both math and code), entropy (for math), and sample efficiency.
- **Baselines**: Group Relative Policy Optimization (GRPO) with importance sampling, DeepCoder (a GRPO-trained coding model).
- **Experimental Setup**: Asynchronous training setup with a trainer and an inference engine that can have significant policy lag. Synchronization occurs periodically between the trainer and inference engine with an interval of L iterations.

### Results
- OAPL outperforms GRPO with importance sampling on competition math benchmarks (AIME 25, HMMT 25 Feb & Nov, BRUMO 25) across various Pass@k metrics, demonstrating improved accuracy and training stability.
- On LiveCodeBench v5, OAPL matches or outperforms DeepCoder, while using approximately 3x fewer generations during training.
- OAPL exhibits improved test-time scaling under the Pass@k metric (for k ranging from 1 to 256), suggesting that it doesn't just sharpen the base model distribution.
- The method demonstrates robustness to significant policy lag (up to 400 gradient steps between the training and inference policies), enabling efficient, effective post-training.
- Entropy analysis shows that OAPL's entropy does not collapse during training, unlike GRPO, contributing to the improved performance on Pass@k metrics.
