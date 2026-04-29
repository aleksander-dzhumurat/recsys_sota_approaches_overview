# Summary of 2307.14906v2.md

**Token Usage**: Input: 4732, Output: 487, Total: 5219

---

### Main Idea
- The paper addresses the limitations of existing session-based recommendation systems like GRU4Rec+ and SASRec when dealing with large item sets in e-commerce platforms such as OTTO.
- These existing systems struggle to maintain both accuracy and scalability, especially concerning training time, when item sets are large.
- The paper introduces TRON (Transformer Recommender using Optimized Negative-sampling), a session-based transformer recommendation system that builds upon SASRec and improves upon it with enhancements related to negative sampling and loss functions, to achieve better accuracy and training time.

### Technologies
- **Architecture:** Transformer-based architecture, specifically building upon SASRec.
- **Negative Sampling:**
    - Top-k negative sampling: Updating only the top-k negatives during training to reduce the computational load.
    - Combination of uniform batchwise sampling and in-batch sessionwise negative sampling.
- **Loss Function:** Sampled Softmax (SSM), a listwise loss function, to alleviate popularity bias and maximize ranking metrics.
- **Datasets:** Diginetica, Yoochoose, and a private OTTO dataset, each representing increasing complexity in terms of events and item sets.
- **Evaluation Metrics:** Recall@20 and MRR@20.
- **Baselines:** GRU4Rec+ and SASRec.
- **Hardware:** NVIDIA Tesla V100 GPU.

### Results
- TRON demonstrates superior accuracy compared to GRU4Rec+ and SASRec across the tested datasets, with the exception of MRR@20 on the Yoochoose dataset.
- TRON maintains training speeds comparable to SASRec, despite handling a larger number of negative samples.
- On the OTTO dataset, TRON showed an accuracy increase of more than 6.5% in both Recall@20 and MRR@20 and a training speedup of 1090% compared to GRU4Rec+.
- A live A/B test on the OTTO platform showed an 18.14% increase in click-through rate, a 23.85% increase in add-to-carts, and a 23.67% uplift in units compared to SASRec.
- The results validate the effectiveness of TRON in a real-world e-commerce setting.
