# Summary of 2106.03819v1.md

**Token Usage**: Input: 10027, Output: 640, Total: 10667

---

### Main Idea
- The paper addresses the user cold start problem in music streaming services, where recommending personalized content to new users with limited interaction data is challenging.
- The authors aim to provide relevant music recommendations to new Deezer users as soon as they register, preventing a negative first impression that might lead them to abandon the service.
- They propose a semi-personalized recommendation system that integrates cold users into an existing embedding space of warm users by leveraging heterogeneous demographic and interaction data processed by a deep neural network, combined with a clustering of warm users.

### Technologies
- **Latent Models for Collaborative Filtering:** The system builds upon an existing large-scale latent model for collaborative filtering trained on "warm" users (users with sufficient interaction data). Two types of embeddings are used: UT-ALS (User-Track Alternating Least Squares) and TT-SVD (Track-Track Singular Value Decomposition).
- **Deep Neural Network:** A feedforward neural network with three hidden layers is used to predict user embeddings based on concatenated demographic and interaction features. ReLU activations and batch normalization are applied.
- **User Clustering:** A k-means algorithm is used to segment warm users into 1000 clusters based on their embeddings. Cold users are assigned to the cluster with the closest centroid.
- **Semi-Personalization:** Combines predicted embeddings with warm user segmentation. The system recommends the most popular tracks within the cluster a cold user is assigned to, rather than relying solely on the user's predicted embedding for nearest neighbor searches.
- **Evaluation Metrics:** Precision, recall, and NDCG are used to evaluate the performance of the system in offline experiments. Display-to-stream and display-to-favorites rates are used in online A/B testing.
- **Implementation Details:** The real-time inference service is a Golang web server using the onnxruntime library. Models are trained offline using PyTorch and exported to ONNX format. Data is stored in Hadoop and Cassandra clusters.
- **Baselines:** Popularity-based method, Registration Day Streams (averaging embeddings of streamed tracks), Input Features Clustering (clustering on input features directly), DropoutNet, and MeLU.

### Results
- Offline experiments showed that the proposed semi-personalized system significantly outperformed the popularity baseline and a direct use of sparse usage data (Registration Day Streams).
- The semi-personalized approach generally outperformed fully personalized variants, indicating the benefit of the user segmentation strategy.
- The TT-SVD version of the Deezer semi-personalized system achieved the best results in offline experiments.
- Online A/B testing on the Deezer app demonstrated significant improvements in display-to-stream and display-to-favorite rates compared to a previous production system.
- The system enables more interpretable recommendations by linking cold users to warm user segments with identifiable characteristics (e.g., common country, age, music genres).
- Performance improved for users with more interactions (streams, skips, artist likes) during the registration day.
- The system primarily recommended tracks among the 5,000 most popular, avoiding extreme popularity bias.
