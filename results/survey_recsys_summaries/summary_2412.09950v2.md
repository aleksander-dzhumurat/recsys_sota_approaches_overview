# Summary of 2412.09950v2.md

**Token Usage**: Input: 29843, Output: 805, Total: 30648

---

### Main Idea
- **Primary research objective:** The paper investigates the overlooked interaction states of "hesitation" and "tolerance" in recommender systems, which occur between initial interest and eventual disinterest. Hesitation is defined as users deliberating over recommended content, clicking without certainty, while tolerance occurs when hesitation escalates into unwanted engagement, leading to frustration and wasted effort.
- **Motivation and significance:** Current recommender systems often treat clicks as binary positive signals, ignoring the nuances of user intentions and emotions. This can lead to suboptimal recommendations, wasted user time, eroded trust, and decreased retention.
- **Proposed approach:** The study uses a multi-method approach consisting of (1) large-scale surveys, (2) behavioral log analyses from e-commerce and short-video platforms, and (3) an online field deployment (A/B testing) to identify, model, and leverage hesitation and tolerance signals. The goal is to shift recommender system design from maximizing clicks to minimizing wasted effort and improving user retention.

### Technologies
- **Surveys:** Two large-scale online surveys (N=6,644 and N=3,864) were conducted to capture users' experiences with recommender systems, focusing on hesitation and tolerance states. The surveys used scenario-based questions to elicit realistic responses and avoid biases associated with directly asking about abstract states.
- **Behavioral Log Analysis:** Datasets from e-commerce (Taobao) and short-video (Kuaishou) platforms were analyzed to identify tolerance behaviors, such as clicking without purchase or watching below one's typical ratio. User engagement was measured by the number of items clicked (Taobao) and videos watched (Kuaishou). Tolerance was correlated with reduced engagement.
- **A/B Testing:** Large-scale online A/B tests were conducted on a commercial video platform with millions of users. Tolerance signals were incorporated into the ranking model by relabeling tolerance samples as either "weak positive" or "negative" signals.  Two distinct strategies were implemented: treating tolerance samples as negatives, and treating tolerance samples as weak positives with a discounting mechanism.
- **Model:** A refined version of the platform's ranking model (SIM) was used.
- **Evaluation Metrics:** The primary evaluation metric was user stickiness, assessed through the Day-2 retention rate change. Secondary metrics included dwell time.

### Results
- **Survey Findings:** (i) Users frequently experience an ambiguous "hesitation" state. (ii) Hesitation, when coupled with unproductive costs and eventual disinterest, often develops into "tolerance." (iii) Tolerance undermines enthusiasm, reduces activity, and may lead to abandonment. The negative emotions are shown to intensify with repeated experiences. A large percentage of respondents indicated that increased tolerance leads to boredom, reduced interaction, and a likelihood of quitting the recommendation function.
- **Behavioral Log Analysis:** Higher tolerance (clicking without purchase in e-commerce, shallow viewing in short-video) correlates with reduced user activity on both platforms.
- **A/B Testing:** Adjusting the labels for tolerance signals consistently improves the Day-2 retention rate. Treating tolerance samples as negative samples resulted in improvements of average 7-day retention reaching 0.67% and 0.36% increase in two separate online tests. The A/B test results also indicate that these gains point to stronger loyalty, and the observed drop in dwell time (users stayed on the platform) offers that quality of engagement matters more than its duration.
- **Contributions:** (1) The paper conceptualizes and operationalizes hesitation and tolerance as measurable interaction states. (2) It provides evidence that these states depress trust, satisfaction, and engagement. (3) It proposes modeling strategies that incorporate tolerance signals as weak positives/negatives. (4) It demonstrates that relabeling tolerance-related signals improves retention and reduces wasted effort.
