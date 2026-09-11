# Research Paper Index

This file lists the papers used most directly to support the revised proposal direction. It intentionally does not redistribute copyrighted PDFs. Use the DOI/official link to access each source.

## 1. Kandula, S. R.; Kassetty, N.; Alang, K. S.; Pandey, P. (2024)

**Title:** Context-aware multi-factor authentication in zero trust architecture: Enhancing security through adaptive authentication  
**Research problem:** Addresses static MFA limitations such as MFA fatigue and weak recognition of contextual threats.  
**Method/approach:** Conceptual/practical context-aware MFA framework for Zero Trust Architecture.  
**Dataset/tools:** No original dataset; draws on literature, practices and commercial context-aware MFA solutions. Discusses UEBA, device fingerprinting, geolocation/geofencing and risk scoring.  
**Main finding:** Supports adapting MFA requirements using contextual risk instead of applying a fixed requirement to every access attempt.  
**Limitation:** No empirical prototype; privacy, signal accuracy, scalability, integration and standardisation remain challenges.  
**Relevance:** Directly supports the static-MFA problem and the proposal decision to use contextual indicators.  
**DOI/official link:** https://doi.org/10.21428/e90189c8.f525ef41  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 2. Carjuman, N.; Fook, L. C.; Hlaing, Z. C. (2026)

**Title:** Enhanced MFA framework against modern security threats  
**Research problem:** Protects against modern authentication threats such as SIM swapping, phishing and MITM relays.  
**Method/approach:** Adaptive MFA framework using a dynamic risk engine.  
**Dataset/tools:** Theoretical design; combines authentication details, biometric information, device signatures and contextual information. AES-256/TLS 1.3 and OS biometric APIs are discussed.  
**Main finding:** Proposes a risk score that can allow, challenge or deny access and lists attack detection, false positives and latency as evaluation dimensions.  
**Limitation:** No physical model, test data or performance validation.  
**Relevance:** Supports transparent risk-driven step-up decisions and highlights the need for prototype evaluation.  
**DOI/official link:** https://doi.org/10.1145/3785520.3785523  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 3. Picard, C.; Pierre, S. (2023)

**Title:** RLAuth: A risk-based authentication system using reinforcement learning  
**Research problem:** Uses contextual risk to adapt authentication decisions rather than relying on a fixed rule.  
**Method/approach:** Deep reinforcement learning for risk-based authentication.  
**Dataset/tools:** Mobile Phone Use contextual dataset; Assignment 1 records 42 participants and 886,915 contexts.  
**Main finding:** Assignment 1 reports a G-Mean of 92.62% for contextual risk classification.  
**Limitation:** Results are tied to a specific dataset, task and learning-based implementation.  
**Relevance:** Demonstrates quantitative contextual-risk evaluation but also why metrics are not directly transferable across environments.  
**DOI/official link:** https://doi.org/10.1109/ACCESS.2023.3286376  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 4. Mostafa, A. M.; Ezz, M.; Elbashir, M. K.; Alruily, M.; Hamouda, E.; Alsarhani, M.; Said, W. (2023)

**Title:** Strengthening cloud security: An innovative multi-factor multi-layer authentication framework for cloud user authentication  
**Research problem:** Strengthens cloud authentication while reducing false alarms and unauthorised access.  
**Method/approach:** Adaptive multi-factor, multi-layer authentication framework.  
**Dataset/tools:** Experimental scenarios with 50–1000 cloud users; identity, location and browser information; email/SMS OTP and fingerprint options.  
**Main finding:** Assignment 1 reports FP 0–2%, FN 0–1%, and approximately 237–278 ms authentication checks at 1,000 users.  
**Limitation:** Privacy concerns and additional attack surfaces; performance depends on user and factor configuration.  
**Relevance:** Supports controllable contextual inputs and authentication latency as an evaluation dimension.  
**DOI/official link:** https://doi.org/10.3390/app131910871  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 5. Syed, A. (2025)

**Title:** Dynamic risk-based authentication using AI scoring models in healthcare applications  
**Research problem:** Improves healthcare authentication using context-aware risk-based MFA.  
**Method/approach:** Federated-learning-enhanced dynamic risk-based authentication.  
**Dataset/tools:** 45-day pilot; 32,000 logins from more than 2,500 users plus sandbox tests; Oracle APEX, TensorFlow Federated, FingerprintJS and Twilio API.  
**Main finding:** Assignment 1 reports 2.5% false positives, approximately 1.1 s latency, 99.98% uptime and 10 intercepted intrusions.  
**Limitation:** Limited explainability, API dependency and about 10% federated-learning overhead.  
**Relevance:** Strong empirical evidence for adaptive authentication while showing the complexity and domain dependence of learning-based solutions.  
**DOI/official link:** https://doi.org/10.47363/JAICC/2025(4)492  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 6. Wazzeh, M.; Ould-Slimane, H.; Talhi, C.; Mourad, A.; Guizani, M. (2022)

**Title:** Warmup and transfer knowledge-based federated learning approach for IoT continuous authentication  
**Research problem:** Investigates privacy-aware continuous authentication for IoT.  
**Method/approach:** Federated learning for continuous authentication.  
**Dataset/tools:** Assignment 1 records MNIST, FEMNIST, CIFAR-10 and UMDAA-02-FD as evaluation datasets.  
**Main finding:** Shows that adaptive/continuous authentication can use behavioural and contextual information beyond the initial login.  
**Limitation:** Continuous authentication has different scope, datasets and computational/privacy concerns from login-stage step-up MFA.  
**Relevance:** Supports the broader trend toward dynamic authentication while helping define the current study boundary at login-stage step-up.  
**DOI/official link:** https://doi.org/10.48550/arXiv.2211.05662  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 7. Saleem, J.; Raza, U.; Hammoudeh, M.; Holderbaum, W. (2025)

**Title:** Machine learning-enhanced attribute-based authentication for secure IoT access control  
**Research problem:** Improves dynamic access decisions in IoT using learned authentication attributes.  
**Method/approach:** Machine-learning-enhanced attribute-based authentication.  
**Dataset/tools:** IoT access requests; Random Forest/ML evaluation according to Assignment 1 synthesis.  
**Main finding:** Assignment 1 reports 86% accuracy and 96% recall for the IoT access-request classification task.  
**Limitation:** Measures a different IoT classification problem, so results are not directly comparable to low-risk web step-up authentication.  
**Relevance:** Useful comparison showing why the current proposal should use metrics matched to its own access-management outcome.  
**DOI/official link:** https://doi.org/10.3390/s25092779  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 8. Syahreen, M.; Hafizah, N.; Maarop, N.; Maslinan, M. (2024)

**Title:** A systematic review on multi-factor authentication framework  
**Research problem:** Reviews recent MFA frameworks and their implementation/evaluation maturity.  
**Method/approach:** Systematic review of MFA frameworks.  
**Dataset/tools:** 23 selected studies according to the Assignment 1 synthesis.  
**Main finding:** Assignment 1 uses the study to support the observation that many MFA frameworks remain at proof-of-concept stage.  
**Limitation:** Review evidence rather than a controlled implementation of adaptive MFA.  
**Relevance:** Supports the proposal need for an implementable and measurable proof of concept.  
**DOI/official link:** https://doi.org/10.14569/IJACSA.2024.01505105  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 9. Baumer, T.; Kern, S.; Fuchs, L.; Pernul, G. (2026)

**Title:** Identity and access management metrics: A systematic review  
**Research problem:** Examines how IAM is measured and evaluated across the literature.  
**Method/approach:** Systematic review of IAM metrics.  
**Dataset/tools:** IAM measurement literature.  
**Main finding:** Assignment 1 records 43 IAM metrics across seven perspectives, illustrating evaluation heterogeneity.  
**Limitation:** Broad IAM measurement review rather than an adaptive-MFA experiment.  
**Relevance:** Supports the decision to define project-specific metrics (LRSR, ERSC, latency) instead of combining unrelated measures.  
**DOI/official link:** https://doi.org/10.1145/3788858  
**Evidence basis used for this repository:** Assignment 1 Section A/B

## 10. Bumiller, A.; Challita, S.; Combemale, B.; Barais, O.; Aillery, N.; Le Lan, G. (2023)

**Title:** On understanding context modelling for adaptive authentication systems  
**Research problem:** Investigates how contextual information is represented and modelled in adaptive authentication.  
**Method/approach:** Systematic mapping/literature study of context modelling for adaptive authentication.  
**Dataset/tools:** Published context-modelling research across adaptive-authentication domains.  
**Main finding:** Identifies recurring contextual features while showing substantial variation in context modelling approaches.  
**Limitation:** Does not itself evaluate a single step-up MFA prototype.  
**Relevance:** Strengthens the proposal rationale for choosing a small, explicit and controllable set of contextual indicators.  
**DOI/official link:** https://doi.org/10.1145/3582696  
**Evidence basis used for this repository:** New paper verified via DOI/DBLP/Crossref-linked metadata

## 11. Han, A. H.; Lee, D. H. (2023)

**Title:** Detecting risky authentication using the OpenID Connect token exchange time  
**Research problem:** Introduces OIDC token-exchange time as a risk-based authentication feature for detecting tunneled connections.  
**Method/approach:** Risk-based authentication feature analysis in an OIDC/IAM context.  
**Dataset/tools:** OIDC token-exchange timing and tunnel-related authentication conditions.  
**Main finding:** Shows that authentication infrastructure itself can provide contextual risk features without relying only on endpoint data.  
**Limitation:** Targets tunneled-connection detection rather than low-risk step-up reduction.  
**Relevance:** Demonstrates the breadth of possible context signals and keeps the current project focused on simpler reproducible indicators.  
**DOI/official link:** https://doi.org/10.3390/s23198256  
**Evidence basis used for this repository:** New paper verified via publisher/PubMed/Korea University metadata

## 12. Rotter, D.; Schwabe, T.; Dürmuth, M. (2025)

**Title:** That’s not you! Applying neural networks to risk-based authentication to detect suspicious logins  
**Research problem:** Improves suspicious-login classification in risk-based authentication.  
**Method/approach:** Feed-forward neural network for risk-based authentication.  
**Dataset/tools:** Public login data primarily containing IP addresses and user-agent strings.  
**Main finding:** The authors report improved login classification and reduced re-authentication rates for legitimate users.  
**Limitation:** Learning-based classification and dataset characteristics differ from the proposal's deterministic controlled policy evaluation.  
**Relevance:** Directly supports the proposition that contextual risk decisions can reduce re-authentication burden for legitimate users.  
**DOI/official link:** https://doi.org/10.1145/3733799.3762970  
**Evidence basis used for this repository:** New paper verified via Leibniz University Hannover/ACM metadata

## 13. Sharp, J.; Womack, B.; Farkas, C.; Dasgupta, D.; Roy, A. (2026)

**Title:** Context-aware and adaptive multi-factor authentication model  
**Research problem:** Adapts the number and trust level of authentication factors to the risk of the login context.  
**Method/approach:** Formal/extensible context-aware adaptive MFA framework with context reasoning and risk-level assessment.  
**Dataset/tools:** Context reasoning, factor trust scores and empirical evaluation; data available on request according to publisher metadata.  
**Main finding:** Publisher metadata reports an F1-score of 0.985 for the integrated risk-level assessment approach.  
**Limitation:** Broader factor-selection and continuous-assessment architecture than the present project's narrow low-risk step-up comparison.  
**Relevance:** Very close technical precedent that validates the general context-aware adaptive MFA direction while leaving a narrower measurable step-up outcome for this proposal.  
**DOI/official link:** https://doi.org/10.1016/j.jisa.2026.104508  
**Evidence basis used for this repository:** New paper verified via ScienceDirect/DBLP metadata
