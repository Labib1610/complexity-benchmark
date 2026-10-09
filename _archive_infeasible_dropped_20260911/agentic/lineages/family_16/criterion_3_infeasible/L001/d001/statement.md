# Problem C — Impossible Time Limit: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A system executes **j** tasks through exactly **two** stages. Every task is executed in stage 1 first and then in stage 2. For each task you are given its duration in stage 1 and in stage 2. Each stage handles only one task at a time, and a task reaches stage 2 only after finishing in stage 1.

There is a required time limit **T**: every task must be completely finished by time **T**.

For every input in this problem it is **guaranteed that the time limit cannot be met**, no matter how the tasks are ordered. Your goal is not to search for an arrangement; it is to **prove** the time limit is impossible with a short certificate that can be checked directly against the input.

It is guaranteed that exactly one of the following two types of bottlenecks applies to the input. You must output a valid certificate of the applicable type. If multiple valid certificates of that type exist, you may output any one of them.

- **Task bottleneck:** A single task, even if running entirely by itself in the system, cannot complete its required sequence of stages within the time limit.
  Print: `JOB i` — where **i** (1-based) is the index of such a task.

- **Stage bottleneck:** A single stage cannot process all of its assigned work within the time limit, even if we assume tasks never experience any waiting time between stages.
  Print: `LOAD c` — where **c** is 1 or 2, representing a stage that has too much total work to finish by the time limit.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a task in stage 1 and stage 2.

## Output

Print a single line containing a valid certificate of the applicable type: either `JOB i` (for a task bottleneck) or `LOAD c` (for a stage bottleneck).

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

In Example 1, task 1 cannot finish its required sequence within 100 time units even if it runs alone, so `JOB 1` proves the time limit is impossible. In Example 2 no single task exceeds 150 on its own, but stage 1 must process 200 units of work in total, which exceeds the 150 time limit, so `LOAD 1` is a valid certificate.