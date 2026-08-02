# 26 — Scale Family 01: Shift Assignment (Graph Coloring) — THE TEMPLATE

> Follow the fixed procedure in `25_START_test_case_scaling.md`.
> Target: `dataset/family_01_graph_coloring/`.
>
> **This is the template family.** Every later scaling file copies this shape. Do it
> carefully and report thoroughly — the user will review this one closely before
> the remaining 15 proceed.

## Family 01 at a glance

| Criterion | Class | Problem | Reference algorithm | Current bound |
|-----------|-------|---------|---------------------|---------------|
| 1 | NPC | 3-coloring, lexicographically smallest | 3^n backtracking with pruning | n ≤ 20 |
| 2 | P | 2-coloring / bipartiteness, lex smallest | BFS, O(n+m) | n ≤ 2·10⁵ |
| 3 | INFEASIBLE | triangle certificate | bitset triangle search, O(n·m/64) | n ≤ 2000 |

**Expect a narrow window on criterion 1.** Our reference is 3^n backtracking; a
naive model solution is likely *also* 3^n backtracking. The room we have comes from
our pruning and from choosing **hard instance structure**, not from an asymptotic
gap. This family is the hardest case — which is exactly why it's the template.

## Step 1 — Write the generator

Create `tools/gen_family_01.py`, seeded and deterministic. It must emit valid inputs
per the statements' formats.

Required generators:

```python
# CLI: python tools/gen_family_01.py --criterion 1 --n 22 --seed 7 > out.in

def gen_3col(n, seed, mode="hard"):
    """Criterion 1: n workers, m conflict pairs. Format: 'n m' then m lines 'u v'.
    mode='hard'  -> instance near the 3-coloring phase transition (see Step 2)
    mode='random'-> Erdos-Renyi at a given edge probability
    """

def gen_2col(n, m, seed, satisfiable=True):
    """Criterion 2: large bipartite-ish graph.
    satisfiable=True  -> build a genuinely 2-colorable graph (split vertices into
                         two sides, only add cross edges)
    satisfiable=False -> add exactly one intra-side edge to force an odd cycle -> NO
    """

def gen_triangle(n, m, seed):
    """Criterion 3: graph guaranteed to contain at least one triangle.
    Plant a triangle, then add random edges. Ensure the lexicographically smallest
    triangle is not trivially 1 2 3 in every case (vary it).
    """
```

Rules: 1-indexed vertices, no self-loops, no duplicate edges, respect each
statement's `m` bound. Fixed seed ⇒ same file every time.

## Step 2 — Criterion 1 (NPC): find the ceiling, use HARD instances

This is the scientific core of the family. Two things matter:

**(a) Instance structure, not just size.** Random sparse graphs are *easy* to
3-color; random dense graphs are *easily* proven uncolorable. The hard instances sit
near the **phase transition**, around average degree ≈ 4.7 (i.e. `m ≈ 2.35·n`) for
random 3-coloring. Instances there force deep backtracking. Generate `mode="hard"`
at approximately this ratio. **Size alone will not create hardness here — the ratio
will.**

**(b) Probe the ceiling empirically.** Do NOT guess. Run:

```bash
for n in 18 20 22 24 26 28 30 32; do
  python tools/gen_family_01.py --criterion 1 --n $n --seed 7 --mode hard > /tmp/probe.in
  /usr/bin/time -f "n=$n  %e s" python dataset/family_01_graph_coloring/criterion_1_npc/reference.py < /tmp/probe.in > /dev/null
done
```

Record every timing. Pick `chosen_max_size` = the largest n where the reference
finishes in **≤ 0.5 s** (25% of the 2 s limit). Report the full probe table.

> If the reference blows past the limit already at n=22, that is a real finding:
> report it. The window may be tiny, and the user may decide criterion 1 needs a
> better reference (e.g. DSATUR-ordered backtracking or a SAT-based exact solver)
> before it can scale. **Do not silently rewrite the reference — report and stop.**

**Emit the ramp.** Five new cases below the ceiling, spread out. Example if the
ceiling lands at n=24: sizes `[14, 18, 21, 23, 24]`. Include a mix of YES and NO
instances (vary the seed / edge ratio) so models can't pass by always guessing one.

## Step 3 — Criterion 2 (P): scale toward the real bound

Easy but important: a *correct but inefficient* solution (e.g. O(n²) adjacency-matrix
BFS, or recursive DFS that blows the stack) must TLE, while our O(n+m) reference is
comfortable.

Emit ~5 cases ramping toward the statement's bound:
sizes roughly `n ∈ [10^3, 10^4, 5·10^4, 10^5, 2·10^5]` with `m ≈ 2n` (respecting
`m ≤ 2·10^5`).

Include at least:
- one large **satisfiable** case (`YES` + assignment),
- one large **unsatisfiable** case (one odd cycle planted → `NO`),
- one case with **many components** (tests the per-component lex-smallest rule).

Time the reference on the largest; it should be well under 1 s. If Python I/O is the
bottleneck, confirm the reference uses `sys.stdin.buffer.read().split()`.

## Step 4 — Criterion 3 (INFEASIBLE): scale freely

Reference is a bitset triangle search, cheap. Ramp toward the bound:
`n ∈ [200, 500, 1000, 1500, 2000]` with `m` near its cap.

Make sure at least one large case has its lexicographically smallest triangle
**not** at low indices, so a solution that just prints the first triangle it finds
(rather than the smallest) fails. That's the case that tests the tie-break rule.

## Step 5 — Generate every `.out` from the reference

For each new `.in`, append with the next free number (existing small cases keep
their numbers — **do not delete or renumber them**):

```bash
D=dataset/family_01_graph_coloring/criterion_1_npc
python $D/reference.py < $D/tests/05.in > $D/tests/05.out
```

Never hand-write an `.out`.

## Step 6 — MANDATORY: prove naive brute force now dies

This is the whole point of the phase. For criterion 1, write:

`tools/naive_family_01_criterion_1.py` — a deliberately naive solution: plain
recursive 3-coloring that tries every vertex × every color with **no pruning beyond
the basic conflict check**, no ordering heuristic, no bitsets. This is what a model
that doesn't recognize intractability would plausibly write.

Then confirm on the **largest** case:

```bash
D=dataset/family_01_graph_coloring/criterion_1_npc
timeout 5 python tools/naive_family_01_criterion_1.py < $D/tests/09.in > /dev/null
echo "exit=$?"   # 124 = timed out = GOOD (this is what we want)

time python $D/reference.py < $D/tests/09.in > /dev/null   # must finish well under 2s
```

**Success criterion:** naive TLEs, reference passes.

**If naive brute force still passes the largest case:** the scaling FAILED for this
family. Report it plainly. Options to raise with the user: push n higher (if the
reference allows), tighten the edge ratio closer to the phase transition, or lower
`time_limit_s`. Do not pretend it worked.

Do the same naive check for criterion 2 (naive = O(n²) matrix BFS → must TLE at
n=2·10⁵) and criterion 3 (naive = triple nested loop O(n³) → must TLE at n=2000).

## Step 7 — Statement bounds MUST match reality

If the ceiling lands above or below the statement's stated bound, the statement is
now **wrong**. Example: statement says `1 ≤ n ≤ 20` but we test at n=24.

**Do not silently diverge.** Either:
- update `statement.md`'s bound to match the new maximum test size, or
- keep tests within the stated bound.

Flag to the user which you did and why. The stated bound is part of the problem —
a model reasons about difficulty from it — so it must be truthful.

## Step 8 — Record provenance in each meta.yaml

Append a `scaling:` block per criterion (schema in file `25`): the full probe table,
`chosen_max_size`, `ramp_sizes`, `naive_tle_confirmed`, `naive_time_at_max`, notes.

## Step 9 — Validate

```bash
python -m harness.reference_check dataset/family_01_graph_coloring
```
Must be clean: reference matches every `.out`, no missing outputs, no statement
leakage.

## Step 10 — Report to the user

Report, per criterion:
1. The **ceiling probe table** (size → reference seconds).
2. The **chosen ramp sizes** and how many test cases each criterion now has.
3. **Naive-vs-reference timing on the largest case** — the proof the scaling worked.
4. Whether any `statement.md` bound had to change.
5. `reference_check` clean confirmation.
6. **Any family-level warning** — especially if the NPC window turned out too narrow
   to be useful.

Then **stop and wait** for `27_scale_family02_sat.md`.

---

## Note for the user (surface this in your report)

Family 01 has the tightest window in the set because the reference and a naive
solution share the same 3^n shape. If the window here is too narrow to be
meaningful, that is worth knowing **now** — it may mean this family needs a
stronger exact reference before it can carry the NPC arm, and other families
(e.g. 04 subset-sum with meet-in-the-middle 2^(n/2) vs naive 2^n) will scale far
more easily. Report honestly rather than forcing a result.
