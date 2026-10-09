#!/usr/bin/env python3
"""Teacher driver: generate statement *versions* from an open-ended plan.

`versions_per_criterion` is a TARGET the planner fills from four sources in priority
order (strategies/PLAN.md):
  1 grid        - every applicable (strategy, intensity) pair, one sample each
  2 sample      - extra samples from used cells (distinct sub-seed), round-robin
  3 composition - compatible strategy pairs applied together (moderate/aggressive)
  4 generation  - derive from an already-accepted (gate PASS) version, capped by
                  max_generation. Runs as a SECOND pass (needs gate results).

Output goes to agentic/versions/, never to dataset/. v000 is the seed (baseline).

CLI: python tools/generate_versions.py --family 01|all [--criterion 1] \
        [--sources grid,sample,composition | --sources generation] [--n N] [--dry-run] [--reset]
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import backends as B

_INTENSITY_ORDER = ["light", "moderate", "aggressive"]
_ALL_SOURCES = ["grid", "sample", "composition", "generation"]


def parse_tagged_statement(text: str) -> dict:
    """Parse the teacher's tag-delimited reply (<STATEMENT>...</STATEMENT> etc.).

    Tag-delimited is far more reliable than JSON for multi-line markdown statements.
    Salvage: if <STATEMENT> is present but its closing tag was truncated, take the rest
    of the text. A reply is usable as long as `statement` is non-empty.
    """
    text = B.strip_thinking(text or "")

    def grab(tag):
        m = re.search(rf"<{tag}>\s*(.*?)</{tag}>", text, re.DOTALL | re.IGNORECASE)
        return m.group(1).strip() if m else ""

    stmt = grab("STATEMENT")
    if not stmt:  # truncated close tag -> take everything after <STATEMENT>
        m = re.search(r"<STATEMENT>\s*(.*)", text, re.DOTALL | re.IGNORECASE)
        if m:
            stmt = re.split(r"</?[A-Z_]+>", m.group(1))[0].strip()
    return {"statement": stmt, "rationale": grab("RATIONALE"),
            "preserved_answer": grab("PRESERVED_ANSWER"),
            "preserved_class": grab("PRESERVED_CLASS"), "risk": grab("RISK")}


# --- library ----------------------------------------------------------------
def load_strategies() -> list[dict]:
    strats = []
    for p in sorted(B.STRATEGIES_DIR.glob("S*.md")):
        lines = p.read_text().splitlines()
        header, i = {}, 0
        while i < len(lines) and lines[i].strip():
            if ":" in lines[i]:
                k, _, v = lines[i].partition(":")
                header[k.strip().lower()] = v.strip()
            i += 1
        sid = header.get("id", p.stem.split("_")[0])
        strats.append({
            "id": sid,
            "summary": header.get("summary", ""),
            "name": f"{sid} — {header.get('summary', '')}",
            "classes": [c.strip() for c in header.get("classes", "all").split(",")],
            "requires_feedback": header.get("requires", "").strip().lower() == "feedback",
            "instruction": "\n".join(lines[i:]).strip(),
            "file": p.name,
        })
    strats.sort(key=lambda s: s["id"])
    return strats


def load_intensities() -> dict:
    text = (B.STRATEGIES_DIR / "INTENSITY.md").read_text()
    out = {}
    for name in _INTENSITY_ORDER:
        m = re.search(rf"\*\*{name}\*\*\s*[—-]\s*(.*?)(?=\n\*\*|\Z)", text, re.DOTALL | re.IGNORECASE)
        out[name] = m.group(1).strip() if m else ""
    return out


def applicable_strategies(seed_class, strategies, allow_feedback=False):
    return [s for s in strategies
            if ("all" in s["classes"] or seed_class in s["classes"])
            and (allow_feedback or not s["requires_feedback"])]


# --- sources 1-3 ------------------------------------------------------------
def _spec(source, strategies, intensity, base_stmt, parent="seed", generation=0, sub_seed=0):
    return {"source": source, "strategies": strategies, "intensity": intensity,
            "base_statement": base_stmt, "parent": parent, "generation": generation,
            "sub_seed": sub_seed}


def grid_specs(applicable, seed_stmt, base_seed):
    return [_spec("grid", [s], inten, seed_stmt, sub_seed=base_seed)
            for inten in _INTENSITY_ORDER for s in applicable]


def sample_specs(applicable, seed_stmt, base_seed, stride, needed):
    cells = [(s, inten) for inten in _INTENSITY_ORDER for s in applicable]
    out, k = [], 0
    while len(out) < needed and cells:
        s, inten = cells[k % len(cells)]
        sub = base_seed + (k // len(cells) + 1) * stride
        out.append(_spec("sample", [s], inten, seed_stmt, sub_seed=sub))
        k += 1
    return out


def composition_specs(applicable, seed_stmt, base_seed, needed):
    pairs = []
    for i in range(len(applicable)):
        for j in range(i + 1, len(applicable)):
            a, b = applicable[i], applicable[j]
            if {a["id"], b["id"]} == {"S04", "S05"}:   # mutually exclusive
                continue
            pairs.append((a, b))
    out, k, comp_int = [], 0, ["moderate", "aggressive"]
    while len(out) < needed and pairs:
        a, b = pairs[k % len(pairs)]
        inten = comp_int[(k // len(pairs)) % 2]
        out.append(_spec("composition", [a, b], inten, seed_stmt, sub_seed=base_seed))
        k += 1
    return out


def generation_specs(out_base, applicable, max_gen, base_seed):
    if max_gen <= 0:
        return []
    parents = []
    for vdir in sorted(out_base.glob("v*")):
        gate = _read_json(vdir / "gate.json")
        edit = _read_json(vdir / "edit.json")
        if gate.get("result") in ("ACCEPT", "PASS") and edit.get("generation", 0) < max_gen \
                and (vdir / "statement.md").exists():
            parents.append((vdir.name, edit.get("generation", 0),
                            (vdir / "statement.md").read_text()))
    out = []
    for i, (pid, gen, pstmt) in enumerate(parents):
        strat = applicable[i % len(applicable)]
        out.append(_spec("generation", [strat], "moderate", pstmt,
                         parent=pid, generation=gen + 1, sub_seed=base_seed + i))
    return out


# --- rendering / io ---------------------------------------------------------
def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text)
    os.replace(tmp, path)


def _meta_fields(meta_text: str) -> dict:
    import yaml
    m = yaml.safe_load(meta_text) or {}
    return {"class": m.get("class", "?"),
            "intended_algorithm": m.get("intended_algorithm", ""),
            "reduction_note": m.get("reduction_note", "")}


def compose(strategies: list[dict]):
    if len(strategies) == 1:
        s = strategies[0]
        return s["name"], s["instruction"]
    names = " + ".join(s["id"] for s in strategies)
    instr = "Apply both of the following, in combination:\n\n" + \
            "\n\n".join(s["instruction"] for s in strategies)
    return f"{names} (combined)", instr


def render_user(tmpl, base_stmt, meta, strat_name, strat_instr, intensity, intensity_text):
    return (tmpl.replace("{SEED_STATEMENT}", base_stmt)
            .replace("{CLASS}", meta["class"])
            .replace("{INTENDED_ALGORITHM}", meta["intended_algorithm"])
            .replace("{REDUCTION_NOTE}", meta["reduction_note"])
            .replace("{STRATEGY_NAME}", strat_name)
            .replace("{STRATEGY_INSTRUCTION}", strat_instr)
            .replace("{INTENSITY}", intensity)
            .replace("{INTENSITY_INSTRUCTION}", intensity_text)
            .replace("{FEEDBACK_BLOCK}", ""))


def _max_version_num(out_base: Path) -> int:
    nums = [int(m.group(1)) for p in out_base.glob("v*")
            if (m := re.match(r"v(\d+)$", p.name))]
    return max(nums) if nums else 0


def emit(vdir, spec, system, user_tmpl, meta, intensities, teacher, run_cfg,
         exec_cfg, dry_run, family, criterion):
    strat_name, strat_instr = compose(spec["strategies"])
    user = render_user(user_tmpl, spec["base_statement"], meta, strat_name, strat_instr,
                       spec["intensity"], intensities.get(spec["intensity"], ""))
    if dry_run:
        print(f"\n===== {vdir.name}  source={spec['source']} "
              f"strategies={[s['id'] for s in spec['strategies']]} "
              f"intensity={spec['intensity']} parent={spec['parent']} =====")
        print("--- SYSTEM ---\n" + system + "\n--- USER ---\n" + user)
        return "DRY"

    resp = B.chat(teacher, system, user,
                  timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=exec_cfg.get("retries", 3))
    parsed = parse_tagged_statement(resp["text"])
    if not parsed.get("statement"):
        resp = B.chat(teacher, system,
                      user + "\n\nUse the <STATEMENT>...</STATEMENT> tag format exactly.",
                      timeout=run_cfg.get("request_timeout_s", 1800),
                      retries=exec_cfg.get("retries", 3))
        parsed = parse_tagged_statement(resp["text"])

    new_statement = (parsed.get("statement") or resp["text"]).strip()
    _atomic_write(vdir / "statement.md", new_statement + "\n")
    _atomic_write(vdir / "edit.json", json.dumps({
        "version": vdir.name,
        "family": family,
        "criterion": criterion,
        "source": spec["source"],
        "strategies": [s["id"] for s in spec["strategies"]],
        "intensity": spec["intensity"],
        "parent": spec["parent"],
        "generation": spec["generation"],
        "sub_seed": spec["sub_seed"],
        "rationale": parsed.get("rationale", ""),
        "preserved_answer": parsed.get("preserved_answer", ""),
        "preserved_class": parsed.get("preserved_class", ""),
        "risk": parsed.get("risk", ""),
        "teacher_id": teacher["id"],
        "teacher_raw": resp["text"],
        "parse_ok": bool(parsed.get("statement")),
        "error": resp["error"],
        "elapsed_s": resp["elapsed_s"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }, indent=2))
    return "ERR" if resp["error"] or not parsed.get("statement") else "GEN"


def run_criterion(family, criterion, sources, args, run_cfg, models, strategies, intensities):
    teacher = models["teacher"]
    exec_cfg = models.get("execution", {})
    slug = B.family_slug(family)
    crit_dir = B.criterion_dirname(criterion)
    seed_crit = B.SEEDS_DIR / slug / crit_dir
    if not (seed_crit / "statement.md").exists():
        print(f"  [warn] seed missing at {seed_crit}; run tools/seed.py --family {family}",
              file=sys.stderr)
        return

    seed_stmt = (seed_crit / "statement.md").read_text()
    meta = _meta_fields((seed_crit / "meta.yaml").read_text())
    base_seed = run_cfg.get("seed", 7)
    stride = run_cfg.get("samples_seed_stride", 1000)
    target = args.n if args.n is not None else run_cfg.get("versions_per_criterion", 40)
    comp_enabled = run_cfg.get("composition_enabled", True)
    max_gen = run_cfg.get("max_generation", 2)
    applicable = applicable_strategies(meta["class"], strategies, allow_feedback=False)

    system = (B.PROMPTS_DIR / "teacher_system.md").read_text()
    user_tmpl = (B.PROMPTS_DIR / "teacher_user_template.md").read_text()
    out_base = B.VERSIONS_DIR / f"family_{family}" / crit_dir
    out_base.mkdir(parents=True, exist_ok=True)

    # Source 1 (grid) fills first. The remainder up to the target is filled by
    # interleaving composition (bounded, higher-value pairs) and sample (unbounded
    # diversity draws) so BOTH sources actually contribute -- otherwise the
    # unbounded sample source would starve composition and the per-source rollup
    # would be meaningless. Generation is a separate second pass (below).
    grid_sample_comp = []
    if "grid" in sources:
        grid_sample_comp += grid_specs(applicable, seed_stmt, base_seed)
    grid_sample_comp = grid_sample_comp[:target]

    remaining = target - len(grid_sample_comp)
    if remaining > 0:
        comp_pool = (composition_specs(applicable, seed_stmt, base_seed, remaining)
                     if ("composition" in sources and comp_enabled) else [])
        sample_pool = (sample_specs(applicable, seed_stmt, base_seed, stride, remaining)
                       if "sample" in sources else [])
        ci = si = 0
        take_comp = True
        while len(grid_sample_comp) < target and (ci < len(comp_pool) or si < len(sample_pool)):
            if take_comp and ci < len(comp_pool):
                grid_sample_comp.append(comp_pool[ci]); ci += 1
            elif si < len(sample_pool):
                grid_sample_comp.append(sample_pool[si]); si += 1
            elif ci < len(comp_pool):
                grid_sample_comp.append(comp_pool[ci]); ci += 1
            else:
                break
            take_comp = not take_comp

    numbered = [(f"v{i:03d}", spec) for i, spec in enumerate(grid_sample_comp, start=1)]

    # source 4 appends after the current highest version number
    if "generation" in sources:
        gen = generation_specs(out_base, applicable, max_gen, base_seed)
        start = max(_max_version_num(out_base), len(grid_sample_comp))
        numbered += [(f"v{start + i:03d}", spec) for i, spec in enumerate(gen, start=1)]

    print(f"[generate] family={family} {crit_dir} class={meta['class']} "
          f"target={target} sources={sorted(sources)} planned={len(numbered)} dry_run={args.dry_run}")
    counts = {}
    for vid, spec in numbered:
        vdir = out_base / vid
        if (vdir / "statement.md").exists() and (vdir / "statement.md").stat().st_size > 0 \
                and not args.reset and not args.dry_run:
            print(f"  [skip] {vid}")
            continue
        tag = emit(vdir, spec, system, user_tmpl, meta, intensities, teacher, run_cfg,
                   exec_cfg, args.dry_run, family, criterion)
        counts[tag] = counts.get(tag, 0) + 1
        if not args.dry_run:
            print(f"  [{tag}] {vid} source={spec['source']} "
                  f"strategies={[s['id'] for s in spec['strategies']]} "
                  f"intensity={spec['intensity']} parent={spec['parent']}")
    print(f"[generate] family={family} {crit_dir} -> {counts}")


def main():
    # Make piping the dry-run into `head`/`less` clean (no BrokenPipeError traceback).
    try:
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)   # id or 'all'
    ap.add_argument("--criterion", type=int, choices=[1, 2])
    ap.add_argument("--sources", default="grid,sample,composition")
    ap.add_argument("--n", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()

    sources = {s.strip() for s in args.sources.split(",") if s.strip()}
    bad = sources - set(_ALL_SOURCES)
    if bad:
        print(f"ERROR: unknown sources {bad}; choose from {_ALL_SOURCES}", file=sys.stderr)
        sys.exit(1)

    run_cfg = B.load_run_config()
    models = B.load_models()
    strategies = load_strategies()
    intensities = load_intensities()

    crits = [args.criterion] if args.criterion else run_cfg.get("criteria", [1, 2])
    for family in B.list_families(args.family):
        for c in crits:
            run_criterion(family, c, sources, args, run_cfg, models, strategies, intensities)
    print("[generate] done.")


if __name__ == "__main__":
    main()
