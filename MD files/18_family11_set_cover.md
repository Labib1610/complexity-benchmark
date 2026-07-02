# 18 — Fill Family 11: Skill Coverage (Set Cover)

> Follow `08_START_family_filling.md`. Target: `dataset/family_11_set_cover/`.

## Domain framing

Hire a few consultants so that together they cover every required skill. Each consultant covers a set of skills. NPC: general sets, budget k. P: every consultant covers exactly two skills (reduces to edge cover). Infeasible: a required skill no consultant has.

## Criterion 1 — NP-complete (Set Cover decision)

- **Class:** NPC. **Letter:** A.
- **Problem:** Universe of `u` skills, `s` consultants each with a skill subset, and budget `k`. Decide whether `k` consultants cover all skills; output the chosen consultants or `NO`.
- **Input:** `u s k`; then `s` lines, each: count then that many skill ids. `1 ≤ u ≤ 20` (DP over skill-subset bitmask, O(2^u · s)), `s ≤ 200`.
- **Output:** `YES` + chosen consultant indices (lexicographically smallest selection of size ≤ k), else `NO`. If heavy, `judge: custom` "any cover of size ≤ k". Pick one.
- **Reference:** bitmask DP over covered-skill sets, reconstructing the smallest cover. Deterministic.

## Criterion 2 — P (size-2 sets = edge cover)

- **Class:** P. **Letter:** B.
- **Problem:** every consultant covers **exactly two** skills. Treat skills as vertices and consultants as edges; covering all skills = an edge cover. Find the **minimum** number of consultants covering every skill (assume every skill appears in at least one consultant).
- **Theorem:** minimum edge cover = `V − maximum matching` (Gallai), computable via matching.
- **Input:** `u s` then `s` lines `a b` (the two skills). `u ≤ 1e5`, `s ≤ 2e5`.
- **Output:** the minimum number of consultants = `u − maxMatching` (on the skill graph). Unique → `exact`.
- **Reference:** maximum matching (general graph matching, or if the instance is bipartite-by-construction use Hopcroft–Karp; otherwise Blossom — to avoid Blossom, you MAY constrain the statement so skills split into two groups and each consultant joins the groups, keeping it bipartite). Decide and keep statement consistent. Don't write "edge cover"/"matching" labels.

## Criterion 3 — Infeasible (uncoverable skill)

- **Class:** INFEASIBLE. **Letter:** C.
- **Problem:** some required skill appears in **no** consultant's set. No selection can cover it — impossible. Report that skill.
- **Input:** `u s` then `s` consultant skill lists; guaranteed some skill covered by nobody.
- **Output:** the smallest id of a skill that no consultant has.
- **Judge:** `exact` (optionally validator confirming the skill is absent from all sets).
- **Reference:** mark covered skills, print smallest uncovered id.

## Test cases

- C1: a coverable instance (`YES`), one needing more than k (`NO`), u=1.
- C2: small size-2-set instances with known minimum covers (a path of skills, a star).
- C3: two instances with an uncoverable skill.

Generate `.out`, run `reference_check`, fix, report, wait for `19`.
