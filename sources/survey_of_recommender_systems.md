# A Survey of Real-World Recommender Systems: Challenges, Constraints, and Industrial Perspectives

**Kuan Zou and Aixin Sun**, Nanyang Technological University, Singapore

> *ACM Reference Format:* Kuan Zou and Aixin Sun. 2025. A Survey of Real-World Recommender Systems: Challenges, Constraints, and Industrial Perspectives. 1, 1 (September 2025), 32 pages. https://doi.org/XXXXXXX.XXXXXXX

---

## Abstract

Recommender systems have generated tremendous value for both users and businesses, drawing significant attention from academia and industry alike. However, due to practical constraints, academic research remains largely confined to offline dataset optimizations, lacking access to real user data and large-scale recommendation platforms. This limitation reduces practical relevance, slows technological progress, and hampers a full understanding of the key challenges in recommender systems.

In this survey, we provide a systematic review of industrial recommender systems and contrast them with their academic counterparts. We highlight key differences in data scale, real-time requirements, and evaluation methodologies, and we summarize major real-world recommendation scenarios along with their associated challenges. We then examine how industry practitioners address these challenges in **Transaction-Oriented Recommender Systems** and **Content-Oriented Recommender Systems**, a new classification grounded in item characteristics and recommendation objectives.

Finally, we outline promising research directions, including the often-overlooked role of user decision-making, the integration of economic and psychological theories, and concrete suggestions for advancing academic research. Our goal is to enhance academia's understanding of practical recommender systems, bridge the growing development gap, and foster stronger collaboration between industry and academia.

**CCS Concepts:** Information systems → Recommender systems

**Additional Key Words and Phrases:** Industrial Recommender Systems, Practical Challenges, Academic–Industry Gap

---

## 1. Introduction

In recent years, the widespread adoption of mobile App/Internet has brought about a surge in fragmented user sessions and more frequent interactions with online services. The explosion of content has made it increasingly important for information to proactively find its target audience. As a result, recommendation technologies have emerged as a crucial solution.

We have witnessed this trend across various domains. E-commerce platforms such as Amazon and Alibaba, content platforms like YouTube, HBO Max and Netflix, and music services such as Spotify have all experienced significant growth driven by various recommendation strategies. More notably, short video platforms such as Douyin and TikTok, Kuaishou, and Instagram Reels have reshaped mobile Internet consumption habits, with recommender systems at their core. Furthermore, performance-driven online advertising, one of the most important revenue streams in the Internet economy, is fundamentally built upon recommendation technologies.

Recommender systems (RecSys) have been studied for decades. However, whether methods from academic research can be directly applied in real-world industrial settings remains a contentious issue. More fundamentally, the objectives pursued by academia and industry often differ in nature:

- **Academia** typically emphasizes methodological innovation — a model demonstrating superior algorithmic performance on public datasets (precision, recall, NDCG) is deemed a valuable contribution.
- **Industry** is driven by business-oriented metrics: whether a method leads to tangible gains in revenue, user engagement, or system efficiency, requiring careful consideration of engineering constraints, system cost, and performance trade-offs, as well as rigorous A/B testing.

This survey conducts a comprehensive review of industrial recommendation papers published over the past five years (2020–2024), summarizing common challenges including large-scale data processing, real-time constraints, response latency, and the cost of training and inference.

### 1.1 Differences from Previous Surveys

We observe a clear absence of systematic reviews focused specifically on real-world recommender systems. The practical challenges, application scenarios, methodological considerations, and evaluation criteria in industry differ markedly from their academic counterparts, yet these industrial aspects and associated constraints have not been systematically analyzed in existing literature.

### 1.2 Methods of Collecting Papers

Papers were collected from major conferences (SIGIR, RecSys, WWW, WSDM, KDD, CIKM) published between 2020–2024. Authorship was used as a key filter to identify work on industrial recommender systems (requiring at least one industry author). Papers were further filtered for methods validated through online A/B testing, ultimately narrowing to 272 papers. Advertising was deliberately excluded, resulting in a final set of **228 papers**.

### 1.3 Significance of this Survey

This survey classifies real-world recommendation systems into two main categories:

> **Definition 1 (Transaction-Oriented Recommender System).** A transaction-oriented recommender system is a system that generates item recommendations with the primary goal of prompting transactional actions from users, optimizing for metrics such as conversion, revenue, or purchase likelihood.

> **Definition 2 (Content-Oriented Recommender System).** A content-oriented recommender system is a system that generates item or content recommendations with the primary goal of facilitating user consumption and engagement, optimizing for metrics such as dwell time, clicks, or user satisfaction rather than transactional outcomes.

---

## 2. Industrial–Academic Differences in Recommender Systems

### 2.1 Differences across Application Scenarios

In the Internet industry, competition fundamentally centers on capturing user attention, attracting new users, increasing engagement time, and fostering loyalty. Key differences across scenarios:

- **Transaction-oriented platforms** (e.g., online retail, e-commerce, travel) aim to maximize Gross Merchandise Volume (GMV).
- **Content platforms** (e.g., news, music) aim to enhance user stickiness and loyalty, motivating users to spend more time on the platform, opening avenues for monetization through memberships or advertisement impressions.

Domain-specific factors differ significantly: e-commerce must consider real-time inventory, delivery speed, fulfillment cycles, and item pricing; music services place higher importance on interest exploration, diversity, user relationships, and group behavior.

### 2.2 Challenges beyond Academic Research

#### 2.2.1 Large Data Scale

Industrial recommender systems are built for user bases in the millions or billions, far exceeding academic dataset sizes. Two major implications:

1. **Balancing effectiveness and latency** — methods requiring minutes to return results are impractical. Industrial systems break the recommendation pipeline into multiple stages (recall, coarse ranking, fine ranking, re-ranking) to ensure both efficiency and quality.
2. **Different evaluation standards** — even a 1% improvement can translate into substantial commercial gains at industrial scale.

#### 2.2.2 Cost as a Critical Consideration

While academia focuses on advancing methodologies, industry must balance overall profitability. Many industrial approaches focus on cost optimization, a reflection of commercial practice. A key advantage of academic research is its ability to propose novel solutions without being constrained by strict cost considerations.

#### 2.2.3 Real-Time Modeling as a Necessity

In e-commerce, user interests are highly dynamic, shifting rapidly over time, across contexts, or in response to external stimuli. Product conditions also fluctuate in real time: delivery speed, fulfillment cycles, prices, and inventory can all update instantly. Even latencies measured in milliseconds can render recommendations obsolete.

#### 2.2.4 Gaps Between Simulation-Based and Online Optimization

Academic studies often remain confined to simulated environments. Key issues include:

- **Cold-start problem**: Newly listed products with little or no historical interaction data can remain underexposed for extended periods.
- **Sparsity**: The user–product interaction matrix is typically large, yet each user interacts with only a small fraction of products.
- **Multi-objective optimization**: Balancing CTR (Click-Through Rate), CVR (Conversion Rate), and GMV involves inherent trade-offs.

#### 2.2.5 Greater Emphasis on Long-Term Gains

Industrial recommender systems aim not only for short-term revenue growth but also for shaping long-term commercial value — user retention, lifetime value, and sustainable platform growth.

---

## 3. Transaction-Oriented Recommender Systems

Transaction-oriented RecSys (T-RecSys) is designed primarily to encourage users to complete specific transactions such as purchases and bookings. Discussion is organized into three stages: new users/items (cold start and sparsity), active interaction (real-time interest capture), and long-term optimization (multi-objective and long-term optimization).

### 3.1 Data Sparsity and Cold Start in T-RecSys

The user-item interaction matrix is highly sparse, and both new users and new products lack sufficient historical interaction data.

**Solution 1: Heterogeneous information networks** fuse diverse knowledge from user behaviors. For example:
- In the insurance domain, Bi et al. address cold-start by transferring knowledge from e-commerce to insurance via a three-level attention mechanism.
- Pan et al. propose a multimodal meta-learning approach using text, images, and IDs through multiple meta-learners, with an embedding generator for new items.

**Solution 2: Exploiting external data sources** to compensate for shortage of interactions:
- Cross-domain data utilization, knowledge transfer, and efficient feature modeling.
- Implicit user feedback (installation data, query keywords from search scenarios).
- Offline-online frameworks: offline generation of cold-start item representations, online lightweight cold-start models.

**LLM-based approaches**: Large language models are increasingly used to address sparsity and cold-start issues, including complementary knowledge-enhanced recommenders and unified foundation models integrating search and recommendation tasks.

### 3.2 Real-time User Preference Modeling in T-RecSys

Key approaches by context:

- **Mobile recommendation**: Estimating probability that each position is actually viewed (addressing position bias and false exposure). Validated on the Taobao platform.
- **Sequential applications**: Semantic fusion at the sequence level integrating text and ID sequences through frequency domain transformations.
- **Trigger-induced recommendation**: Deep interest highlight networks with user intent networks, fusion embedding modules, and hybrid interest extraction to highlight instant interests.
- **Graph structures**: Triangular structures in item co-occurrence graphs, explicit neighbor interaction modeling, knowledge graph-based relational graphs.
- **Platform-specific approaches**: Ride-hailing driver repositioning, food delivery dual-periodic preference modeling, spatiotemporal features for food recommendation, e-commerce intelligent request strategies, online travel stage-aware sequential matching.

### 3.3 Multi-objective and Long-term Optimization in T-RecSys

Recommendation systems must balance multiple business objectives that often conflict:

- **Multi-task multi-view graph representation learning**: Jointly optimizes intra-view representations and cross-view relationships; trained on 57 billion samples on the Taobao platform.
- **Cross-domain co-training frameworks**: Explicitly leverage popularity bias through feature decoupling and domain adaptation.
- **Reinforcement learning** (mainstream for short-term/long-term balance): Modeling item lifecycles and predicting cumulative returns to give cold-start items more exposure.
- **Engineering efficiency focus**: Automatic vocabulary size and embedding dimension search (Google Play deployment reduced parameters ~30% while increasing app installations by 1.02%).

---

## 4. Content-Oriented Recommender Systems

Content-oriented RecSys generates recommendations for immediate user consumption and engagement. This survey focuses on three types of content: video, news, and audio.

### 4.1 Video Recommender Systems

#### 4.1.1 Challenges for Video Recommendation

1. **Interest diversity vs. recommendation precision**: Users maintain wide-ranging interests; overemphasis on homogeneous content risks fatigue, while excessive diversity dilutes relevance.
2. **Complex and noisy feedback signals**: Clicks, watch time, likes, and comments differ in reliability; negative samples may contain weak positives.
3. **Context-dependency**: User choices vary across scenarios (public vs. private settings, commuting vs. leisure).

#### 4.1.2 Agile Capture of Short-Term Interests

- **Short-sequence modeling**: Integration of multimodal and cross-domain signals.
- **Long-sequence modeling**: TWIN-V2 — a divide-and-conquer approach using offline hierarchical clustering and cluster-aware target attention online.

Key metrics: Click-Through Rate (CTR), completion rate, average viewing duration.

#### 4.1.3 Refined Interest Modeling

- **Multi-task learning**: Separating shared and task-specific knowledge through multi-level experts.
- **Graph learning**: Contrastive learning for multi-region TV recommendation; meta-knowledge-enhanced multi-view graph contrastive learning.
- **Novelty and diversity**: Multi-cluster interest modeling, feature-aware representations, context distillation to uncover latent interests.
- **Shared accounts**: Session-aware co-attention with device-ID weak supervision to distinguish multiple viewers.

#### 4.1.4 Real-time Interest Response

- **On-device re-ranking**: Lightweight models dynamically adjusting sequences using real-time feedback.
- **Real-time bandit systems**: Diag-LinUCB algorithm for million-level queries per second.

Evaluation metrics: response latency, short-term interaction lift (likes, saves), timeliness of adapting to interest shifts.

#### 4.1.5 Debiasing in Video Recommendation

Common biases: exposure, position, popularity, and duration bias.

- **Duration bias**: Causal intervention (backdoor adjustment) to remove confounding effect of video length on exposure.
- **Watch-time debiasing**: Distributional labels (percentile rank, effective/long views) with causal adjustment based on video-duration grouping.

### 4.2 News Recommender Systems

#### 4.2.1 Challenges for News Recommendation

1. **Freshness**: News cycles are fast; article relevance decays quickly; trending stories have short lifecycles.
2. **Diverse user interests**: Spanning multiple categories (politics, sports, entertainment) and geographies.
3. **Credibility and authority**: Source identity is a key factor; users strongly prefer authoritative publishers.
4. **Content repeatability**: News articles lose value quickly once consumed or once popularity declines.
5. **Topic clustering**: Articles frequently develop around the same event; systems must account for topic continuity while avoiding redundancy.

#### 4.2.2 Timeliness and Real-time Performance

- Caching news vectors, removing redundant data, simplifying representations to enable pre-trained language models to train up to **100× faster**.
- Feature embedding importance evaluation and pruning for hourly model refreshes.
- Multi-model and A/B testing frameworks to dynamically prioritize trending news.

#### 4.2.3 Deep Content Understanding

- **LLM-based embeddings**: Generating news embeddings, inferring user interests from article topics, people, and locations (addressing cold-start for non-logged-in users).
- **Mixture-of-experts networks**: Extracting user preferences and factual knowledge from LLMs.
- **Conditional variational autoencoders**: Modeling latent distribution of side information for cold items.

#### 4.2.4 Multi-objective Optimization

- Multi-task learning with contrastive shared networks, jointly optimizing CTR, reading time, and other metrics.
- Constrained optimization and re-ranking to control category distribution and source diversity.
- "Immersion paths" and "novelty paths" to balance deep reading with cross-topic exploration.

### 4.3 Audio Recommender Systems

Audio scenarios include podcasts and music, grouped together due to highly similar user contexts, consumption habits, and item types.

#### 4.3.1 Challenges in Audio Recommendation

1. **Cold start**: Both user cold start (new/minimal-history users) and item cold start (newly released works).
2. **Diversity requirements**: Unlike other platforms, audio users actively seek exploration; repetitive suggestions reduce satisfaction.
3. **Multi-signal complexity**: Subscription signals (long-term goals) vs. play signals (immediate consumption) reflect different user intents.

#### 4.3.2 Cold-start in Audio Recommendation

- **External knowledge injection**: LLMs to infer preference factors (genre, style) and factual knowledge; deployed on a music platform with significant improvements.
- **Semi-personalized models** (Deezer): Combining clustering with deep neural networks.
- **Two-tower architecture**: "Virtual behaviors" via cross-modal dual autoencoder for zero-interaction users.

#### 4.3.3 Diversity Exploration

- **Playlist continuation** (Deezer): Independent vector representations with sequence modeling (convolutional + recurrent), achieving **70% increase** in users adding recommended songs.
- **Multinomial blending** (Amazon Music): Handling multiple content types while preserving personalized rankings and accounting for long-term value.
- **"Interest clock"** (Douyin Music): Adjusting time-based recommendation weights to prevent homogeneous content loops.

#### 4.3.4 Multi-objective Optimization and Multi-signal Selection

- Joint modeling of subscriptions and plays, or calibration techniques.
- **Counterfactual evaluation** to simulate long-term effects offline, reducing large-scale online experiment costs.

---

## 5. Reflections and Future Directions for RecSys Research

### 5.1 Optimization Shifts in Industrial Recommender Systems

As both user scale and data volume grow exponentially, the optimization focus has shifted through distinct stages:

| Stage | Focus |
|---|---|
| Cold-start | Initial retention and conversion; building user trust |
| Data Sparsity | Accurate modeling for personalized results |
| Single-Objective Optimization | Behavior-based evaluation; measuring recommendation quality |
| Multi-Objective Optimization | Balancing technical and business metrics |
| Long-term Business Goals | Sustainable growth; long-term user value |

### 5.2 The Technical Roadmap of Recommender Systems

**Heuristic methods** (early stage): Collaborative filtering, rule-based recommendations — computationally efficient, easy to interpret.

**Discriminative methods**: Supervised learning optimized for goal-oriented metrics (CTR, CVR, GMV, dwell time). Encompass classical ML, deep learning, incremental/continual learning, and reinforcement learning.

**Generative methods**: Graph neural networks, GANs, meta-learning, Transformers, and LLMs. Particularly suited for cold-start, cross-domain recommendation, content discovery, and multimodal contexts.

**Foundation model paradigm shift** (last two years): Recommender systems reframed as generative modeling tasks:
- Scaling to trillion parameters with no observed performance saturation.
- Unifying heterogeneous user behaviors into single long sequences.
- Next-token prediction over user-item sequences for ranking.
- Outcome-conditioned multi-token generation for retrieval.
- End-to-end single-stage generative frameworks eliminating retrieve-rank cascades.

Emerging trends: (1) Unification of retrieval and ranking; (2) Multi-objective alignment with business goals; (3) Validation of scaling laws; (4) User-side generation for cold-start scenarios.

### 5.3 RecSys Research in Academia

Due to practical constraints, academia lacks A/B testing capability; most evaluations rely on offline experiments with small-scale, often outdated datasets. Key research directions:

#### 5.3.1 A Deeper Interpretation of User Behavior

Most systems rely exclusively on observed behaviors (clicks, views, purchases), neglecting pre-action decision-making processes:

- **Hesitation**: Before a click occurs, users frequently experience a state of hesitation; a click does not always signal genuine interest.
- **Tolerance**: Users who consume content they are not truly interested in often develop negative sentiments toward the system.
- **Post-action cognition**: A user who watches a video to completion may do so out of curiosity rather than genuine interest; repeatedly recommending similar content may cause dissatisfaction.

Incorporating concepts from psychology and cognitive science into recommender systems can unlock greater user and commercial value.

#### 5.3.2 Theory-Guided Optimization of Industrial Recommendation

Mainstream practice often relies on empirical weight tuning of metrics (CTR, CVR, GMV, watch time). Academia should provide:

- **Long-term**: Integrating user retention, cross-period utility, and satisfaction beyond short-term conversion.
- **Short-term**: Formulating metrics like CTR, latency, and cost as constraints; applying multi-objective optimization, hierarchical optimization, and causal inference.

#### 5.3.3 Problem Definitions More Aligned with Real-World Practice

- **Computational constraints**: Explicitly integrate latency, computational cost, and energy consumption into optimization problems.
- **Better benchmarks**: Move beyond MovieLens/Amazon (low sparsity, mild cold-start, stationary distributions); work on datasets better capturing realistic user behavior and modeling dataset shift.
- **Multi-party platforms**: Industrial systems balance interests of users, item providers, content creators, and advertisers; incorporate mechanism design and game theory.
- **Offline-online consistency**: Develop theoretical guarantees and universal simulation environments to replace traditional benchmarks.

### 5.4 RecSys Research in Industry

Recommendations for industry:

- Release production-tested, out-of-the-box recommender models with effective tuning methodologies and practical implementation guidelines.
- Create datasets tailored to specific objectives and transform them into user-friendly simulation environments.
- Disseminate research on cost and performance optimization at the system/platform level.

---

## 6. Conclusion

This survey reviews the applications of recommender systems in industry, covering online transaction scenarios and content scenarios including video, news, and audio. We highlight the business characteristics and objectives of these scenarios, and based on their respective technical challenges, categorize and analyze recent papers from major conferences.

Academic research on recommender systems emphasizes algorithms, while industry must additionally balance system performance, cost, and effectiveness within a broader evaluation framework centered on commercial profitability. Looking ahead, we hope to see more practically meaningful research that unites the strengths of academia and industry to jointly advance the field.

---

## References

[1] Agrawal et al. (2023). Beyond labels: Leveraging deep learning and LLMs for content metadata. RecSys.

[2] An et al. (2024). DDCDR: A Disentangle-based Distillation Framework for Cross-Domain Recommendation. KDD.

[3] Badrinath et al. (2025). PinRec: Outcome-Conditioned, Multi-Token Generative Retrieval for Industry-Scale Recommendation Systems. arXiv:2504.10507.

[4] Bai et al. (2022). A contrastive sharing model for multi-task recommendation. WWW.

[5] Bai et al. (2024). GradCraft: Elevating Multi-task Recommendations through Holistic Gradient Crafting. KDD.

[6] Baltescu et al. (2022). Itemsage: Learning product embeddings for shopping recommendations at Pinterest. KDD.

[7] Baran et al. (2023). Accelerating creator audience building through centralized exploration. RecSys.

[8] Bauer et al. (2024). Exploring the Landscape of Recommender Systems Evaluation. ACM Trans. Recomm. Syst.

[9] Bendada et al. (2023). A scalable framework for automatic playlist continuation on music streaming services. SIGIR.

[10] Bi et al. (2020). A heterogeneous information network based cross domain insurance recommendation system for cold start users. SIGIR.

[11] Briand et al. (2021). A semi-personalized system for user cold start recommendation on music streaming apps. KDD.

[12] Cai et al. (2022). Reloop: A self-correction continual learning loop for recommender systems. SIGIR.

[13] Cai et al. (2023). Model-free Reinforcement Learning with Stochastic Reward Stabilization for Recommender Systems. SIGIR.

[14] Celikik et al. (2022). Reusable Self-Attention Recommender Systems in Fashion Industry Applications. RecSys.

[15] Chai et al. (2022). User-aware multi-interest learning for candidate matching in recommenders. SIGIR.

[16] Chen et al. (2024). Missing Interest Modeling with Lifelong User Behavior Data for Retrieval Recommendation. CIKM.

[17] Chen et al. (2024). A Multi-modal Modeling Framework for Cold-start Short-video Recommendation. RecSys.

[18] Chen et al. (2024). Macro graph neural networks for online billion-scale recommender systems. WWW.

[19] Chen et al. (2020). Improving recommendation quality in Google Drive. KDD.

[20] Chen et al. (2024). Feedback Reciprocal Graph Collaborative Filtering. CIKM.

[21] Chen et al. (2024). Shopping trajectory representation learning with pre-training for e-commerce customer understanding and recommendation. KDD.

[22] Chen et al. (2023). Contextual multi-armed bandit for email layout recommendation. RecSys.

[23] Chen et al. (2021). Curriculum meta-learning for next POI recommendation. KDD.

[24] Chen et al. (2022). Co-training disentangled domain adaptation network for leveraging popularity bias in recommenders. SIGIR.

[25] Dai et al. (2023). DPAN: Dynamic Preference-based and Attribute-aware Network for Relevant Recommendations. CIKM.

[26] Deng et al. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. arXiv:2502.18965.

[27] Deng et al. (2024). MMBee: Live Streaming Gift-Sending Recommendations via Multi-Modal Fusion and Behaviour Expansion. KDD.

[28] Edizel et al. (2024). Towards understanding the gaps of offline and online evaluation metrics. RecSys.

[29] Fan et al. (2024). Our Model Achieves Excellent Performance on MovieLens: What Does It Mean? ACM Trans. Inf. Syst.

[30] Fang et al. (2023). Alleviating Matching Bias in Marketing Recommendations. SIGIR.

[31] Farias et al. (2023). Correcting for interference in experiments: A case study at Douyin. RecSys.

[32] Feng et al. (2021). Zero shot on the cold-start problem: Model-agnostic interest learning for recommender systems. CIKM.

[33] Feng et al. (2020). ATBRG: Adaptive target-behavior relational graph network for effective recommendation. SIGIR.

[34] Firooz et al. (2025). 360Brew: A decoder-only foundation model for personalized ranking and recommendation. arXiv:2501.16450.

[35] Gao et al. (2021). Learning an end-to-end structure for retrieval in large-scale recommendations. CIKM.

[36] Gong et al. (2022). Real-time short video recommendation on mobile devices. CIKM.

[37] Gong et al. (2023). A unified search and recommendation foundation model for cold-start scenario. CIKM.

[38] Gou et al. (2024). Controllable multi-behavior recommendation for in-game skins with large sequential model. KDD.

[39] Grün and Neufeld (2023). Transparently serving the public: Enhancing public service media values through exploration. RecSys.

[40] Ha-Thuc et al. (2021). From producer success to retention: A new role of search and recommendation systems on marketplaces. SIGIR.

[41] Han et al. (2024). Enhancing CTR Prediction through Sequential Recommendation Pre-training. CIKM.

[42] Han et al. (2025). MTGR: Industrial-Scale Generative Recommendation Framework in Meituan. arXiv:2505.18654.

[43] He et al. (2020). Contextual user browsing bandits for large-scale online mobile recommendation. RecSys.

[44] Horn et al. (2024). "More to Read" at the Los Angeles Times: Solving a Cold Start Problem with LLMs. RecSys.

[45] Hu et al. (2023). BOSS: A bilateral occupational-suitability-aware recommender system for online recruitment. KDD.

[46] Huai et al. (2023). M2GNN: Metapath and multi-interest aggregated graph neural network for tag-based cross-domain recommendation. SIGIR.

[47] Huan et al. (2022). An industrial framework for cold-start recommendation in zero-shot scenarios. SIGIR.

[48] Huang et al. (2024). EXIT: An EXplicit Interest Transfer Framework for Cross-Domain Recommendation. CIKM.

[49] Huang et al. (2025). Towards Large-scale Generative Ranking. arXiv:2505.04180.

[50] Huang et al. (2021). Sliding spectrum decomposition for diversified recommendation. KDD.

[51] Huangfu et al. (2024). To Explore or Exploit? A Gradient-informed Framework for Graph based Recommendation. CIKM.

[52] Jeunen et al. (2024). Multi-objective recommendation via multivariate policy learning. RecSys.

[53] Ji et al. (2021). Reinforcement Learning to Optimize Lifetime Value in Cold-Start Recommendation. CIKM.

[54] Ji et al. (2023). A Critical Study on Data Leakage in Recommender System Offline Evaluation. ACM Trans. Inf. Syst.

[55] Jian et al. (2023). A Practical Online Allocation Framework at Industry-scale in Constrained Recommendation. SIGIR.

[56] Jiang et al. (2022). Triangle graph interest network for click-through rate prediction. WSDM.

[57] Jiang et al. (2024). Prompt Tuning for Item Cold-start Recommendation. RecSys.

[58] Jiang et al. (2024). MMGCL: Meta Knowledge-Enhanced Multi-view Graph Contrastive Learning for Recommendations. RecSys.

[59] Joglekar et al. (2020). Neural input search for large scale recommendation models. KDD.

[60] Kekuda et al. (2024). Embedding based retrieval for long tail search queries in e-commerce. RecSys.

[61] Khrylchenko et al. (2025). Scaling Recommender Transformers to One Billion Parameters. arXiv:2507.15994.

[62] Klimashevskaia et al. (2023). Evaluating the effects of calibrated popularity bias mitigation: a field study. RecSys.

[63] Koneru et al. (2024). Enhancing Recommendation Quality of the SASRec Model by Mitigating Popularity Bias. RecSys.

[64] Kouki et al. (2020). From the lab to production: A case study of session-based recommendations in the home-improvement domain. RecSys.

[65] Kruse et al. (2023). Creating the next generation of news experience on ekstrabladet.dk with recommender systems. RecSys.

[66] Kung et al. (2024). Improving embedding-based retrieval in friend recommendation with ANN query expansion. SIGIR.

[67] Lan et al. (2025). Next-User Retrieval: Enhancing Cold-Start Recommendations via Generative Next-User Modeling. arXiv:2506.15267.

[68] Lang et al. (2021). Architecture and operation adaptive network for online recommendations. KDD.

[69] Le et al. (2023). CEC: Towards Learning Global Optimized Recommendation through Causality Enhanced Conversion Model. SIGIR.

[70] Lei et al. (2021). SEMI: A sequential multi-modal information transfer network for e-commerce micro-video recommendations. KDD.

[71] Li et al. (2024). Contextual distillation model for diversified recommendation. KDD.

[72] Li et al. (2021). Path-based deep network for candidate item matching in recommenders. SIGIR.

[73] Li et al. (2024). MODEM: Decoupling User Behavior for Shared-Account Video Recommendations on Large Screen Devices. RecSys.

[74] Li et al. (2024). Modeling user fatigue for sequential recommendation. SIGIR.

[75] Li et al. (2020). PURS: Personalized unexpected recommender system for improving user satisfaction. RecSys.

[76] Li et al. (2023). STAN: Stage-adaptive network for multi-task recommendation. RecSys.

[77] Li et al. (2024). Scene-wise Adaptive Network for Dynamic Cold-start Scenes Optimization in CTR Prediction. RecSys.

[78] Li et al. (2024). Recent developments in recommender systems: A survey. IEEE Computational Intelligence Magazine.

[79] Li et al. (2023). AutoOpt: Automatic hyperparameter scheduling and optimization for deep CTR prediction. RecSys.

[80] Li et al. (2024). Explainable and Coherent Complement Recommendation Based on Large Language Models. CIKM.

[81] Lichtenberg et al. (2024). Ranking across different content types: The robust beauty of multinomial blending. RecSys.

[82] Lin et al. (2024). Bootstrapping Conditional Retrieval for User-to-Item Recommendations. RecSys.

[83] Lin et al. (2023). Exploring the spatiotemporal features of online food recommendation service. SIGIR.

[84] Lin et al. (2023). Tree based progressive regression model for watch-time prediction in short-video recommendation. KDD.

[85] Lin et al. (2022). Feature-aware diversified re-ranking with disentangled representations for relevant recommendation. KDD.

[86] Lindstrom et al. (2024). Encouraging Exploration in Spotify Search through Query Recommendations. RecSys.

[87] Liu et al. (2020). AutoGroup: Automatic feature grouping for modelling explicit high-order feature interactions in CTR prediction. SIGIR.

[88] Liu et al. (2024). A Unified Search and Recommendation Framework Based on Multi-Scenario Learning for Ranking in E-commerce. SIGIR.

[89] Liu et al. (2022). Multi-faceted hierarchical multi-task learning for recommender systems. CIKM.

[90] Liu et al. (2023). Multitask Ranking System for Immersive Feed and No More Clicks. CIKM.

[91] Liu et al. (2023). STGIN: Spatial-Temporal Graph Interaction Network for Large-scale POI Recommendation. CIKM.

[92] Liu et al. (2024). A Self-Adaptive Fairness Constraint Framework for Industrial Recommender System. CIKM.

[93] Lu et al. (2022). Deep unified representation for heterogeneous recommendation. WWW.

[94] Lu et al. (2015). Recommender system application developments: a survey. Decision support systems.

[95] Lv et al. (2023). Deep situation-aware interaction network for click-through rate prediction. RecSys.

[96] Ma et al. (2024). Modeling User Intent Beyond Trigger: Incorporating Uncertainty for Trigger-Induced Recommendation. CIKM.

[97] Ma et al. (2022). Two-layer bandit optimization for recommendations. RecSys.

[98] McInerney et al. (2020). Counterfactual evaluation of slate recommendations with sequential reward interactions. KDD.

[99] Mei et al. (2022). A lightweight transformer for next-item product recommendation. RecSys.

[100] Meisburger et al. (2023). BOLT: An Automated Deep Learning Framework for Training and Deploying Large-Scale Search and Recommendation Models. CIKM.

[101] Mondal et al. (2022). Aspire: Air shipping recommendation for e-commerce products via causal inference framework. KDD.

[102] Nazari et al. (2022). Choice of implicit signal matters: Accounting for user aspirations in podcast recommendations. WWW.

[103] Nie et al. (2024). A hybrid multi-agent conversational recommender system with LLM and search engine in e-commerce. RecSys.

[104] Nie et al. (2022). MIC: Model-agnostic integrated cross-channel recommender. CIKM.

[105] Pan et al. (2022). Multimodal Meta-Learning for Cold-Start Sequential Recommendation. CIKM.

[106] Pan et al. (2023). Learning and optimization of implicit negative feedback for industrial short-video recommender system. CIKM.

[107] Pande et al. (2023). Personalized Category Frequency prediction for Buy It Again recommendations. RecSys.

[108] Park et al. (2024). SLH-BIA: Short-Long Hawkes Process for Buy It Again Recommendations at Scale. SIGIR.

[109] Ploshkin et al. (2025). Yambda-5B - A Large-Scale Multi-modal Dataset for Ranking And Retrieval. arXiv:2505.22238.

[110] Qian et al. (2022). Intelligent request strategy design in recommender system. KDD.

[111] Qin et al. (2023). Learning to distinguish multi-user coupling behaviors for TV recommendation. WSDM.

[112] Qin et al. (2021). Bootstrapping recommendations at Chrome Web Store. KDD.

[113] Qu et al. (2022). Single-shot embedding dimension search in recommender system. SIGIR.

[114] Rangadurai et al. (2022). NxtPost: User to post recommendations in Facebook groups. KDD.

[115] Ren et al. (2024). Non-autoregressive generative models for reranking recommendation. KDD.

[116] Ren et al. (2023). GreenSeq: Automatic design of green networks for sequential recommendation systems. SIGIR.

[117] Sagtani et al. (2023). Quantifying and leveraging user fatigue for interventions in recommender systems. SIGIR.

[118] Shao et al. (2024). Optimizing for Participation in Recommender System. RecSys.

[119] Shen et al. (2021). SAR-Net: A Scenario-Aware Ranking Network for Personalized Fair Recommendation in Hundreds of Travel Scenarios. CIKM.

[120] Shen et al. (2022). Deep interest highlight network for click-through rate prediction in trigger-induced recommendation. WWW.

[121] Shi et al. (2023). Embedding based retrieval in friend recommendation. SIGIR.

[122] Shi et al. (2021). WG4Rec: Modeling textual content with word graph for news recommendation. CIKM.

[123] Si et al. (2024). TWIN-V2: Scaling ultra-long user behavior sequence modeling for enhanced CTR prediction at Kuaishou. CIKM.

[124] Sierag and Zielnicki (2022). Client Time Series Model: a Multi-Target Recommender System based on Temporally-Masked Encoders. RecSys.

[125] Song et al. (2022). Friend recommendations with self-rescaling graph neural networks. KDD.

[126] Spišák et al. (2024). On Interpretability of Linear Autoencoders. RecSys.

[127] Su et al. (2024). RPAF: A Reinforcement Prediction-Allocation Framework for Cache Allocation in Large-Scale Recommender Systems. RecSys.

[128] Sun (2023). Take a Fresh Look at Recommender Systems from an Evaluation Standpoint. SIGIR.

[129] Sun et al. (2020). Neighbor interaction aware graph convolution networks for recommendation. SIGIR.

[130] Tang et al. (2020). Progressive Layered Extraction (PLE): A Novel Multi-Task Learning Model for Personalized Recommendations. RecSys.

[131] Tang et al. (2024). Touch the core: Exploring task dependence among hybrid targets for recommendation. RecSys.

[132] Tian et al. (2024). ReLand: Integrating Large Language Models' Insights into Industrial Recommenders. RecSys.

[133] Tong et al. (2023). Navigating the feedback loop in recommender systems. RecSys.

[134] Tu et al. (2023). Disentangled Interest importance aware Knowledge Graph Neural Network for Fund Recommendation. CIKM.

[135] Wan et al. (2024). LARR: Large Language Model Aided Real-time Scene Recommendation. RecSys.

[136] Wang et al. (2021). Fulfillment-Time-Aware Personalized Ranking for On-Demand Food Recommendation. CIKM.

[137] Wang et al. (2020). M2GRL: A multi-task multi-view graph representation learning framework for web-scale recommender systems. KDD.

[138] Wang et al. (2024). Future impact decomposition in request-level recommendations. KDD.

[139] Wang et al. (2024). Do Not Wait: Learning Re-Ranking Model Without User Feedback At Serving Time in E-Commerce. RecSys.

[140] Wang et al. (2022). Recommending for a multi-sided marketplace with heterogeneous contents. RecSys.

[141] Wang et al. (2023). Diversity-aware deep ranking network for recommendation. CIKM.

[142] Wang et al. (2023). An industrial framework for personalized serendipitous recommendation in E-commerce. RecSys.

[143] Wilm et al. (2023). Scaling session-based transformer recommendations using optimized negative sampling and loss functions. RecSys.

[144] Wilm et al. (2024). Pareto Front Approximation for Multi-Objective Session-Based Recommender Systems. RecSys.

[145] Wu et al. (2020). MIND: A Large-scale Dataset for News Recommendation. ACL.

[146] Wu and Grbovic (2020). How Airbnb tells you will enjoy sunset sailing in Barcelona? SIGIR.

[147] Wu et al. (2023). RUEL: Retrieval-augmented user representation with edge browser logs for sequential recommendation. CIKM.

[148] Wu et al. (2024). Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction. RecSys.

[149] Xi et al. (2024). Towards open-world recommendation with knowledge augmentation from large language models. RecSys.

[150] Xian et al. (2021). Ex3: Explainable attribute-aware item-set recommendations. RecSys.

[151] Xiao et al. (2022). Training large-scale news recommenders with pretrained language models in the loop. KDD.

[152] Xiao et al. (2024). Deep evolutional instant interest network for CTR prediction in trigger-induced recommendation. WSDM.

[153] Xie et al. (2021). Real-time relevant recommendation suggestion. WSDM.

[154] Xie et al. (2021). CausCF: Causal collaborative filtering for recommendation effect estimation. CIKM.

[155] Xu et al. (2020). Privileged features distillation at Taobao recommendations. KDD.

[156] Xu et al. (2020). Gemini: A novel and universal heterogeneous graph information fusing framework for online recommendations. KDD.

[157] Xu et al. (2024). Sequence-level Semantic Representation Fusion for Recommender Systems. CIKM.

[158] Xu et al. (2023). Optimizing long-term value for auction-based recommender systems via on-policy reinforcement learning. RecSys.

[159] Xu et al. (2024). Rethinking cross-domain sequential recommendation under open-world assumptions. WWW.

[160] Xu et al. (2020). When recommender systems meet fleet management. WWW.

[161] Yang et al. (2023). Graph exploration matters: improving diversity in WeChat feed recommendation. CIKM.

[162] Yang et al. (2024). Enhancing Playback Performance in Video Recommender Systems with an On-Device Gating and Ranking Framework. CIKM.

[163] Yang et al. (2024). MLoRA: Multi-domain low-rank adaptive network for CTR prediction. RecSys.

[164] Yao et al. (2024). User welfare optimization in recommender systems with competing content creators. KDD.

[165] Ye et al. (2023). A Transformer-Based Substitute Recommendation Model Incorporating Weakly Supervised Customer Behavior Data. SIGIR.

[166] Yi et al. (2023). Online matching: A real-time bandit system for large-scale recommendations. RecSys.

[167] Yin et al. (2023). Heterogeneous knowledge fusion: A novel approach for personalized recommendation via LLM. RecSys.

[168] Yuan et al. (2023). Hydrus: Improving Personalized Quality of Experience in Short-form Video Services. SIGIR.

[169] Zhai et al. (2024). Actions speak louder than words: Trillion-parameter sequential transducers for generative recommendations. arXiv:2402.17152.

[170] Zhan et al. (2022). Deconfounding duration bias in watch-time prediction for video recommendation. KDD.

[171] Zhang et al. (2023). Shark: A lightweight model compression approach for large-scale recommender systems. CIKM.

[172] Zhang et al. (2023). Multi-gate Mixture-of-Contrastive-Experts with Graph-based Gating Mechanism for TV Recommendation. CIKM.

[173] Zhang et al. (2024). Effective Utilization of Large-scale Unobserved Data in Recommendation Systems. CIKM.

[174] Zhang et al. (2022). Multi-task fusion via reinforcement learning for long-term user satisfaction in recommender systems. KDD.

[175] Zhang et al. (2024). An enhanced batch query architecture in real-time recommendation. CIKM.

[176] Zhang et al. (2019). Deep learning based recommender system: A survey and new perspectives. ACM Computing Surveys.

[177] Zhang et al. (2023). A collaborative transfer learning framework for cross-domain recommendation. KDD.

[178] Zhang et al. (2023). Constrained social community recommendation. KDD.

[179] Zhang et al. (2023). Leveraging watch-time feedback for short-video recommendations: A causal labeling framework. CIKM.

[180] Zhang et al. (2024). Self-Auxiliary Distillation for Sample Efficient Learning in Google-Scale Recommenders. RecSys.

[181] Zhang et al. (2022). Scenario-adaptive and self-supervised model for multi-scenario personalized recommendation. CIKM.

[182] Zhang et al. (2024). Unified Dual-Intent Translation for Joint Modeling of Search and Recommendation. KDD.

[183] Zhang et al. (2023). Modeling dual period-varying preferences for takeaway recommendation. KDD.

[184] Zhang et al. (2024). Co-optimize Content Generation and Consumption in a Large Scale Video Recommendation System. RecSys.

[185] Zhao et al. (2023). Uncovering user interest from biased and noised watch time in video recommendation. RecSys.

[186] Zhao et al. (2023). M5: Multi-Modal Multi-Interest Multi-Scenario Matching for Over-the-Top Recommendation. KDD.

[187] Zhao et al. (2024). Breaking the barrier: utilizing large language models for industrial recommendation systems through an inferential knowledge graph. CIKM.

[188] Zhao et al. (2022). Improving item cold-start recommendation via model-agnostic conditional variational autoencoder. SIGIR.

[189] Zheng et al. (2024). Mirror: A multi-view reciprocal recommender system for online recruitment. SIGIR.

[190] Zhu et al. (2022). SASNet: Stage-aware Sequential Matching for Online Travel Recommendation. CIKM.

[191] Zhu et al. (2022). Spherical Graph Embedding for Item Retrieval in Recommendation System. CIKM.

[192] Zhu et al. (2024). Interest clock: Time perception in real-time streaming recommendation system. SIGIR.

[193] Zou et al. (2024). Hesitation and Tolerance in Recommender Systems. arXiv:2412.09950.