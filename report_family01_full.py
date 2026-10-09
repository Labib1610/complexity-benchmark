#!/usr/bin/env python3
"""Per-criterion report for family 01: test cases -> worst case -> overall, all six models.
- 'test cases' = pass rate over all hardened statement-variants (verdict.json case-level).
- 'worst case' = the worst-case tier built under dataset/.../{worstcase,adversarial}, graded now.
Run after run_frontier_variants.py has populated the frontier verdict.json files.
"""
import json, subprocess, sys, importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ATT = ROOT / "agentic/attempts/family_01"
STU = ["gpt-oss-120b", "qwen3-coder", "deepseek-v4-flash", "glm-5"]
FRONT = ["gpt-5.6-sol", "gemini-3.7-flash-frontier"]
ALL = STU + FRONT
CR = [("criterion_1_npc", "C1 NPC", 2.0),
      ("criterion_2_p", "C2 P", 1.0),
      ("criterion_3_infeasible", "C3 Infeasible", 2.0)]
FSOL = Path("/tmp/claude-1000/-home-labib-Desktop-labib-codes-research-codes-np-completeness/"
            "be21154c-a603-4a78-9e3e-e4be864e11ad/scratchpad")  # frontier worst-case solutions

_CACHE = ROOT / ".worstcase_grade_cache.json"
def _load_cache():
    try:
        return json.loads(_CACHE.read_text())
    except Exception:
        return {}
def _save_cache(d):
    _CACHE.write_text(json.dumps(d))

def hardening(c, m):
    p = t = 0
    for vd in sorted((ATT / c).glob("v*")):
        vj = vd / m / "verdict.json"
        if not vj.exists():
            continue
        for case in json.loads(vj.read_text()).get("cases", []):
            t += 1
            p += case.get("verdict") == "PASS"
    return p, t

def norm(s): return "\n".join(l.rstrip() for l in s.strip().split("\n"))

def load_validator(c):
    vp = ROOT / f"dataset/family_01_graph_coloring/{c}/validator.py"
    if not vp.exists():
        return None
    spec = importlib.util.spec_from_file_location("_v", vp)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def worstcase(c, m, lim):
    """Grade the worst-case + adversarial tiers. C1 uses witness grading (tools/worstcase_coloring),
    C2/C3 use exact-match vs reference .out."""
    base = ROOT / f"dataset/family_01_graph_coloring/{c}"
    dirs = [d for d in (base / "worstcase", base / "adversarial") if d.exists()]
    cases = sorted(x for d in dirs for x in d.glob("*.in"))
    if not cases:
        return 0, 0
    # locate solution
    if m in STU:
        sol = ATT / c / "v000" / m / "solution.py"
    else:
        tagmap = {"criterion_1_npc": "wc", "criterion_2_p": "c2c3sol", "criterion_3_infeasible": "c2c3sol"}
        if c == "criterion_1_npc":
            sol = FSOL / "wc" / f"{m}_sol.py"
        else:
            tag = "c2" if c == "criterion_2_p" else "c3"
            sol = FSOL / "c2c3sol" / f"{tag}_{m}.py"
    if not sol.exists():
        return None
    sys.path.insert(0, str(ROOT / "tools"))
    import worstcase_coloring as WC
    cache = _load_cache()
    p = t = 0
    dirty = False
    for f in cases:
        t += 1
        key = f"{c}|{m}|{f.parent.name}/{f.name}"
        if key in cache:
            p += cache[key]; continue
        inp = f.read_text()
        try:
            out = subprocess.run([sys.executable, str(sol)], input=inp,
                                 capture_output=True, text=True, timeout=lim).stdout
            if c == "criterion_1_npc" and (f.parent.name == "worstcase"):
                ok, _ = WC.grade(inp, out); ok = bool(ok)
            else:
                ok = norm(out) == norm(f.with_suffix(".out").read_text())
        except subprocess.TimeoutExpired:
            ok = False
        cache[key] = int(ok); dirty = True; p += ok
        if len(cache) % 25 == 0:
            _save_cache(cache)
    if dirty:
        _save_cache(cache)
    return p, t

for c, label, lim in CR:
    print(f"\n===== {label} =====")
    print(f"{'model':<22}{'test cases':>12}{'worst case':>12}{'OVERALL':>10}")
    print("-" * 56)
    for m in ALL:
        hp, ht = hardening(c, m)
        w = worstcase(c, m, lim)
        if ht == 0 and w is None:
            print(f"{m:<22}{'(no data)':>12}"); continue
        wp, wt = (w if w else (0, 0))
        tp, tt = hp + wp, ht + wt
        tc = f"{100*hp/ht:.1f}%" if ht else "n/a"
        wc_ = f"{100*wp/wt:.1f}%" if wt else "n/a"
        ov = f"{100*tp/tt:.1f}%" if tt else "n/a"
        print(f"{m:<22}{tc:>12}{wc_:>12}{ov:>10}   ({hp}/{ht} | {wp}/{wt})")
