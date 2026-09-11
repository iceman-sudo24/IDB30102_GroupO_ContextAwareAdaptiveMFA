# Preliminary Source Code

These components demonstrate the technical direction of RO2 and RO3. They are intentionally small because Assignment 2 is a research-proposal stage, not the completed final system.

## Files

- `risk_engine.py` — transparent 0–3 context-risk score.
- `static_mfa.py` — baseline policy that always requests step-up after valid primary authentication.
- `adaptive_mfa.py` — context-aware policy that requests step-up only for score 2–3.
- `run_scenarios.py` — processes the synthetic scenario set.
- `test_policy.py` — basic implementation checks.
- `totp_demo.py` — optional TOTP feasibility demonstration using PyOTP.

## Run

From the repository root:

```bash
python 04_Source_Code/test_policy.py
python 04_Source_Code/run_scenarios.py --input 05_Data_or_Sample_Input/scenario_definitions.csv
```

Optional TOTP demo:

```bash
python -m pip install -r 04_Source_Code/requirements.txt
python 04_Source_Code/totp_demo.py
```

## Research integrity note

Output from these scripts is **preliminary technical evidence**. The final research evaluation must be run under the defined Chapter 3 procedure and documented separately. Machine timing from this simple script is not a final latency result.
