# Summary of 2309.08787v1.md

**Token Usage**: Input: 4372, Output: 667, Total: 5039

---

### Main Idea
- The paper addresses the challenges of using genre labels in movie recommender systems. The core idea is to introduce "Genre Spectrum," a new way of representing genre information in a continuous latent space, capturing nuanced genre blends that discrete labels fail to convey.
- The motivation stems from the limitations of traditional genre labels, which are noisy, inconsistent, subjective, and fail to capture the intensity or combination of genres within a title.
- The proposed approach involves transforming discrete genre labels into a latent space where each dimension represents an abstract concept, allowing genres to manifest as subspaces defined by a range of combinations of latent dimensions. This "Genre Spectrum" is hypothesized to be more expressive than discrete labels.

### Technologies
- **Textual Metadata**: The paper leverages textual metadata (genre, language, year, plot synopsis, ratings, reviews, etc.) from 1.1M movies from IMDb, Rotten Tomatoes, and Gracenote.
- **Language Modeling**: Language modeling techniques are used to learn textual embeddings of movies.
- **Multi-Layer Feedforward Dense Neural Network**: A neural network ingests textual embeddings and predicts genre probabilities in a multi-label classification setup.
- **Cross-Entropy Loss**: The model is trained using cross-entropy loss, averaged over all genre classes.
- **Genre Spectrum Embedding**: The output from the penultimate layer of the neural net (transformer component) is used as the genre-spectrum embedding.
- **UMAP (Uniform Manifold Approximation and Projection)**: Used for visualizing genre spectrum embeddings in a 2D plot.
- **Data Augmentation**: Data augmentation (random convex combination of training samples) is used to improve the quality of embeddings, especially for less-popular movies.
- **NLP Models**: Doc2Vec (96 dimensions), pretrained BERT (768 dimensions), and OpenAI GPT-4 (1536 dimensions) are used to generate textual embeddings for comparison.
- **Evaluation Metric**: Genre similarity in the top-k neighborhood, calculated as the fraction of nearest neighbors sharing a primary genre, is used for evaluation.
- **A/B Testing**: Genre spectrum embeddings were evaluated in an online A/B test within Tubi's recommender system.

### Results
- Genre Spectrum embeddings consistently outperform corresponding textual embeddings (Doc2Vec, BERT, GPT-4) in genre similarity across different popularity buckets.
- The improvement in genre similarity is more significant for less-popular movies, suggesting that Genre Spectrum embeddings are more robust to noisy metadata.
- Data augmentation further improves genre similarity scores.
- Qualitative evaluation (UMAP visualization) shows that genres form cohesive clusters in the latent space.
- Online A/B testing in Tubi's recommender system resulted in a statistically significant 0.6% improvement in 'tvt-capped' (total view time capped at 4 hours per day), demonstrating the effectiveness of Genre Spectrum embeddings in enhancing personalization and user engagement.
- The paper also hints at future work involving the use of Large Language Models (LLMs) for generating more specific annotations in the form of "micro-genres" and their potential applications in optimizing the organization of movie recommendations on user's home screen by enriching the pool of carousel themes.
