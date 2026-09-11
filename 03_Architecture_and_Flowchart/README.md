# 03_Architecture_and_Flowchart

This folder contains the proposed technical diagrams for the research project:

**Context-Aware Adaptive Multi-Factor Authentication for Reducing Low-Risk Step-Up Authentication in Web-Based Access Management**

The diagrams support **Research Objective 2 (RO2)**, which is to develop a context-aware adaptive MFA prototype that applies risk-based step-up authentication to web access attempts.

## Files

- `figure_3_1_dsr_fit.*`  
  Shows how the six Design Science Research stages are applied to the proposed study.

- `figure_3_2_architecture_fit.*`  
  Shows the proposed system architecture, including primary authentication, contextual information collection, risk assessment, adaptive step-up MFA, access decision, and logging.

- `figure_3_3_flowchart_fit.*`  
  Shows the authentication process from credential validation to contextual risk classification, step-up TOTP authentication, and final access decision.

- `figure_3_4_evaluation_fit.*`  
  Shows the proposed comparison between the static MFA baseline and the context-aware adaptive MFA approach.

- `figure_3_5_gantt_fit.*`  
  Shows the proposed research timeline mapped to the Design Science Research phases.

- `Group_O_Chapter3_Editable_Diagrams.drawio`  
  Editable source file for the diagrams.

## Relationship to the Proposal

The architecture and flowchart in this folder are intended to remain consistent with **Chapter 3: Research Methodology** of the research proposal.

The main proposed authentication behaviour is:

- **Low-risk authentication attempt → no step-up MFA**
- **Elevated-risk authentication attempt → require TOTP step-up MFA**
- **Failed required authentication → deny access**

The proposed system is evaluated against a static MFA baseline using:

- Low-Risk Step-Up Authentication Rate (LRSR)
- Elevated-Risk Step-Up Coverage (ERSC)
- Authentication Decision Latency

These diagrams represent the proposed design and evaluation plan at the research-proposal stage and should not be interpreted as final experimental results.
