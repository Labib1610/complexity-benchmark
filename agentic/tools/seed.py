#!/usr/bin/env python3
"""Copy a family's seed problem from dataset/ into agentic/seeds/.

Two tiers are copied from dataset/ (file 48):
  - anchor  : small original cases 01-04  -> seeds/<slug>/<crit>/tests/
  - scaled  : Phase-2 large cases 05+     -> seeds/<slug>/<crit>/tests_scaled/
The third tier (corner) is produced later by gen_tests.py into the universal
store and is NOT copied here. tests/ stays anchor-only so the gate's reference
check and seed_criterion() see only the small, hand-verifiable cases.
Read-only on dataset/.

Usage: python tools/seed.py --family 01
"""
import argparse
import shutil
import sys
from pathlib import Path

import backends as B

SMALL_CASES = {"01", "02", "03", "04"}
SCALED_DIRNAME = "tests_scaled"
COPY_FILES = ["statement.md", "meta.yaml", "reference.py", "validator.py"]


def copy_family(family: str) -> None:
    slug = None
    src_family = sorted((B.ROOT / "dataset").glob(f"family_{family}_*"))
    if not src_family:
        print(f"ERROR: no dataset/family_{family}_* found", file=sys.stderr)
        sys.exit(1)
    src_family = src_family[0]
    slug = src_family.name
    dst_family = B.SEEDS_DIR / slug

    print(f"Seeding {slug} -> agentic/seeds/{slug} (small cases {sorted(SMALL_CASES)} only)")
    for crit in sorted(src_family.glob("criterion_*")):
        dst_crit = dst_family / crit.name
        (dst_crit / "tests").mkdir(parents=True, exist_ok=True)

        for fname in COPY_FILES:
            s = crit / fname
            if s.exists():
                shutil.copy2(s, dst_crit / fname)

        copied = 0
        for stem in sorted(SMALL_CASES):
            for ext in (".in", ".out"):
                s = crit / "tests" / f"{stem}{ext}"
                if s.exists():
                    shutil.copy2(s, dst_crit / "tests" / f"{stem}{ext}")
            if (dst_crit / "tests" / f"{stem}.in").exists():
                copied += 1
        # guard: make sure no large case sneaked into the anchor tier
        strays = [p.name for p in (dst_crit / "tests").glob("*.in")
                  if p.stem not in SMALL_CASES]
        if strays:
            print(f"  WARNING removing non-small cases from anchor tier: {strays}")
            for p in strays:
                (dst_crit / "tests" / p).unlink(missing_ok=True)

        # scaled tier: every dataset case NOT in the anchor set (05, 06, ...),
        # into a separate dir so it never pollutes tests/. Absent for criteria
        # that Phase 2 never scaled -- that is fine, just copy zero.
        scaled_dir = dst_crit / SCALED_DIRNAME
        scaled = 0
        for s in sorted((crit / "tests").glob("*.in")):
            if s.stem in SMALL_CASES:
                continue
            out = s.with_suffix(".out")
            if not out.exists():
                continue
            scaled_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(s, scaled_dir / s.name)
            shutil.copy2(out, scaled_dir / out.name)
            scaled += 1
        print(f"  {crit.name}: {copied} anchor + {scaled} scaled test case(s) copied")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)   # id or 'all'
    args = ap.parse_args()
    if args.family == "all":
        families = [d.name.split("_")[1] for d in sorted((B.ROOT / "dataset").glob("family_*"))]
    else:
        families = [args.family]
    for fam in families:
        copy_family(fam)
    print("Done. dataset/ was not modified.")


if __name__ == "__main__":
    main()
