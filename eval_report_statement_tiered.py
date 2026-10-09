#!/usr/bin/env python3
"""
NPC report: STATEMENT-level pass rate, split by tier (TEST -> WORST -> OVERALL).

A statement is counted as "solved" in a tier iff the model clears ALL of that tier's
test cases for that statement:
  - TEST  tier = NORMAL cases (anchor + scaled + corner + seed)   -> statement solved if all pass
  - WORST tier = cases named "worst_*" or numeric >= 16           -> statement solved if all pass

Per model (per family and OVERALL, per time limit):
  TEST %    = statements fully solved on NORMAL cases / statements that have NORMAL cases
  WORST %   = statements fully solved on WORST  cases / statements that have WORST  cases
  OVERALL % = (TEST % + WORST %) / 2     (equal weight; if a family has no worst tier,
                                          OVERALL = TEST % and WORST shows '-')

NOTE: families 02 (sat), 05 (3-D matching), 09 (clique/IS) have NO packaged worst-tier
test files (their worst tier was a separate planted-witness probe, not .in/.out files),
so their WORST column is '-'. 01/14/16/17-22 have a packaged worst tier.

Reads evaluation/grades/**/*.json. Safe any time.
    python eval_report_statement_tiered.py
"""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
OUT  = ROOT.parent / "evaluation"
GRADES = OUT / "grades"
REPORTS = OUT / "reports"
CRIT_LABEL = {"1": "NPC", "2": "P"}


def tier(name):
    if name.startswith("worst_"):
        return "worst"
    if name.isdigit():
        return "worst" if int(name) >= 16 else "normal"
    return "normal"


def load():
    rows = []
    for jf in GRADES.glob("**/*.json"):
        if jf.name.endswith(".fail.json"):
            continue
        try:
            d = json.loads(jf.read_text())
        except Exception:
            continue
        if "limit" in d and "cases" in d:
            rows.append(d)
    return rows


def stmt_tiers(cases):
    """Return (has_normal, normal_solved, has_worst, worst_solved) for one statement."""
    nrm = [c for c in cases if tier(c["name"]) == "normal"]
    wst = [c for c in cases if tier(c["name"]) == "worst"]
    ns = bool(nrm) and all(c["pass"] for c in nrm)
    ws = bool(wst) and all(c["pass"] for c in wst)
    return bool(nrm), ns, bool(wst), ws


def trio(nsolved, ndenom, wsolved, wdenom):
    tn = (100.0 * nsolved / ndenom) if ndenom else None
    tw = (100.0 * wsolved / wdenom) if wdenom else None
    ts = f"{tn:.1f}% ({nsolved}/{ndenom})" if tn is not None else "-"
    ws = f"{tw:.1f}% ({wsolved}/{wdenom})" if tw is not None else "-"
    parts = [x for x in (tn, tw) if x is not None]
    os = f"{(sum(parts)/len(parts)):.1f}%" if parts else "-"
    return ts, ws, os


def block(title, models, get):
    w = max([len(m) for m in models] + [12])
    head = f"{'model':<{w}}{'TEST% (stmts)':>22}{'WORST% (stmts)':>22}{'OVERALL%':>12}"
    lines = [title, head, "-" * len(head)]
    for m in models:
        ts, ws, os = trio(*get(m))
        lines.append(f"{m:<{w}}{ts:>22}{ws:>22}{os:>12}")
    return lines


def main():
    rows = load()
    if not rows:
        print("no grades yet under", GRADES); return
    limits = sorted({r["limit"] for r in rows})
    families = sorted({r["family"] for r in rows})
    crits = sorted({r["crit"] for r in rows})
    models = sorted({r["model"] for r in rows})

    # agg[(fam,crit,model,limit)] = [n_solved, n_denom, w_solved, w_denom]
    agg = defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        hn, ns, hw, ws = stmt_tiers(r["cases"])
        a = agg[(r["family"], r["crit"], r["model"], r["limit"])]
        if hn: a[1] += 1; a[0] += int(ns)
        if hw: a[3] += 1; a[2] += int(ws)
    oall = defaultdict(lambda: [0, 0, 0, 0])
    for (fam, crit, m, lim), v in agg.items():
        o = oall[(crit, m, lim)]
        for i in range(4): o[i] += v[i]

    lines = []
    out_json = {"per_family": {}, "overall": {}}
    for fam in families:
        for crit in crits:
            present = [m for m in models if any((fam, crit, m, l) in agg for l in limits)]
            if not present:
                continue
            lines.append(f"\n############### FAMILY {fam}  ({CRIT_LABEL.get(crit, crit)}) ###############")
            for lim in limits:
                lines += block(f"-- {lim}s --  statements fully solved per tier (OVERALL = avg of TEST% & WORST%)",
                               present, lambda m, lim=lim, fam=fam, crit=crit: agg[(fam, crit, m, lim)])
                lines.append("")
            out_json["per_family"].setdefault(fam, {})[crit] = {
                m: {str(l): dict(zip(("normal_solved", "normal_stmts", "worst_solved", "worst_stmts"),
                                     agg[(fam, crit, m, l)])) for l in limits} for m in present}

    for crit in crits:
        present = [m for m in models if any((crit, m, l) in oall for l in limits)]
        if not present:
            continue
        lines.append(f"\n=============== OVERALL — ALL FAMILIES ({CRIT_LABEL.get(crit, crit)}) ===============")
        for lim in limits:
            lines += block(f"-- {lim}s --  statements fully solved per tier (OVERALL = avg of TEST% & WORST%)",
                           present, lambda m, lim=lim, crit=crit: oall[(crit, m, lim)])
            lines.append("")
        out_json["overall"][crit] = {
            m: {str(l): dict(zip(("normal_solved", "normal_stmts", "worst_solved", "worst_stmts"),
                                 oall[(crit, m, l)])) for l in limits} for m in present}

    text = "\n".join(lines)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary_statement_tiered.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary_statement_tiered.json").write_text(json.dumps(out_json, indent=2))
    print(f"\nsaved -> {REPORTS/'summary_statement_tiered.md'}  and  {REPORTS/'summary_statement_tiered.json'}")


if __name__ == "__main__":
    main()
