# Problem B — Production Scheduling for a Dependency Hierarchy

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing plant schedules its production tasks along a single timeline of consecutive hours, one task per hour, with as many hours as tasks — a one-to-one placement of tasks onto hours numbered along the timeline. The dependency relationships between tasks form a strict hierarchy: apart from a single final task, every task feeds directly into exactly one consumer task, so the dependency links form a connected, loop-free structure spanning all tasks.

Each dependency link incurs a holding cost whose amount equals the number of hours between the two tasks it joins; storage details and execution order do not affect this cost. The plant has a single **total** holding budget covering the sum of all link costs — there is no per-link cap and no restriction on items sharing the warehouse.

Find a one-to-one placement of the tasks onto the timeline whose total link cost is at most the budget, or report that the budget cannot be met. (Because the links form a hierarchy rather than an arbitrary web, the structure is more regular than a general network, but the total-cost objective is still what must be respected.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — a dependency link.
(The structure is a hierarchy: m = n-1.)

## Output
Print `YES` then a line with n integers — the hour (1..n, a permutation) of task 1,2,...,n —
such that the total cost is <= B. Otherwise print `NO`.

## Example

### Input
```
5 4 5
1 2
1 3
3 4
3 5
```

### Output
```
YES
2 1 3 5 4
```
