"""Basic tests for the proposal-stage deterministic policy."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from risk_engine import Context, assess_risk
from adaptive_mfa import evaluate_adaptive_mfa
from static_mfa import evaluate_static_mfa


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    all_normal = Context(True, True, True)
    one_abnormal = Context(False, True, True)
    two_abnormal = Context(False, False, True)
    all_abnormal = Context(False, False, False)

    check(assess_risk(all_normal).score == 0, "all-normal context should score 0")
    check(assess_risk(one_abnormal).risk_level == "LOW", "score 1 should be LOW")
    check(assess_risk(two_abnormal).risk_level == "ELEVATED", "score 2 should be ELEVATED")
    check(assess_risk(all_abnormal).score == 3, "all-abnormal context should score 3")
    check(evaluate_static_mfa(True).step_up_required, "static baseline should require step-up")
    check(not evaluate_adaptive_mfa(True, all_normal).step_up_required, "low risk should not require step-up")
    check(evaluate_adaptive_mfa(True, two_abnormal).step_up_required, "elevated risk should require step-up")
    check(evaluate_adaptive_mfa(False, all_normal).access_state == "DENY_PRIMARY_AUTH_FAILED", "invalid primary auth should be denied")
    print("All proposal-stage policy checks passed.")


if __name__ == "__main__":
    main()
