# Research Gap Analysis

## Evidence from the previous SLR

The Assignment 1 synthesis found a clear movement from rigid/static MFA toward adaptive and risk-based authentication. Contextual signals include device information, user behaviour, location, network conditions, time and resource/access context. Several studies report promising experimental results, but the environments and evaluation measures differ substantially.

## Recurring limitations relevant to this proposal

- conceptual or prototype-only adaptive MFA frameworks;
- inconsistent datasets and test environments;
- different metrics across classification, system performance and usability studies;
- privacy and explainability concerns;
- behavioural drift and threshold selection;
- limited long-term or real-world validation.

## Specific proposal gap

Existing research provides limited directly comparable evidence showing **how much context-aware adaptive MFA reduces step-up authentication for predefined low-risk legitimate web-access attempts compared with static MFA under the same controlled conditions**, while also confirming that predefined elevated-risk attempts still trigger step-up authentication and recording the latency introduced by contextual decision-making.

## What this proposal does not claim

The proposal does **not** claim that adaptive MFA is new, that the three chosen contextual indicators are universally optimal, or that the prototype will outperform every existing RBA/CAA-MFA system. The proposed contribution is a narrow, repeatable proof-of-concept comparison tied directly to the approved title.
