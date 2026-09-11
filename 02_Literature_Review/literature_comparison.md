# Literature Comparison — Context-Aware Adaptive MFA

This comparison narrows the broader Assignment 1 SLR to studies that directly support the approved proposal direction.

| Study | Main approach | Context / data | Evaluation emphasis | Key limitation / implication |
|---|---|---|---|---|
| Kandula et al. (2024) | Context-aware MFA in Zero Trust | Device, behaviour, location, network/access context | Conceptual risk/adaptation discussion | Strong problem relevance but no empirical prototype |
| Carjuman et al. (2026) | Dynamic adaptive-MFA risk engine | Auth details, biometric, device and contextual inputs | Attack detection, false positives and latency proposed | No physical model/test data |
| Picard & Pierre (2023) | Reinforcement-learning RBA | Mobile Phone Use contextual data | G-Mean | Quantitative but dataset/task specific |
| Mostafa et al. (2023) | Adaptive multi-layer cloud authentication | Identity, location, browser; 50–1000 users | FP/FN, latency, scalability | Cloud-specific multi-factor architecture |
| Syed (2025) | Federated-learning dynamic RBA | 32,000 healthcare logins | FP rate, latency, uptime | Domain specific and more complex than needed here |
| Wazzeh et al. (2022) | Federated continuous authentication | Behavioural/continuous-auth datasets | Learning-based continuous authentication | Extends beyond login-stage step-up |
| Saleem et al. (2025) | ML-enhanced attribute authentication | IoT access requests | Accuracy/recall | Different IoT classification task |
| Bumiller et al. (2023) | Context-modelling review | Adaptive-authentication context literature | Context categories/modelling practices | No single step-up implementation; shows model heterogeneity |
| Han & Lee (2023) | OIDC-timing RBA feature | Token-exchange timing | Risky/tunneled connection detection | Different threat and decision target |
| Rotter et al. (2025) | FNN-based RBA | Public login data, mainly IP/user agent | Login classification and re-authentication burden | Learning-based and dataset dependent |
| Sharp et al. (2026) | Context-aware adaptive MFA | Risk reasoning + factor trust | F1 score and adaptive factor selection | Broader model than this study's controlled step-up outcome |
| Baumer et al. (2026) | IAM metrics systematic review | IAM measurement literature | 43 metrics across seven perspectives | Shows why evaluation must match the exact research question |
| Syahreen et al. (2024) | MFA-framework systematic review | 23 selected studies | Framework comparison | Supports concern about proof-of-concept evaluation maturity |

## Comparative conclusion

The literature already establishes that context can influence authentication requirements. The main unresolved issue for this proposal is not whether adaptive MFA can exist, but whether a controlled web-based prototype can **measureably reduce step-up authentication for predefined low-risk attempts under the same scenario set used for a static-MFA baseline**, while elevated-risk attempts continue to receive step-up authentication and the latency cost is recorded.
