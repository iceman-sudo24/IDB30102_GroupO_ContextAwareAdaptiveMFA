# Evaluation Metrics Identified from the Literature

Previous studies evaluate different functions and therefore use different metrics.

| Evaluation category | Examples in the reviewed literature | Proposal implication |
|---|---|---|
| Context/risk classification | G-Mean, accuracy, precision, recall, F1, false-positive rate | Useful for ML classifiers, but not automatically the main outcome for this rule-based step-up study |
| Authentication/system performance | Latency, processing time, throughput, resource use | Supports measuring Authentication Decision Latency |
| MFA/usability burden | Authentication time, completion time, re-authentication frequency, user satisfaction | Supports measuring the frequency of low-risk step-up authentication |
| Broad IAM measurement | Baumer et al. (2026) identify many metrics across multiple perspectives | Reinforces the need to select a small metric set tied directly to the research objective |

## Metrics defined for this proposal

### Low-Risk Step-Up Authentication Rate (LRSR)

`LRSR = (low-risk attempts receiving step-up MFA / total predefined low-risk attempts) × 100`

This is the **primary title-aligned outcome**.

### Elevated-Risk Step-Up Coverage (ERSC)

`ERSC = (predefined elevated-risk attempts triggering step-up MFA / total predefined elevated-risk attempts) × 100`

This verifies that reducing low-risk challenges does not cause the implemented policy to miss the elevated-risk scenarios it is explicitly designed to challenge.

### Authentication Decision Latency

Elapsed time used to produce the policy decision. This captures the processing cost introduced by contextual risk assessment.

**Important:** LRSR and ERSC are study-specific operational metrics. They should not be described as established standard IAM metrics.
