# Methods and Algorithms Identified in Relevant Literature

The relevant studies use several implementation families:

1. **Transparent rule/risk engines** — contextual conditions contribute to a risk decision which changes MFA requirements.
2. **Reinforcement learning** — e.g., RLAuth uses learned policies for contextual risk-based authentication.
3. **Federated learning / AI scoring** — used in continuous or dynamic risk-based authentication to learn from distributed/contextual data.
4. **Conventional machine learning** — classification using attributes such as IP, user agent or access-request features.
5. **Context reasoning / factor trust** — context and trust values determine the number or strength of MFA factors required.

## Method selected for this proposal

The proposal deliberately uses a **simple transparent rule-based risk engine** rather than machine learning. This keeps the contribution aligned with the approved title: measuring the effect of contextual risk on **low-risk step-up authentication**, not optimising a classifier. It also makes the complete scenario set deterministic and reproducible at proposal stage.
