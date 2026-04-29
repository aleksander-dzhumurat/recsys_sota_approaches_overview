# Summary of 2508.00908v1.md

**Token Usage**: Input: 17233, Output: 725, Total: 17958

---

### Main Idea
- The paper addresses the gap in research on fairness in algorithmic hiring recommender systems by considering the perspectives of multiple stakeholders: job seekers, recruiters, companies, and the recruitment agency itself. It argues that traditional approaches to fairness in algorithmic hiring focus primarily on job seekers, neglecting the fairness concerns of other stakeholders. The paper aims to operationalize fairness in a multi-stakeholder candidate recommendation scenario, emphasizing the importance of understanding and incorporating the lived experiences of all stakeholders.
- The motivation stems from the increasing use of AI in hiring and the potential for biased decisions that can harm various stakeholders. The EU AI Act highlights the need for responsible AI, including fairness considerations. The significance of the work lies in its attempt to reconcile the different and sometimes conflicting perspectives on fairness and to map these perspectives to existing fairness metrics, to improve current practices.
- The proposed approach involves conducting semi-structured interviews with 40 stakeholders to explore their experiences with unfairness in hiring and to co-design definitions of fairness and associated metrics. The study uses these qualitative insights to map stakeholder needs to fairness definitions and metrics from the existing literature, specifically in the context of a Danish recruitment agency.

### Technologies
- The primary method used is qualitative research through semi-structured interviews. 40 interviews were conducted across four stakeholder groups: recruiters, other recruitment agency employees, job seekers, and companies. The interview guide covered topics such as fairness definitions, reflections on hypothetical scenarios, lived experiences with (un)fairness, and evaluation brainstorm.
- Goodtape.io was used for transcribing the recorded interviews, and NVivo was used for performing thematic analysis on the transcribed interviews.
- A content-based recommender system based on a cross-encoder architecture is used by the recruitment agency. This system takes textual input from job postings and CVs to predict a matching score, which is then used to recommend the top N relevant CVs for each job posting. This provides the context for the fairness evaluation in the hiring process.
- The paper maps qualitative findings to categories of fairness metrics from the literature, including individual fairness metrics like coverage and the Gini index, and group fairness metrics like Conditional Demographic (Dis)Parity (CDP), skew, category-based diversity metrics, and deviation from consumer fairness parity (DCF).

### Results
- The study revealed that stakeholders' initial understanding of fairness aligns closely with individual fairness, emphasizing qualifications and trusting the systems without much reflection on biases. However, after reflecting on hypothetical scenarios, their focus shifted more towards group fairness, considering attributes like gender, age, and company size.
- The interviews highlighted several factors that can lead to unfairness, including recruiter experience, tool limitations, time constraints, and biased wording in job ads. Job seekers reported experiencing unfairness due to age, gender identity, ethnicity, and family life stage. Companies expressed concerns about similarity attraction bias.
- The study mapped these qualitative insights to specific fairness metrics, with Conditional Demographic (Dis)Parity (CDP) emerging as a key measure. Other important properties included rank-awareness and diversity. For example, comparing the distribution of shortlisted candidates to the available pool of job seekers, measuring skew in ranked outputs, and considering diversity in terms of sensitive attributes.
- Limitations include a limited sample diversity (especially in terms of job seekers' gender identity and racial/ethnic identity, as well as the limited number of companies interviewed) and a focus on a specific context (Danish recruitment agency). The study also acknowledged that an empirical analysis using these metrics has not yet been conducted.
