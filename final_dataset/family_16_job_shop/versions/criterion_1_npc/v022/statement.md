# Problem A — Quantum Circuit Alignment

Time limit: 5 s
Memory limit: 256 MB

## Description

You are optimizing the execution of $j$ independent quantum sub-routines on a processor with $m$ distinct QPU cores. Each sub-routine is a linear sequence of gate operations. 

Because the sub-routines are strictly sequential, they can be thought of as simple chains of instructions. Your task is merely to interleave their execution to minimize the total time until all sub-routines are complete. 

The execution rules are:
- Within any single sub-routine, its gates must be executed in the exact order they are listed. A gate can only begin after the previous gate in that sub-routine has completely finished.
- Each gate targets a specific QPU core and requires an exact number of nanoseconds to run.
- A QPU core can only process one gate at a time.
- Once a gate begins executing on a core, it runs continuously until its required duration has elapsed.
- Different cores operate independently and can execute gates simultaneously.

Given that the total number of gates across all sub-routines never exceeds 50, you must find the optimal interleaving of core access that minimizes the overall completion time (the exact nanosecond when the final gate of the final sub-routine finishes).

## Input

The first line contains two integers $j$ and $m$ (1 ≤ $j$ ≤ 10, 1 ≤ $m$ ≤ 10), representing the number of sub-routines and the number of available QPU cores.

Each of the next $j$ lines describes a single sub-routine. The line begins with an integer $o$, the number of gates in that sub-routine. This is followed by $o$ pairs of integers `core duration` (1 ≤ `core` ≤ $m$, 1 ≤ `duration` ≤ 1000), listing the gates in the strict order they must be executed. 

The total number of gates across all $j$ sub-routines is guaranteed to be at most 50.

## Output

Print a single integer: the minimum number of nanoseconds required to complete all sub-routines.

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

In Example 1, two identical sub-routines each pass through cores 1, 2, and 3 (requiring 2 nanoseconds on each). The second sub-routine can trail the first through the cores, finishing at 8 nanoseconds. 
In Example 3, the two sub-routines use different cores and execute perfectly in parallel, so the overall completion time is just the maximum of their individual durations (4 nanoseconds).
