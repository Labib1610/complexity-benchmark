# Version plan

`versions_per_criterion` in run_config is a target, not a formula. The planner fills it
using four sources in priority order. Version numbering is deterministic given the run
seed.

v000 is reserved for the unmodified seed (report baseline).

## Source 1 — base grid
Every (strategy, intensity) pair applicable to this criterion's class, one sample each.
Strategies declare `classes:` in their file; inapplicable ones are skipped, not
substituted. Typical yield: 27-36 depending on class.

## Source 2 — extra samples
If the target is not met, draw additional samples from cells already used. The teacher
runs at temperature 0.9, so repeated draws from the same (strategy, intensity) produce
genuinely different statements. Distribute round-robin across cells so no single
strategy dominates. Each sample gets a distinct sub-seed.

Empirical note: in the Family 01 batch, this source was the least effective (mean delta
+0.12, the worst of the four). Temperature alone produces paraphrase, not genuine
diversity. Persona conditioning of the teacher prompt is the intended fix.

## Source 3 — composition
Pairs of compatible strategies applied together (both instructions injected, joined by
"Apply both of the following, in combination:"). Skip pairs that conflict — S04 and S05
are mutually exclusive, S12 requires feedback. Composition uses intensity `moderate` or
`aggressive` only; a light composition is indistinguishable from a light single.

## Source 4 — next generation
Derive a version from an **already-accepted** version rather than from the seed. The
parent's statement replaces `{SEED_STATEMENT}` in the teacher prompt; the hidden metadata
block still comes from the original `meta.yaml`. Track `parent` and `generation` in
`edit.json`. Only parents with `gate_result: PASS` are eligible. Generation depth is
capped by `max_generation` in run_config (default 2) so drift stays reviewable.

## Scaling
Raise `versions_per_criterion` and the planner extends automatically through sources 2-4.
There is no upper bound imposed by the strategy library.
