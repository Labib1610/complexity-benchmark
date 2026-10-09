#!/usr/bin/env python3
"""
NPC report, STATEMENT-LEVEL pass rate (companion to eval_report.py).

Difference from eval_report.py: eval_report.py reports a micro-average over TEST
CASES (cases passed / cases tried). THIS report instead counts how many STATEMENTS a
model *clearly passed* -- a statement counts only if the model clears ALL of its test
cases (passed == total). That is the "fraction of problems solved" view used for the
students + frontier before.

For each family (and OVERALL across families), per model, one column per time limit:
  PASS % = 100 * (# statements fully solved) / (# statements attempted)
plus the raw (solved / attempted) counts.

Reads evaluation/grades/**/*.json. Safe any time (even mid-run).
    python eval_report_statement.py
"""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
OUT  = ROOT.parent / "evaluation"
GRADES = OUT / "grades"
REPORTS = OUT / "reports"
CRIT_LABEL = {"1": "NPC", "2": "P"}


def load():
    rows = []
    for jf in GRADES.glob("**/*.json"):
        if jf.name.endswith(".fail.json"):
            continue
        try:
            d = json.loads(jf.read_text())
        except Exception:
            continue
        if "limit" in d and "passed" in d and "total" in d:
            rows.append(d)
    return rows


def fmt_table(title, models, limits, cell_fn):
    w = max([len(m) for m in models] + [12])
    head = f"{'model':<{w}}" + "".join(f"{str(l)+'s':>18}" for l in limits)
    lines = [title, head, "-" * len(head)]
    for m in models:
        lines.append(f"{m:<{w}}" + "".join(f"{cell_fn(m, l):>18}" for l in limits))
    return lines


def main():
    rows = load()
    if not rows:
        print("no grades yet under", GRADES); return
    limits = sorted({r["limit"] for r in rows})
    families = sorted({r["family"] for r in rows})
    crits = sorted({r["crit"] for r in rows})
    models = sorted({r["model"] for r in rows})

    # agg[(fam,crit,model,limit)] = [n_statements_fully_solved, n_statements]
    agg = defaultdict(lambda: [0, 0])
    for r in rows:
        k = (r["family"], r["crit"], r["model"], r["limit"])
        solved = (r["total"] > 0 and r["passed"] == r["total"])
        agg[k][0] += int(solved); agg[k][1] += 1
    oall = defaultdict(lambda: [0, 0])
    for (fam, crit, m, lim), (s, n) in agg.items():
        o = oall[(crit, m, lim)]; o[0] += s; o[1] += n

    def cell(getter):
        def f(m, l):
            s, n = getter(m, l)
            return f"{(100*s/n):.1f}% ({s}/{n})" if n else "-"
        return f

    lines = []
    out_json = {"per_family": {}, "overall": {}}
    for fam in families:
        for crit in crits:
            present = [m for m in models if any((fam, crit, m, l) in agg for l in limits)]
            if not present:
                continue
            get = lambda m, l: agg[(fam, crit, m, l)]
            lines.append(f"\n############### FAMILY {fam}  ({CRIT_LABEL.get(crit, crit)}) ###############")
            lines += fmt_table("STATEMENTS fully solved (all test cases passed) — % (solved/attempted)",
                               present, limits, cell(get))
            out_json["per_family"].setdefault(fam, {})[crit] = {
                m: {str(l): {"solved": agg[(fam, crit, m, l)][0], "statements": agg[(fam, crit, m, l)][1]}
                    for l in limits} for m in present}

    for crit in crits:
        present = [m for m in models if any((crit, m, l) in oall for l in limits)]
        if not present:
            continue
        get = lambda m, l: oall[(crit, m, l)]
        lines.append(f"\n=============== OVERALL — ALL FAMILIES ({CRIT_LABEL.get(crit, crit)}) ===============")
        lines += fmt_table("STATEMENTS fully solved (all test cases passed) — % (solved/attempted)",
                           present, limits, cell(get))
        out_json["overall"][crit] = {
            m: {str(l): {"solved": oall[(crit, m, l)][0], "statements": oall[(crit, m, l)][1]}
                for l in limits} for m in present}

    text = "\n".join(lines)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary_statement.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary_statement.json").write_text(json.dumps(out_json, indent=2))
    print(f"\nsaved -> {REPORTS/'summary_statement.md'}  and  {REPORTS/'summary_statement.json'}")


if __name__ == "__main__":
    main()
