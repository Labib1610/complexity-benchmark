# Problem A — Kitchen Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description

A restaurant kitchen has **m** workstations and must prepare **j** dishes. Each dish is a fixed sequence of steps; each step must use a specific workstation for a given number of minutes. The rules are:

- The steps of a dish must run in their listed order (a step starts only after the previous step of the same dish has finished).
- Each workstation processes only one step at a time.
- Once started, a step runs to completion (no interruption).

Schedule all steps so that the time at which the **last** step finishes is as small as possible. Report that smallest possible finish time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one dish: an integer **o** (the number of steps) followed by **o** pairs of integers `workstation duration` (1 ≤ workstation ≤ m, 1 ≤ duration ≤ 1000), listing the dish's steps in order.
The total number of steps across all dishes is at most 50.

## Output

Print a single integer: the smallest possible time at which all dishes are finished.

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

In Example 1, two identical dishes each pass through workstations 1, 2, 3 (2 minutes each); the second dish trails the first through the pipeline and finishes at time 8. In Example 3 the two dishes use different workstations and run in parallel, finishing at time 4.
