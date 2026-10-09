# Problem A — Studio Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A studio has **m** workstations and must complete **j** projects. Each project is a fixed sequence of steps; each step requires a specific workstation for a given number of hours. The rules are:

- The steps of a project must be performed in their listed order (a step starts only after the previous step of the same project has finished).
- Each workstation handles only one step at a time.
- Once started, a step runs to completion without interruption.

Arrange all steps so that the time at which the last step finishes is as small as possible. Report that smallest possible completion time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one project: an integer **o** (the number of steps) followed by **o** pairs of integers `workstation duration` (1 ≤ workstation ≤ m, 1 ≤ duration ≤ 1000), listing the project's steps in order.
The total number of steps across all projects is at most 50.

## Output

Print a single integer: the smallest possible time at which all projects are finished.

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

In Example 1, two identical projects each pass through workstations 1, 2, 3 (2 hours each); the second project trails the first through the process and finishes at hour 8. In Example 3 the two projects use different workstations and run in parallel, finishing at hour 4.
