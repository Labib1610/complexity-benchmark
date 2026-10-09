#!/usr/bin/env python3
"""Adversarial corner-case test generation -> universal per-problem test store.

The teacher proposes edge-case INPUTS that might break a naive or shortcut solution
(minimum sizes, boundary values, ties/lexicographic edges, degenerate structure). The
seed's own reference.py -- which is correct -- is run on each to produce the TRUE
output. Valid, de-duplicated cases are saved under:

    agentic/tests/family_XX/criterion_n/NN.in , NN.out

shared by ALL versions of that problem (same task, same reference). run_students scores
students on these IN ADDITION to the seed's small tests.

Cases are requested in a tag-delimited format (raw stdin between <case>...</case>) --
far more reliable for multi-line stdin than JSON with escaped newlines -- and the author
runs at low temperature. Anything the reference rejects (bad format/bounds, or too slow)
is discarded, so only valid cases survive.

CLI: python tools/gen_tests.py --family 01 [--criterion 1] [--n 12] [--dry-run] [--reset]
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import backends as B
import generate_versions as GV

_SYSTEM = (
    "You are a test designer for a programming problem. You are given the exact problem "
    "statement (with its input format and bounds) and, privately, its intended algorithm. "
    "Produce adversarial INPUT cases that a correct solution must handle but a shortcut or "
    "naive one is likely to get wrong: minimum sizes, boundary values, ties and "
    "lexicographic-tie-break edges, degenerate structure, and corners of the intended "
    "algorithm. Keep every input SMALL and compact (at most ~15 lines each); do NOT emit "
    "maximum-size or stress-test inputs -- this is about correctness corners, not speed. "
    "Every input MUST obey the stated input format and bounds exactly.\n\n"
    "Output ONLY the cases. Wrap each case's raw stdin exactly between <case> and </case> "
    "tags, with the literal input lines (real newlines) in between and nothing else. "
    "Example of the required output shape:\n"
    "<case>\n3 0\n</case>\n<case>\n4 1\n1 2\n</case>"
)

_CASE_RE = re.compile(r"<case>\s*\n?(.*?)</case>", re.DOTALL | re.IGNORECASE)


def _parse_cases(text: str) -> list[str]:
    """Preferred: <case>...</case> blocks. Fallback: a JSON {"cases":[{"input":...}]}."""
    blocks = [m.group(1) for m in _CASE_RE.finditer(text)]
    inputs = [b.strip("\n") for b in blocks if b.strip()]
    if inputs:
        return inputs
    # fallback for models that still answered in JSON
    parsed = B.extract_json(text)
    if isinstance(parsed, dict):
        out = []
        for c in parsed.get("cases", []):
            s = (c.get("input") if isinstance(c, dict) else "") or ""
            if s.strip():
                out.append(s.strip("\n"))
        if out:
            return out
    # last resort: salvage any "input": "..." string values
    out = []
    for m in re.finditer(r'"input"\s*:\s*("(?:[^"\\]|\\.)*")', text, re.DOTALL):
        try:
            out.append(json.loads(m.group(1)).strip("\n"))
        except Exception:
            pass
    return out


def _run_reference(ref_path: Path, stdin_text: str, timeout: float = 30.0):
    try:
        p = subprocess.run([sys.executable, str(ref_path)], input=stdin_text.encode(),
                           capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, "timeout"
    if p.returncode != 0:
        return None, (p.stderr.decode()[:200] or "nonzero exit")
    return p.stdout.decode(), None


def _next_num(tests_dir: Path) -> int:
    nums = [int(p.stem) for p in tests_dir.glob("*.in") if p.stem.isdigit()]
    return (max(nums) + 1) if nums else 1


def gen_for_criterion(family, criterion, args, run_cfg, models):
    author = dict(models["teacher"])     # copy so we can lower the temperature
    author["temperature"] = 0.2          # deterministic, format-compliant
    exec_cfg = models.get("execution", {})
    slug = B.family_slug(family)
    crit_dir = B.criterion_dirname(criterion)
    seed_dir = B.SEEDS_DIR / slug / crit_dir
    statement = (seed_dir / "statement.md").read_text()
    meta = GV._meta_fields((seed_dir / "meta.yaml").read_text())
    ref_path = seed_dir / "reference.py"

    store = B.TESTS_DIR / f"family_{family}" / crit_dir
    store.mkdir(parents=True, exist_ok=True)
    if args.reset:
        for p in list(store.glob("*.in")) + list(store.glob("*.out")):
            p.unlink(missing_ok=True)
    existing = {hashlib.sha1(p.read_bytes()).hexdigest() for p in store.glob("*.in")}

    user = (f"PROBLEM STATEMENT:\n{statement}\n\n"
            f"HIDDEN (do not reveal): intended algorithm = {meta['intended_algorithm']}\n\n"
            f"Produce {args.n} adversarial input cases, each wrapped in <case>...</case>.")
    print(f"[gen_tests] family={family} {crit_dir} class={meta['class']} want={args.n} "
          f"dry_run={args.dry_run}")
    if args.dry_run:
        print("--- SYSTEM ---\n" + _SYSTEM + "\n--- USER (head) ---\n" + user[:800])
        return

    resp = B.chat(author, _SYSTEM, user, timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=exec_cfg.get("retries", 3))
    (store / "author_raw.txt").write_text(resp["text"] or "")
    cases = _parse_cases(resp["text"] or "")
    if not cases:
        head = (resp["text"] or "").strip()[:300].replace("\n", " ")
        print(f"  [warn] no parseable cases (error={resp['error']}). "
              f"raw saved to {store/'author_raw.txt'} | head: {head!r}")
        return

    kept, rejected, provenance = 0, 0, []
    for stdin_text in cases:
        if not stdin_text.endswith("\n"):
            stdin_text += "\n"
        h = hashlib.sha1(stdin_text.encode()).hexdigest()
        if h in existing:
            continue
        out, err = _run_reference(ref_path, stdin_text)     # reference = ground truth
        if out is None:
            rejected += 1
            continue
        existing.add(h)
        num = _next_num(store)
        (store / f"{num:02d}.in").write_text(stdin_text)
        (store / f"{num:02d}.out").write_text(out)
        provenance.append({"case": f"{num:02d}", "author": author["id"]})
        kept += 1
    (store / "provenance.json").write_text(json.dumps({
        "family": family, "criterion": criterion, "author": author["id"],
        "kept": kept, "rejected": rejected,
        "timestamp": datetime.now(timezone.utc).isoformat(), "cases": provenance,
    }, indent=2))
    print(f"  kept {kept} valid adversarial case(s), rejected {rejected} "
          f"(bad format/bounds or too slow) -> {store}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--criterion", type=int, choices=[1, 2])
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()

    run_cfg = B.load_run_config()
    models = B.load_models()
    crits = [args.criterion] if args.criterion else run_cfg.get("criteria", [1, 2])
    for family in B.list_families(args.family):
        for c in crits:
            gen_for_criterion(family, c, args, run_cfg, models)
    print("[gen_tests] done.")


if __name__ == "__main__":
    main()
