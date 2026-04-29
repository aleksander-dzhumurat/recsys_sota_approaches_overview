### Main Idea

- **Research Objective:** The paper investigates the quality and potential biases of automatically generated natural language (NL) user taste profiles derived from music streaming data using Large Language Models (LLMs). The goal is to understand if these profiles accurately represent user preferences and whether their quality varies based on user and item characteristics.
- **Motivation and Significance:** LLM-generated profiles offer a scrutable alternative to opaque collaborative filtering representations, enhancing transparency and user control in recommendation systems. However, LLMs can inherit and amplify biases, potentially leading to unfair representations of different user groups. Assessing the alignment between user perception and the utility of these profiles is crucial for ensuring trust and fairness.
- **Proposed Approach:** The study evaluates profile quality along two dimensions: user-self identification (via a user study) and recommendation relevance (assessed in a downstream task). It analyzes the relationship between these dimensions and user attributes (e.g., mainstreamness, taste diversity) and item features (e.g., genre, country of origin).

### Technologies

- **LLMs:** Llama 3.2, DeepSeek-R1, and Gemini 2.0 Flash are used to generate NL profiles from user listening histories.
- **Two-Step Sampling Strategy:** A novel approach to sample user listening data, first identifying top-n most played artists within a given time window, then selecting most played tracks per artist to mitigate artist-level redundancy and balance short- and long-term preference signals.
- **User Study:** An online study with 64 participants to evaluate the generated profiles on a 7-point Likert scale, measuring how well each profile matches their music taste.
- **User Characteristics:** High-level metrics collected, including Generalist-Specialist Score (GS-Score), median rank of listened tracks (mainstreamness), and mean age of songs.
- **Item Metadata:** Track title, play count, artist name, album name, release year, artist main and secondary genres, and country of origin.
- **Evaluation Metrics:** User ratings from the Likert scale, recall@10, and ndcg@10.
- **Statistical Analysis:** ANOVA, Cohen's d, linear regression models with bootstrapping, and Doubly Robust (DR) estimation of the Average Treatment Effect (ATE) to analyze biases.
- **Recommendation Approach:** Embedding NL profiles and item metadata into a shared latent space, fine-tuning a bi-encoder on a music-specific ranker.

### Results

- **User Ratings:** Users generally rated profiles based on their own consumption data higher than random profiles. Llama-based profiles consistently received higher scores, suggesting that the LLM's specific writing style plays a role in self-recognition.
- **User Characteristics and Profile Quality:** Specialist users (high GS-scores) tend to rate profiles more positively. Older users and those who listen to older songs also rated profiles more favorably.
- **Item Characteristics and Profile Quality:** Profiles with a higher proportion of rap tracks were negatively associated with ratings, while profiles with a greater share of U.S.-origin tracks correlated positively. DR estimation confirmed that certain content types significantly influence user ratings, even after controlling for confounders.
- **Correlation Between User Ratings and Recommendation Performance:** A weak positive linear relationship was observed between user ratings and recommendation performance (recall@10 and ndcg@10), indicating a misalignment between perceived representativeness and algorithmic utility.
- **Limitations:** The study used a limited number of LLMs and a relatively small user sample.
- **Future Work:** Explore targeted fine-tuning or debiasing strategies to reduce representation gaps and decouple profile generation for user-facing experiences from those optimized solely for recommendation.
