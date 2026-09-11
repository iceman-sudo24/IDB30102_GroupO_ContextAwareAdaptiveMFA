# Controlled Test Environment

## Purpose

The test environment is designed to compare static and adaptive MFA under the **same predefined authentication contexts**.

## Data type

Synthetic / controlled authentication scenarios only. No real organisational login records or personal user credentials are required.

## Scenario design

Three binary contextual indicators create eight possible combinations:

- device familiarity;
- network/location consistency;
- access-time consistency.

Risk score = number of abnormal conditions.

- 0–1 → LOW
- 2–3 → ELEVATED

The eight combinations are repeated across five test accounts and three repetitions, yielding **120 planned attempts**:

- 60 predefined low-risk attempts;
- 60 predefined elevated-risk attempts.

## Why the ground truth is defined before execution

Each scenario is assigned its expected score/risk before running the prototype. This prevents circular evaluation where the system defines its own answer and is then treated as correct by definition.

## Baseline

Static MFA requires step-up authentication after valid primary authentication regardless of contextual risk.

## Proposed policy

Adaptive MFA uses the contextual risk engine:

- LOW → allow without step-up;
- ELEVATED → require step-up MFA.

## Data protection

The CSV files contain only synthetic identifiers. Do not add real names, passwords, OTP secrets, tokens, IP addresses tied to real persons, or private organisational information.
