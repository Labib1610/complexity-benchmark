#!/usr/bin/env python3
"""
Summarize the evaluation grades into the tables you asked for.

For each family, for each criterion, it prints:
  (A) PASS %  = total test cases passed / total test cases tried, per model, one
      column per time constraint (1s / 2s / 5s / 10s).
  (B) AVG CASES = average number of test cases a model passes per statement,
      per model, one column per time constraint.
And then the same two tables aggregated across ALL families (OVERALL).

Reads evaluation/grades/**/*.json (written by evaluate.py). Safe to run any time,
even mid-run -- it just summarizes whatever grades exist so far.

    python eval_report.py            # print + write evaluation/reports/summary.{md,json}
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
        if jf.name.endswith(".fail.json"):   # skip transient-failure sidecars (no grade fields)
            continue
        try:
            d = json.loads(jf.read_text())
        except Exception:
            continue
        if "limit" in d and "passed" in d:   # only real grade records
            rows.append(d)
    return rows


def fmt_table(title, models, limits, cell_fn):
    """cell_fn(model, limit) -> string. Returns list of text lines."""
    w = max([len(m) for m in models] + [12])
    head = f"{'model':<{w}}" + "".join(f"{str(l)+'s':>12}" for l in limits)
    lines = [title, head, "-" * len(head)]
    for m in models:
        lines.append(f"{m:<{w}}" + "".join(f"{cell_fn(m, l):>12}" for l in limits))
    return lines


def summarize(rows, limits):
    # keys
    families = sorted({r["family"] for r in rows})
    crits    = sorted({r["crit"] for r in rows})
    models   = sorted({r["model"] for r in rows})

    # agg[(fam,crit,model,limit)] = [sum_passed, sum_total, n_statements]
    agg = defaultdict(lambda: [0, 0, 0])
    for r in rows:
        k = (r["family"], r["crit"], r["model"], r["limit"])
        agg[k][0] += r["passed"]; agg[k][1] += r["total"]; agg[k][2] += 1
    # overall (across families) keyed (crit,model,limit)
    oall = defaultdict(lambda: [0, 0, 0])
    for (fam, crit, model, limit), (p, t, n) in agg.items():
        o = oall[(crit, model, limit)]; o[0] += p; o[1] += t; o[2] += n

    lines = []
    out_json = {"per_family": {}, "overall": {}}

    def pct_cell(get):
        def f(m, l):
            p, t, n = get(m, l)
            return f"{(100*p/t):.1f}% ({p}/{t})" if t else "-"
        return f

    def avg_cell(get):
        def f(m, l):
            p, t, n = get(m, l)
            return f"{(p/n):.1f}" if n else "-"
        return f

    for fam in families:
        for crit in crits:
            present = [m for m in models if any((fam, crit, m, l) in agg for l in limits)]
            if not present:
                continue
            get = lambda m, l: agg[(fam, crit, m, l)]
            hdr = f"\n############### FAMILY {fam}  ({CRIT_LABEL.get(crit, crit)}) ###############"
            lines.append(hdr)
            lines += fmt_table("(A) PASS %  (test cases passed / tried)", present, limits, pct_cell(get))
            lines.append("")
            lines += fmt_table("(B) AVG test cases passed per statement", present, limits, avg_cell(get))
            out_json["per_family"].setdefault(fam, {})[crit] = {
                m: {str(l): {"passed": agg[(fam, crit, m, l)][0],
                             "total": agg[(fam, crit, m, l)][1],
                             "statements": agg[(fam, crit, m, l)][2]} for l in limits}
                for m in present}

    for crit in crits:
        present = [m for m in models if any((crit, m, l) in oall for l in limits)]
        if not present:
            continue
        get = lambda m, l: oall[(crit, m, l)]
        lines.append(f"\n=============== OVERALL — ALL FAMILIES ({CRIT_LABEL.get(crit, crit)}) ===============")
        lines += fmt_table("(A) PASS %  (test cases passed / tried)", present, limits, pct_cell(get))
        lines.append("")
        lines += fmt_table("(B) AVG test cases passed per statement", present, limits, avg_cell(get))
        out_json["overall"][crit] = {
            m: {str(l): {"passed": oall[(crit, m, l)][0], "total": oall[(crit, m, l)][1],
                         "statements": oall[(crit, m, l)][2]} for l in limits}
            for m in present}

    return "\n".join(lines), out_json


def main():
    rows = load()
    if not rows:
        print("no grades yet under", GRADES); return
    limits = sorted({r["limit"] for r in rows})
    text, js = summarize(rows, limits)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary.json").write_text(json.dumps(js, indent=2))
    print(f"\nsaved -> {REPORTS/'summary.md'}  and  {REPORTS/'summary.json'}")


if __name__ == "__main__":
    main()
