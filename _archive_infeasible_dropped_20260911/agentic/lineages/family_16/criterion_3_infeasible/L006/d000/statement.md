# SLA Rejection Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud computing platform provides a two-stage pipeline for processing client requests. A batch of **j** jobs has been submitted, which must pass through exactly **two** machines. To maintain data integrity, every job must be processed on machine 1 first and then on machine 2. Each machine can only process one job at a time, and a job can only arrive at machine 2 after it has completely finished on machine 1.

The client has requested a strict Service Level Agreement (SLA) deadline of **T** milliseconds: all **j** jobs must be completely finished by time **T**.

For every input in this problem, the requested SLA is guaranteed to be impossible to meet, regardless of how the jobs are scheduled. Your task is to generate a short rejection certificate that proves the deadline is impossible, which is verifiable directly against the input.

Exactly one of the following rejection reasons always applies. Print the one that holds:

- **A single job is too long.** If a specific job's processing times on both machines add up to more than **T**, that job alone (running on machine 1 then machine 2, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based index) is such a job.

- **A machine is overloaded.** Because a machine processes jobs one at a time, it requires a time span at least equal to the sum of all its processing times. If the total processing time required on machine 1 (or machine 2) exceeds **T**, the deadline is impossible.
  Print: `LOAD c` — where **c** is 1 or 2, representing the machine whose total processing time exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing times of a job on machine 1 and machine 2, respectively.

## Output

Print a single line: `JOB i` (where a job's p1 + p2 exceeds T) or `LOAD c` (where machine c's total load exceeds T).

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

In Example 1, job 1 needs 70 + 60 = 130 > 100 milliseconds in sequence, so `JOB 1` proves the SLA is impossible. In Example 2 no single job exceeds 150, but machine 1 must process 50+50+50+50 = 200 > 150 milliseconds of work in total, so `LOAD 1` is the rejection certificate.
