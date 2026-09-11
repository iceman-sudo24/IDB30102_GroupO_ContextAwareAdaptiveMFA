# Context-Aware Adaptive Multi-Factor Authentication for Reducing Low-Risk Step-Up Authentication in Web-Based Access Management

**Course:** IDB30102 Research Methodology  
**Group:** O  
**Assigned Research Area:** Identity and Access Management (IAM)  
**Repository name:** `IDB30102_GroupO_ContextAwareAdaptiveMFA`

> **Proposal-stage repository.** This repository contains research evidence and preliminary technical components. It does **not** claim that the final experimental evaluation has already been completed.

## Group Members

| Name | Student ID | Role |
|---|---|---|
| ISYRAF BIN SALAHUDDIN | 52215225140 | Group Leader |
| AHMAD SYAUQI IZZAT BIN MUSDAR EFFENDI | 52215225077 | Member |
| ABDUL MUHAYMIN BIN ABDUL MATIN | 52227225179 | Member |
| KAMARUL BAHRI BIN KAMARULZAMAN | 52215225082 | Member |
| MUHAMMAD HARITH FARHAN BIN AHMAD YUSOFF | 52215226127 | Member |

## IMPORTANT NOTE (!!)
This is the second version of this Repository due to mistakes within the first one that led to its deletions. As our group is still currently in the learning stage when it comes to Github usage and proficiency, we were susceptible to mistakes such as the incorrect ways to commit, make files, make folders, organize the repo, setup the repo and others - especially learning the ropes of **git commands**.

## Research Problem

Static MFA can apply the same additional authentication requirement even when the contextual risk of access attempts differs. This may cause legitimate low-risk access attempts to receive step-up authentication unnecessarily from the perspective of the study's predefined low-risk policy. At the same time, existing adaptive MFA studies use heterogeneous contextual signals, datasets, environments and evaluation measures, making direct comparison difficult.

## Research Aim

To develop a context-aware adaptive multi-factor authentication approach for reducing low-risk step-up authentication in web-based access management while maintaining appropriate authentication responses to elevated-risk access attempts.

## Research Objectives

1. **RO1:** To analyse contextual risk indicators and evaluation measures relevant to adaptive MFA for web-based access management.
2. **RO2:** To develop a context-aware adaptive MFA prototype that applies risk-based step-up authentication to web access attempts.
3. **RO3:** To evaluate the proposed prototype against static MFA using low-risk step-up authentication rate, elevated-risk step-up coverage and authentication decision latency.

## Proposed Solution

The proposed proof of concept uses three controllable contextual indicators:

- device familiarity;
- network/location consistency;
- access-time consistency.

Each abnormal condition contributes one risk point in the proposal-stage rule model:

- **Score 0–1:** Low risk → no step-up MFA;
- **Score 2–3:** Elevated risk → step-up MFA required.

The equal weighting is a transparent **researcher-defined prototype rule**, not a claim that these factors have equal importance in production systems.

## Research Methodology and Development Model

- **Research Methodology:** Design Science Research (DSR)
- **Development Model:** Evolutionary Prototyping

DSR phases used in the proposal:

1. Problem Identification and Motivation
2. Define Objectives of a Solution
3. Design and Development
4. Demonstration
5. Evaluation
6. Communication

## Proposed Evaluation Plan

### Baseline

**Static MFA:** after valid primary credentials, step-up MFA is required regardless of contextual risk.

### Proposed approach

**Context-aware adaptive MFA:** the contextual rule engine determines whether step-up MFA is required.

### Test environment

A controlled local web-access environment using synthetic/test accounts and a complete set of eight binary contextual combinations. Five test accounts and three repetitions are planned, producing **120 planned authentication attempts (60 low-risk and 60 elevated-risk)**.

### Metrics

- **Low-Risk Step-Up Authentication Rate (LRSR)**  
  `(low-risk attempts receiving step-up / total low-risk attempts) × 100`
- **Elevated-Risk Step-Up Coverage (ERSC)**  
  `(elevated-risk attempts triggering step-up / total elevated-risk attempts) × 100`
- **Authentication Decision Latency**  
  elapsed time required to produce the policy decision.

The primary proposal success condition is a lower LRSR than static MFA while the predefined elevated-risk scenarios continue to trigger step-up authentication. Latency is reported as a performance cost rather than given an unsupported pass threshold.

## Proposed System Architecture

See [`03_Architecture_and_Flowchart/`](03_Architecture_and_Flowchart/). The diagrams are the same proposal-stage designs intended for Chapter 3.

Core flow:

`Primary Authentication → Context Collection → Risk Assessment → Low Risk: Allow / Elevated Risk: Step-Up TOTP → Access Decision + Logging`

## Objective-to-Repository Mapping

| Research Objective | Repository Evidence |
|---|---|
| RO1 | `01_Research_Papers/`, `02_Literature_Review/` |
| RO2 | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| RO3 | `05_Data_or_Sample_Input/`, `06_Results_or_Expected_Output/` |
| All objectives | `07_References/` |

## Preliminary Technical Components

The proposal-stage code demonstrates the feasibility of the core authentication-policy logic rather than a finished production application.

- `risk_engine.py` — transparent contextual risk scoring;
- `static_mfa.py` — static MFA baseline policy;
- `adaptive_mfa.py` — adaptive step-up policy;
- `totp_demo.py` — optional TOTP proof of concept using PyOTP;
- `run_scenarios.py` — executes the synthetic scenarios through the two policy modes;
- `test_policy.py` — basic unit tests for the proposal-stage policy logic.

A future full prototype can place the same components behind a lightweight Flask web interface and local SQLite test-user store. Those components are **planned**, not represented here as already complete.

## How to Run the Preliminary Code

Requires Python 3.10+.

From the repository root:

```bash
python 04_Source_Code/test_policy.py
python 04_Source_Code/run_scenarios.py --input 05_Data_or_Sample_Input/scenario_definitions.csv
```

The scenario runner prints a technical demonstration summary only. It does not produce or claim final research findings.

Optional TOTP demonstration:

```bash
python -m pip install -r 04_Source_Code/requirements.txt
python 04_Source_Code/totp_demo.py
```

## Academic Integrity and Data Handling

- No real passwords, authentication tokens, private credentials or confidential user records are included.
- Synthetic scenarios and test account identifiers are used.
- Research-paper PDFs are not redistributed unless legally permitted; the repository uses citations/DOIs/official links instead.
- External libraries and technical resources are acknowledged under `07_References/`.
- Any final GitHub commit history should reflect **actual team work**. The included contribution plan is a suggested workflow, not a fabricated record of completed work.

## Status

**Proposal stage — preliminary research and technical evidence only.**
