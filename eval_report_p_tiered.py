#!/usr/bin/env python3
"""
P report in the TEST -> WORST -> OVERALL pattern (companion to eval_report_tiered.py).

Same tiering and equal-weight average as the NPC tiered report, but P has no limit
sweep: each statement is judged at its own stated limit, so there is a single table
per family.

  TEST %    = cases passed / tried in the NORMAL tier (anchor + scaled + others)
  WORST %   = cases passed / tried in the WORST tier  (name starts "worst_" or numeric >= 16)
  OVERALL % = (TEST % + WORST %) / 2

Reads evaluation/grades_p/**/result.json. Safe any time.
    python eval_report_p_tiered.py
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


def pct(p, t):
    return (100.0 * p / t) if t else None


def trio(np_, nt, wp, wt):
    tn, tw = pct(np_, nt), pct(wp, wt)
    ts = f"{tn:.1f}% ({np_}/{nt})" if tn is not None else "-"
    ws = f"{tw:.1f}% ({wp}/{wt})" if tw is not None else "-"
    parts = [x for x in (tn, tw) if x is not None]
    os = f"{(sum(parts)/len(parts)):.1f}%" if parts else "-"
    return ts, ws, os


def block(title, models, get):
    w = max([len(m) for m in models] + [12])
    head = f"{'model':<{w}}{'TEST%':>20}{'WORST%':>20}{'OVERALL%':>12}"
    lines = [title, head, "-" * len(head)]
    for m in models:
        ts, ws, os = trio(*get(m))
        lines.append(f"{m:<{w}}{ts:>20}{ws:>20}{os:>12}")
    return lines


def main():
    rows = load()
    if not rows:
        print("no P grades yet under", GRADES); return
    families = sorted({r["family"] for r in rows})
    models = sorted({r["model"] for r in rows})
    agg = defaultdict(lambda: [0, 0, 0, 0])   # (fam,model) -> [n_pass,n_tot,w_pass,w_tot]
    for r in rows:
        a = agg[(r["family"], r["model"])]
        for c in r.get("cases", []):
            if tier(c["name"]) == "worst":
                a[3] += 1; a[2] += int(bool(c["pass"]))
            else:
                a[1] += 1; a[0] += int(bool(c["pass"]))
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
        lines += block("OVERALL = avg of TEST% and WORST%", present, lambda m, fam=fam: agg[(fam, m)])
        lines.append("")
        out_json["per_family"][fam] = {
            m: dict(zip(("normal_pass", "normal_total", "worst_pass", "worst_total"), agg[(fam, m)]))
            for m in present}
    present = [m for m in models if m in oall]
    lines.append("\n=============== OVERALL — ALL FAMILIES (P) ===============")
    lines += block("OVERALL = avg of TEST% and WORST%", present, lambda m: oall[m])
    out_json["overall"] = {
        m: dict(zip(("normal_pass", "normal_total", "worst_pass", "worst_total"), oall[m]))
        for m in present}

    text = "\n".join(lines)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary_p_tiered.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary_p_tiered.json").write_text(json.dumps(out_json, indent=2))
    print(f"\nsaved -> {REPORTS/'summary_p_tiered.md'}  and  {REPORTS/'summary_p_tiered.json'}")


if __name__ == "__main__":
    main()
