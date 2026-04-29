### Main Idea
- The paper addresses the emerging research area of personalized preference alignment for Large Language Models (LLMs).
- It recognizes that a one-size-fits-all approach is insufficient for aligning LLMs to users because individual preferences vary across users and contexts.
- The paper focuses on adapting LLM behavior to dynamic user preferences across individuals, groups, and contexts to enhance user satisfaction. It presents a taxonomy of techniques, including training-time, inference-time, and user-modeling-based methods.

### Technologies
- **Technique Taxonomy**: Divides personalized preference alignment methods into training-time and inference-time approaches, as well as user-modeling techniques.
- **Training-time Methods**:
    - Building models with user-specific parameters (e.g., per-user PEFT modules, soft prompts, user-specific heads).
    - Training models sensitive to input user preferences (e.g., instruction-following LLMs that adapt to user-written values, context-conditioned reward models).
- **Inference-time Methods**:
    - Prompting-based methods: Modify input context via in-context examples, retrieval, or prompt rewriting.
    - Reward- and value-guided decoding: Integrate personalized alignment objectives directly into the LLM decoding by adjusting token probabilities based on reward signals or value functions.
    - Logit rectification: Modify the internal decision process of LLMs by integrating corrective signals directly into the decoding stage.
- **User Modeling**: User modeling is used to enable personalized preference alignment even in the absence of user preferences.
- **Datasets and Benchmarks**: Surveys existing datasets (e.g., DSP, P-SOUP, MULTIFACETED, PRISM, PersonalLLM) and benchmarks for personalized alignment, including real-world and simulated datasets.
- **Evaluation Metrics**: LLM-as-a-judge, pairwise comparisons, multi-dimensional scoring.

### Results
- The paper categorizes and analyzes various techniques for personalized preference alignment, highlighting their strengths and limitations.
- Training-time methods can achieve personalized adaptation, but may struggle to ensure global model performance and scalability.
- Inference-time methods allow for on-the-fly adaptation, but may be limited by context length, computational overhead, and reliance on static representations of user preferences.
- User modeling approaches can improve user satisfaction even without explicit preference modeling.
- The paper identifies the lack of universally acknowledged evaluation and benchmarks as a key challenge.
- The survey serves as an up-to-date resource for practitioners and researchers working on personalized and pluralistic alignment and, more broadly, LLM personalization and alignment. It identifies future directions such as online and continuous personalized alignment and addressing long and complex user-generated value statements.
