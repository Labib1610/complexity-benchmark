# Agentic Adversarial Hardening Framework — Design for Review

**Project:** Complexity-Aware Code Generation Benchmark
**Phase:** Agentic dataset hardening (teacher–student adversarial loop)
**Status:** Design proposal for review before implementation

---

## 1. One-paragraph summary

We already have 48 base problems (16 families × 3 criteria: P / NP-complete /
infeasible). Instead of scaling input *size* (which conflates reasoning ability with
code efficiency and runtime), we add an **agentic teacher–student loop**. A
closed-source **teacher (editor) model** rewrites each problem's *statement* and
*test cases* to expose conceptual reasoning failures in a panel of **student models**
(open-source + one closed-source), guided by the students' own reasoning traces. Every
version, edit, rationale, and trace is saved. The result is a **dynamic,
contamination-resistant benchmark** where success depends on genuine
complexity-class reasoning rather than memorization — and a record of *how* and *where*
each model's reasoning breaks.

---

## 2. Why this, and why now (the motivation we can defend)

Our first static run gave suspiciously high accuracy (gpt-oss 97.9%). Two reviewer
objections follow:

1. **Contamination** — "these are classic textbook problems; the models memorized them."
2. **Ceiling** — "if everyone scores high, the benchmark doesn't discriminate."

Scaling input size does not fully answer either: a memorized algorithm still applies
under a bigger input, and large inputs punish *code efficiency and Python runtime*, not
reasoning — a model can understand the problem perfectly and still time out. That is a
weak signal for a **reasoning** benchmark.

The agentic approach answers both objections directly:
- **Contamination** → problems are continuously **re-authored** by the teacher, so any
  given version post-dates the students' training data. This is the accepted
  contamination-resistance strategy in the literature (see §7).
- **Ceiling** → difficulty is **anchored to actual model failure**, not to fixed labels,
  so the benchmark self-calibrates to stay discriminative.

**Crucially, difficulty here means conceptual, not computational.** Small inputs (easy
to verify by hand) with framings that are hard to *reason about* correctly. This keeps
the benchmark measuring thinking, not runtime.

---

## 3. Roles

| Role | Model(s) | Job |
|------|----------|-----|
| **Teacher / Editor** | 1 strong closed-source (e.g. GPT / Claude / Gemini) | Rewrites statements and test cases to induce student reasoning failures |
| **Students (feedback panel)** | 3+ open-source (qwen3, gemma3, gpt-oss) + optionally 1 closed-source | Attempt each version; their code AND reasoning traces are the feedback signal |
| **Held-out students** | ≥1 open-source + the strong closed-source models NOT used as teacher | Never seen by the teacher during hardening; used ONLY to test whether hardness transfers |
| **Validity gate (Orchestrator)** | deterministic checks + optionally a separate verifier model | Approves/rejects every teacher edit; protects ground truth |

**Why held-out models matter:** if the teacher tunes only against qwen/gemma/gpt-oss,
we risk a benchmark that is hard *for those three* and trivial for frontier models. The
held-out panel is what lets us claim the hardness is **real and transferable**, not a
model-specific quirk. This is the difference between an anecdote and a result.

---

## 4. The two attack surfaces

The teacher operates on **two fronts**, each with a different objective:

### 4a. Statement hardening (conceptual reasoning attack)
Rewrite the problem *description* so a careful reasoner still succeeds but a
pattern-matcher fails. On-thesis moves (allowed):
- **Obscure the complexity-class cue.** Describe a tractable structure operationally
  instead of naming it (e.g. "each node has exactly one parent and there are no cycles
  among parents" instead of "the graph is a tree"), so a model that relied on the label
  now has to *recognize* the structure.
- **Misdirection toward the wrong regime.** Frame an easy (P) problem so it superficially
  resembles its NP-complete sibling → model over-engineers an exponential solution.
  Or frame an NP-complete problem so it looks tractable → model writes a fast wrong
  heuristic. (This is exactly our P/NPC/infeasible axis, weaponized.)
- **Disguise infeasibility.** Hide the contradiction so the model confidently "solves"
  a problem that has no solution → drives the confident-wrong rate up.

### 4b. Test-case hardening (coverage attack)
Strengthen the *test suite* to catch solutions that pass by luck. On-thesis moves:
- Add **boundary and adversarial inputs** that a correct-but-shortcut solution fails
  (edge cases, the specific structure that breaks a greedy heuristic, the instance
  where an approximate answer diverges from optimal).
- Add the **input that separates the intended algorithm from a plausible wrong one**
  (e.g. the case where "print the first triangle" ≠ "print the smallest triangle").

The two fronts are complementary: statement hardening makes models *write* wrong code;
test hardening makes sure wrong code is *caught*. Both are logged separately.

---

## 5. The non-negotiable constraint: the validity gate

**Every teacher edit — to a statement or a test case — must pass a validity gate before
it is accepted.** Without this, the teacher drifts the problem into something our answer
key no longer matches, and the benchmark silently corrupts. The gate checks:

For **statement edits**:
1. **Ground truth preserved** — the existing `reference.py` still produces the correct
   answer for the rewritten statement. (If the edit changed the actual answer, reject.)
2. **Class preserved** — the complexity class (P/NPC/infeasible) is unchanged. The
   teacher may make a class *harder to detect*, never *change what it is*.
3. **No ambiguity / contradiction** — the rewritten statement is still unambiguous and
   solvable. A careful human (or a separate verifier model) must still get it right.
4. **No class leakage** — the rewrite didn't accidentally name the class.

For **test-case edits**:
1. **Reference agreement** — the new input's expected output is produced by running
   `reference.py` (unlimited offline time), never hand-authored.
2. **Validity** — the input satisfies the problem's stated constraints.

**Design rule:** the teacher's objective is *not* "minimize student accuracy by any
means." It is **"maximize the gap between a careful reasoner and a pattern-matcher,
subject to the validity gate."** Optimizing raw failure produces ambiguity and noise
(cheap, uninteresting). Optimizing the *reasoning gap* under validity produces genuine
conceptual difficulty (our contribution). This distinction is what separates our work
from a generic adversarial-paraphrase paper.

---

## 6. The loop (one family, one iteration)

```
For a given problem version v_t:

1. GENERATE   Each student model solves v_t. Save: code + full reasoning trace + verdict.
2. ANALYZE    Teacher reads the students' traces. Identifies the shared reasoning move
              that led to success (the "crutch") — e.g. "all students keyed off the word
              'tree' to pick the linear-time DP."
3. EDIT       Teacher proposes v_{t+1}: a statement rewrite and/or test-case additions
              that remove the crutch / target the identified weakness. Saves its rationale.
4. GATE       Validity gate checks v_{t+1} (ground truth preserved, class preserved,
              unambiguous, reference-generated outputs). If it fails, reject and ask the
              teacher to revise (bounded retries).
5. RE-TEST    Students solve v_{t+1}. Measure the change in the reasoning gap.
6. TRANSFER   Periodically, run held-out models on v_{t+1} to confirm hardness generalizes.
7. STOP       When the gap stops widening, or a max-iteration budget is hit, or the gate
              can no longer find a valid harder edit. Finalize the version.
```

**Finalization is failure-anchored:** a version is "done" when it reliably separates
reasoners from pattern-matchers — difficulty grounded in real model behavior, not labels.

---

## 7. What we save (provenance — half the paper's evidence)

Everything, versioned, per problem:
- `v0` = the frozen original statement + tests (the control / baseline arm).
- `v1, v2, …` = each hardened version: statement, tests, teacher edit + rationale.
- Per student per version: generated code, **full reasoning trace**, verdict, error type.
- Per version: validity-gate result (pass/fail + reason), and held-out transfer results.
- The **trajectory**: how the reasoning gap evolved across iterations.

This record supports every claim: contamination-resistance (versions post-date training),
the reasoning-gap effect (traces show the crutch being removed), transfer (held-out
results), and a taxonomy of *how* models fail (error types across versions).

---

## 8. Metrics (what we report)

- **Reasoning gap** per version: (careful-reasoner accuracy) − (pattern-matcher accuracy),
  or more concretely the accuracy spread across the student panel, and the P vs NPC gap.
- **Degradation curve**: student accuracy vs iteration — does hardening reliably reduce it?
- **Transfer**: held-out model accuracy on hardened vs original versions. **The headline
  claim depends on this.**
- **Confident-wrong rate on infeasible** across versions — does disguising infeasibility
  raise hallucinated-solution rates?
- **Failure taxonomy**: distribution of error types (wrong algorithm class, TLE from
  over-engineering, confident-wrong, runtime error) and how it shifts as problems harden.

---

**Our one-line contribution claim:**
> *An agentic teacher–student framework that adversarially hardens both the statements
> and the test cases of complexity-class triples (P / NP-complete / infeasible), guided by
> student reasoning traces and protected by an executable validity gate, yielding a
> dynamic, contamination-resistant benchmark that isolates genuine complexity-class
> reasoning from memorization and surface pattern-matching.*

No existing paper combines: complexity-class control + executable ground-truth validity
gate + dual (statement + test) hardening + reasoning-trace-guided editing. That
intersection is the novelty.

---

## 9. Proposed build order (staged, each verified before the next)

1. **Multi-provider API layer** — GPT, Claude, Gemini, OpenRouter, each with an enable
   flag and a role assignment (teacher / student / held-out). Reuse existing backends.
2. **The validity gate** — the single most important component. Build and unit-test it
   *before* any editing loop: given an edited statement + the reference, confirm ground
   truth holds and class is preserved; given a new test input, generate its output from
   the reference and validate constraints.
3. **Provenance store** — versioned per-problem directory (`v0`, `v1`, …) with statements,
   tests, edits, rationales, student traces, gate results, transfer results.
4. **Single-step edit, one family** — teacher reads one panel's traces, proposes one
   statement edit + one test edit, gate checks, re-test. Verify end to end.
5. **Full loop + transfer** — iterate, version, hold-out transfer, stopping rule.
6. **Pilot on 3–4 families**, review results, then scale to all 48.

We will implement this exactly as before: numbered Markdown instruction files handed to
Claude Code one at a time, each self-contained and validated before the next.

---

## 10. What stays fixed from the existing project

- The **48 base problems remain frozen as `v0`** — the control arm. We never overwrite them.
- The **reference solutions are the ground truth** and are never rewritten by the teacher;
  they are only *used* by the gate to validate edits and generate outputs.
- The **harness** (runner, checker, verdicts, the hardened timeout) is reused unchanged.
- **Statements still never name the complexity class** — the teacher must respect this.
