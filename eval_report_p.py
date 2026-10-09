#!/usr/bin/env python3
"""
Summarize the P evaluation (evaluate_p.py) -- one pass% per model per family, the
same style used for students + frontier before (no time-limit columns, since P has
no sweep; each statement is judged at its own stated time limit).

Per family (and OVERALL across families) it prints:
  (A) PASS %  = test cases passed / tried, per model.
  (B) AVG     = average test cases passed per statement, per model.

Reads evaluation/grades_p/**/result.json. Safe to run any time (even mid-run).
    python eval_report_p.py     # print + write evaluation/reports/summary_p.{md,json}
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
        try: rows.append(json.loads(jf.read_text()))
        except Exception: pass
    return rows


def table(title, models, cell):
    w = max([len(m) for m in models] + [12])
    head = f"{'model':<{w}}{'PASS %':>18}{'AVG cases':>14}"
    lines = [title, head, "-" * len(head)]
    for m in models:
        pc, av = cell(m)
        lines.append(f"{m:<{w}}{pc:>18}{av:>14}")
    return lines


def main():
    rows = load()
    if not rows:
        print("no P grades yet under", GRADES); return
    families = sorted({r["family"] for r in rows})
    models   = sorted({r["model"] for r in rows})
    # agg[(fam,model)] = [passed, total, n_statements]
    agg = defaultdict(lambda: [0, 0, 0])
    for r in rows:
        k = (r["family"], r["model"])
        agg[k][0] += r["passed"]; agg[k][1] += r["total"]; agg[k][2] += 1
    oall = defaultdict(lambda: [0, 0, 0])
    for (fam, m), (p, t, n) in agg.items():
        o = oall[m]; o[0] += p; o[1] += t; o[2] += n

    def cell_for(getter):
        def f(m):
            p, t, n = getter(m)
            pc = f"{(100*p/t):.1f}% ({p}/{t})" if t else "-"
            av = f"{(p/n):.1f}" if n else "-"
            return pc, av
        return f

    out_lines = []
    out_json = {"per_family": {}, "overall": {}}
    for fam in families:
        present = [m for m in models if (fam, m) in agg]
        if not present: continue
        out_lines.append(f"\n############### FAMILY {fam}  (P) ###############")
        out_lines += table("PASS % and AVG test cases passed per statement",
                           present, cell_for(lambda m: agg[(fam, m)]))
        out_json["per_family"][fam] = {m: {"passed": agg[(fam, m)][0], "total": agg[(fam, m)][1],
                                           "statements": agg[(fam, m)][2]} for m in present}
    present = [m for m in models if m in oall]
    out_lines.append("\n=============== OVERALL — ALL FAMILIES (P) ===============")
    out_lines += table("PASS % and AVG test cases passed per statement",
                       present, cell_for(lambda m: oall[m]))
    out_json["overall"] = {m: {"passed": oall[m][0], "total": oall[m][1],
                               "statements": oall[m][2]} for m in present}

    text = "\n".join(out_lines)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary_p.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary_p.json").write_text(json.dumps(out_json, indent=2))
    print(f"\nsaved -> {REPORTS/'summary_p.md'}  and  {REPORTS/'summary_p.json'}")


if __name__ == "__main__":
    main()
