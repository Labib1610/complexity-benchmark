# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A system processes **j** jobs through exactly two sequential stages. Every job must clear stage 1 completely before it can enter stage 2. For each job, you are given its required duration in stage 1 and in stage 2. A stage can only advance one job at any given moment.

There is a required time limit **T**: every job must be completely finished by time **T**.

For every input in this problem, it is guaranteed that the time limit cannot be met, no matter how the jobs are ordered. Your task is to prove the time limit is impossible by outputting a short certificate that can be checked directly against the input. 

Exactly one of the following reasons will always apply. Print the certificate for the one that holds:

* `JOB i` (where **i** is a 1-based index): Certifies that job **i** cannot possibly finish by the deadline due to its own sequential stage requirements, even if it were scheduled optimally as the only job in the system.
* `LOAD c` (where **c** is either 1 or 2): Certifies that stage **c** cannot possibly process all its assigned work by the deadline due to its serial processing constraint, even if it never had to wait for the other stage.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a job in stage 1 and stage 2.

## Output

Print a single line containing either `JOB i` (where job **i**'s isolated requirements exceed the deadline) or `LOAD c` (where the total volume of work for stage **c** exceeds the deadline).

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

In Example 1, `JOB 1` proves the time limit is impossible because job 1 alone requires more time across its two stages than the 100 units available. 
In Example 2, `LOAD 1` is the certificate because stage 1 is assigned more total sequential work than could possibly be completed in 150 time units.