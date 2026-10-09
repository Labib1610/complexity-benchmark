#!/usr/bin/env python3
"""
P report: STATEMENT-level pass rate split by tier (TEST -> WORST -> OVERALL).
Companion to eval_report_statement_tiered.py; P has no limit sweep (one table/family).

A statement is "solved" in a tier iff the model clears ALL that tier's cases:
  TEST  tier = NORMAL cases (anchor + scaled + corner + seed)
  WORST tier = cases "worst_*" or numeric >= 16
  TEST %    = stmts solved on NORMAL / stmts with NORMAL
  WORST %   = stmts solved on WORST  / stmts with WORST
  OVERALL % = (TEST % + WORST %) / 2   (WORST '-' if the family has no worst tier)

Reads evaluation/grades_p/**/result.json. Safe any time.
    python eval_report_p_statement_tiered.py
"""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent
OUT  = ROOT.parent / "evaluation"
GRADES = OUT / "grades_p"
REPORTS = OUT / "reports"


def tier(name):
    if name.startswith("worst_"):
        return "worst"
    if name.isdigit():
        return "worst" if int(name) >= 16 else "normal"
    return "normal"


def load():
    rows = []
    for jf in GRADES.glob("**/result.json"):
        try:
            rows.append(json.loads(jf.read_text()))
        except Exception:
            pass
    return rows


def stmt_tiers(cases):
    nrm = [c for c in cases if tier(c["name"]) == "normal"]
    wst = [c for c in cases if tier(c["name"]) == "worst"]
    return bool(nrm), (bool(nrm) and all(c["pass"] for c in nrm)), \
           bool(wst), (bool(wst) and all(c["pass"] for c in wst))


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
        print("no P grades yet under", GRADES); return
    families = sorted({r["family"] for r in rows})
    models = sorted({r["model"] for r in rows})
    agg = defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        hn, ns, hw, ws = stmt_tiers(r.get("cases", []))
        a = agg[(r["family"], r["model"])]
        if hn: a[1] += 1; a[0] += int(ns)
        if hw: a[3] += 1; a[2] += int(ws)
    oall = defaultdict(lambda: [0, 0, 0, 0])
    for (fam, m), v in agg.items():
        o = oall[m]
        for i in range(4): o[i] += v[i]

    lines = []
    out_json = {"per_family": {}, "overall": {}}
    for fam in families:
        present = [m for m in models if (fam, m) in agg]
        if not present:
            continue
        lines.append(f"\n############### FAMILY {fam}  (P) ###############")
        lines += block("statements fully solved per tier (OVERALL = avg of TEST% & WORST%)",
                       present, lambda m, fam=fam: agg[(fam, m)])
        lines.append("")
        out_json["per_family"][fam] = {
            m: dict(zip(("normal_solved", "normal_stmts", "worst_solved", "worst_stmts"), agg[(fam, m)]))
            for m in present}
    present = [m for m in models if m in oall]
    lines.append("\n=============== OVERALL — ALL FAMILIES (P) ===============")
    lines += block("statements fully solved per tier (OVERALL = avg of TEST% & WORST%)",
                   present, lambda m: oall[m])
    out_json["overall"] = {
        m: dict(zip(("normal_solved", "normal_stmts", "worst_solved", "worst_stmts"), oall[m]))
        for m in present}

    text = "\n".join(lines)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary_p_statement_tiered.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary_p_statement_tiered.json").write_text(json.dumps(out_json, indent=2))
    print(f"\nsaved -> {REPORTS/'summary_p_statement_tiered.md'}  and  {REPORTS/'summary_p_statement_tiered.json'}")


if __name__ == "__main__":
    main()
