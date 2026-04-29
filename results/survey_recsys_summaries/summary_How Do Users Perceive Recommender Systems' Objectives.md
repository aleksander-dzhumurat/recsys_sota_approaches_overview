# Summary of How Do Users Perceive Recommender Systems' Objectives.md

**Token Usage**: Input: 27927, Output: 778, Total: 28705

---

### Main Idea

- The paper addresses the need for more transparent and accountable recommender systems by proposing a novel approach to justify recommendations based on service models.
- Current recommender systems often lack explicit representation of the services and actors involved in a user's interaction with an item, from selection to usage, limiting their ability to assess the impact on the user's overall experience.
- The proposed solution uses service blueprints to extract experience data from user reviews, organizing the justification of recommendations around different stages of interaction with the item, providing users with a holistic view.

### Technologies

- **Service Blueprints**: A visual modeling technique used to map customer experience during different stages of interaction with a service.  The authors extend a pre-existing blueprint for hotel bookings to model the Airbnb home-renting process, focusing on "Customer Actions" and "Physical Evidence" layers.
- **Coarse-grained and Fine-grained Evaluation Dimensions**:  The service blueprint is used to define two levels of evaluation dimensions. Fine-grained dimensions relate to specific customer actions and tangibles (e.g., "Ambiance," "Kitchen"), while coarse-grained dimensions summarize the overall experience (e.g., "In apartment experience").
- **Sentiment Analysis**: TextBlob and Vader libraries are used to compute the polarity (positive or negative) of aspect-adjective pairs extracted from user reviews.
- **Aspect Extraction**: NLP techniques including lemmatization, dependency parsing, and the Double Propagation algorithm are used to extract aspects of items from user reviews.
- **User Interface (UI) Design**:  Five different UI models are implemented: two service-based justification models (m-thumbs, m-aspects), and three baseline models (m-summary, m-opinions, m-reviews). The UIs feature visualizations of coarse-grained evaluation dimensions and allow users to explore fine-grained details.
- **Statistical Analysis**: Kruskal-Wallis tests, Mann-Whitney tests, and Structural Equation Modeling (SEM) are used to analyze data from a user study and determine the statistical significance of the findings.  The CEI-II (Curiosity and Exploration Inventory-II) and Need for Cognition (NfC) questionnaires are used to categorize participants by personality traits and cognitive styles.

### Results

- **User Study**: A user study involving 59 participants compared the proposed service-based justification models (m-thumbs, m-aspects) with three baselines (m-summary, m-opinions, m-reviews).
- **Perceived User Awareness Support**: The service-based justification models (m-thumbs) were rated higher in "Perceived User Awareness Support" compared to the baselines, indicating that users found the service-based information more helpful in understanding items.
- **Interface Adequacy and Satisfaction**: Users with different levels of "Curiosity" or low "Need for Cognition" (NfC) rated the "Interface Adequacy" and "Satisfaction" of the service-based models higher than the baselines. High NfC participants preferred direct inspection of item reviews.
- **Structural Equation Modeling (SEM)**: The SEM analysis confirmed a positive correlation between the proposed service-based model and the "Perceived User Awareness Support".  It also revealed a positive correlation between the "Curiosity and Exploration Inventory" and "Interface Adequacy"
- **Limitations and Future Work**: The study highlights the need for personalization to cater to diverse interaction styles and cognitive needs. Future work includes personalizing the UI, integrating functions from different models, tailoring aspect presentation based on user preferences, and extending the service blueprint to model more complex scenarios.  The authors also plan to test the approach in other domains and improve the models by incorporating more information exploration functions.
