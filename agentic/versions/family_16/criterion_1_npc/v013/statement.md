# Problem A — Pipeline Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

A streamlined manufacturing facility contains **m** independent workstations and is tasked with completing **j** production batches. Each batch is defined by a simple, linear protocol: a fixed sequence of phases that must be executed one after another. Every phase requires exclusive use of a designated workstation for a specific duration.

The facility operates under the following straightforward rules:
- **Strict Sequential Flow:** A batch's phases must be executed in the exact order specified. A phase can only begin once the preceding phase for that same batch has entirely finished.
- **Exclusive Access:** A workstation can handle at most one phase at any given moment. 
- **Continuous Execution:** Once a workstation starts a phase, it runs continuously without interruption until the required duration elapses.

Because each batch is just a linear sequence of steps and the total number of phases across all batches is extremely small (at most 50), the system is heavily constrained by its own dependencies. In many common scenarios, batches smoothly trail one another through the workstations. Your task is to find the most compact alignment of these phases that minimizes the overall completion time—the exact moment when the final phase of the last batch finishes.

## Input

The first line provides two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).

Each of the following **j** lines details the protocol for a single batch. A line begins with an integer **o** (the number of phases in the batch), followed by **o** pairs of integers formatted as `workstation duration` (1 ≤ workstation ≤ m, 1 ≤ duration ≤ 1000). These pairs appear in the strict order the phases must be executed.

The sum of **o** across all **j** batches will not exceed 50.

## Output

Print a single integer representing the earliest possible time that all batches can be completely processed.

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

In Example 1, two identical batches sequentially visit workstations 1, 2, and 3 (requiring 2 time units each). The second batch smoothly trails the first through the pipeline, finishing at time 8. In Example 3, the two batches utilize different workstations and run perfectly in parallel, finishing at time 4.
