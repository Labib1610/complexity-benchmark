# Problem A — Shipyard Refitting

Time limit: 5 s   Memory limit: 256 MB

## Description

A shipyard operates **m** distinct specialized facilities and must refit **j** vessels. Each vessel requires a predetermined sequence of refit phases. Each phase dictates which specific facility must be used and the exact number of hours it will take. 

Because modifications build upon prior work, a vessel's phases must be executed in the exact order they are listed, starting a phase only after the previous one concludes. Each facility has the capacity to service only one vessel at a time. Once a facility begins a phase for a vessel, that phase must run to completion without interruption. 

Determine the smallest possible number of hours from the start of the refits until all vessels have completed all of their required phases.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines details the requirements for one vessel: an integer **p** (the number of phases) followed by **p** pairs of integers `facility duration` (1 ≤ facility ≤ m, 1 ≤ duration ≤ 1000), listing the vessel's phases in their required chronological order.
The total number of phases across all vessels is at most 50.

## Output

Print a single integer: the smallest possible number of hours required for all vessels to complete all their phases.

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

In Example 1, two identical vessels each require facility 1, then 2, then 3 (each taking 2 hours). The second vessel trails the first through the facilities, with its final phase concluding at hour 8. In Example 3, the two vessels require different facilities and proceed in parallel, concluding at hour 4.
