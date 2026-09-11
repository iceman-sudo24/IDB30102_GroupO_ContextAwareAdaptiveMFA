"""Static MFA baseline policy for the proposal-stage comparison."""
from dataclasses import dataclass

@dataclass(frozen=True)
class StaticDecision:
    primary_authentication_valid: bool
    step_up_required: bool
    access_state: str


def evaluate_static_mfa(primary_authentication_valid: bool) -> StaticDecision:
    if not primary_authentication_valid:
        return StaticDecision(False, False, "DENY_PRIMARY_AUTH_FAILED")
    return StaticDecision(True, True, "STEP_UP_REQUIRED")
