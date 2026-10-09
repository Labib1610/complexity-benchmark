# Problem C — Unmeetable Limit: Prove It

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility handles **j** jobs through exactly **two** stations. Every job is handled at station 1 first and then at station 2. For each job you are given its duration at station 1 and at station 2. Each station handles only one job at a time, and a job reaches station 2 only after finishing at station 1.

There is a required target limit **T**: every job must be completely finished by time **T**.

For every input in this problem it is **guaranteed that the target limit cannot be met**, no matter how the jobs are sequenced. Your task is not to search for a sequence; it is to **prove** the limit is impossible with a short piece of evidence that can be checked directly against the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **A single job takes too much time.** If some job's two durations add up to more than **T**, that job alone (station 1 then station 2, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is such a job.

- **A station has too much work.** A station handles its jobs one at a time, so it needs at least the sum of all its durations. If the total work at station 1 (or station 2) exceeds **T**, the target limit is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total duration at station **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a job at station 1 and station 2.

## Output

Print a single line: `JOB i` (a job whose p1 + p2 exceeds T) or `LOAD c` (a station c whose total load exceeds T).

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

In Example 1, job 1 needs 70 + 60 = 130 > 100 time units in sequence, so `JOB 1` proves the limit is impossible. In Example 2 no single job exceeds 150, but station 1 must handle 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the evidence.
