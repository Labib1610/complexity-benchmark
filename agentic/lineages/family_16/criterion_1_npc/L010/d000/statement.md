# Problem A — Project Planning

Time limit: 5 s   Memory limit: 256 MB

## Description

A company manages **m** facilities and must complete **j** projects. Each project is a fixed sequence of phases; each phase must run at a specific facility for a given number of cycles. The rules are:

- The phases of a project must run in their listed order (a phase starts only after the previous phase of the same project has finished).
- Each facility processes only one phase at a time.
- Once started, a phase runs to completion (no interruption).

Arrange all phases so that the cycle at which the **last** phase finishes is as small as possible. Report that smallest possible finish cycle.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one project: an integer **o** (the number of phases) followed by **o** pairs of integers `facility duration` (1 ≤ facility ≤ m, 1 ≤ duration ≤ 1000), listing the project's phases in order.
The total number of phases across all projects is at most 50.

## Output

Print a single integer: the smallest possible cycle at which all projects are finished.

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

In Example 1, two identical projects each pass through facilities 1, 2, 3 (2 cycles each); the second project trails the first through the sequence and finishes at cycle 8. In Example 3 the two projects use different facilities and run simultaneously, finishing at cycle 4.
