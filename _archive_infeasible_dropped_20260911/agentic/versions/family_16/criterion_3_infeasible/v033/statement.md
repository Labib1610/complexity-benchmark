# Problem C — Unachievable Target: Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

A data pipeline processes **j** independent workloads. The pipeline consists of Node 1 and Node 2. Every workload must be fully resolved by Node 1 before it can be transmitted to Node 2. For each workload, you receive the number of microseconds it must exclusively occupy Node 1 and Node 2. A Node can handle exactly one workload at any given instant.

A strict operational window of **T** microseconds is enforced. Every workload must complete its passage through both Nodes before this window expires. 

For all configurations evaluated by this system, the operational window is structurally insufficient, regardless of the sequence in which workloads are submitted. Do not attempt to find a valid sequence. Instead, your objective is to output a specific diagnostic code that proves the window is insufficient.

The input data is guaranteed to trigger exactly one of the following two diagnostic codes. Output the one that applies:

- **An individual workload exceeds the window.** If the sequential duration required by a single workload (its time on Node 1 plus its time on Node 2) is strictly greater than **T**, output `JOB i`, where **i** (1-based) is the index of such a workload.
- **A Node's cumulative volume exceeds the window.** Since a Node cannot process workloads concurrently, its minimum active time is the sum of its requirements across all workloads. If this sum for Node **c** (where **c** is 1 or 2) is strictly greater than **T**, output `LOAD c`.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the microseconds a workload requires on Node 1 and Node 2, respectively.

## Output

Print a single line containing the applicable diagnostic code: either `JOB i` or `LOAD c`.

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

In Example 1, workload 1 requires 70 + 60 = 130 > 100 microseconds in sequence, so `JOB 1` proves the window is insufficient. In Example 2, no single workload exceeds 150, but Node 1 must process 50+50+50+50 = 200 > 150 microseconds of volume in total, so `LOAD 1` is the correct diagnostic code.
