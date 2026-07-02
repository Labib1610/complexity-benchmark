"""Aggregate per-problem verdict.json files into summary.csv and metrics table."""

from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path


_CSV_COLUMNS = [
    "model", "family_id", "family_name", "criterion_id",
    "class_label", "overall_verdict", "first_failure", "n_cases", "n_passed",
]


def load_verdicts(results_dir: Path) -> list[dict]:
    """Load all verdict.json files under results_dir."""
    records = []
    for vfile in sorted(results_dir.rglob("verdict.json")):
        with open(vfile) as f:
            data = json.load(f)
        records.append(data)
    return records


def write_summary_csv(records: list[dict], out_path: Path) -> None:
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=_CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for r in records:
            n_cases = len(r.get("cases", []))
            n_passed = sum(1 for c in r.get("cases", []) if c.get("verdict") == "PASS")
            writer.writerow({
                "model": r.get("model", ""),
                "family_id": r.get("family_id", ""),
                "family_name": r.get("family_name", ""),
                "criterion_id": r.get("criterion_id", ""),
                "class_label": r.get("class_label", ""),
                "overall_verdict": r.get("overall", ""),
                "first_failure": r.get("first_failure", ""),
                "n_cases": n_cases,
                "n_passed": n_passed,
            })


def compute_metrics(records: list[dict]) -> dict:
    """Return per-model metrics dict."""
    # model -> class_label -> (pass_count, total_count)
    by_model: dict[str, dict[str, list[int, int]]] = defaultdict(
        lambda: defaultdict(lambda: [0, 0])
    )
    # model -> infeasible confident-wrong count, infeasible total
    infeasible: dict[str, list[int, int]] = defaultdict(lambda: [0, 0])

    for r in records:
        model = r.get("model", "unknown")
        cls = r.get("class_label", "UNKNOWN")
        verdict = r.get("overall", "")
        by_model[model][cls][1] += 1
        if verdict == "PASS":
            by_model[model][cls][0] += 1
        if cls == "INFEASIBLE":
            infeasible[model][1] += 1
            if verdict == "WRONG_ANSWER":
                infeasible[model][0] += 1

    metrics = {}
    for model, class_stats in by_model.items():
        total_pass = total_all = 0
        per_class = {}
        for cls, (p, t) in class_stats.items():
            per_class[cls] = p / t if t else 0.0
            total_pass += p
            total_all += t
        cw_pass, cw_total = infeasible[model]
        metrics[model] = {
            "pass_at_1_by_class": per_class,
            "pass_at_1_overall": total_pass / total_all if total_all else 0.0,
            "confident_wrong_rate_infeasible": cw_pass / cw_total if cw_total else 0.0,
        }
    return metrics


def print_metrics_table(metrics: dict) -> None:
    classes = ["P", "NPC", "INFEASIBLE"]
    header = f"{'Model':<30} {'P':>8} {'NPC':>8} {'INFEAS':>8} {'Overall':>8} {'CW-Rate':>8}"
    print(header)
    print("-" * len(header))
    for model, m in sorted(metrics.items()):
        pc = m["pass_at_1_by_class"]
        row = (
            f"{model:<30}"
            f" {pc.get('P', float('nan')):>8.2%}"
            f" {pc.get('NPC', float('nan')):>8.2%}"
            f" {pc.get('INFEASIBLE', float('nan')):>8.2%}"
            f" {m['pass_at_1_overall']:>8.2%}"
            f" {m['confident_wrong_rate_infeasible']:>8.2%}"
        )
        print(row)


def aggregate(results_dir: Path | str, out_csv: Path | str | None = None) -> None:
    results_dir = Path(results_dir)
    records = load_verdicts(results_dir)
    if not records:
        print(f"No verdict.json files found under {results_dir}", file=sys.stderr)
        return

    if out_csv is None:
        out_csv = results_dir / "summary.csv"
    out_csv = Path(out_csv)
    write_summary_csv(records, out_csv)
    print(f"Wrote {len(records)} rows to {out_csv}")

    metrics = compute_metrics(records)
    print_metrics_table(metrics)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Aggregate verdict.json files into summary.csv")
    parser.add_argument("results_dir", help="Path to results directory")
    parser.add_argument("--out", default=None, help="Output CSV path")
    args = parser.parse_args()
    aggregate(args.results_dir, args.out)
