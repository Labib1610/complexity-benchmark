#!/usr/bin/env python3
"""
NPC report in the TEST -> WORST -> OVERALL pattern (the format used before).

Each test case is classified into a tier by its name:
  - WORST tier  : name starts with "worst_"  OR  a numeric name >= 16
                  (obscure families use 01..30; 16..30 are the worst/TLE tier).
  - NORMAL tier : everything else -- anchor + scaled + corner + seed
                  ("anchor+scaled and others").

For each model (per family and OVERALL, per time limit) it reports:
  TEST %    = cases passed / tried in the NORMAL tier   (micro-average over cases)
  WORST %   = cases passed / tried in the WORST  tier   (usually ~0)
  OVERALL % = (TEST % + WORST %) / 2                     (EQUAL-WEIGHT average)

This equal-weight average of the two tiers is the "overall" number from the earlier
reports; it stops the many easy anchor/scaled cases from drowning out the worst tier.

Reads evaluation/grades/**/*.json. Safe any time.
    python eval_report_tiered.py
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


def pct(p, t):
    return (100.0 * p / t) if t else None


def trio_cell(np_, nt, wp, wt):
    """Return (test_str, worst_str, overall_str)."""
    tn, tw = pct(np_, nt), pct(wp, wt)
    ts = f"{tn:.1f}% ({np_}/{nt})" if tn is not None else "-"
    ws = f"{tw:.1f}% ({wp}/{wt})" if tw is not None else "-"
    parts = [x for x in (tn, tw) if x is not None]
    os = f"{(sum(parts)/len(parts)):.1f}%" if parts else "-"
    return ts, ws, os


def fmt_block(title, models, agg_get):
    """agg_get(model) -> (np,nt,wp,wt). 3 columns: TEST / WORST / OVERALL."""
    w = max([len(m) for m in models] + [12])
    head = f"{'model':<{w}}{'TEST%':>20}{'WORST%':>20}{'OVERALL%':>12}"
    lines = [title, head, "-" * len(head)]
    for m in models:
        ts, ws, os = trio_cell(*agg_get(m))
        lines.append(f"{m:<{w}}{ts:>20}{ws:>20}{os:>12}")
    return lines


def main():
    rows = load()
    if not rows:
        print("no grades yet under", GRADES); return
    limits = sorted({r["limit"] for r in rows})
    families = sorted({r["family"] for r in rows})
    crits = sorted({r["crit"] for r in rows})
    models = sorted({r["model"] for r in rows})

    # agg[(fam,crit,model,limit)] = [normal_pass, normal_tot, worst_pass, worst_tot]
    agg = defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        k = (r["family"], r["crit"], r["model"], r["limit"])
        a = agg[k]
        for c in r["cases"]:
            if tier(c["name"]) == "worst":
                a[3] += 1; a[2] += int(bool(c["pass"]))
            else:
                a[1] += 1; a[0] += int(bool(c["pass"]))
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
                lines += fmt_block(f"-- time limit {lim}s --  (OVERALL = avg of TEST% and WORST%)",
                                   present, lambda m, lim=lim, fam=fam, crit=crit: agg[(fam, crit, m, lim)])
                lines.append("")
            out_json["per_family"].setdefault(fam, {})[crit] = {
                m: {str(l): dict(zip(("normal_pass", "normal_total", "worst_pass", "worst_total"),
                                     agg[(fam, crit, m, l)])) for l in limits} for m in present}

    for crit in crits:
        present = [m for m in models if any((crit, m, l) in oall for l in limits)]
        if not present:
            continue
        lines.append(f"\n=============== OVERALL — ALL FAMILIES ({CRIT_LABEL.get(crit, crit)}) ===============")
        for lim in limits:
            lines += fmt_block(f"-- time limit {lim}s --  (OVERALL = avg of TEST% and WORST%)",
                               present, lambda m, lim=lim, crit=crit: oall[(crit, m, lim)])
            lines.append("")
        out_json["overall"][crit] = {
            m: {str(l): dict(zip(("normal_pass", "normal_total", "worst_pass", "worst_total"),
                                 oall[(crit, m, l)])) for l in limits} for m in present}

    text = "\n".join(lines)
    print(text)
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "summary_tiered.md").write_text("```\n" + text + "\n```\n")
    (REPORTS / "summary_tiered.json").write_text(json.dumps(out_json, indent=2))
    print(f"\nsaved -> {REPORTS/'summary_tiered.md'}  and  {REPORTS/'summary_tiered.json'}")


if __name__ == "__main__":
    main()
