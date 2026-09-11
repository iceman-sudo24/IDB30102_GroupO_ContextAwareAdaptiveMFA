# Expected / Sample Output

> **EXPECTED / SAMPLE — NOT FINAL EXPERIMENTAL RESULTS**

The final evaluation should produce one row per controlled scenario and an aggregate comparison of static and adaptive MFA.

Example decision trace format:

```text
Scenario: S05-U01-R1
Context: unfamiliar device + unexpected network + expected time
Expected risk: ELEVATED
Static policy: STEP_UP_REQUIRED
Adaptive policy: STEP_UP_REQUIRED
Adaptive score: 2
Decision latency: [MEASURE DURING EVALUATION]
```

For a low-risk scenario, the expected adaptive policy behaviour is `ALLOW_NO_STEP_UP`, while the static baseline still requests step-up authentication.

The final report should distinguish clearly between:

- **expected policy behaviour** (defined before testing),
- **observed system output** (recorded during the controlled evaluation), and
- **interpretation** (reported after results are collected).
