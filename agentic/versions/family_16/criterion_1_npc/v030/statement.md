# Problem A — Artifact Restoration

Time limit: 5 s   Memory limit: 256 MB

## Description

A museum employs **m** specialists to restore **j** historical artifacts. The restoration of each artifact demands a prescribed series of steps. Each step requires the undivided attention of a specific specialist for a designated number of hours. The restoration process is governed by the following constraints:

- An artifact's steps are strictly dependent on one another. A step becomes available to be worked on only after all preceding steps listed for that specific artifact have been fully concluded.
- A specialist is capable of working on at most one step at any given time.
- Once a specialist initiates a step, they must work on it continuously until the required hours for that step have elapsed.

All specialists are available to begin work at hour 0. Your task is to organize the work across all specialists such that the total time elapsed—from hour 0 until the final step of every artifact is concluded—is as small as possible. Output this minimum possible time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes the requirements for one artifact: an integer **o** (the number of steps) followed by **o** pairs of integers `specialist duration` (1 ≤ specialist ≤ m, 1 ≤ duration ≤ 1000), listing the artifact's steps in their dependent order.
The total number of steps across all artifacts is at most 50.

## Output

Print a single integer: the earliest possible hour by which all artifacts can be fully restored.

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

In Example 1, two identical artifacts require specialists 1, 2, and 3 in that order (for 2 hours each). The second artifact's steps can be staggered behind the first artifact's steps, concluding at hour 8. In Example 3, the two artifacts require different specialists, meaning their steps can be performed simultaneously, concluding at hour 4.
