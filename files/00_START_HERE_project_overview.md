# 00 — START HERE: Project Overview & Build Order

> **You are Claude Code.** This is the first of a series of instruction files the user will give you **one at a time, in numbered order**. Read this file fully, then **wait** for the user to drop the next file (`01_...md`). Do **not** jump ahead or scaffold things described in later files until you are given them.

## What we are building

A research benchmark called **Complexity-Aware Code Generation**. It tests whether LLMs understand computational complexity structure (P vs NP-complete vs infeasible) when generating code.

The benchmark has **16 problem families**. Each family has **3 criteria**:

- **Criterion 1 — NP-complete** (hard variant)
- **Criterion 2 — P** (a small constraint change makes it polynomial)
- **Criterion 3 — Infeasible** (a constraint change makes it have no valid solution)

So there are **16 × 3 = 48 problems** total.

For every problem we have:
1. A **problem statement** shown to models (must NOT name the complexity class).
2. A **reference solution** (ground truth) we write.
3. **Test cases** (input/output pairs) validated against the reference.

We then take a fixed set of **research models** (open-source via Ollama, closed-source via API), give each model the **same fixed prompt** per problem, collect the code it writes, and run that code against the test cases. The **statements + test cases are the benchmark**; the **model code is what we evaluate**.

Later we add two constraint studies on top of the same dataset:
- **Time-budget study** (strict runtime limit, partial credit).
- **Token-budget study** (cap on generation length).
- **Multi-turn transition study** (complexity class shifts across turns).

These reuse the dataset unchanged — they only change the prompt and the runner config.

## Core design principle (do not violate)

**The dataset is model-agnostic and lives completely separately from any run.**

- Adding a new model later must NOT touch `dataset/`.
- Adding a new family later must NOT require re-running existing models.
- Every experiment is a dated, self-contained folder under `runs/`.

## The build order (the numbered files you will receive)

| File | What it makes |
|------|---------------|
| `00` (this) | Overview. Nothing created yet. |
| `01_scaffold_directories.md` | The full empty directory tree + top-level README. |
| `02_conventions.md` | The five "fixed" convention docs everything depends on. |
| `03_harness.md` | The shared runner, checker, and aggregator code. |
| `04_family_template_family01.md` | Family 1 built end-to-end as the worked template. |
| `05_remaining_families_scaffold.md` | Empty, correctly-structured folders for families 02–16 + a fill-in guide. |
| `06_generation_and_evaluation_drivers.md` | The Phase-2 (generate) and Phase-3 (evaluate) drivers + model registry. |
| `07_constraint_studies.md` | Time-budget, token-budget, and multi-turn study extensions. |

## Global conventions you must follow throughout

- **Language for all reference and model solutions: Python 3.** Single-language keeps the runner and checker simple. Do not introduce other languages unless a later file explicitly says so.
- **I/O model: stdin → stdout.** Every solution reads from standard input and writes to standard output. No file reading inside solutions.
- **Filenames for test cases:** zero-padded two digits — `01.in`, `01.out`, `02.in`, … This is the "number followed" pattern the user referenced: when the user later adds case `07.in`, the tooling must pick it up automatically with no code change.
- **Statements never name the complexity class.** No "this is NP-complete", "this graph is a tree", "this is bipartite", etc., in any `statement.md`. That metadata lives in `meta.yaml`, which models never see.
- **Everything is reproducible from config.** No hard-coded model lists or paths inside logic; read them from YAML.

## What to do right now

1. Acknowledge you have read and understood this overview.
2. Briefly restate the build order back to the user in 2–3 sentences so they can confirm.
3. **Stop and wait** for `01_scaffold_directories.md`. Do not create any files yet.
