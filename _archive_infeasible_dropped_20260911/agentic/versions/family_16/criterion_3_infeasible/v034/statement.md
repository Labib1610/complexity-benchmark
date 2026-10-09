# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A creative agency must deliver **j** bespoke advertising jobs. The production pipeline consists of exactly **two** specialists: a Copywriter (specialist 1) and an Illustrator (specialist 2). Every job first requires drafting by the Copywriter, followed by visual design from the Illustrator. For each job, you are given the exact number of hours each specialist requires. A specialist can only focus on one job at a time, and the Illustrator cannot begin their work on a given job until the Copywriter has fully completed the text for it.

There is a strict agency deadline **T**: every job must be completely finished by hour **T**.

For every input in this problem, it is **guaranteed that the deadline cannot be met**, no matter how the jobs are scheduled. Your task is not to search for a schedule; it is to **prove** the deadline is impossible with a short certificate that can be checked directly against the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **A single job is too long.** If some job's two work times add up to more than **T**, that job alone (Copywriter then Illustrator, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is such a job.

- **A specialist is overloaded.** A specialist works on jobs one at a time, so they need at least the sum of all their required work hours. If the total workload assigned to specialist 1 (or specialist 2) exceeds **T**, the deadline is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total work hours for specialist **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the work times of a job for specialist 1 and specialist 2.

## Output

Print a single line: `JOB i` (a job whose p1 + p2 exceeds T) or `LOAD c` (a specialist c whose total load exceeds T).

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

In Example 1, job 1 needs 70 + 60 = 130 > 100 hours in sequence, so `JOB 1` proves the deadline is impossible. In Example 2, no single job exceeds 150, but specialist 1 must complete 50+50+50+50 = 200 > 150 hours of work in total, so `LOAD 1` is the certificate.
