# Problem C — Unmeetable Quota Verification

Time limit: 2 s   Memory limit: 256 MB

## Description

A distributed computing cluster is assigned a batch of **j** jobs. The cluster consists of exactly two sequential processing nodes. Every job must be processed first on Node 1, and subsequently on Node 2. Each node is single-threaded and can process only one job at a time. A job can only be transferred to Node 2 after its Node 1 execution has completely finished.

The entire batch of jobs must be fully completed by a hard deadline of **T** cycles from the start.

Due to hardware constraints, the following invariants are guaranteed for every batch:
- The maximum sequential execution time for any single job across both nodes is strictly less than $2,000,001$ cycles.
- The total aggregate processing time required on Node 1 across all jobs is at most $200,000,000,000$ cycles, and the same holds for Node 2.
- The number of jobs **j** is always strictly less than **T** + $200,000$.

For every batch provided to your program, it is **guaranteed that the deadline T cannot be met**, regardless of the scheduling order. Your task is not to find a schedule, but to output a short certificate proving that the deadline is impossible. 

Exactly one of the following reasons always applies. Print the one that holds:

- **Sequential Bottleneck:** If some job's processing time on Node 1 plus its processing time on Node 2 strictly exceeds **T**, that job alone (Node 1 then Node 2, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is such a job.

- **Resource Overcommitment:** A node runs its jobs one at a time, so it needs at least the sum of all its processing times. If the total required cycles on Node 1 (or Node 2) strictly exceeds **T**, the deadline is impossible.
  Print: `LOAD c` — where **c** is 1 or 2, and the total processing time on Node **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing times of a job on Node 1 and Node 2.

## Output

Print a single line: `JOB i` (a job whose p1 + p2 exceeds T) or `LOAD c` (a node c whose total load exceeds T).

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

In Example 1, job 1 needs 70 + 60 = 130 > 100 cycles in sequence, so `JOB 1` proves the deadline is impossible. In Example 2 no single job exceeds 150, but Node 1 must process 50+50+50+50 = 200 > 150 cycles of work in total, so `LOAD 1` is the certificate.
