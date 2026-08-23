#!/usr/bin/env python3
"""Unit tests for H2 bound extraction/normalization (gate.py).

Regression guard for the two H2 bugs:
  1. large + scientific/LaTeX bounds must parse to the same value as their plain form;
  2. the SEED and the REWRITE must go through the identical extraction path -- the seed
     writes `2·10⁵` with a Unicode middle-dot and a superscript ⁵ (no caret), which must
     still parse to 200000, not 2.

Run:  python3 tools/test_gate_bounds.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gate as G  # noqa: E402

HERE = Path(__file__).resolve().parents[1]
SEED = HERE / "seeds" / "family_01_graph_coloring" / "criterion_2_p" / "statement.md"


def test_all_forms_parse_to_200000():
    forms = ["200000", "200,000", "2·10^5", r"2 \times 10^5", r"2 \cdot 10^5",
             "2e5", "2E5", "2 * 10^5", r"2\times10^{5}", r"$2 \cdot 10^5$",
             "2·10⁵", "2×10⁵", "10⁵ times 2 no"[:3]]  # includes superscript forms
    for f in ["200000", "200,000", "2·10^5", r"2 \times 10^5", r"2 \cdot 10^5",
              "2e5", "2E5", "2 * 10^5", r"2\times10^{5}", r"$2 \cdot 10^5$",
              "2·10⁵", "2×10⁵", "2\\cdot10⁵"]:
        got = G._parse_number(G._preclean(f))
        assert got == 200000, f"{f!r} -> {got}, expected 200000"
    # bare superscript power
    assert G._parse_number(G._preclean("10⁵")) == 100000


def test_seed_bound_parses_to_200000():
    """The seed's 2·10⁵ must parse to 200000, NOT 2 (the original bug)."""
    stmt = SEED.read_text()
    inp, out = G._section(stmt, "Input"), G._section(stmt, "Output")
    vals = G.bound_values(inp + "\n" + out)
    assert 200000 in vals, f"seed bound_values={sorted(vals)} missing 200000"
    assert 2 not in vals, f"seed bound_values={sorted(vals)} wrongly contains 2 (mantissa)"


def test_seed_and_latex_rewrite_agree():
    """Same value written the seed way vs the LaTeX way must compare equal under H2."""
    seed_line = "## Input\n1 ≤ n ≤ 2·10⁵, 0 ≤ m ≤ 2·10⁵\n## Output\nprint YES"
    new_line = "## Input\n1 ≤ n ≤ 2\\cdot 10^5, 0 ≤ m ≤ 2 \\times 10^{5}\n## Output\nprint YES"
    res = G.check_io_contract(seed_line, new_line)
    assert res["pass"], f"H2 should pass; detail={res['detail']} " \
                        f"seed={res['bounds_seed']} new={res['bounds_new']}"


def test_dropped_bound_still_rejected():
    # subset semantics: changing 2*10^5 -> 3*10^5 drops the seed value 200000 -> reject
    res = G.check_io_contract("## Input\n1 ≤ n ≤ 2·10⁵\n## Output\nx",
                              "## Input\n1 ≤ n ≤ 3·10^5\n## Output\nx")
    assert not res["pass"] and "200000" in res["detail"], res["detail"]


def test_added_bound_allowed():
    # subset semantics: making an implicit index range explicit is faithful -> accept
    res = G.check_io_contract("## Input\n3 ≤ n ≤ 2000\n## Output\nx",
                              "## Input\n3 ≤ n ≤ 2000, 1 ≤ u, v ≤ n\n## Output\nx")
    assert res["pass"], res["detail"]


def test_prose_bound_captured():
    # "at most / capacity of / limit of" with digit numbers must be captured
    vals = G.bound_values("headcount is at least 3 and never exceeds a maximum "
                          "capacity of exactly 2000 workers; limit of 200,000")
    assert {3, 2000, 200000} <= vals, sorted(vals)


def test_equation_rhs_not_a_bound():
    # '=' in a domain equation must NOT be captured as a bound
    vals = G.bound_values("two integers u v (1 ≤ u, v ≤ n) with x_u + x_v = 3")
    assert 3 not in vals, sorted(vals)


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"  ok: {t.__name__}")
    print(f"[test_gate_bounds] {len(tests)} tests passed")
