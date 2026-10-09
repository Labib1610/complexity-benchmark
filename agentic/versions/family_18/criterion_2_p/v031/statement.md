# Problem B — Pipeline Task Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A processing pipeline schedules its tasks across a single timeline of execution slots, one task per slot, with as many slots as tasks — a one-to-one assignment of tasks onto positions numbered along the timeline. The information handovers between tasks form a strict hierarchy: apart from a single top-level task, every task receives data from exactly one parent task, so the handover links form a connected, loop-free structure spanning all tasks.

Each handover link incurs a wait time whose duration equals the number of slot positions between the two tasks it joins; processing details and handover direction do not affect this duration. The pipeline has a single **total** wait budget covering the sum of all link durations — there is no per-link cap and no restriction on handovers spanning the same period.

Find a one-to-one assignment of the tasks onto the timeline whose total link duration is at most the budget, or report that the budget cannot be met. (Because the links form a hierarchy rather than an arbitrary web, the structure is more regular than a general network, but the total-duration objective is still what must be respected.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — a link.
(The structure is a strict hierarchy: m = n-1.)

## Output
Print `YES` then a line with n integers — the position (1..n, a permutation) of task 1,2,...,n —
such that the total wait is <= B. Otherwise print `NO`.

## Example
**Input:**
```
4 3 4
1 2
1 3
1 4
```

**Output:**
```
YES
2 1 3 4
```
