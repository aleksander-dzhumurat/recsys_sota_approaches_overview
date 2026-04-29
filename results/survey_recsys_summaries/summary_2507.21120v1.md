# Summary of 2507.21120v1.md

**Token Usage**: Input: 9787, Output: 925, Total: 10712

---

### Main Idea
- **Core Concept:** The research addresses the limitation of current Visual Art Recommender Systems (VA RecSys) in Art Therapy (AT) by introducing Cross-Domain Recommendation (CDR) using music-driven preference elicitation. Current systems rely on visual stimuli, potentially missing affective dimensions.
- **Problem Solved:** The study aims to enhance personalization in AT by leveraging music to elicit emotional responses that inform therapeutic art recommendations. Existing methods lack affective knowledge transfer between music and visual art.
- **Proposed Approach:** The authors propose and evaluate a family of affect-aware CDR algorithms that use music preferences to recommend therapeutic paintings. The hypothesis is that integrating affective cues from music and visual art can improve the quality and therapeutic impact of art recommendations.

### Technologies
- **Algorithms/Models:**
  - **Mozart:** Affect-aware contrastive alignment using MERT (for music) and ResNet50 (for paintings) feature extraction, modality-specific autoencoders, and a contrastive learning objective based on continuous valence-arousal (V-A) values.
  - **Haydn:** Affective Space Search using a k-nearest neighbors (kNN) approach to retrieve paintings based on the affective alignment of music and painting V-A vectors.
  - **Salieri:** Multimodal alignment with Large Language Models (LLMs) and Vision-Language Models (VLMs). It uses GPT-4o for semantic descriptions and BERT for embedding generation, combined with MERT and ResNet50.
- **Frameworks/Libraries:**
  - ResNet50 for image feature extraction
  - MERT for music feature extraction
  - BERT for textual embedding
  - GPT-4o for LLM/VLM
- **Datasets:**
  - DEAM (Database for Emotional Analysis of Music): Contains 1,802 instrumental music excerpts annotated with valence and arousal values.
  - WikiArt Emotions Dataset: Contains 4,105 paintings annotated with multiple emotions and their intensities.
- **Evaluation Metrics:**
  - User-centric metrics: Accuracy, Diversity, Novelty, Serendipity, Immersion, Engagement.
  - Affective state assessment: Pick-A-Mood tool and the short version of the Positive and Negative Affect Schedule (PANAS) scale.
- **Experimental Setup:**
  - A large-scale online user study with 200 participants diagnosed with mental health conditions.
  - A web application for preference elicitation, guided AT sessions, and affective state assessment.
- **Novel Contributions:**
  - Introduction of CDR to the field of AT by integrating music and VA domains.
  - Development and evaluation of three novel affect-aware CDR algorithms based on music preferences.

### Results
- **Key Findings:**
  - All three CDR algorithms (Mozart, Haydn, Salieri) performed comparably to a state-of-the-art visual-only baseline in terms of user-centric recommendation quality metrics.
  - Guided art therapy, in general, led to a mood enhancement effect across all recommendation groups, shifting participants from negative to positive moods.
  - Thematic analysis of user reflections revealed that all engines predominantly elicited Hope, with Salieri showing the highest focus.
  - Music-based approaches demonstrate a competitive therapeutic profile, even outperforming SOTA in most user-centric metrics of recommendation quality
- **Quantitative Results:**
  - After guided art therapy, the majority of participants reported being in a positive mood (72.6%), compared to before therapy (46.6%).
  - Salieri elicited the highest number of "Hope" responses (127), followed by Visual (124), Mozart (118), and Haydn (116).
- **Key Insights:**
  - Music-driven preference elicitation is an effective alternative to visual-only elicitation in personalized AT.
  - CDR holds potential for digital AT via multimodal frameworks, such as connecting to music streaming applications.
  - Salieri excels in promoting Hope.
  - Haydn delivers interpretable affective alignment.
- **Limitations/Future Work:**
  - Scarcity of therapeutically curated painting collections with reliable affective labels.
  - Stimulus homogeneity as a result of filtered samples implemented as safety measures.
  - Future work includes crowdsourced studies to curate robust therapeutic datasets and longitudinal studies to validate the therapeutic impacts of these approaches.
