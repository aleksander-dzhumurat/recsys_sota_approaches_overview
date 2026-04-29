### Main Idea

-   The paper addresses the challenge of multi-modal recommender systems (MRSs) suffering from performance degradation in real-world scenarios where some modalities (e.g., images, text) are missing for certain items.
-   The authors argue that existing MRSs either ignore missing modalities or use naive imputation methods, failing to capture the unique characteristics of each modality and hindering the development of high-quality item representations.
-   They propose DGMRec (Disentangling and Generating Modality Recommender), a novel framework that disentangles modality features into general and specific components from an information-based perspective. DGMRec generates missing modality features by integrating aligned features from other modalities and leveraging user modality preferences.

### Technologies

-   **Feature Disentanglement:** Employs separate encoders (general and specific) to extract modality features. Information-based loss functions (Contrastive Log-ratio Upper Bound (CLUB) and InfoNCE loss) are used to disentangle the general and specific features within a single modality while simultaneously learning shared traits across different modalities.
-   **Missing Modality Generation:** Uses an autoencoder architecture to reconstruct an item's modality features. A modality feature generator creates missing modality features by leveraging aligned features from other available modalities and interacted users' modality preferences.
-   **Item-Item Graph Enhancement:** Enhances the item-item graph using generated features, achieving more robust and richer semantic relations between items. An adaptive update strategy smoothly integrates new connections using a hyperparameter.
-   **Collaborative Filtering Integration**: Aligns modality features with user-item interaction data. Two alignment methods bridge collaborative filtering with modality features: 1) fusing ID embeddings and modality features and 2) behavior-modality alignment.
-   **Evaluation Metrics:** Recall@K and NDCG@K are used to evaluate the performance of the model.
-   **Datasets:** Experiments conducted on Amazon Baby, Sports, Clothing datasets, and TikTok dataset.

### Results

-   DGMRec consistently outperforms state-of-the-art MRSs in challenging scenarios, including missing modalities and new item settings, as well as diverse missing ratios and varying levels of missing modalities. The performance improvement over existing methods ranges from 4.57% to 14.06% depending on the dataset and evaluation metric.
-   The model performs well even when one or more modalities are missing, showing the effectiveness of generating modality features.
-   DGMRec enables cross-modal retrieval, a task inapplicable for existing MRSs, highlighting its adaptability and potential for real-world applications.
-   Ablation studies demonstrate the contribution of each component in DGMRec, including feature disentanglement, modality generation, and alignment with collaborative filtering knowledge.
-   The disentanglement module effectively separates general and specific modality features, as shown in visualizations and similarity score analysis.
