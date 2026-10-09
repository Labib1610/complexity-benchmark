# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A processing facility must complete **j** tasks. Each task must first pass through Stage 1, and subsequently through Stage 2. You are given the duration each task requires in Stage 1 and Stage 2. Each stage can only process a single task at any given time, and a task can only begin Stage 2 after its Stage 1 processing is fully complete.

The facility has a hard deadline **T**: all tasks must be entirely finished by time **T**. 

The constraints of the facility guarantee the following two properties for all batches of tasks:
1. The total time any single task spends in both stages combined will never exceed 2,000,000 units.
2. The absolute difference between any task's Stage 1 duration and Stage 2 duration is strictly less than 1,000,000 units.

For every dataset provided, **it is guaranteed that the deadline T is impossible to meet**, regardless of the scheduling order chosen. Your objective is not to find a schedule, but to output a short, verifiable certificate proving the deadline cannot be met.

Exactly one of the following reasons always applies. Print the one that holds:

- **An individual task is too lengthy.** If a task's combined processing time across Stage 1 and Stage 2 is strictly greater than **T**, that task alone (Stage 1 then Stage 2, in sequence) cannot be completed before the deadline. 
  Print: `JOB i` — where **i** (1-based) is the index of such a task.

- **A stage is over-capacitated.** Since each stage processes tasks sequentially, it requires an amount of active time equal to the sum of durations of all tasks assigned to it. If the aggregate processing time required for Stage 1 (or Stage 2) across all tasks is strictly greater than **T**, the deadline cannot be met.
  Print: `LOAD c` — where **c** is the stage number (1 or 2) whose total required time exceeds **T**.

## Input

The first line provides two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
The subsequent **j** lines each contain two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the required time for the task in Stage 1 and Stage 2, respectively.

## Output

Print a single line: `JOB i` (a task whose p1 + p2 exceeds T) or `LOAD c` (a stage c whose total required time exceeds T).

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

In Example 1, task 1 needs 70 + 60 = 130 > 100 time units in sequence, so `JOB 1` proves the deadline is impossible. In Example 2 no single task exceeds 150, but Stage 1 must process 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the certificate.
