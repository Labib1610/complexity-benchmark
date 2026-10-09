# Render Pipeline: Stage 1

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud rendering engine processes batches of $j$ animation sequences. Every sequence must be processed strictly in order: first by the Geometry Node, and then by the Texture Node. A node can only work on one sequence at a given moment. The overall deadline to finish the entire batch is $T$ milliseconds.

To prevent wasting compute credits on impossible deadlines, the workflow manager executes a preliminary assessment before attempting to build a schedule. The pipeline consists of:

- **Stage 0:** Asset synchronization and dependency resolution.
- **Stage 1:** Feasibility filter (your task).
- **Stage 2:** Heuristic scheduling and timeline allocation.
- **Stage 3:** Distributed execution.

You are responsible for implementing Stage 1. This stage evaluates the raw time requirements and halts the pipeline if the deadline $T$ is structurally impossible to meet. It identifies two specific failure modes:

- **Sequential Violation:** If a single sequence $i$ has a combined processing time across both nodes that is strictly greater than $T$, the pipeline must halt and output `JOB i` (where $i$ is the 1-based index of such a sequence).
- **Capacity Violation:** If the sum of processing times of all sequences on the Geometry Node exceeds $T$, output `LOAD 1`. If the sum of processing times of all sequences on the Texture Node exceeds $T$, output `LOAD 2`.

For this assignment, you only need to simulate Stage 1. You are guaranteed that every test case provided will trigger exactly one of these two violation categories, meaning the pipeline will always halt at Stage 1. Your program must simply output the corresponding error code.

## Input

The first line contains two integers $j$ and $T$ (1 ≤ $j$ ≤ 200,000, 1 ≤ $T$ ≤ 1,000,000,000).
The following $j$ lines each contain two integers $p_1$ and $p_2$ (1 ≤ $p_1, p_2$ ≤ 1,000,000). These represent the milliseconds required by that sequence on the Geometry Node and the Texture Node, respectively.

## Output

Print a single line containing the exact failure code: either `JOB i` (for a sequence $i$ where $p_1 + p_2 > T$) or `LOAD c` (where $c$ is the node, 1 for Geometry or 2 for Texture, whose total required time exceeds $T$).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, sequence 1 requires 70 + 60 = 130 milliseconds sequentially. Because 130 > 100, it triggers a Sequential Violation. The program halts and outputs `JOB 1`.
In Example 2, no individual sequence exceeds the 150-millisecond deadline. However, the total time required on the Geometry Node is 50 + 50 + 50 + 50 = 200 milliseconds. Because 200 > 150, it triggers a Capacity Violation, resulting in `LOAD 1`.
