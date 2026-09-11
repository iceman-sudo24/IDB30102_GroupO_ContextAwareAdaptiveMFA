"""Adaptive MFA policy using the transparent proposal-stage risk engine."""
from dataclasses import dataclass
from risk_engine import Context, RiskDecision, assess_risk

@dataclass(frozen=True)
class AdaptiveDecision:
    primary_authentication_valid: bool
    risk: RiskDecision | None
    step_up_required: bool
    access_state: str


def evaluate_adaptive_mfa(primary_authentication_valid: bool, context: Context) -> AdaptiveDecision:
    if not primary_authentication_valid:
        return AdaptiveDecision(False, None, False, "DENY_PRIMARY_AUTH_FAILED")

    risk = assess_risk(context)
    if risk.step_up_required:
        return AdaptiveDecision(True, risk, True, "STEP_UP_REQUIRED")
    return AdaptiveDecision(True, risk, False, "ALLOW_NO_STEP_UP")
