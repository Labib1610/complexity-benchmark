# Problem A — System Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A computing system has **m** resources and must process **j** queries. Each query is a fixed sequence of steps; each step must run on a specific resource for a given number of cycles. The rules are:

- The steps of a query must run in their listed order (a step starts only after the previous step of the same query has finished).
- Each resource processes only one step at a time.
- Once started, a step runs to completion (no interruption).

Coordinate all steps so that the cycle at which the **last** step finishes is as small as possible. Report that smallest possible finish cycle.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one query: an integer **o** (the number of steps) followed by **o** pairs of integers `resource duration` (1 ≤ resource ≤ m, 1 ≤ duration ≤ 1000), listing the query's steps in order.
The total number of steps across all queries is at most 50.

## Output

Print a single integer: the smallest possible cycle at which all queries are finished.

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

In Example 1, two identical queries each pass through resources 1, 2, 3 (2 cycles each); the second query trails the first through the pipeline and finishes at cycle 8. In Example 3 the two queries use different resources and run in parallel, finishing at cycle 4.
