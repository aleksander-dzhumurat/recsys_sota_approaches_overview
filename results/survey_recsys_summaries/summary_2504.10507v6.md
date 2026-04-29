# Summary of 2504.10507v6.md

**Token Usage**: Input: 15526, Output: 764, Total: 16290

---

### Main Idea

- **Primary Research Objective**: The paper introduces PinRec, a generative retrieval model for Pinterest, designed to address the limitations of existing generative retrieval methods in terms of scalability, flexibility for multiple metrics, and output diversity.
- **Motivation and Significance**: Current generative retrieval models struggle to meet the demands of large-scale industrial recommender systems like Pinterest. They lack the ability to optimize for diverse engagement outcomes and generate sufficiently diverse item sequences efficiently. PinRec aims to solve these challenges, marking the first rigorous study on implementing generative retrieval at Pinterest's scale.
- **Proposed Approach**: PinRec employs outcome-conditioned generation to balance various outcome metrics (saves, clicks, etc.) to align with business goals and user exploration. It also incorporates multi-token generation to enhance output diversity while optimizing generation efficiency.

### Technologies

- **Key Technical Components**:
    - Transformer decoder architecture for next-token prediction
    - Outcome-conditioned generation using learnable embeddings for each outcome type (engagement actions, surface constraints)
    - Temporal multi-token prediction using learnable embeddings for temporal offsets
    - Dense embedding vectors for item representation
- **Specific Algorithms, Models, or Frameworks**:
    - Transformer
    - OmniSage embeddings for Pins
    - OmniSearchSage query representation for search queries
    - Faiss IVF-HNSW index for approximate nearest neighbor search
    - CUDA Graphs and KV Cache for serving optimization
- **Datasets, Evaluation Metrics, or Experimental Setups**:
    - User interaction history from Pinterest (Homefeed, Search, Related Pins)
    - Offline evaluation using unordered recall@k and proportion of unique items retrieved
    - Online A/B experiments measuring repins, grid clicks, time spent, fulfilled sessions, and unfulfilled sessions
- **Novel Technical Contributions or Innovations**:
    - Outcome-conditioned generative retrieval for optimizing multiple business metrics
    - Multi-token generation for efficient sequence generation and improved item diversity
    - Optimized autoregressive generation and serving infrastructure for industrial-scale deployment

### Results

- **Main Experimental Findings**:
    - PinRec outperforms baseline models (SASRec, PinnerFormer, TIGER, HTSU) in unordered recall@10 across Homefeed, Related Pins, and Search.
    - Outcome-conditioning improves recall for the conditioned action while decreasing recall for others.
    - Multi-token generation significantly reduces latency and improves unordered recall and diversity.
- **Quantitative Results**:
    - Online A/B tests show that PinRec-{MT, OC} significantly increased successful site sessions, time spent on site, and site-wide grid clicks (+2% sitewide clicks and +4% search repins)
    - PinRec-UC improves search metrics with increased session-wide search fulfillment (+2.27% Search Fulfillment Rate) and improved CPA (1.83% reduction) and shopping conversion volume (1.87% increase) for promoted product retrieval.
    - PinRec-OC improves related pins metrics significantly with a +0.26% increase in fulfilled sessions.
- **Key Insights or Discoveries**:
    - Outcome-conditioned generation allows for improved controllability in recommendations, tailoring them to specific business goals.
    - Multi-token generation provides a better trade-off between performance, diversity, and efficiency compared to single-token generation.
    - The intra-feed relaxation technique is more naturally aligned with user interaction patterns on Pinterest compared to strict next-token prediction.
- **Limitations or Future Work**:
    - Applying generative approaches to ranking
    - Optimizing input sequences to the model
    - Developing language model alignment techniques to enhance the use of engagement signals from users.
