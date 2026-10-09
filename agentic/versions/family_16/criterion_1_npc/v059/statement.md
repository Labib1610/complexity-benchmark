# Problem A — Manufacturing Floor

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing floor has **m** fabricators and must construct **j** blueprints. Each blueprint consists of a strict sequence of stages; each stage requires the exclusive use of a specific fabricator for a continuous number of time units. The rules are:

- The stages of a blueprint must be executed in the exact order they are listed. A stage cannot begin until the preceding stage for that same blueprint is fully completed.
- A fabricator can execute at most one stage at any given moment.
- Once a fabricator starts a stage, it cannot be interrupted until that stage is done.

Determine the timing for all stages such that the moment the final stage is completed is as early as possible. Output this earliest possible completion time.

## Input

The first line contains two integers **j** and **m** (there is at least 1 blueprint and up to 10, limited by the active loading docks; similarly, there is at least 1 fabricator and up to 10, limited by the available power phases).
Each of the next **j** lines describes one blueprint: an integer **o** (the number of stages) followed by **o** pairs of integers `fabricator_index duration` (the fabricator index is between 1 and **m**; the duration is at least 1 and capped at the part's thermal limit of 1000), listing the blueprint's stages in order.
The total number of stages across all blueprints is limited to at most 50 by the factory's inventory of tracking tags.

## Output

Print a single integer: the earliest possible time at which all blueprints are completely constructed.

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

In Example 1, two identical blueprints each pass through fabricators 1, 2, and 3 (taking 2 time units each); the second blueprint trails the first through the sequence and finishes at time 8. In Example 3, the two blueprints use different fabricators and run concurrently, finishing at time 4.
