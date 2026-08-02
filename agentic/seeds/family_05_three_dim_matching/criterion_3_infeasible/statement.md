# Problem C — Unassignable Worker

Time limit: 1 s   Memory limit: 256 MB

## Description

There are **k** workers (numbered 1..k) and **k** tasks (numbered 1..k). Each worker can only handle certain tasks; you are given a list of allowed `(worker, task)` pairs.

A valid plan would assign each worker one distinct allowed task. In the input you are given, **at least one worker has no allowed task at all**, so no valid plan can exist.

Report the smallest-numbered worker that has no allowed task.

## Input

The first line contains two integers **k** and **e** (1 ≤ k ≤ 1000, 0 ≤ e ≤ 100000): the number of workers/tasks and the number of allowed pairs.
Each of the next **e** lines contains two integers **x** and **y** (1 ≤ x, y ≤ k), meaning worker x is allowed to do task y. No pair is listed more than once. It is guaranteed that at least one worker appears in no pair.

## Output

Print a single integer: the smallest-numbered worker that has no allowed task.

## Examples

### Example 1

**Input**
```
3 2
1 1
3 3
```

**Output**
```
2
```

### Example 2

**Input**
```
4 3
2 1
3 2
4 4
```

**Output**
```
1
```

## Note

In Example 1, worker 2 appears in no allowed pair, so worker 2 can never be assigned a task.
