# Problem C — Impossible Time Limit: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A system executes **j** tasks through exactly **two** stages. Every task is executed in stage 1 first and then in stage 2. For each task you are given its duration in stage 1 and in stage 2. Each stage handles only one task at a time, and a task reaches stage 2 only after finishing in stage 1.

There is a required time limit **T**: every task must be completely finished by time **T**.

For every input in this problem it is **guaranteed that the time limit cannot be met**, no matter how the tasks are ordered. Your goal is not to search for an arrangement; it is to **prove** the time limit is impossible with a short certificate that can be checked directly against the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **A single task is too long.** If some task's two durations add up to more than **T**, that task alone (stage 1 then stage 2, in sequence) cannot finish by **T**.
  Print: `JOB i` — where **i** (1-based) is such a task.

- **A stage is overloaded.** A stage runs its tasks one at a time, so it needs at least the sum of all its durations. If the total work in stage 1 (or stage 2) exceeds **T**, the time limit is impossible.
  Print: `LOAD c` — where **c** is 1 or 2 and the total duration in stage **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a task in stage 1 and stage 2.

## Output

Print a single line: `JOB i` (a task whose p1 + p2 exceeds T) or `LOAD c` (a stage c whose total load exceeds T).

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

In Example 1, task 1 needs 70 + 60 = 130 > 100 time units in sequence, so `JOB 1` proves the time limit is impossible. In Example 2 no single task exceeds 150, but stage 1 must process 50+50+50+50 = 200 > 150 units of work in total, so `LOAD 1` is the certificate.
