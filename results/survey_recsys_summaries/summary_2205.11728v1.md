# Summary of 2205.11728v1.md

**Token Usage**: Input: 10575, Output: 672, Total: 11247

---

### Main Idea
- The paper introduces ItemSage, a single set of product embeddings developed at Pinterest to provide relevant recommendations across various shopping use cases (user, image, and search-based).
- The motivation behind ItemSage is to enhance the shopping experience on Pinterest by leveraging multi-faceted product information, including both images and text, and optimizing for multiple engagement types like purchases, add-to-cart actions, clicks, and saves.
- The proposed solution is a transformer-based architecture capable of aggregating information from both text and image modalities using multi-task learning to optimize for several engagement types. This leads to a candidate generation system that is efficient for all engagement objectives of the end-to-end recommendation system.

### Technologies
- **Architecture:** A transformer encoder is used as the basic building block for learning product embeddings, which takes a sequence of embeddings representing image and text features as input.
- **Modalities:** Image features are represented by pretrained PinSage embeddings. Text features (title, description, etc.) are embedded using the hash embedding trick to manage the large vocabulary size.
- **Multi-Task Learning:** The model is trained on multiple tasks (clicks, saves, add-to-cart actions, checkouts) using a combined training batch approach to optimize for all engagement types.
- **Loss Function:** A softmax loss with logQ correction and mixed negative sampling (in-batch positives and random negatives) is used to train the model.
- **Evaluation:** Offline benchmarks are used to evaluate the model's performance, using engagement-weighted recall at k as the main metric. A/B experiments on live traffic are conducted to measure the impact on key business metrics.
- **Compatibility:** The embeddings are designed to be compatible with PinSage embeddings for images and SearchSage embeddings for search queries, using cosine similarity as a measure of embedding distance.
- **Deployment:** ItemSage embeddings are deployed to power Pinterest shopping recommendations, using HNSW (Hierarchical Navigable Small Worlds) index for candidate generation and online feature store for ranking applications.
- **Innovation:** The work introduces a transformer architecture to aggregate image and text modalities to learn product representations for production-scale recommendation systems. It also uses multi-task learning to optimize a single embedding for multiple engagement types in a multi-modal vertical recommendation system.

### Results
- The experimental results demonstrate the effectiveness of ItemSage embeddings, with significant improvements over single modality baselines.
- Offline experiments show that the transformer architecture outperforms the MLP-Concat-MLP model baseline in terms of recall, with notable improvements in search tasks for clicks and saves.
- A/B experiments on live traffic show substantial gains in key business metrics, with up to +7% gross merchandise value/user and +11% click volume.
- The ablation studies indicate that using multi-modal features leads to better performance than using features from a single modality. The mixed negative sampling approach also improves the model's performance.
- Multi-task learning improves performance across product verticals and engagement types, with significant gains in add-to-cart actions and checkouts.
- Using ItemSage embeddings to infer whether a product is intended for male or female users yielded a 3.6% improvement in top-1 accuracy over the previous baseline.
