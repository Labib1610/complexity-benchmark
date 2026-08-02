# Problem B — Task Assignment

Time limit: 2 s   Memory limit: 256 MB

## Description

There are **k** workers (numbered 1..k) and **k** tasks (numbered 1..k). Each worker can only handle certain tasks; you are given a list of allowed `(worker, task)` pairs.

Assign to each worker exactly one task so that:

- every worker is assigned an allowed task, and
- no two workers are assigned the same task.

(Because there are equally many workers and tasks, this means every task is used exactly once.)

Determine whether such an assignment exists, and if so report one.

## Input

The first line contains two integers **k** and **e** (1 ≤ k ≤ 1200, 0 ≤ e ≤ 800000): the number of workers/tasks and the number of allowed pairs.
Each of the next **e** lines contains two integers **x** and **y** (1 ≤ x, y ≤ k), meaning worker x is allowed to do task y. No pair is listed more than once.

## Output

If a valid assignment exists, print `YES` on the first line, then on the second line print **k** integers where the i-th integer is the task assigned to worker i. Any assignment satisfying the rules is accepted.

If no valid assignment exists, print `NO`.

## Examples

### Example 1

**Input**
```
3 4
1 1
1 2
2 1
3 3
```

**Output**
```
YES
2 1 3
```

### Example 2

**Input**
```
2 2
1 1
2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1
```

**Output**
```
YES
1
```

## Note

In Example 2, both workers can only do task 1, so they cannot be given distinct tasks.
