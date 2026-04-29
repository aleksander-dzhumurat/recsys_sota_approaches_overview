# Summary of 2407.19658v1.md

**Token Usage**: Input: 5816, Output: 865, Total: 6681

---

### Main Idea

- **Problem:** The paper addresses the challenge of effectively integrating sequential recommendation pre-trained models into Click-Through Rate (CTR) prediction tasks in industrial recommendation systems. Existing methods either ignore the additional inference costs or fail to transfer effective information from the pre-trained models for specific estimated items.
- **Motivation and Significance:** Understanding user interests via historical behavior sequences is crucial for CTR prediction. Pre-training through self-supervised learning can capture user dynamic preferences. However, naively integrating pre-trained models can lead to high inference costs and inefficient knowledge transfer. The paper aims to create a framework that balances performance gains from pre-training with practical deployment constraints.
- **Proposed Approach:** The authors propose a Sequential Recommendation Pre-training framework for CTR prediction (SRP4CTR). It includes a Fine-Grained BERT (FG-BERT) for encoding item IDs and side information during pre-training, a uni cross-attention mechanism for low-cost knowledge transfer between the pre-trained model and the estimated item during fine-tuning, and a querying transformer technique to facilitate the knowledge transfer from the pre-trained model to industrial CTR models. The entire framework leverages a 'folded inference' strategy to minimize online computation.

### Technologies

- **Fine-Grained BERT (FG-BERT):** A bidirectional transformer model that encodes both item IDs and corresponding side information concurrently during the pre-training phase. It utilizes a multi-attribute masking prediction approach.
- **Uni Cross-Attention:** A unidirectional attention mechanism that establishes a connection between the predicted item and the pre-trained model, allowing for tailored interest capture at a low cost. The parameters are untied, sharing only input's embedding parameters and the projection parameters for Key and Value at each layer.
- **Querying Transformer:** A novel transformer encoder that uses learnable query tokens to aggregate user behavior tokens before passing them to the CTR model, enhancing performance in downstream tasks. User/context features may be used to initialize the queries.
- **Folded Inference:** A deployment strategy where user sequence information is encoded once and tiled across items to reduce inference costs, especially beneficial in industrial settings with high query volume.
- **Datasets:** MovieLens-20M and Taobao datasets were used for offline experiments.
- **Evaluation Metric:** Area Under the Curve (AUC) was used to evaluate the performance of the CTR task. "efficiency-FLOPs" (FLOPs with batch size 1) and "inference-FLOPs" (FLOPs with batch size 100) are introduced to evaluate inference cost.
- **Experimental Setups:** Adam optimizer, polynomial decay learning rate, two-layer transformer (L=200), various batch sizes, parameter freezing/learning based on dataset. Baseline models used for comparison include PNN, BST, DIN, DIEN, and CAN.

### Results

- **Overall Performance:** SRP4CTR demonstrates improvements over traditional CTR-based methods (PNN, BST, DIN, DIEN, CAN) on both MovieLens-20M and Taobao datasets. FG-BERT, the proposed pre-training method, outperformed other pre-training approaches like original BERT, ELECTRA, and S3.
- **Long-Tail Performance:** SRP4CTR significantly narrowed the learning gap between long-tail items and other items compared to traditional CTR prediction methods (DIN and CAN).
- **Ablation Studies:** The ablation studies validate the effectiveness of the uni cross-attention module and querying transformer within SRP4CTR.
- **Inference Cost Analysis:** SRP4CTR delivers a significant increase in efficiency-FLOPs compared to DIN and CAN variants while only slightly increasing inference-FLOPs, showcasing the efficiency of folded inference.
- **Online A/B Testing:** Deployed in the Meituan Takeaway recommender system, SRP4CTR increased Gross Merchandise Volume (GMV) by 1.66% and CTR by 0.70% in main recommendation scenarios. Compared to the baseline (DIN+MMOE), it shows an 182% increase in efficiency-FLOPs with only a 21% increase in inference-FLOPs.
