# Problem A — Hierarchical Pipeline Compilation

Time limit: 5 s   Memory limit: 256 MB

## Description
A data processing engine executes tasks in parallel pipelines. There are exactly $3q$ distinct tasks in the system, sequentially numbered from 1 to $3q$.

To maximize throughput, tasks must be bundled into execution pipelines. A valid pipeline always consists of exactly three distinct tasks. The engine's optimizer has already pre-calculated a list of $t$ candidate pipelines that can safely execute together. To guarantee forward data progression, every candidate pipeline lists its three tasks in strictly increasing order.

Because the workload is perfectly balanced, the total number of tasks is exactly three times the number of required pipelines. Your objective is to compile a final execution plan by selecting exactly $q$ pipelines from the candidate list. This selection must be perfectly efficient: every single one of the $3q$ tasks must be assigned to exactly one selected pipeline. No task can be left unassigned, and no task can be duplicated across multiple pipelines.

Given the pre-validated, strictly ordered nature of the candidate pipelines, determine if a perfect execution plan can be compiled. If so, output the selected pipelines.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of tasks to be processed is $3q$.
Each of the subsequent $t$ lines provides three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing a candidate pipeline of three tasks.

## Output
If a valid execution plan exists, print `YES` on the first line. Then, print $q$ lines, each containing the three tasks of a selected pipeline.
If no such plan is possible, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
