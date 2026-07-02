"""Dataset discovery layer — reads the on-disk layout, no model knowledge."""

from __future__ import annotations

import glob
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class TestCase:
    name: str
    in_path: Path
    out_path: Path


@dataclass
class Criterion:
    family_id: str
    criterion_id: str
    dir: Path
    meta: dict
    statement_path: Path
    reference_path: Path
    tests: list[TestCase]
    validator_path: Path | None


@dataclass
class Family:
    family_id: str
    dir: Path
    meta: dict
    criteria: list[Criterion]


def _load_meta(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def discover_criteria(family_dir: Path) -> list[Criterion]:
    criteria = []
    for cdir in sorted(family_dir.glob("criterion_*")):
        if not cdir.is_dir():
            continue
        meta_path = cdir / "meta.yaml"
        meta = _load_meta(meta_path) if meta_path.exists() else {}

        tests_dir = cdir / "tests"
        test_cases = []
        if tests_dir.exists():
            for in_path in sorted(tests_dir.glob("*.in")):
                out_path = in_path.with_suffix(".out")
                test_cases.append(TestCase(
                    name=in_path.stem,
                    in_path=in_path,
                    out_path=out_path,
                ))

        validator_path = cdir / "validator.py"
        criteria.append(Criterion(
            family_id=family_dir.name,
            criterion_id=cdir.name,
            dir=cdir,
            meta=meta,
            statement_path=cdir / "statement.md",
            reference_path=cdir / "reference.py",
            tests=test_cases,
            validator_path=validator_path if validator_path.exists() else None,
        ))
    return criteria


def discover_families(dataset_dir: Path | str) -> list[Family]:
    dataset_dir = Path(dataset_dir)
    families = []
    for fdir in sorted(dataset_dir.glob("family_*")):
        if not fdir.is_dir():
            continue
        criteria = discover_criteria(fdir)
        # Use meta from first criterion as family-level meta if available
        family_meta = criteria[0].meta if criteria else {}
        families.append(Family(
            family_id=fdir.name,
            dir=fdir,
            meta=family_meta,
            criteria=criteria,
        ))
    return families


def iter_problems(dataset_dir: Path | str):
    """Yield every Criterion across all families."""
    for family in discover_families(dataset_dir):
        for criterion in family.criteria:
            yield criterion
