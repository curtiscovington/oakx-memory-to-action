#!/usr/bin/env python3
"""Generate dependency-free SVG figures from frozen result summaries."""

from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("OAKX_FIGURE_OUT", ROOT / "figures"))


def esc(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bar_chart(path: Path, title: str, subtitle: str, labels: list[str], values: list[float], colors: list[str]) -> None:
    width, height = 1200, 680
    left, right, top, bottom = 120, 50, 125, 120
    chart_w, chart_h = width - left - right, height - top - bottom
    slot = chart_w / len(values)
    bar_w = slot * 0.58
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{esc(title)}</title>',
        f'<desc id="desc">{esc(subtitle)}</desc>',
        '<rect width="100%" height="100%" fill="#fbfaf7"/>',
        f'<text x="{left}" y="48" font-family="Inter,Arial,sans-serif" font-size="30" font-weight="700" fill="#17202a">{esc(title)}</text>',
        f'<text x="{left}" y="80" font-family="Inter,Arial,sans-serif" font-size="17" fill="#566573">{esc(subtitle)}</text>',
    ]
    for tick in range(0, 101, 25):
        y = top + chart_h * (1 - tick / 100)
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}" stroke="#d5d8dc" stroke-width="1"/>')
        parts.append(f'<text x="{left-18}" y="{y+6:.1f}" text-anchor="end" font-family="Inter,Arial,sans-serif" font-size="15" fill="#566573">{tick}%</text>')
    for index, (label, value, color) in enumerate(zip(labels, values, colors)):
        x = left + slot * index + (slot - bar_w) / 2
        bar_h = chart_h * value / 100
        y = top + chart_h - bar_h
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" rx="8" fill="{color}"/>')
        parts.append(f'<text x="{x+bar_w/2:.1f}" y="{y-14:.1f}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="22" font-weight="700" fill="#17202a">{value:.1f}%</text>')
        words = label.split("\n")
        for line_index, word in enumerate(words):
            parts.append(f'<text x="{x+bar_w/2:.1f}" y="{top+chart_h+34+line_index*23:.1f}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="16" fill="#2c3e50">{esc(word)}</text>')
    parts.append(f'<text x="24" y="{top+chart_h/2:.1f}" transform="rotate(-90 24 {top+chart_h/2:.1f})" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="16" fill="#566573">Strict task success</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def grouped_chart(path: Path, summary: dict) -> None:
    conditions = ["baseline", "oakx"]
    metrics = [("Root cause", "root_accuracy"), ("Exact value", "value_accuracy"), ("Strict success", "strict_success_rate")]
    width, height = 1200, 700
    left, right, top, bottom = 120, 55, 125, 125
    chart_w, chart_h = width-left-right, height-top-bottom
    group_w = chart_w / len(metrics)
    bar_w = 95
    colors = {"baseline": "#95a5a6", "oakx": "#2471a3"}
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">OAKX separated retrieval from execution</title>',
        '<desc id="desc">Baseline and matching OAKX accuracy on root cause, exact value, and strict success.</desc>',
        '<rect width="100%" height="100%" fill="#fbfaf7"/>',
        f'<text x="{left}" y="48" font-family="Inter,Arial,sans-serif" font-size="30" font-weight="700" fill="#17202a">OAKX separated retrieval from execution</text>',
        f'<text x="{left}" y="80" font-family="Inter,Arial,sans-serif" font-size="17" fill="#566573">Frozen 12-task scaled run; eight-call investigation budget</text>',
    ]
    for tick in range(0,101,25):
        y=top+chart_h*(1-tick/100)
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}" stroke="#d5d8dc"/>')
        parts.append(f'<text x="{left-18}" y="{y+6:.1f}" text-anchor="end" font-family="Inter,Arial,sans-serif" font-size="15" fill="#566573">{tick}%</text>')
    for gi,(label,key) in enumerate(metrics):
        center=left+group_w*(gi+0.5)
        for ci,condition in enumerate(conditions):
            value=summary["arms"][condition][key]*100
            x=center + (ci-0.5)*bar_w*1.35 - bar_w/2
            bar_h=chart_h*value/100; y=top+chart_h-bar_h
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w}" height="{bar_h:.1f}" rx="7" fill="{colors[condition]}"/>')
            parts.append(f'<text x="{x+bar_w/2:.1f}" y="{y-12:.1f}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="18" font-weight="700" fill="#17202a">{value:.1f}%</text>')
        parts.append(f'<text x="{center:.1f}" y="{top+chart_h+38}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="17" fill="#2c3e50">{esc(label)}</text>')
    legend_y=height-38
    for index,condition in enumerate(conditions):
        x=left+index*190
        label="No OAKX" if condition=="baseline" else "Matching OAKX"
        parts.append(f'<rect x="{x}" y="{legend_y-15}" width="20" height="20" rx="3" fill="{colors[condition]}"/>')
        parts.append(f'<text x="{x+30}" y="{legend_y+1}" font-family="Inter,Arial,sans-serif" font-size="16" fill="#2c3e50">{label}</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts)+"\n",encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ablation = json.loads((ROOT / "runs-ablation/20260830-123547/summary.json").read_text())
    scaled = json.loads((ROOT / "runs-scaled/20260830-120856/summary.json").read_text())
    cells = ablation["cells"]
    bar_chart(
        OUT / "ablation-strict-success.svg",
        "OAKX and deterministic execution solve different bottlenecks",
        "Frozen 2×2 ablation; 12 tasks per cell; eight-call investigation budget",
        ["Neither", "Calculator\nonly", "OAKX\nonly", "OAKX +\ncalculator"],
        [cells["no_oakx_no_calculator"]["strict_rate"]*100, cells["no_oakx_calculator"]["strict_rate"]*100, cells["oakx_no_calculator"]["strict_rate"]*100, cells["oakx_calculator"]["strict_rate"]*100],
        ["#95a5a6", "#d4ac0d", "#2471a3", "#148f77"],
    )
    grouped_chart(OUT / "retrieval-and-execution.svg", scaled)


if __name__ == "__main__":
    main()
