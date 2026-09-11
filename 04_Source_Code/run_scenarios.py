"""Run synthetic authentication scenarios through static and adaptive policies.

This script is a preliminary technical demonstration. Timing output depends on the
machine executing the code and must NOT be presented as final research results.
"""
from __future__ import annotations
import argparse
import csv
from pathlib import Path
from time import perf_counter_ns
from statistics import mean

from risk_engine import Context
from static_mfa import evaluate_static_mfa
from adaptive_mfa import evaluate_adaptive_mfa


def parse_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "normal", "familiar", "consistent"}


def run(input_file: Path) -> None:
    rows = []
    with input_file.open(newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            context = Context(
                device_familiar=parse_bool(row["device_familiar"]),
                network_location_consistent=parse_bool(row["network_location_consistent"]),
                access_time_consistent=parse_bool(row["access_time_consistent"]),
            )

            t0 = perf_counter_ns()
            static = evaluate_static_mfa(True)
            static_ns = perf_counter_ns() - t0

            t0 = perf_counter_ns()
            adaptive = evaluate_adaptive_mfa(True, context)
            adaptive_ns = perf_counter_ns() - t0

            rows.append({
                **row,
                "static_step_up": int(static.step_up_required),
                "adaptive_step_up": int(adaptive.step_up_required),
                "adaptive_score": adaptive.risk.score if adaptive.risk else "",
                "adaptive_risk": adaptive.risk.risk_level if adaptive.risk else "",
                "static_decision_ns": static_ns,
                "adaptive_decision_ns": adaptive_ns,
            })

    low = [r for r in rows if r["expected_risk"] == "LOW"]
    elevated = [r for r in rows if r["expected_risk"] == "ELEVATED"]

    def pct(num: int, den: int) -> float:
        return 100.0 * num / den if den else 0.0

    static_lrsr = pct(sum(int(r["static_step_up"]) for r in low), len(low))
    adaptive_lrsr = pct(sum(int(r["adaptive_step_up"]) for r in low), len(low))
    static_ersc = pct(sum(int(r["static_step_up"]) for r in elevated), len(elevated))
    adaptive_ersc = pct(sum(int(r["adaptive_step_up"]) for r in elevated), len(elevated))

    print("PRELIMINARY IMPLEMENTATION CHECK — NOT FINAL RESEARCH RESULTS")
    print(f"Scenarios processed: {len(rows)}")
    print(f"Low-risk scenarios: {len(low)} | Elevated-risk scenarios: {len(elevated)}")
    print(f"Static LRSR:   {static_lrsr:.1f}%")
    print(f"Adaptive LRSR: {adaptive_lrsr:.1f}%")
    print(f"Static ERSC:   {static_ersc:.1f}%")
    print(f"Adaptive ERSC: {adaptive_ersc:.1f}%")
    print(f"Mean static policy time:   {mean(int(r['static_decision_ns']) for r in rows):.0f} ns")
    print(f"Mean adaptive policy time: {mean(int(r['adaptive_decision_ns']) for r in rows):.0f} ns")
    print("Timing values are machine-dependent technical traces, not proposal findings.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    run(args.input)
