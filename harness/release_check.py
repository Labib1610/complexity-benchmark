"""Automated release-acceptance gates (subset of the audit's gate list that is
machine-checkable *today*, without the dataset rebuild).

The audit (MD files/COMPLEXITY_BENCHMARK_AUDIT.md) lists 16 acceptance gates. Most require the
P1--P3 dataset/research rebuild (strong-baseline calibration, hidden generators, same-schema
pairs, independent oracles). A handful are pure code checks that can be enforced right now and
will *keep* the rebuild honest. This tool runs those and clearly reports the rest as pending.

Implemented here:
  G1  no evaluation path expands a declared task limit   (audit B1, gate 1)   -- static assert
  G2  no PASS exceeds the effective limit                (audit B1, gate 2)   -- scans a results dir
  G7  a constant output cannot pass an INFEASIBLE arm    (audit B5, gate 7)   -- live probe
  G9  no exact duplicate inputs across the dataset       (audit B6, gate 9)   -- sha256 audit
  G16 generated code is sandboxed                        (audit B10, gate 16) -- live escape probe

Reported-but-not-automatable (need the rebuild): gates 3,4,5,6,8,10,11,12,13,14,15.

Usage:
  python -m harness.release_check                        # dataset gates (G1,G7,G9,G16)
  python -m harness.release_check --results runs/<run>/results/raw   # also G2 on a results dir
Exit code is nonzero if any implemented gate fails.
"""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent

from harness.checker import judge_problem, normalize          # noqa: E402
from harness.dataset import iter_problems                     # noqa: E402


# ── G1: the tightening rule is present in the single choke point ────────────────
def gate_g1_limit_tightening() -> tuple[bool, list[str]]:
    """Static guard: judge_problem must tighten (min) by default; only the oracle may expand."""
    import inspect
    from harness import checker
    src = inspect.getsource(checker.judge_problem)
    ok = ("min(declared, timeout_override)" in src) and ("allow_expand" in src)
    msgs = [] if ok else ["judge_problem no longer enforces min(declared, override) — B1 regressed"]
    return ok, msgs


# ── G2: no recorded PASS ran past the effective limit ──────────────────────────
def gate_g2_no_overlimit_pass(results_dir: Path) -> tuple[bool, list[str]]:
    msgs: list[str] = []
    if not results_dir.exists():
        return True, [f"(skipped — no results dir at {results_dir})"]
    n_checked = 0
    for vf in sorted(results_dir.rglob("verdict.json")):
        data = json.loads(vf.read_text())
        eff = data.get("effective_limit_s")
        decl = data.get("declared_limit_s")
        if eff is None or decl is None:
            msgs.append(f"{vf}: missing declared/effective limit (pre-B1 record)")
            continue
        if eff > decl + 1e-9:
            msgs.append(f"{vf}: effective_limit {eff}s > declared {decl}s")
        for c in data.get("cases", []):
            n_checked += 1
            if c.get("verdict") == "PASS" and c.get("elapsed_s", 0) > eff + 1e-6:
                msgs.append(f"{vf}: PASS case {c.get('name')} at {c.get('elapsed_s')}s > limit {eff}s")
    ok = not msgs
    if ok:
        msgs.append(f"(checked {n_checked} PASS/case records — all within the effective limit)")
    return ok, msgs


# ── G7: a constant program must NOT pass an INFEASIBLE arm ──────────────────────
def gate_g7_constant_cannot_pass() -> tuple[bool, list[str]]:
    """For every INFEASIBLE criterion whose .out files are all identical, synthesize a program
    that prints exactly that constant and confirm judge_problem does NOT PASS it. A PASS means the
    arm is gameable by a constant (audit B5)."""
    msgs: list[str] = []
    gameable: list[str] = []
    checked = 0
    for crit in iter_problems(ROOT / "dataset"):
        if crit.meta.get("class") != "INFEASIBLE":
            continue
        outs = [tc.out_path.read_text() for tc in crit.tests if tc.out_path.exists()]
        if not outs:
            continue
        uniq = {normalize(o) for o in outs}
        if len(uniq) != 1:
            continue  # multiple certificate outputs — not trivially constant-gameable
        checked += 1
        constant = next(iter(uniq))
        with tempfile.TemporaryDirectory() as td:
            sol = Path(td) / "const_sol.py"
            # print the constant verbatim, ignoring stdin
            sol.write_text("import sys\nsys.stdin.read()\n"
                           f"print({constant!r})\n")
            v = judge_problem(crit, sol)
        if v.overall == "PASS":
            gameable.append(f"{crit.family_id}/{crit.criterion_id} (constant {constant!r} PASSES all tests)")
    if gameable:
        msgs.append(f"{len(gameable)} INFEASIBLE arm(s) are constant-gameable:")
        msgs.extend("    " + g for g in gameable)
    else:
        msgs.append(f"(checked {checked} all-constant INFEASIBLE arms — none passed by a constant)")
    return not gameable, msgs


# ── G9: no exact-duplicate inputs across the dataset ────────────────────────────
def gate_g9_no_duplicate_inputs() -> tuple[bool, list[str]]:
    by_hash: dict[str, list[str]] = defaultdict(list)
    total = 0
    for crit in iter_problems(ROOT / "dataset"):
        for tc in crit.tests:
            if tc.in_path.exists():
                total += 1
                h = hashlib.sha256(tc.in_path.read_bytes()).hexdigest()
                by_hash[h].append(str(tc.in_path.relative_to(ROOT)))
    dupes = {h: fs for h, fs in by_hash.items() if len(fs) > 1}
    msgs: list[str] = []
    n_dup_files = sum(len(fs) for fs in dupes.values())
    if dupes:
        msgs.append(f"{len(dupes)} duplicate-input group(s) covering {n_dup_files}/{total} files:")
        for h, fs in list(dupes.items())[:20]:
            msgs.append(f"    {h[:12]}: " + " , ".join(fs))
        if len(dupes) > 20:
            msgs.append(f"    ... and {len(dupes) - 20} more group(s)")
    else:
        msgs.append(f"(checked {total} inputs — no exact duplicates)")
    return not dupes, msgs


# ── G16: generated code cannot read cwd / secrets ───────────────────────────────
def gate_g16_sandbox() -> tuple[bool, list[str]]:
    import os
    from harness.runner import run_solution
    os.environ["RELEASE_CHECK_SECRET"] = "leak-canary"
    with tempfile.TemporaryDirectory() as td:
        probe = Path(td) / "escape.py"
        probe.write_text(
            "import os\n"
            "print('CWD_FILES', os.listdir('.'))\n"
            "print('HAS_SECRET', 'RELEASE_CHECK_SECRET' in os.environ)\n")
        r = run_solution(probe, "", 5, 256)
    msgs, ok = [], True
    if "HAS_SECRET True" in r.stdout:
        ok = False; msgs.append("environment secret leaked into the sandbox")
    if "CWD_FILES []" not in r.stdout:
        ok = False; msgs.append(f"working directory not isolated: {r.stdout.strip()}")
    if ok:
        msgs.append("(sandbox isolates cwd and scrubs environment)")
    return ok, msgs


_PENDING_GATES = {
    3:  "every optimization criterion has a tested feasibility parser + objective (needs objective.py)",
    4:  "each pair preserves schema/objective except one approved switch (needs pair rewrite + gate)",
    5:  "one task/IO schema per family (needs statement rewrite)",
    6:  "no criterion called NP-complete solely from a related task (needs metadata/label rework)",
    8:  "hidden tests generated after code freeze from multiple distributions (needs generators)",
    10: "two independent/proof-producing oracles agree on every scored case (needs 2nd oracle)",
    11: "hard tiers calibrated against optimized exact + heuristic portfolios (needs baselines)",
    12: "P tiers pass with a pre-registered timing margin (needs re-calibration)",
    13: "hardening requires zero current-panel passers within the limit (run harden_loop at scale)",
    14: "final models/generators/seeds untouched by development (process discipline)",
    15: "raw artifacts reproduce every reported number (needs sealed run + provenance)",
}


def main(argv=None) -> int:
    import argparse
    p = argparse.ArgumentParser(description="Run the machine-checkable release-acceptance gates.")
    p.add_argument("--results", default=None,
                   help="Path to a results/raw dir to run G2 (over-limit PASS scan).")
    args = p.parse_args(argv)

    checks = [
        ("G1  limit-tightening present (B1)", gate_g1_limit_tightening),
        ("G7  constant cannot pass INFEASIBLE (B5)", gate_g7_constant_cannot_pass),
        ("G9  no duplicate inputs (B6)", gate_g9_no_duplicate_inputs),
        ("G16 sandbox isolation (B10)", gate_g16_sandbox),
    ]
    if args.results:
        checks.insert(1, ("G2  no over-limit PASS (B1)",
                          lambda: gate_g2_no_overlimit_pass(Path(args.results))))

    failed = 0
    print("=" * 72)
    print("RELEASE CHECK — automatable acceptance gates")
    print("=" * 72)
    for label, fn in checks:
        ok, msgs = fn()
        print(f"\n[{'PASS' if ok else 'FAIL'}] {label}")
        for m in msgs:
            print(f"    {m}")
        if not ok:
            failed += 1

    print("\n" + "-" * 72)
    print("PENDING (require the P1–P3 rebuild — not automatable yet):")
    for n, desc in _PENDING_GATES.items():
        print(f"    gate {n:>2}: {desc}")

    print("\n" + "=" * 72)
    if failed:
        print(f"RESULT: {failed} implemented gate(s) FAILED.")
    else:
        print("RESULT: all implemented gates passed "
              "(pending gates still require the dataset rebuild).")
    print("=" * 72)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
