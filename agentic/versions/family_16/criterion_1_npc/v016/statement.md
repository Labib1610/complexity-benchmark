# Problem A — Manufacturing Plant Timetable

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing plant operates $m$ distinct workstations and needs to fulfill $j$ production orders. Each order requires a specific sequence of tasks to be completed. Every task specifies which workstation it needs and the exact number of time units it takes.

The production process must adhere to the following conditions:
- The tasks for any given order must be performed in the exact sequence they are listed. A task can only commence after the preceding task for that same order has fully concluded.
- A workstation can process at most one task at any given time.
- Once a workstation starts a task, it must continue processing it without interruption until the task's required duration is met.

Your objective is to organize the tasks such that the final task of the last completed order finishes as early as possible. Output this earliest possible completion time.

## Input

The first line provides two integers $j$ and $m$ (1 ≤ $j$ ≤ 10, 1 ≤ $m$ ≤ 10), representing the number of production orders and the number of workstations, respectively.

Each of the subsequent $j$ lines details a single production order. A line begins with an integer $o$, representing the number of tasks in that order. This is followed by $o$ pairs of integers, where each pair denotes `workstation duration` (1 ≤ workstation ≤ $m$, 1 ≤ duration ≤ 1000) for a task. The pairs are listed in the strict sequence the tasks must be performed.

The input is guaranteed to satisfy the following conditions:
- The total number of tasks across all production orders combined will not exceed 50.
- No single production order will contain more than 50 tasks.
- No single workstation will be assigned more than 50 tasks across all orders.
- The sum of the durations of all tasks across all orders is at most 50,000.

## Output

Print a single integer representing the earliest possible time at which all production orders are entirely finished.

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

In Example 1, there are two identical production orders that both require workstations 1, 2, and 3 in sequence (spending 2 time units at each). The second order can follow the first one closely, allowing both to be finished by time 8. In Example 3, the two orders utilize different workstations and can be executed simultaneously, finishing at time 4.
