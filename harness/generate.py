"""Phase-2 driver: generate model solutions for every (model, problem) pair.

Usage:
  python -m harness.generate --config runs/<date>_<name>/run_config.yaml [options]

Options:
  --only <model_id>   Run a single model from the registry.
  --reset             Ignore existing checkpoints and re-generate.
  --sample <n>        Limit to first n problems (smoke-test mode).
  --seed <n>          Random seed (recorded in gen_meta; not used yet).
  --dry-run           Instead of calling a backend, copy reference.py as solution.py.
                      Use with evaluate to confirm the full pipeline produces PASS.

Study variants (set study: in run_config.yaml):
  main          Default — one generation per (model, problem).
  token_budget  Sweeps token levels from run_config token_budget.levels;
                writes to generations/<model>/__tok<level>/... per level.
  time_budget   Same generation as main; runtime enforcement is in evaluate.
  multiturn     Delegated to harness/multiturn.py at evaluate time.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent

# Fixed prompt — mirrors conventions/prompt_template.md exactly.
_SYSTEM = (
    "You are an expert competitive programmer. You write correct, efficient Python 3\n"
    "solutions. Your program reads all input from standard input and writes only the\n"
    "required answer to standard output. Output only a single Python 3 code block and\n"
    "nothing else — no explanation before or after."
)

_USER_TMPL = (
    "Solve the following problem in Python 3.\n\n"
    "{STATEMENT}\n\n"
    "Requirements:\n"
    "- Read from standard input, write to standard output.\n"
    "- Output only the answer in the exact format specified.\n"
    "- Return only one Python 3 code block."
)


# ── helpers ───────────────────────────────────────────────────────────────────

def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.parent / f".tmp_{path.name}"
    try:
        tmp.write_text(text, encoding="utf-8")
        tmp.rename(path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def _load_registry(registry_path: Path) -> dict[str, dict]:
    raw = yaml.safe_load(registry_path.read_text())
    return {m["id"]: m for m in raw["models"]}


def _resolve_problems(dataset_dir: Path, families_filter, criteria_filter):
    from harness.dataset import iter_problems
    problems = list(iter_problems(dataset_dir))

    if families_filter != "all":
        allowed = {str(f).zfill(2) for f in families_filter}
        problems = [p for p in problems if p.meta.get("family", "") in allowed]

    if criteria_filter != "all":
        allowed = {int(c) for c in criteria_filter}
        problems = [p for p in problems if p.meta.get("criterion") in allowed]

    return problems


def _gen_dir(run_dir: Path, model_id: str, criterion, tok_level=None) -> Path:
    base = run_dir / "generations" / model_id
    if tok_level is not None:
        base = base / f"__tok{tok_level}"
    return base / criterion.family_id / criterion.criterion_id


def _prompt_hash(system: str, user: str) -> str:
    return hashlib.sha256((system + user).encode()).hexdigest()[:16]


# ── main ──────────────────────────────────────────────────────────────────────

def main(argv=None):
    parser = argparse.ArgumentParser(description="Phase-2: generate model solutions")
    parser.add_argument("--config", required=True, help="Path to run_config.yaml")
    parser.add_argument("--only", default=None, help="Restrict to one model id")
    parser.add_argument("--reset", action="store_true", help="Ignore checkpoints")
    parser.add_argument("--sample", type=int, default=None, help="Limit to first N problems")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (recorded only)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Copy reference.py instead of calling a backend (for pipeline tests)")
    args = parser.parse_args(argv)

    run_dir = Path(args.config).parent
    config = yaml.safe_load(Path(args.config).read_text())
    registry = _load_registry(ROOT / "models" / "registry.yaml")
    dataset_dir = ROOT / "dataset"

    # Resolve model list
    model_ids = [args.only] if args.only else config.get("models", list(registry.keys()))
    models = []
    for mid in model_ids:
        if mid not in registry:
            print(f"[generate] WARNING: model {mid!r} not in registry — skipping", file=sys.stderr)
            continue
        models.append(registry[mid])

    # Resolve problem list
    problems = _resolve_problems(
        dataset_dir,
        config.get("families", "all"),
        config.get("criteria", "all"),
    )

    # Skip problems with placeholder references (NotImplementedError families)
    ready = []
    for p in problems:
        if not p.reference_path.exists():
            continue
        if "NotImplementedError" in p.reference_path.read_text():
            continue
        ready.append(p)

    if args.sample:
        ready = ready[: args.sample]

    temperature = config.get("generation", {}).get("temperature", 0.2)
    seed = args.seed if args.seed is not None else config.get("seed", 0)
    study = config.get("study", "main")

    # Token-budget sweep: collect levels; other studies use a single None-level pass.
    if study == "token_budget":
        tok_levels = config.get("token_budget", {}).get("levels", [4096])
        _min_thinking_budget = 1024
        for model in models:
            if model.get("thinking"):
                for lv in tok_levels:
                    if lv < _min_thinking_budget:
                        print(
                            f"[generate] WARNING: level {lv} is below {_min_thinking_budget} "
                            f"for thinking model {model['id']} — output may be truncated",
                            file=sys.stderr,
                        )
    else:
        tok_levels = [None]

    print(f"[generate] run={run_dir.name}  study={study}  models={len(models)}"
          f"  problems={len(ready)}  dry-run={args.dry_run}"
          + (f"  tok_levels={tok_levels}" if study == "token_budget" else ""))

    for tok_level in tok_levels:
        for model in models:
            mid = model["id"]
            effective_budget = tok_level if tok_level is not None else model.get("token_budget", 4096)

            for criterion in ready:
                out_dir = _gen_dir(run_dir, mid, criterion, tok_level)
                solution_path = out_dir / "solution.py"

                if (solution_path.exists() and solution_path.stat().st_size > 0
                        and not args.reset):
                    label = f"__tok{tok_level}/" if tok_level else ""
                    print(f"  [skip] {mid}/{label}{criterion.family_id}/{criterion.criterion_id}")
                    continue

                statement = criterion.statement_path.read_text()
                user_msg = _USER_TMPL.replace("{STATEMENT}", statement)

                t0 = time.monotonic()

                if args.dry_run:
                    raw = criterion.reference_path.read_text()
                    code = raw
                else:
                    from harness.backends import generate
                    from harness.extract import extract_code, strip_thinking
                    raw = generate(
                        backend=model["backend"],
                        model_string=model["model_string"],
                        system=_SYSTEM,
                        user=user_msg,
                        max_tokens=effective_budget,
                        temperature=temperature,
                        thinking=model.get("thinking", False),
                    )
                    if model.get("thinking"):
                        raw_stripped = strip_thinking(raw)
                    else:
                        raw_stripped = raw
                    code = extract_code(raw_stripped)

                elapsed = time.monotonic() - t0

                _atomic_write(solution_path, code)
                _atomic_write(out_dir / "raw.txt", raw)
                _atomic_write(out_dir / "gen_meta.json", json.dumps({
                    "model_id": mid,
                    "family_id": criterion.family_id,
                    "criterion_id": criterion.criterion_id,
                    "prompt_hash": _prompt_hash(_SYSTEM, user_msg),
                    "token_budget": effective_budget,
                    "tok_level": tok_level,
                    "temperature": temperature,
                    "seed": seed,
                    "elapsed_s": round(elapsed, 3),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "dry_run": args.dry_run,
                    "study": study,
                }, indent=2))

                tag = "DRY" if args.dry_run else "GEN"
                level_tag = f"[tok={tok_level}] " if tok_level else ""
                print(f"  [{tag}] {level_tag}{mid}/{criterion.family_id}/{criterion.criterion_id}"
                      f"  ({elapsed:.1f}s)")

    print("[generate] done.")


if __name__ == "__main__":
    main()
