#!/usr/bin/env python3
"""Gate report (file 50, PART B9).

Reads every gate.json under versions/family_XX/ and produces:
  1. a per-(strategy, intensity) table:
     strategy | intensity | n | accept % | H-fail breakdown | mean G1..G4 | mean composite
  2. a threshold-sensitivity table: accept-rate as G1/G2 thresholds vary over {3, 4, 5}
     (holding G3>=5, G4>=3 and all hard constraints).

Writes reports/gate_report.md and prints a summary.

  python tools/report_gate.py --family 01 [--criterion 1]
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

import backends as B

REPORT = B.REPORTS_DIR / "gate_report.md"
_CRITS = ["G1_unambiguity", "G2_completeness", "G3_faithfulness", "G4_naturalness"]
_SHORT = {"G1_unambiguity": "G1", "G2_completeness": "G2",
          "G3_faithfulness": "G3", "G4_naturalness": "G4"}
_HARD = ["H1_example_consistency", "H2_io_contract", "H3_leakage",
         "H4_s09_nonbinding", "H5_solver_roundtrip"]
_ACCEPT = {"ACCEPT", "PASS"}


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def collect(family, criterion):
    rows = []
    base = B.VERSIONS_DIR / f"family_{family}"
    crit_dirs = [B.criterion_dirname(criterion)] if criterion else \
        [d.name for d in sorted(base.glob("criterion_*"))]
    for cd in crit_dirs:
        cbase = base / cd
        if not cbase.exists():
            continue
        for vdir in sorted(cbase.glob("v*")):
            gate = _read_json(vdir / "gate.json")
            edit = _read_json(vdir / "edit.json")
            if not gate:
                continue
            rows.append({
                "strategy": "+".join(edit.get("strategies", []) or []) or "-",
                "intensity": edit.get("intensity", "") or "-",
                "result": gate.get("result"),
                "composite": gate.get("composite"),
                "graded": {c: gate.get("graded", {}).get(c, {}).get("score") for c in _CRITS},
                "hard": {h: gate.get("hard", {}).get(h, {}).get("pass") for h in _HARD},
            })
    return rows


def _mean(xs):
    xs = [x for x in xs if isinstance(x, (int, float))]
    return round(sum(xs) / len(xs), 2) if xs else None


def strategy_table(rows):
    groups = defaultdict(list)
    for r in rows:
        groups[(r["strategy"], r["intensity"])].append(r)
    lines = ["| strategy | intensity | n | accept % | H-fail (H1/H2/H3/H4/H5) | "
             "mean G1 | G2 | G3 | G4 | mean composite |",
             "|---|---|--:|--:|---|--:|--:|--:|--:|--:|"]
    for (strat, inten), rs in sorted(groups.items()):
        n = len(rs)
        acc = sum(1 for r in rs if r["result"] in _ACCEPT)
        hfail = [sum(1 for r in rs if r["hard"].get(h) is False) for h in _HARD]
        means = [_mean([r["graded"][c] for r in rs]) for c in _CRITS]
        comp = _mean([r["composite"] for r in rs])
        lines.append(f"| {strat} | {inten} | {n} | {100*acc/n:.0f}% | "
                     f"{'/'.join(str(x) for x in hfail)} | "
                     f"{means[0]} | {means[1]} | {means[2]} | {means[3]} | {comp} |")
    return "\n".join(lines)


def sensitivity_table(rows):
    """Accept-rate as G1/G2 thresholds vary over {3,4,5}. Holds G3>=5, G4>=3 and requires
    every hard constraint that has an explicit verdict to pass (None = not-applicable)."""
    def hard_ok(r):
        return all(r["hard"].get(h) is not False for h in _HARD)

    def graded_accept(r, t1, t2):
        g = r["graded"]
        return (g["G1_unambiguity"] is not None and g["G1_unambiguity"] >= t1
                and g["G2_completeness"] is not None and g["G2_completeness"] >= t2
                and g["G3_faithfulness"] is not None and g["G3_faithfulness"] >= 5
                and g["G4_naturalness"] is not None and g["G4_naturalness"] >= 3)

    n = len(rows) or 1
    lines = ["| G1 thr \\ G2 thr | 3 | 4 | 5 |", "|---|--:|--:|--:|"]
    for t1 in (3, 4, 5):
        cells = []
        for t2 in (3, 4, 5):
            acc = sum(1 for r in rows if hard_ok(r) and graded_accept(r, t1, t2))
            cells.append(f"{100*acc/n:.0f}%")
        lines.append(f"| **{t1}** | {cells[0]} | {cells[1]} | {cells[2]} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2])
    args = ap.parse_args()

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    out = ["# Gate report", ""]
    for family in B.list_families(args.family):
        rows = collect(family, args.criterion)
        if not rows:
            continue
        acc = sum(1 for r in rows if r["result"] in _ACCEPT)
        out += [f"## family_{family}  (n={len(rows)}, accepted={acc}, "
                f"{100*acc/len(rows):.0f}%)", "",
                "### By strategy × intensity", "", strategy_table(rows), "",
                "### Threshold sensitivity (accept-rate; G3≥5, G4≥3, hard pass held)", "",
                sensitivity_table(rows), ""]
        print(f"[gate_report] family_{family}: {len(rows)} versions, {acc} accepted "
              f"({100*acc/len(rows):.0f}%)")
    REPORT.write_text("\n".join(out) + "\n")
    print(f"[gate_report] wrote {REPORT}")


if __name__ == "__main__":
    main()
