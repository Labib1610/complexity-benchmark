# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A system processes **j** jobs through exactly two sequential stages. Every job must clear stage 1 completely before it can enter stage 2. For each job, you are given its required duration in stage 1 and in stage 2. A stage can only advance one job at any given moment.

There is a required time limit **T**: every job must be completely finished by time **T**.

For every input in this problem, it is guaranteed that the time limit cannot be met, no matter how the jobs are ordered. Your task is to prove the time limit is impossible by outputting a short certificate that can be checked directly against the input. 

Exactly one of the following reasons will always apply. Print the certificate for the one that holds:

* `JOB i` (where **i** is a 1-based index): If job **i** were to start at time 0 and transition between stages instantly without waiting, it would still be active strictly after time **T**.
* `LOAD c` (where **c** is either 1 or 2): If stage **c** were to process its assigned tasks back-to-back with zero idle time starting at time 0, it would still be active strictly after time **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a job in stage 1 and stage 2.

## Output

Print a single line containing either `JOB i` (where job **i** alone requires a schedule extending past the deadline) or `LOAD c` (where stage **c**'s continuous operation extends past the deadline).

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

In Example 1, `JOB 1` proves the time limit is impossible because if job 1 starts at time 0 and transitions instantly, it remains active for 130 units, which extends strictly after the 100 units available. 
In Example 2, `LOAD 1` is the certificate because if stage 1 processes its assigned tasks back-to-back starting at time 0, it requires 200 units of continuous operation, meaning it is still active strictly after time 150.