#!/usr/bin/env python3
"""
P report, STATEMENT-LEVEL pass rate (companion to eval_report_p.py).

Like eval_report_p.py but the percentage counts how many STATEMENTS a model *clearly
passed* -- a statement counts only if the model clears ALL of its test cases
(passed == total) -- rather than the micro-average over test cases.

Per family (and OVERALL), per model:
  PASS % = 100 * (# statements fully solved) / (# statements attempted)

Reads evaluation/grades_p/**/result.json. Safe any time.
    python eval_report_p_statement.py
"""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
OUT  = ROOT.parent / "evaluation"
GRADES = OUT / "grades_p"
REPORTS = OUT / "reports"


def load():
    rows = []
    for jf in GRADES.glob("**/result.json"):
        try:
            rows.append(json.loads(jf.read_text()))
        except Exception:
            pass
    return rows


def table(title, models, cell):
    w = max([len(m) for m in models] + [12])
    head = f"{'model':<{w}}{'PASS % (solved/attempted)':>30}"
    lines = [title, head, "-" * len(head)]
    for m in models:
        lines.append(f"{m:<{w}}{cell(m):>30}")
    return lines


def main():
    rows = load()
    if not rows:
        print("no P grades yet under", GRADES); return
    families = sorted({r["family"] for r in rows})
    models   = sorted({r["model"] for r in rows})
    # agg[(fam,model)] = [solved, attempted]
    agg = defaultdict(lambda: [0, 0])
    for r in rows:
        solved = (r.get("total", 0) > 0 and r.get("passed") == r.get("total"))
        k = (r["family"], r["model"])
        agg[k][0] += int(solved); agg[k][1] += 1
    oall = defaultdict(lambda: [0, 0])
    for (fam, m), (s, n) in agg.items():
        o = oall[m]; o[0] += s; o[1] += n

    def cell_for(getter):
        def f(m):
            s, n = getter(m)
            return f"{(100*s/n):.1f}% ({s}/{n})" if n else "-"
        return f

    lines = []
    out_json = {"per_family": {}, "overall": {}}
    for fam in families:
        present = [m for m in models if (fam, m) in agg]
        if not present:
            continue
        lines.append(f"\n############### FAMILY {fam}  (P) ###############")
        lines += table("STATEMENTS fully solved (all test cases passed)",
                       present, cell_for(lambda m: agg[(fam, m)]))
        out_json["per_family"][fam] = {m: {"solved": agg[(fam, m)][0],
                                           "statements": agg[(fam, m)][1]} for m in present}
    present = [m for m in models if m in oall]
    lines.append("\n=============== OVERALL — ALL FAMILIES (P) ===============")
    lines += table("STATEMENTS fully solved (all test cases passed)",
                   present, cell_for(lambda m: oall[m]))
    out_json["overall"] = {m: {"solved": oall[m][0], "statements": oall[m][1]} for m in present}

    text = "\n".join(lines)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary_p_statement.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary_p_statement.json").write_text(json.dumps(out_json, indent=2))
    print(f"\nsaved -> {REPORTS/'summary_p_statement.md'}  and  {REPORTS/'summary_p_statement.json'}")


if __name__ == "__main__":
    main()
