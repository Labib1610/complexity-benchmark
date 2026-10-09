# Family 01 — Worst-Case (Phase-Transition) Tier

A hard, **gradeable** NP-complete tier that escapes the gradeable-NPC ceiling, built after the
audit's P0/P1 rebuild to test whether strong models have any real optimisation for worst-case
3-colouring (they do not).

## The idea

Normal gradeable NPC tests are capped by the **gradeable ceiling**: the reference must solve a case
to produce its answer key, so no case can be hard for a competent solver. This tier sidesteps that for
YES-instances:

- Instances are **planted, near-threshold 3-colourable graphs** — a random balanced 3-partition with
  edges added only *across* parts at ratio m/n ≈ 2.3 (the 3-colouring threshold). They are 3-colourable
  **by construction**, and near the threshold the planted colouring is hidden among many
  near-solutions, so they are the hardest colourable regime.
- Grading is **witness-only**: since the answer is YES by construction, the grader just verifies the
  model's output is a proper 3-colouring of all n vertices (O(n+m)). **No reference solve, no
  feasibility recompute** — so arbitrarily large / hard instances are gradeable.

## Files
- `tools/worstcase_coloring.py` — `planted_3col(n,ratio,seed)` generator + `grade()` witness-only grader (CLI: `--gen`, `--grade`).
- `tools/run_worstcase.py` — runs the saved student solutions against the tier and reports pass rate.
- `dataset/family_01_graph_coloring/criterion_1_npc/worstcase/NN.in` — 10 instances, ramp n=400..1200 at ratio 2.3 (2 seeds each).

## Result (panel v000 solutions, 2 s limit)

| Model | PASS% | notes |
|---|---|---|
| gpt-oss-120b     | **20%** | solves n=400 only; TLE from n=600 (MRV+forward-checking, real search blow-up) |
| deepseek-v4-flash | **0%** | TLE everywhere |
| qwen3-coder      | **0%** | TLE everywhere |
| glm-5            | **0%** | emits improper colourings (buggy solver) |

Contrast with the *normal* NPC tier for the same models (98 / 91 / 56 / 42%). Reproduced separately:
gpt-oss is 100% at n≤200 and 0% at n≥800 near the threshold, but 100% on *dense* (ratio 4.0) graphs
even at n=800 — the classic **easy → hard → easy** phase-transition signature.

## Frontier confirmation (2 s limit, 10-case tier)

| Model | code | PASS% |
|---|---|---|
| gpt-5.6-sol              | 5705 B | **0%** (TLE all 10, incl. n=400) |
| gemini-3.7-flash-frontier | 9072 B | **0%** (TLE all 10) |

Even the strongest frontier models — writing 5.7 KB / 9 KB exact solvers — TLE on every instance.
The tier is SOTA-resistant across the whole field (best result anywhere: gpt-oss 20%).

## Smallest breaking n (ratio 2.3, 2 s, 3 seeds/point)

| model | n200 | n250 | n300 | n350 | n400 | n500 | first break |
|---|---|---|---|---|---|---|---|
| gpt-oss-120b | Y | Y | Y | T | Y | T | ~350 |
| gpt-5.6-sol  | Y | T | Y | T | T | T | ~250 |

Strong solvers are reliable to **n≈200–300**, break around **n≈250–350** (noisy near threshold), and
all fail by **n=500**. So a near-threshold graph of only **~250–400 vertices** already defeats frontier
models — "a complex graph with minimal nodes." Below ~n=200 the pruned search tree is too small for the
exponential to bite, so n≈300–400 is the practical floor. (gemini's saved solution is implementation-slow
and TLEs even tiny graphs — a solver-quality artifact, not a hardness signal.)

## C2 / C3 stress tiers — built and run (empirical confirmation)

Worst-case tiers were also built for the other two criteria and run on all six models:
- **C2 (2-colouring, P)**: `criterion_2_p/worstcase/*.in` — large planted-bipartite graphs up to n=2·10⁵
  (+ NO-instances via a same-side edge). Exact-match vs `reference.py` (lex-smallest), 1 s.
- **C3 (certify non-2-colourability = find a triangle)**: `criterion_3_infeasible/worstcase/*.in` —
  dense random graphs up to n=2000, m=2·10⁵ with genuine lex-smallest triples. Exact-match, 2 s.

| Model | C1 NPC (10) | C2 P-stress (8) | C3 infeasible-stress (8) |
|---|---|---|---|
| gpt-oss-120b | 20% | 100% | 100% |
| gpt-5.6-sol | 0% | 100% | 100% |
| gemini-3.7-flash | 0% | 100% | 100% |
| deepseek-v4-flash | 0% | 100% | 100% |
| qwen3-coder | 0% | 100% | 100% |
| glm-5 | 0% | 100% | 100% |

**The stress tiers caught nobody (100% across the board):** every model already writes the correct
polynomial algorithm, so scaling to n=200k / dense-2000 just confirms competence. They are worth
**keeping as guardrails** (they would flag any future exponential/naïve solver) but are **not
discriminators**. Only C1 (NPC) separates the field. Reference times: C2 0.24 s, C3 0.10 s (tiers fair).

## P / INFEASIBLE have no hard-and-gradeable worst-case (the asymmetry)

- **P arms**: a correct polynomial solver handles any size fast (by definition of P); a worst-case tier
  only catches models that *don't* use the poly algorithm — it can never defeat a correct one.
- **INFEASIBLE arms**: designed with cheap checkable certificates (odd cycle / MOD / SIZE / …), so they
  are poly-findable and easy. A *hard* infeasible instance = no short certificate = co-NP-hard, and then
  the reference cannot certify NO cheaply either → not gradeable (the gradeable-**NO** ceiling).
- Only **NPC YES-instances** are simultaneously hard-for-everyone *and* cheaply gradeable (verify the
  witness). The worst-case tier is fundamentally an NPC-YES phenomenon.

## Why this matters (the finding)

- **No unique optimisation beats worst-case 3-colouring.** The strongest panel model has a genuine
  optimisation (MRV + forward-checking) that crushes small/easy/dense instances, but it TLEs at the
  phase transition (n≥600–800) — genuine NP-hardness, not a heuristic gap.
- **Surface (statement) hardening plateaus; instance hardening works.** Rewording can't defeat a
  competent solver (structural floor: the shortcut *is* the task), but planted near-threshold
  instances do — and they are gradeable by witness-checking.
- This is the concrete **P2/P3 direction**: make the NPC tiers SOTA-resistant with planted,
  near-threshold, witness-graded instances at a size where competent solvers TLE — not more rewrites.

## Regenerate / run
```
python tools/worstcase_coloring.py --gen --n 800 --ratio 2.3 --seed 1 > case.in   # one instance
python tools/run_worstcase.py --limit 2.0                                          # grade the panel
```

## Honest caveats
- YES-only: this tier does not add hard NO-instances (near-threshold UNSAT/uncolourable proofs are
  not cheaply gradeable — that remains the ceiling for NO-instances).
- The n where models TLE is partly Python-implementation-bound (their own code), which is fair: the
  benchmark measures the solution they actually produce under the time limit.
- Frontier-model confirmation (GPT-5.6 Sol / Gemini) is **done**: both 0% (see above).
