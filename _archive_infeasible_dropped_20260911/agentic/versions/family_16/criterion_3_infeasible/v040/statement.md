# Problem C — System Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

A factory processes **j** jobs through exactly **two** machines. Every job is processed on machine 1 first and then on machine 2. For each job you are given its processing time on machine 1 and on machine 2. Each machine processes only one job at a time, and a job reaches machine 2 only after finishing on machine 1.

There is a required deadline **T**: every job must be completely finished by time **T**.

Your task is to evaluate the system constraints and generate a diagnostic certificate. Exactly one of the following limit violations will always apply to the given input. Print the one that holds:

- **A single job is too long.** If some job's two processing times add up to more than **T**, print: `JOB i` — where **i** (1-based) is such a job.

- **A machine is overloaded.** If the total processing time of all jobs on machine 1 (or machine 2) exceeds **T**, print: `LOAD c` — where **c** is 1 or 2 and the total processing time on machine **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing times of a job on machine 1 and machine 2.

## Output

Print a single line: `JOB i` (a job whose p1 + p2 exceeds T) or `LOAD c` (a machine c whose total load exceeds T).

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

In Example 1, job 1 requires 70 + 60 = 130 > 100 time units, so `JOB 1` is the correct diagnostic output. In Example 2, no single job exceeds 150, but machine 1 must process 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the certificate.
