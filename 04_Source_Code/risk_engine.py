"""Proposal-stage contextual risk engine.

This module demonstrates the deterministic rule model described in Chapter 3.
It is a proof-of-concept component, not a production authentication engine.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Context:
    device_familiar: bool
    network_location_consistent: bool
    access_time_consistent: bool

@dataclass(frozen=True)
class RiskDecision:
    score: int
    risk_level: str
    step_up_required: bool
    reasons: tuple[str, ...]


def assess_risk(context: Context) -> RiskDecision:
    reasons = []
    score = 0

    if not context.device_familiar:
        score += 1
        reasons.append("unrecognised_device")
    if not context.network_location_consistent:
        score += 1
        reasons.append("unexpected_network_or_location")
    if not context.access_time_consistent:
        score += 1
        reasons.append("unusual_access_time")

    risk_level = "LOW" if score <= 1 else "ELEVATED"
    return RiskDecision(
        score=score,
        risk_level=risk_level,
        step_up_required=(risk_level == "ELEVATED"),
        reasons=tuple(reasons),
    )
