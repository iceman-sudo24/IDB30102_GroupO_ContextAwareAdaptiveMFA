# Proposed Evaluation Metrics

> **PROPOSAL-STAGE DEFINITIONS — NOT FINAL RESULTS**

## 1. Low-Risk Step-Up Authentication Rate (LRSR)

`LRSR = (number of predefined low-risk attempts receiving step-up MFA / total predefined low-risk attempts) × 100`

Primary interpretation: lower LRSR under adaptive MFA than static MFA supports the title-aligned outcome.

## 2. Elevated-Risk Step-Up Coverage (ERSC)

`ERSC = (number of predefined elevated-risk attempts triggering step-up MFA / total predefined elevated-risk attempts) × 100`

For the deterministic proposal-stage policy, the intended implementation requirement is **100% coverage of the predefined elevated-risk scenario set**. This is a functional policy requirement, not a claim of 100% real-world threat detection.

## 3. Authentication Decision Latency

Time from the start of the policy-decision operation to completion of the step-up/no-step-up decision.

Latency is reported as a performance cost. No arbitrary pass threshold is imposed at proposal stage.

## Planned comparison

| Approach | LRSR | ERSC | Mean/median decision latency |
|---|---:|---:|---:|
| Static MFA | TO BE MEASURED | TO BE MEASURED | TO BE MEASURED |
| Adaptive MFA | TO BE MEASURED | TO BE MEASURED | TO BE MEASURED |
