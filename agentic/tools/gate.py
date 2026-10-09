#!/usr/bin/env python3
"""Automated gate for generated statement versions (file 50, PART B).

Two-part scheme -- hard constraints (binary, fatal) and graded criteria (0-5,
thresholded). They measure different things and are never merged.

Hard constraints (H*, fatal on explicit failure):
  H1 example consistency  -- run reference.py on each example input in the rewritten
                             statement; its output must match the stated example output.
                             EXECUTED.
  H2 I/O contract         -- Input/Output sections present; every numeric bound and any
                             tie-break rule matches the seed (bounds compared numerically).
  H3 no class leakage     -- deterministic forbidden-term scan.
  H4 S09 constraint       -- only when S09 was used: evaluate the teacher's formal
                             constraint against every seed test input; any violation -> fail.
                             EXECUTED (small constraint grammar).
  H5 solver round-trip    -- give the rewrite to a strong solver model NOT in the student
                             panel; its solution must pass the seed's anchor tests. EXECUTED.

Graded criteria (G1-G4, verifier temperature 0, each with a one-sentence justification):
  G1 unambiguity  G2 completeness  G3 faithfulness  G4 naturalness

Acceptance (B3):
  ACCEPT iff H1..H5 all pass AND G1>=4 AND G2>=4 AND G3>=5 AND G4>=3
  FLAG   if hard pass but a graded score is exactly one below its threshold
         (or a hard check could not be verified)
  REJECT otherwise
Composite (B4, for SELECTION):  0.40*G3 + 0.30*G1 + 0.20*G2 + 0.10*G4

Per run_config stop_on_gate_fail=false, failures are recorded, never deleted.

CLI: python tools/gate.py --family 01 [--criterion 1] [--version v003]
"""
import argparse
import dataclasses
import json
import os
import re
import sys
import tempfile
from pathlib import Path

import backends as B

from harness.checker import judge_problem, judge_custom, normalize
from harness.dataset import discover_criteria, TestCase
from harness.reference_check import _FORBIDDEN_TERMS
from harness.runner import run_solution

# forbidden terms the harness regex misses (file 42/43 list): structural reveals + hints
_EXTRA_FORBIDDEN = re.compile(
    r"\b(tree|DAG|acyclic|matching|clique|cover|knapsack|"
    r"brute[- ]force is fine|easy variant|hard variant|trivially)\b", re.IGNORECASE)

# graded-criterion key map used by threshold/composite math
_GKEY = {"G1": "G1_unambiguity", "G2": "G2_completeness",
         "G3": "G3_faithfulness", "G4": "G4_naturalness"}
_DEFAULT_THRESHOLDS = {"G1": 4, "G2": 4, "G3": 5, "G4": 3}
_DEFAULT_WEIGHTS = {"G3": 0.40, "G1": 0.30, "G2": 0.20, "G4": 0.10}

ACCEPTED = {"ACCEPT", "PASS"}      # "PASS" kept for reading legacy gate.json
REJECTED = {"REJECT", "FAIL"}

_FALLBACK_SOLVER_SYSTEM = (
    "You are an expert competitive programmer. Read the problem and output a single "
    "self-contained Python 3 solution that reads stdin and writes stdout. Put the code "
    "in one ```python fenced block.")
_FALLBACK_SOLVER_USER = "{STATEMENT}\n\nWrite the complete Python 3 solution."


# --- statement parsing ------------------------------------------------------
def _section(statement: str, header: str) -> str:
    lines = statement.splitlines()
    out, capture = [], False
    for ln in lines:
        s = ln.strip()
        if s.lower().startswith("## ") or (s.startswith("#") and s.lstrip("#").strip()):
            capture = s.lstrip("#").strip().lower().startswith(header.lower())
            continue
        if capture:
            out.append(ln.rstrip())
    return "\n".join(out).strip()


_FENCE_BLOCK = re.compile(r"```[a-zA-Z0-9]*\n(.*?)```", re.DOTALL)


def parse_examples(statement: str) -> list[tuple[str, str]]:
    """Pull (input, output) example pairs from fenced blocks. Each fenced block is
    labelled by the nearest preceding word 'input' or 'output'. Consecutive
    input->output blocks form one example. Returns [] if none are found."""
    labelled = []
    for m in _FENCE_BLOCK.finditer(statement):
        pre = statement[:m.start()].lower()
        i_in, i_out = pre.rfind("input"), pre.rfind("output")
        label = "input" if i_in >= i_out else "output"
        labelled.append((label, m.group(1)))
    pairs, pending = [], None
    for label, body in labelled:
        if label == "input":
            pending = body
        elif label == "output" and pending is not None:
            pairs.append((pending, body))
            pending = None
    return pairs


# --- H2: numeric bounds -----------------------------------------------------
# Comparison operators (ASCII, unicode, and LaTeX spellings). NOTE: '=' is intentionally
# excluded -- range bounds use inequalities, whereas '=' denotes equations/definitions
# (e.g. "x_u + x_v = 3"), whose right-hand side is not a bound.
_CMP = r"(?:≤|≥|⩽|⩾|<|>|\\leq|\\geq|\\le|\\ge)"

# Prose comparison phrases: a bound may be stated in words without a symbolic operator,
# e.g. "at most 200000", "no more than 2*10^5", "maximum capacity of 2000". We capture the
# first numeric expression that follows such a phrase (allowing a few filler words).
_PROSE_CMP = re.compile(
    r"(?i)\b(?:at least|at most|no more than|no less than|no greater than|no larger than|"
    r"no smaller than|not exceed(?:ing)?|cannot exceed|can not exceed|does not exceed|"
    r"do not exceed|never exceeds?|up to|as large as|as many as|as few as|"
    r"maximum(?:\s+\w+){0,3}\s+of|minimum(?:\s+\w+){0,3}\s+of|capacity of|limit of|"
    r"capped (?:at|by)|bounded by)\b")

# A single numeric expression, in any of the forms a bound may be written. Ordered most-
# specific first so e.g. "2*10^5" matches as one token, not just the leading "2".
_NUMEXPR = r"""(?:
      \d+(?:\.\d+)?\s*[eE][-+]?\d+                                      # 2e5 / 2E5
    | \d+(?:\.\d+)?\s*(?:\\cdot|\\times|[·*×])\s*10\s*\^\s*\{?\s*\d+\s*\}?  # 2*10^5 / 2\cdot10^{5}
    | 10\s*\^\s*\{?\s*\d+\s*\}?                                         # 10^5 / 10^{5}
    | \d{1,3}(?:,\d{3})+                                                # 200,000
    | \d[\d_]*                                                          # 200000 / 1_000 / 40
)"""


_SUPERSCRIPT = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
                "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}


def _desuperscript(text: str) -> str:
    """Turn a run of Unicode superscript digits into caret notation, so exponents written
    as `10⁵` normalize to `10^5` and go through the same power-form path as `10^5`/`10^{5}`.
    (The seed statements use `2·10⁵` with a superscript ⁵ and no caret.)"""
    out, i, n = [], 0, len(text)
    while i < n:
        if text[i] in _SUPERSCRIPT:
            run = ""
            while i < n and text[i] in _SUPERSCRIPT:
                run += _SUPERSCRIPT[text[i]]
                i += 1
            out.append("^" + run)
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def _preclean(text: str) -> str:
    """Drop $...$ math delimiters and LaTeX spacing, and normalize Unicode superscript
    exponents, so bound tokens parse uniformly regardless of how they were written."""
    text = _desuperscript(text)
    text = text.replace("$", " ")
    for s in ("\\,", "\\;", "\\!", "\\ ", "\\quad", "\\qquad", "~"):
        text = text.replace(s, " ")
    return text


def _parse_number(raw: str):
    """Parse a matched numeric expression to an int value, or None if unparseable.
    Handles plain ints, thousands separators, underscores, scientific (e/E) and
    scientific/LaTeX power forms (a·10^b, a\\times10^{b}, 10^b)."""
    s = raw.strip()
    s = (s.replace("\\cdot", "*").replace("\\times", "*").replace("·", "*").replace("×", "*")
          .replace("{", "").replace("}", "").replace(",", "").replace("_", ""))
    s = re.sub(r"\s+", "", s)
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\*10\^([-+]?\d+)", s)
    if m:
        return int(round(float(m.group(1)) * 10 ** int(m.group(2))))
    m = re.fullmatch(r"10\^([-+]?\d+)", s)
    if m:
        return int(round(10 ** int(m.group(1))))
    m = re.fullmatch(r"(\d+(?:\.\d+)?)[eE]([-+]?\d+)", s)
    if m:
        return int(round(float(m.group(1)) * 10 ** int(m.group(2))))
    if re.fullmatch(r"\d+", s):
        return int(s)
    return None


_NUMEXPR_RE = re.compile(_NUMEXPR, re.VERBOSE)


def bound_matches(section_text: str) -> list:
    """[(raw_substring, parsed_value)] for every numeric expression that is a bound: one
    that sits on either side of a symbolic comparison operator, OR that follows a prose
    comparison phrase ("at most 200000", "capacity of 2000"). Deduplicated on (raw, value)."""
    text = _preclean(section_text)
    seen, out = set(), []

    def add(raw):
        raw = " ".join(raw.split())
        key = (raw, _parse_number(raw))
        if key not in seen:
            seen.add(key)
            out.append([key[0], key[1]])

    # 1. numbers adjacent to a symbolic comparison operator
    for pat in (rf"({_NUMEXPR})\s*{_CMP}", rf"{_CMP}\s*({_NUMEXPR})"):
        for m in re.finditer(pat, text, re.VERBOSE):
            add(m.group(1))
    # 2. numbers stated in prose: the first numeric expression that STARTS within a short
    #    window after a comparison phrase (allows fillers like "capacity of exactly 2000").
    #    Search the unbounded tail so a power expression isn't truncated mid-token (which
    #    would otherwise capture a bare mantissa like "2" from "2*10^5").
    for pm in _PROSE_CMP.finditer(text):
        nm = _NUMEXPR_RE.search(text[pm.end():])
        if nm and nm.start() <= 40:
            add(nm.group(0))
    return out


def bound_values(section_text: str) -> set:
    """The distinct parsed integer bound values in a section (unparseable ones dropped)."""
    return {v for _, v in bound_matches(section_text) if v is not None}


_TIEBREAK = re.compile(r"lexicograph|tie[- ]break|smallest|largest|minim|maxim", re.IGNORECASE)


def check_io_contract(seed_stmt: str, version_stmt: str) -> dict:
    seed_in, seed_out = _section(seed_stmt, "Input"), _section(seed_stmt, "Output")
    new_in, new_out = _section(version_stmt, "Input"), _section(version_stmt, "Output")
    has_sections = bool(new_in) and bool(new_out)
    seed_bm = bound_matches(seed_in + "\n" + seed_out)
    new_bm = bound_matches(new_in + "\n" + new_out)
    seed_vals = {v for _, v in seed_bm if v is not None}
    new_vals = {v for _, v in new_bm if v is not None}
    # Subset semantics: the rewrite must not DROP or WEAKEN any seed bound (every seed bound
    # value must still appear), but MAY add bounds -- making an implicit index range explicit
    # ("1 <= u,v <= n") or restating a bound in prose is faithful, not a violation. A genuine
    # change (e.g. 2*10^5 -> 3*10^5) drops the seed value and is still rejected.
    dropped = sorted(seed_vals - new_vals)
    added = sorted(new_vals - seed_vals)
    bounds_ok = not dropped
    seed_tb = bool(_TIEBREAK.search(seed_out))
    new_tb = bool(_TIEBREAK.search(new_out))
    tiebreak_ok = (not seed_tb) or new_tb
    ok = has_sections and bounds_ok and tiebreak_ok
    detail = []
    if not has_sections:
        detail.append("missing Input/Output section")
    if not bounds_ok:
        detail.append(f"bounds dropped by rewrite: {dropped} (added={added})")
    if not tiebreak_ok:
        detail.append("seed has a tie-break rule the rewrite dropped")
    # bounds_seed / bounds_new carry raw matched substrings alongside parsed values, so a
    # future mismatch is diagnosable from gate.json alone (no re-run needed).
    return {"pass": ok, "bounds_seed": seed_bm, "bounds_new": new_bm,
            "values_seed": sorted(seed_vals), "values_new": sorted(new_vals),
            "tiebreak_seed": seed_tb, "tiebreak_new": new_tb,
            "detail": "; ".join(detail) or "ok"}


# --- H3: leakage ------------------------------------------------------------
def leakage_hits(text: str) -> list[str]:
    hits = [m.group() for m in _FORBIDDEN_TERMS.finditer(text)]
    hits += [m.group() for m in _EXTRA_FORBIDDEN.finditer(text)]
    return sorted(set(h.lower() for h in hits))


# --- H1: example consistency (executed) -------------------------------------
def check_examples(version_stmt: str, seed_crit) -> dict:
    pairs = parse_examples(version_stmt)
    if not pairs:
        return {"pass": None, "detail": "no examples found", "_uncertain": False}
    judge_mode = seed_crit.meta.get("judge", "exact")
    timeout = float(seed_crit.meta.get("time_limit_s", 10))
    mem = int(seed_crit.meta.get("memory_limit_mb", 256))
    good = 0
    for i, (inp, expected) in enumerate(pairs, 1):
        if judge_mode == "custom" and seed_crit.validator_path is not None:
            # multiple outputs may be valid; check the stated example is itself valid
            ok, _ = judge_custom(seed_crit.validator_path, inp, expected)
        else:
            rr = run_solution(seed_crit.reference_path, inp, timeout, mem)
            ok = rr.status == "OK" and normalize(rr.stdout) == normalize(expected)
        if ok:
            good += 1
        else:
            return {"pass": False, "detail": f"example {i}/{len(pairs)} inconsistent",
                    "_uncertain": False}
    return {"pass": True, "detail": f"{good}/{len(pairs)} examples reproduce",
            "_uncertain": False}


# --- H4: S09 non-binding constraint (executed, small grammar) ---------------
_CONSTRAINT = re.compile(
    r"(sum|max|min|count)\s*\(?\s*(all|values|weights|degrees|elements)?\s*\)?\s*"
    r"(<=|<|>=|>|==|≤|≥)\s*(\d+)", re.IGNORECASE)


def _ints_of(input_text: str) -> list[int]:
    return [int(t) for t in re.findall(r"-?\d+", input_text)]


def check_s09_nonbinding(constraint: str, seed_crit) -> dict:
    """Evaluate a formally-stated non-binding constraint against every seed test input.
    Supports  AGG(selector) OP N  where AGG in {sum,max,min,count} over the input's
    integers. If the constraint cannot be parsed, we cannot confirm it is non-binding
    -> uncertain (FLAG), never a silent pass."""
    if not constraint:
        return {"pass": None, "detail": "no constraint stated", "_uncertain": True}
    m = _CONSTRAINT.search(constraint)
    if not m:
        return {"pass": None, "detail": f"unparseable constraint: {constraint[:80]!r}",
                "_uncertain": True}
    agg, _sel, op, n = m.group(1).lower(), m.group(2), m.group(3), int(m.group(4))
    op = {"≤": "<=", "≥": ">="}.get(op, op)
    fn = {"sum": sum, "max": max, "min": min, "count": len}[agg]
    import operator as _op
    cmp = {"<=": _op.le, "<": _op.lt, ">=": _op.ge, ">": _op.gt, "==": _op.eq}[op]
    for tc in seed_crit.tests:
        ints = _ints_of(tc.in_path.read_text())
        if not ints:
            continue
        lhs = fn(ints)
        if not cmp(lhs, n):
            return {"pass": False,
                    "detail": f"binding on {tc.name}: {agg}={lhs} not {op} {n}",
                    "_uncertain": False}
    return {"pass": True, "detail": f"non-binding on {len(seed_crit.tests)} inputs",
            "_uncertain": False}


# --- H5: solver round-trip (executed) ---------------------------------------
def _read_prompt(name, fallback):
    p = B.PROMPTS_DIR / name
    return p.read_text() if p.exists() else fallback


def _solver_bundle(run_cfg: dict):
    gc = (run_cfg or {}).get("gate", {}) or {}
    sr = gc.get("solver_roundtrip", {}) or {}
    if not sr.get("enabled"):
        return None
    if sr.get("backend") and sr.get("model_string"):
        cfg = {"id": sr.get("model_id", "solver"), "backend": sr["backend"],
               "base_url": sr.get("base_url", ""), "model_string": sr["model_string"],
               "api_key_env": sr.get("api_key_env", "GEMINI_API_KEY"),
               "temperature": sr.get("temperature", 0.1),
               "top_p": sr.get("top_p"),
               "max_tokens": sr.get("max_tokens", 12288),
               "thinking": sr.get("thinking", False),
               "extra_headers": sr.get("extra_headers")}
    else:
        models = B.load_models()
        mid = sr.get("model_id")
        cfg = None
        for key in ("teacher", "verifier"):
            if models.get(key, {}).get("id") == mid:
                cfg = models[key]
        for m in models.get("solvers", []) or []:
            if m.get("id") == mid:
                cfg = m
        if cfg is None:
            return None
    sysp = _read_prompt("student_system.md", _FALLBACK_SOLVER_SYSTEM)
    usr = _read_prompt("student_user_template.md", _FALLBACK_SOLVER_USER)
    return cfg, sysp, usr


def check_solver_roundtrip(version_stmt: str, seed_crit, run_cfg: dict,
                           out_dir=None, log_name="solver_attempt.txt") -> dict:
    bundle = _solver_bundle(run_cfg)
    if bundle is None:
        return {"pass": None, "solver": None, "anchor": "n/a",
                "detail": "disabled or unresolved", "_uncertain": False}
    cfg, sysp, usr = bundle
    panel = {s["id"] for s in B.load_models().get("students", [])}
    if cfg.get("id") in panel:
        return {"pass": None, "solver": cfg.get("id"), "anchor": "n/a",
                "detail": "solver is in the student panel; skipped", "_uncertain": True}
    user = usr.replace("{STATEMENT}", version_stmt)
    resp = B.chat(cfg, sysp, user, timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=B.load_models().get("execution", {}).get("retries", 3))
    # Always persist the raw solver reply for diagnosis (file-47 gap): a reasoning model
    # can spend its whole budget on <think> and get truncated before the code fence.
    if out_dir is not None:
        try:
            Path(out_dir).mkdir(parents=True, exist_ok=True)
            (Path(out_dir) / log_name).write_text(resp["text"] or "")
        except Exception:
            pass
    # Reasoning models emit <think> blocks; strip them first. A non-reasoning solver
    # (thinking: false) emits none, so we skip the extra strip -- extract_code's own
    # internal strip still handles any stray tag harmlessly.
    raw = resp["text"]
    if cfg.get("thinking"):
        raw = B.strip_thinking(raw)
    code = B.extract_code(raw)
    if resp["error"] or not code.strip():
        return {"pass": None, "solver": cfg.get("id"), "anchor": "n/a",
                "detail": resp["error"] or "solver produced no code", "_uncertain": True,
                **B.usage_of(resp)}
    # Test set: anchors always; optionally the STANDARD corner cases too (tests: anchor+corner
    # in run_config). The adversarial adv_* cases are EXCLUDED -- those are built to defeat
    # solvers, so requiring a solver to pass them would reject every hard statement. Running
    # H5 on the standard corner cases raises the ceiling: the statement must stay solvable on
    # ordinary edge cases, not just the tiny anchors.
    crit_for_h5 = seed_crit
    sr = ((run_cfg or {}).get("gate", {}) or {}).get("solver_roundtrip", {}) or {}
    if "corner" in (sr.get("tests") or "anchor"):
        store = B.TESTS_DIR / f"family_{seed_crit.family_id}" / seed_crit.criterion_id
        extra = []
        if store.exists():
            for inp in sorted(store.glob("*.in")):
                if inp.stem.startswith("adv_"):
                    continue                     # skip adversarial traps
                outp = inp.with_suffix(".out")
                if outp.exists():
                    extra.append(TestCase(name="c" + inp.stem, in_path=inp, out_path=outp))
        if extra:
            crit_for_h5 = dataclasses.replace(seed_crit, tests=list(seed_crit.tests) + extra)
    fh = tempfile.NamedTemporaryFile("w", suffix=".py", delete=False)
    try:
        fh.write(code)
        fh.close()
        pv = judge_problem(crit_for_h5, fh.name)
    finally:
        os.unlink(fh.name)
    npass = sum(1 for c in pv.cases if c.verdict == "PASS")
    return {"pass": pv.overall == "PASS", "solver": cfg.get("id"),
            "anchor": f"{npass}/{len(pv.cases)}",
            "detail": pv.first_failure or "all solver tests pass", "_uncertain": False,
            **B.usage_of(resp)}


# --- graded criteria (verifier) ---------------------------------------------
def _parse_graded(text: str) -> dict:
    def num(tag):
        m = re.search(rf"<{tag}>\s*([0-5])", text)
        return int(m.group(1)) if m else None

    def just(tag):
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    return {
        "G1_unambiguity":  {"score": num("G1_unambiguity"),  "justification": just("G1_justification")},
        "G2_completeness": {"score": num("G2_completeness"), "justification": just("G2_justification")},
        "G3_faithfulness": {"score": num("G3_faithfulness"), "justification": just("G3_justification")},
        "G4_naturalness":  {"score": num("G4_naturalness"),  "justification": just("G4_justification")},
    }


def composite(graded: dict, weights: dict):
    total = 0.0
    for k, w in weights.items():
        sc = graded.get(_GKEY[k], {}).get("score")
        if sc is None:
            return None
        total += w * sc
    return round(total, 3)


def _decide(hard: dict, graded: dict, thresholds: dict) -> str:
    if any(h.get("pass") is False for h in hard.values()):
        return "REJECT"
    deficits, missing = [], False
    for k, t in thresholds.items():
        sc = graded.get(_GKEY[k], {}).get("score")
        if sc is None:
            missing = True
        else:
            deficits.append(t - sc)
    if missing:
        return "FLAG"                        # verifier score unreadable -> human review
    worst = max(deficits)
    if worst <= 0:
        if any(h.get("_uncertain") for h in hard.values()):
            return "FLAG"                    # a hard check could not be verified
        return "ACCEPT"
    if worst == 1:
        return "FLAG"                        # exactly one below threshold
    return "REJECT"


# --- seed helpers -----------------------------------------------------------
def seed_criterion(slug: str, crit_dir: str):
    for c in discover_criteria(B.SEEDS_DIR / slug):
        if c.criterion_id == crit_dir:
            return c
    return None


def _gate_cfg(run_cfg: dict):
    gc = (run_cfg or {}).get("gate", {}) or {}
    thresholds = {**_DEFAULT_THRESHOLDS, **(gc.get("thresholds") or {})}
    weights = {**_DEFAULT_WEIGHTS, **(gc.get("composite_weights") or {})}
    return thresholds, weights


def evaluate_statement(version_stmt: str, seed_stmt: str, seed_crit, verifier_cfg,
                       run_cfg, verifier_system: str, verifier_user_tmpl: str, *,
                       strategies=None, s09_constraint=None,
                       out_dir=None, solver_log_name="solver_attempt.txt") -> dict:
    """Run the two-part gate on a candidate statement (text) and return the result dict
    (B5 schema). Used by gate_version (from a file) and by the feedback loops (in memory).
    `strategies` is the strategy id list that produced this candidate (drives H4);
    `s09_constraint` is the teacher's formally-stated constraint when S09 was used."""
    thresholds, weights = _gate_cfg(run_cfg)
    strategies = strategies or []

    # --- hard constraints ---------------------------------------------------
    h1 = check_examples(version_stmt, seed_crit)
    h2 = check_io_contract(seed_stmt, version_stmt)
    hits = leakage_hits(version_stmt)
    h3 = {"pass": not hits, "hits": hits}
    if any(str(s).startswith("S09") for s in strategies):
        h4 = check_s09_nonbinding(s09_constraint or "", seed_crit)
    else:
        h4 = {"pass": None, "detail": "not applicable", "_uncertain": False}
    h5 = check_solver_roundtrip(version_stmt, seed_crit, run_cfg,
                                out_dir=out_dir, log_name=solver_log_name)

    hard = {
        "H1_example_consistency": h1,
        "H2_io_contract": h2,
        "H3_leakage": h3,
        "H4_s09_nonbinding": h4,
        "H5_solver_roundtrip": h5,
    }

    # --- graded criteria (verifier, temperature 0) --------------------------
    user = verifier_user_tmpl.replace("{SEED}", seed_stmt).replace("{CANDIDATE}", version_stmt)
    resp = B.chat(verifier_cfg, verifier_system, user,
                  timeout=run_cfg.get("request_timeout_s", 1800),
                  retries=B.load_models().get("execution", {}).get("retries", 3))
    # The verifier is a reasoning model: strip its <think> block first so tag names that
    # appear inside the reasoning cannot be mistaken for the final graded scores.
    graded = _parse_graded(B.strip_thinking(resp["text"]))
    comp = composite(graded, weights)

    result = _decide(hard, graded, thresholds)
    if resp["error"] and all(graded[k]["score"] is None for k in graded):
        result = "FLAG"                      # could not obtain scores -> human review

    verifier = {"called": True, "error": resp["error"], "raw": resp["text"],
                "overall": result.lower(), **B.usage_of(resp)}

    return {
        "result": result,
        "hard": {k: {kk: vv for kk, vv in v.items() if kk != "_uncertain"}
                 for k, v in hard.items()},
        "graded": graded,
        "composite": comp,
        "thresholds_applied": thresholds,
        "judge": {"model": verifier_cfg.get("id"), "temperature": 0, **B.usage_of(resp)},
        # back-compat keys read by harden_loop / feedback logging:
        "leakage_hits": hits,
        "verifier": verifier,
    }


# --- gate negotiation feedback (file 52 change 5) ---------------------------
# The gate produces DIAGNOSTICS ONLY -- never statement text. It reports which checks
# failed and actionable advice; the teacher writes all content and a FRESH gate call
# re-validates. This keeps the gate an independent validator, not a co-author.
_H_ADVICE = {
    "H1_example_consistency": "the reference no longer reproduces a worked example -- fix the example values so they are consistent",
    "H2_io_contract": "restore the exact numeric bound(s)/tie-break/format from the seed; you may RE-PRESENT them (e.g. in prose) but not change or drop them",
    "H3_leakage": "remove the complexity-class vocabulary or structural giveaway you introduced",
    "H4_s09_nonbinding": "make the added constraint non-binding on every existing input, or drop it",
    "H5_solver_roundtrip": "an independent solver failed the anchor tests -- the task drifted; keep the exact same question as the seed",
}
_G_ADVICE = {
    "G1": "disambiguate the flagged phrase -- it admits more than one reading",
    "G2": "add the information needed to solve it that is currently missing",
    "G3": "the rewrite asks a materially different question -- return it to the seed's exact task",
    "G4": "make it read more like a problem a person would naturally write",
}


def negotiation_feedback(gres: dict) -> dict:
    """Structured, actionable feedback from a gate result -- for the teacher to revise.
    Contains only diagnostics (no statement content)."""
    hard = gres.get("hard", {})
    graded = gres.get("graded", {})
    thr = gres.get("thresholds_applied", _DEFAULT_THRESHOLDS)
    rejected, details, advice, keep = [], {}, [], []
    for k, v in hard.items():
        if v.get("pass") is False:
            tag = k.split("_")[0]
            rejected.append(tag)
            details[f"{tag}_detail"] = str(v.get("detail") or v.get("hits") or "failed")
            advice.append(_H_ADVICE.get(k, f"fix {tag}"))
    for gk, t in thr.items():
        cell = graded.get(_GKEY[gk], {})
        sc = cell.get("score")
        if sc is None or sc < t:
            rejected.append(gk)
            details[f"{gk}_detail"] = cell.get("justification") or "below threshold"
            advice.append(_G_ADVICE.get(gk, f"raise {gk}"))
        else:
            j = (cell.get("justification") or "").strip()
            keep.append(f"{gk} scored {sc} ({j[:70]})" if j else f"{gk} scored {sc}")
    return {"rejected_because": rejected, **details,
            "actionable_advice": "; ".join(advice) or "none",
            "do_not_change": keep}


# --- CLI over on-disk versions ----------------------------------------------
def _edit_meta(vdir: Path) -> dict:
    try:
        return json.loads((vdir / "edit.json").read_text())
    except Exception:
        return {}


def gate_version(vdir: Path, seed_stmt: str, seed_crit, verifier_cfg, run_cfg,
                 verifier_system: str, verifier_user_tmpl: str) -> dict:
    meta = _edit_meta(vdir)
    res = evaluate_statement(
        (vdir / "statement.md").read_text(), seed_stmt, seed_crit, verifier_cfg, run_cfg,
        verifier_system, verifier_user_tmpl,
        strategies=meta.get("strategies") or [],
        s09_constraint=meta.get("s09_constraint") or meta.get("added_constraint"),
        out_dir=vdir)
    return {"version": vdir.name, **res}


def iter_version_dirs(family, criterion, version):
    base = B.VERSIONS_DIR / f"family_{family}"
    crits = [B.criterion_dirname(criterion)] if criterion else \
        [d.name for d in sorted(base.glob("criterion_*"))]
    for cd in crits:
        cbase = base / cd
        if not cbase.exists():
            continue
        vers = [cbase / version] if version else sorted(cbase.glob("v*"))
        for v in vers:
            if (v / "statement.md").exists():
                yield cd, v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)   # id or 'all'
    ap.add_argument("--criterion", type=int, choices=[1, 2])
    ap.add_argument("--version")
    args = ap.parse_args()

    models = B.load_models()
    run_cfg = B.load_run_config()
    verifier_cfg = models["verifier"]
    verifier_system = (B.PROMPTS_DIR / "verifier_system.md").read_text()
    verifier_user_tmpl = (B.PROMPTS_DIR / "verifier_user_template.md").read_text()

    total = {"ACCEPT": 0, "FLAG": 0, "REJECT": 0}
    for family in B.list_families(args.family):
        slug = B.family_slug(family)
        for crit_dir, vdir in iter_version_dirs(family, args.criterion, args.version):
            sc = seed_criterion(slug, crit_dir)
            if sc is None:
                print(f"ERROR: no seed criterion for {crit_dir}", file=sys.stderr)
                continue
            res = gate_version(vdir, sc.statement_path.read_text(), sc, verifier_cfg,
                               run_cfg, verifier_system, verifier_user_tmpl)
            (vdir / "gate.json").write_text(json.dumps(res, indent=2))
            total[res["result"]] = total.get(res["result"], 0) + 1
            hfail = [k.split("_")[0] for k, v in res["hard"].items() if v.get("pass") is False]
            print(f"  [{res['result']}] family_{family}/{crit_dir}/{vdir.name} "
                  f"composite={res['composite']} hard_fail={hfail or '-'}")
    print(f"[gate] {total}")


if __name__ == "__main__":
    main()
