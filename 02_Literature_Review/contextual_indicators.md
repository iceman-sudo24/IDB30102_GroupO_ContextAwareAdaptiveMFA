# Contextual Indicators for the Proposed Prototype

The literature uses many contextual signals. For the controlled proof of concept, three indicators are selected because they are common in adaptive-authentication research and can be represented without collecting real personal data.

| Proposed indicator | Proposal-stage normal condition | Proposal-stage abnormal condition | Literature rationale |
|---|---|---|---|
| Device familiarity | Recognised test device | Unrecognised test device | Device characteristics/fingerprinting recur in adaptive MFA and RBA studies such as Kandula et al. (2024), Rotter et al. (2025) and Sharp et al. (2026). |
| Network/location consistency | Expected configured context | Unexpected configured context | Location/network context is used or discussed by Kandula et al. (2024), Mostafa et al. (2023) and broader adaptive-authentication literature. |
| Access-time consistency | Expected test access period | Unusual test access period | Time is a common contextual dimension identified in adaptive-authentication context modelling and RBA research. |

## Proposal-stage scoring rule

Each abnormal condition contributes **1 point**.

- Score **0–1** → Low risk → no step-up MFA
- Score **2–3** → Elevated risk → step-up MFA

This equal weighting is intentionally transparent and reproducible. It is a **researcher-defined proof-of-concept rule**, not a claim that each factor carries equal real-world risk.
