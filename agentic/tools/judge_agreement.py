#!/usr/bin/env python3
"""Inter-judge agreement on the graded criteria (file 50, PART B7).

Re-judges a stratified random sample of versions (stratified by strategy, intensity, and
composite-score band) with two ADDITIONAL judges from different providers, temperature 0,
using the same verifier prompt. Together with the original verifier score stored in each
gate.json, that gives up to three raters per criterion. Computes pairwise quadratic-
weighted Cohen's kappa and the unanimous-agreement rate. Writes reports/judge_agreement.json.

This also mitigates the current same-provider exposure (teacher and verifier are both
Gemini): the added judges should be chosen from other providers.

  python tools/judge_agreement.py --family 01 --sample 100 --judges <id1> <id2>
"""
import argparse
import json
import random
from pathlib import Path

import backends as B
import gate as GT

REPORT = B.REPORTS_DIR / "judge_agreement.json"
_CRITS = ["G1_unambiguity", "G2_completeness", "G3_faithfulness", "G4_naturalness"]


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def resolve_model(models: dict, mid: str) -> dict | None:
    for key in ("teacher", "verifier"):
        if models.get(key, {}).get("id") == mid:
            return models[key]
    for group in ("students", "solvers", "judges"):
        for m in models.get(group, []) or []:
            if m.get("id") == mid:
                return m
    return None


def _band(composite) -> str:
    if not isinstance(composite, (int, float)):
        return "na"
    if composite < 3.0:
        return "<3"
    if composite < 4.0:
        return "3-4"
    if composite < 4.5:
        return "4-4.5"
    return ">=4.5"


def collect_sample(family, criterion, n, seed=13):
    """Stratified sample across (strategy, intensity, composite band)."""
    strata = {}
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
            if not gate or not (vdir / "statement.md").exists():
                continue
            key = ("+".join(edit.get("strategies", []) or []) or "-",
                   edit.get("intensity", "") or "-", _band(gate.get("composite")))
            strata.setdefault(key, []).append((cd, vdir, gate))
    rng = random.Random(seed)
    for v in strata.values():
        rng.shuffle(v)
    # round-robin across strata until we have n
    picked, keys = [], list(strata.keys())
    rng.shuffle(keys)
    i = 0
    while len(picked) < n and any(strata.values()):
        k = keys[i % len(keys)]
        if strata[k]:
            picked.append(strata[k].pop())
        i += 1
        if i > n * 20:
            break
    return picked


def weighted_kappa(a, b, k=6):
    """Quadratic-weighted Cohen's kappa over ordinal categories 0..k-1."""
    pairs = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    if not pairs:
        return None
    n = len(pairs)
    O = [[0.0] * k for _ in range(k)]
    for x, y in pairs:
        O[x][y] += 1
    row = [sum(O[i]) for i in range(k)]
    col = [sum(O[i][j] for i in range(k)) for j in range(k)]
    W = [[((i - j) ** 2) / ((k - 1) ** 2) for j in range(k)] for i in range(k)]
    num = sum(W[i][j] * O[i][j] for i in range(k) for j in range(k))
    den = sum(W[i][j] * row[i] * col[j] / n for i in range(k) for j in range(k))
    if den == 0:
        return 1.0
    return round(1 - num / den, 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2, 3])
    ap.add_argument("--sample", type=int, default=100)
    ap.add_argument("--judges", nargs="+", required=True, help="two+ model ids, diff providers")
    args = ap.parse_args()

    models = B.load_models()
    run_cfg = B.load_run_config()
    verifier_system = (B.PROMPTS_DIR / "verifier_system.md").read_text()
    verifier_user_tmpl = (B.PROMPTS_DIR / "verifier_user_template.md").read_text()

    judge_cfgs = []
    for mid in args.judges:
        cfg = resolve_model(models, mid)
        if cfg is None:
            raise SystemExit(f"judge model {mid!r} not found in models.yaml")
        judge_cfgs.append(cfg)

    for family in B.list_families(args.family):
        slug = B.family_slug(family)
        sample = collect_sample(family, args.criterion, args.sample)
        rater_ids = [models["verifier"]["id"]] + [c["id"] for c in judge_cfgs]
        # scores[criterion] -> list over units of [r0, r1, r2]
        scores = {c: [] for c in _CRITS}
        n_units = 0
        for cd, vdir, gate in sample:
            sc = GT.seed_criterion(slug, cd)
            if sc is None:
                continue
            seed_stmt = sc.statement_path.read_text()
            cand = (vdir / "statement.md").read_text()
            # rater 0 = original verifier score already in gate.json
            row_by_crit = {c: [gate.get("graded", {}).get(c, {}).get("score")] for c in _CRITS}
            user = verifier_user_tmpl.replace("{SEED}", seed_stmt).replace("{CANDIDATE}", cand)
            for jc in judge_cfgs:
                resp = B.chat(jc, verifier_system, user,
                              timeout=run_cfg.get("request_timeout_s", 1800),
                              retries=models.get("execution", {}).get("retries", 3))
                g = GT._parse_graded(resp["text"])
                for c in _CRITS:
                    row_by_crit[c].append(g.get(c, {}).get("score"))
            for c in _CRITS:
                scores[c].append(row_by_crit[c])
            n_units += 1
            print(f"  judged {family}/{cd}/{vdir.name} ({n_units}/{len(sample)})")

        # pairwise kappa per criterion + unanimous rate
        per_crit = {}
        n_r = len(rater_ids)
        for c in _CRITS:
            rows = scores[c]
            kappas = {}
            for i in range(n_r):
                for j in range(i + 1, n_r):
                    a = [r[i] for r in rows]
                    b = [r[j] for r in rows]
                    kappas[f"{rater_ids[i]}|{rater_ids[j]}"] = weighted_kappa(a, b)
            unanim = sum(1 for r in rows
                         if all(x is not None for x in r) and len(set(r)) == 1)
            valid = sum(1 for r in rows if all(x is not None for x in r))
            per_crit[c] = {"pairwise_weighted_kappa": kappas,
                           "unanimous_rate": round(unanim / valid, 4) if valid else None,
                           "n_complete": valid}

        out = {"family": family, "criterion": args.criterion, "n_units": n_units,
               "raters": rater_ids, "per_criterion": per_crit}
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(out, indent=2))
        print(f"[judge_agreement] family_{family}: {n_units} units, raters={rater_ids}")
        for c in _CRITS:
            print(f"  {c}: unanimous={per_crit[c]['unanimous_rate']} "
                  f"kappa={per_crit[c]['pairwise_weighted_kappa']}")


if __name__ == "__main__":
    main()
