# Phase Alignment for Data Transfer Tasks

Time limit: 2 s   Memory limit: 256 MB

## Description
A data processing facility is built by installing two independent banks of hardware: a bank of $N_1$ primary processors and a bank of $N_2$ secondary processors. The facility must execute $M$ data transfer tasks. Each task establishes a dedicated link between exactly one primary processor and one secondary processor. By design, no task ever links two processors from the same bank.

To prevent resource conflicts, the tasks must be scheduled into discrete, numbered time slots. Each task takes exactly one time slot to complete. A processor (whether primary or secondary) can only participate in one task at a time. Therefore, if two tasks require the same processor, they must be scheduled in different time slots.

The overall duration of the schedule is dictated by the processor with the heaviest workload. If the single most active processor in the entire facility is involved in $K$ tasks, the schedule will inherently require at least $K$ time slots. Your objective is to compress the timeline: assign every task to a time slot numbered from $1$ to $K$. The strict separation between primary and secondary banks ensures that a schedule using exactly $K$ time slots is always possible.

## Input
The first line contains three integers $N_1$, $N_2$, and $M$ ($1 \le N_1, N_2 \le 100000$, $0 \le M \le 400000$).
The following $M$ lines each contain two integers $u$ and $v$ ($1 \le u \le N_1$, $1 \le v \le N_2$), representing a task that links primary processor $u$ and secondary processor $v$.

## Output
Print `YES` on the first line.
On the second line, print $M$ space-separated integers. The $i$-th integer must be the time slot assigned to the $i$-th task in the input, using only values from $1$ to $K$ (where $K$ is the highest number of tasks assigned to any single processor).

## Example
**Input**
```text
4 4 6
1 1
1 2
2 2
3 3
3 4
4 4
```

**Output**
```text
YES
1 2 1 1 2 1
```
