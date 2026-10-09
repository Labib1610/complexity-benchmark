# Problem B — Two-Stage Fabrication

Time limit: 1 s   Memory limit: 256 MB

## Description

A high-capacity fabrication plant is tasked with completing a batch of **j** custom components. You must determine an ordering for these components that minimizes the total time required to finish all of them.

The plant features exactly two specialized machines: a former and a finisher. Every component must pass through the former first, and then proceed to the finisher. The process is governed by several strict constraints:

- The former and the finisher can each work on at most one component at any given moment.
- A component cannot enter the finisher until it has fully exited the former.
- The components must be fed into both machines in the identical sequence. There is no overtaking; if component A enters the former before component B, component A must also enter the finisher before component B.
- To ensure machine longevity, the input parameters guarantee that the sum of all forming and finishing times across all **j** components is at most 400,000,000,000.
- Every component requires a strictly positive amount of time on each machine, meaning the combined time spent by any single component across both machines is at least 2.

Since the former can prepare subsequent components while the finisher is working on earlier ones, the overall completion time is highly sensitive to the order in which the components are processed. Your task is to calculate the earliest possible time that the finisher completes the final component, assuming the best possible sequence is chosen.

## Input

The first line provides the number of components, **j** (1 ≤ **j** ≤ 200000).
The subsequent **j** lines each contain two integers, **f_i** and **s_i** (1 ≤ **f_i**, **s_i** ≤ 1000000). These represent the time required by the **i**-th component on the former and the finisher, respectively.

## Output

Output a single integer representing the minimum possible time the finisher completes the last component.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single component occupies the former for 5 time units, and then the finisher for 3 time units. It finishes at time 8.
