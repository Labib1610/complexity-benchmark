# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A port authority is processing **j** shipping contracts, tracked in the terminal's queue as `JOB`s. Every `JOB` must first be cleared by the customs scanner (facility 1) and subsequently hoisted by the gantry crane (facility 2). For each `JOB`, you are given its required processing time at facility 1 and facility 2. Each facility handles only one `JOB` at a time, and a `JOB` advances to facility 2 only after its clearance at facility 1 is complete.

There is a hard departure deadline **T**: every `JOB` must be fully processed before time **T** elapses.

For every input in this problem, it is **guaranteed that the departure deadline cannot be met**, regardless of the order in which the terminal schedules the operations. Your task is not to find a schedule, but to **prove** that the deadline is impossible by providing a concise certificate that can be verified directly from the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **A single contract is too lengthy.** If some `JOB`'s two facility times add up to more than **T**, that `JOB` alone (facility 1 then facility 2, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is such a `JOB`.

- **A facility is over-allocated.** A facility handles its `JOB`s one at a time, so it needs at least the sum of all its required times. If the total workload on facility 1 (or facility 2) exceeds **T**, the deadline is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total time on facility **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required times of a `JOB` at facility 1 and facility 2.

## Output

Print a single line: `JOB i` (a `JOB` whose p1 + p2 exceeds T) or `LOAD c` (a facility c whose total required time exceeds T).

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

In Example 1, `JOB` 1 needs 70 + 60 = 130 > 100 time units in sequence, making it impossible to finish by the deadline. Thus, `JOB 1` proves the deadline cannot be met. In Example 2, no individual `JOB` exceeds 150 time units, but facility 1 must process 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the certificate.
