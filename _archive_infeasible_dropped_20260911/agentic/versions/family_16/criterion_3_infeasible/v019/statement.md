# Problem C — Pre-flight Validation Module

Time limit: 2 s
Memory limit: 256 MB

## Description

The automated batch-processing pipeline consists of three stages: Intake, Pre-flight Validation, and Heuristic Scheduling. You are responsible for implementing the **Pre-flight Validation** module.

During the **Intake** stage, a client submits a batch of $j$ tasks and a maximum latency budget $T$. Every task requires sequential processing: it must first be processed by Subsystem 1, and only after completion can it be processed by Subsystem 2. Each subsystem is strictly serial and can only process one task at a time.

Your **Pre-flight Validation** module runs next. Its purpose is to quickly reject batches that are physically impossible to complete within the budget $T$, bypassing the computationally expensive **Heuristic Scheduling** stage. For this problem, every submitted batch is guaranteed to fail validation. Your module must not search for a schedule; instead, it must generate a short rejection certificate proving the batch is invalid.

Exactly one of the following two structural violations will be present in every batch. Your module must identify which rule is violated and print the corresponding rejection code:

- **Isolated Task Violation:** A task's total minimum processing time (its duration on Subsystem 1 plus its duration on Subsystem 2) strictly exceeds the latency budget $T$. Even without any other tasks, this task alone would fail.
  Output: `JOB i` (where `i` is the 1-based index of such a task).

- **Subsystem Saturation:** Because a subsystem can only process one task at a time, it requires a total active time equal to the sum of its assigned durations for all tasks. If this total active time on Subsystem 1 (or Subsystem 2) strictly exceeds the budget $T$, the batch cannot be completed.
  Output: `LOAD c` (where `c` is the subsystem number, 1 or 2, whose total duration exceeds $T$).

## Input

The first line provides two integers $j$ and $T$ (1 ≤ $j$ ≤ 200000, 1 ≤ $T$ ≤ 1000000000), representing the number of tasks in the batch and the latency budget, respectively.
Each of the following $j$ lines provides two integers $p_1$ and $p_2$ (1 ≤ $p_1, p_2$ ≤ 1000000). These are the processing durations of the task on Subsystem 1 and Subsystem 2.

## Output

Print a single line containing the rejection certificate: either `JOB i` (for a task whose combined duration $p_1 + p_2$ exceeds $T$) or `LOAD c` (for a subsystem $c$ whose total sum of durations exceeds $T$).

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

In Example 1, the first task requires 70 + 60 = 130 time units across both subsystems. Since 130 > 100, the task violates the budget on its own, so `JOB 1` is the correct rejection code.
In Example 2, no individual task exceeds the budget of 150. However, Subsystem 1 must process tasks sequentially for a total of 50 + 50 + 50 + 50 = 200 time units. Since 200 > 150, Subsystem 1 is saturated, making `LOAD 1` the correct rejection code.
