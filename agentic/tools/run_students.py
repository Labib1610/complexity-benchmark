#!/usr/bin/env python3
"""Student driver: each enabled student attempts each surviving version.

For every (version, student): send the FIXED student prompt with that version's
statement, save solution.py + raw.txt + trace.txt, and score with the existing
harness checker against the seed's small tests. Version v000 is the unmodified seed
(the baseline).

Concurrency (config/models.yaml execution): API students run up to api_max_workers
concurrently; Ollama students run sequentially while ollama_parallel is false. Flip
the flag and raise ollama_max_workers to parallelize -- no code change needed.

CLI: python tools/run_students.py --family 01 [--criterion 1] [--only <student_id>]
"""
import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import backends as B

from harness.checker import judge_problem
from harness.dataset import discover_criteria, TestCase

_THINK = re.compile(r"<think(?:ing)?>(.*?)</think(?:ing)?>", re.DOTALL | re.IGNORECASE)

_FALLBACK_STUDENT_SYSTEM = (
    "You are an expert competitive programmer. Read the problem and output a single "
    "self-contained Python 3 solution that reads stdin and writes stdout. Put the "
    "code in one ```python fenced block.")
_FALLBACK_STUDENT_USER = "{STATEMENT}\n\nWrite the complete Python 3 solution."


def _load_prompt(name, fallback):
    p = B.PROMPTS_DIR / name
    return p.read_text() if p.exists() else fallback


def seed_criteria_map(family, slug):
    """Seed criteria, each augmented with the universal adversarial tests (if any),
    so students are scored on the small seed cases AND the generated corner cases."""
    m = {c.criterion_id: c for c in discover_criteria(B.SEEDS_DIR / slug)}
    for cd, c in m.items():
        store = B.TESTS_DIR / f"family_{family}" / cd
        if not store.exists():
            continue
        for inp in sorted(store.glob("*.in")):
            outp = inp.with_suffix(".out")
            if outp.exists():
                c.tests.append(TestCase(name="u" + inp.stem, in_path=inp, out_path=outp))
    return m


def gate_ok(vdir: Path) -> bool:
    g = vdir / "gate.json"
    if not g.exists():
        return True  # not yet gated -> attempt anyway
    try:
        return json.loads(g.read_text()).get("result") not in ("FAIL", "REJECT")
    except json.JSONDecodeError:
        return True


def build_tasks(family, criterion, slug, seedmap):
    """Yield (crit_dir, seed_crit, version_id, statement_text, version_dir_or_None)."""
    base = B.VERSIONS_DIR / f"family_{family}"
    crit_dirs = [B.criterion_dirname(criterion)] if criterion else \
        [c for c in seedmap.keys()]
    for cd in crit_dirs:
        sc = seedmap.get(cd)
        if sc is None:
            continue
        # v000 baseline = the unmodified seed statement
        yield cd, sc, "v000", sc.statement_path.read_text(), None
        cbase = base / cd
        if cbase.exists():
            for vdir in sorted(cbase.glob("v*")):
                stmt = vdir / "statement.md"
                if stmt.exists() and gate_ok(vdir):
                    yield cd, sc, vdir.name, stmt.read_text(), vdir


def attempt(task, student, sys_tmpl, user_tmpl, run_cfg, exec_cfg):
    cd, sc, vid, statement, _ = task
    out_dir = B.ATTEMPTS_DIR / f"family_{_family}" / cd / vid / student["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    if (out_dir / "verdict.json").exists() and not _reset:
        return f"[skip] {cd}/{vid}/{student['id']}"

    user = user_tmpl.replace("{STATEMENT}", statement)
    resp = B.chat(student, sys_tmpl, user,
                  timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=exec_cfg.get("retries", 3))
    raw = resp["text"]
    (out_dir / "raw.txt").write_text(raw)
    tr = "\n\n".join(m.group(1).strip() for m in _THINK.finditer(raw))
    (out_dir / "trace.txt").write_text(tr)
    code = B.extract_code(raw)
    sol = out_dir / "solution.py"
    sol.write_text(code)

    if resp["error"] or not code.strip():
        verdict = {"overall": "RUNTIME_ERROR", "cases": [], "n_cases": 0,
                   "n_passed": 0, "error": resp["error"] or "empty solution",
                   **B.usage_of(resp)}
    else:
        pv = judge_problem(sc, sol)
        verdict = {
            "overall": pv.overall,
            "cases": [{"name": c.name, "verdict": c.verdict} for c in pv.cases],
            "n_cases": len(pv.cases),
            "n_passed": sum(1 for c in pv.cases if c.verdict == "PASS"),
            "error": resp["error"],
            **B.usage_of(resp),   # input/output/thinking tokens, cost, elapsed_s
        }
    (out_dir / "verdict.json").write_text(json.dumps(verdict, indent=2))
    return f"[{verdict['overall']}] {cd}/{vid}/{student['id']}"


_family = None    # set per family in main so attempt() can build the output path
_reset = False    # when True, ignore existing verdict.json and re-run


def main():
    global _family, _reset
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)   # id or 'all'
    ap.add_argument("--criterion", type=int, choices=[1, 2, 3])
    ap.add_argument("--only")
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--workers", type=int, default=None,
                    help="override concurrency (use 1 to respect free-tier rate limits)")
    args = ap.parse_args()
    _reset = args.reset

    models = B.load_models()
    run_cfg = B.load_run_config()
    exec_cfg = models.get("execution", {})

    students = [s for s in models["students"] if s.get("enabled", True)]
    if args.only:
        students = [s for s in students if s["id"] == args.only]
    api_students = [s for s in students if s["backend"] == "openai_compat"]
    ollama_students = [s for s in students if s["backend"] == "ollama"]

    sys_tmpl = _load_prompt("student_system.md", _FALLBACK_STUDENT_SYSTEM)
    user_tmpl = _load_prompt("student_user_template.md", _FALLBACK_STUDENT_USER)

    def run_group(group_students, tasks, workers):
        jobs = [(t, s) for s in group_students for t in tasks]
        if workers <= 1:
            for t, s in jobs:
                print("  " + attempt(t, s, sys_tmpl, user_tmpl, run_cfg, exec_cfg))
        else:
            with ThreadPoolExecutor(max_workers=workers) as ex:
                futs = [ex.submit(attempt, t, s, sys_tmpl, user_tmpl, run_cfg, exec_cfg)
                        for t, s in jobs]
                for f in futs:
                    print("  " + f.result())

    if args.workers is not None:
        api_workers = ollama_workers = max(1, args.workers)
    else:
        api_workers = exec_cfg.get("api_max_workers", 1) if exec_cfg.get("api_parallel") else 1
        ollama_workers = exec_cfg.get("ollama_max_workers", 1) if exec_cfg.get("ollama_parallel") else 1

    for family in B.list_families(args.family):
        _family = family
        slug = B.family_slug(family)
        seedmap = seed_criteria_map(family, slug)
        tasks = list(build_tasks(family, args.criterion, slug, seedmap))
        print(f"[students] family_{family} ({slug})  versions*students="
              f"{len(tasks)}x{len(students)}  (api={len(api_students)}, ollama={len(ollama_students)})")
        run_group(api_students, tasks, api_workers)      # API: concurrent if enabled
        run_group(ollama_students, tasks, ollama_workers)  # Ollama: sequential unless flipped
    print("[students] done.")


if __name__ == "__main__":
    main()
