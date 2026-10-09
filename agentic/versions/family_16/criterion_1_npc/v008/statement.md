# Problem A — Production Pipeline Scheduler

Time limit: 5 s   Memory limit: 256 MB

## Description

In our automated manufacturing pipeline, customer orders are first compiled into job tickets and sent to the scheduling module. Once a schedule is finalized, it is transmitted to the factory floor software for physical execution. Your task is to implement the central scheduling module.

The factory has **m** machines and must process **j** jobs. Each job is a fixed sequence of operations; each operation must run on a specific machine for a given number of time units. The rules are:

- The operations of a job must run in their listed order (an operation starts only after the previous operation of the same job has finished).
- Each machine processes only one operation at a time.
- Once started, an operation runs to completion (no interruption).

Schedule all operations so that the time at which the **last** operation finishes is as small as possible. Report that smallest possible finish time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one job: an integer **o** (the number of operations) followed by **o** pairs of integers `machine duration` (1 ≤ machine ≤ m, 1 ≤ duration ≤ 1000), listing the job's operations in order.
The total number of operations across all jobs is at most 50.

## Output

Print a single integer: the smallest possible time at which all jobs are finished.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical jobs each pass through machines 1, 2, 3 (2 time units each); the second job trails the first through the pipeline and finishes at time 8. In Example 3 the two jobs use different machines and run in parallel, finishing at time 4.
