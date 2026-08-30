#!/usr/bin/env python3
"""Verify the compact frozen result bundle used by the article."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCALED = ROOT / "runs-scaled/20260830-120856"
ABLATION = ROOT / "runs-ablation/20260830-123547"


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def main() -> None:
    scaled = rows(SCALED / "episodes.jsonl")
    ablation = rows(ABLATION / "episodes.jsonl")
    assert len(scaled) == 36
    assert len(ablation) == 48
    assert all(row["status"] == "completed" for row in scaled + ablation)
    source_ref = "runs-scaled/20260830-120856"
    reused = [row for row in ablation if "reused_from" in row]
    assert len(reused) == 24
    assert all(row["reused_from"] == source_ref for row in reused)
    ablation_manifest = json.loads((ABLATION / "manifest.json").read_text())
    ablation_summary = json.loads((ABLATION / "summary.json").read_text())
    assert ablation_manifest["source_run"] == source_ref
    assert ablation_summary["manifest"] == ablation_manifest

    scaled_conditions = Counter(row["condition"] for row in scaled)
    assert scaled_conditions == {"baseline": 12, "placebo": 12, "oakx": 12}
    scaled_successes = Counter(
        row["condition"] for row in scaled if row["grade"]["strict_success"]
    )
    assert scaled_successes == {"oakx": 6}
    oakx_scaled = [row for row in scaled if row["condition"] == "oakx"]
    assert all(row["grade"]["root_ok"] for row in oakx_scaled)
    assert all(row["grade"]["authoritative_source_read"] for row in oakx_scaled)

    expected_cells = {
        "no_oakx_no_calculator": 0,
        "no_oakx_calculator": 2,
        "oakx_no_calculator": 6,
        "oakx_calculator": 11,
    }
    assert Counter(row["condition"] for row in ablation) == {
        cell: 12 for cell in expected_cells
    }
    for cell, expected in expected_cells.items():
        actual = sum(
            row["grade"]["strict_success"]
            for row in ablation
            if row["condition"] == cell
        )
        assert actual == expected, (cell, actual, expected)

    combined = [row for row in ablation if row["condition"] == "oakx_calculator"]
    assert all(row["grade"]["root_ok"] for row in combined)
    assert all(row["grade"]["authoritative_source_read"] for row in combined)
    calculator_calls = [
        tool
        for row in combined
        for tool in row["tool_transcript"]
        if tool["tool"] == "calculate_expression"
    ]
    assert len(calculator_calls) == 9
    assert all("value" in call["result"] for call in calculator_calls)

    print(
        "PUBLIC_RESULTS_OK "
        "scaled=36 ablation=48 oakx=6/12 oakx_calculator=11/12 calculator_checks=9"
    )


if __name__ == "__main__":
    main()
