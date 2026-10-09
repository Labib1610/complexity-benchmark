# Problem A — Parallel Processing of Dependent Operations

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing facility must process a batch of $n$ operations before a strict deadline of $T$ cycles. All operations have an identical duration of exactly one cycle. The facility operates a bank of $M$ identical parallel processing units. During any single cycle, each processing unit can execute at most one operation. Therefore, the maximum number of operations that can be concurrently executed in a single cycle is limited by $M$. Leaving a unit inactive during a cycle carries no penalty, and completing operations early provides no additional benefit, provided all operations are finished within the $T$ cycles.

The operations are interconnected. Certain operations generate components required by others, creating precedence dependencies. If operation $a$ must be completed before operation $b$ can commence, operation $b$ must be scheduled in a cycle strictly after the cycle in which $a$ is executed. Scheduling them in the same cycle is invalid because the component produced by $a$ only becomes available at the start of the subsequent cycle. There are no setup times, operation priorities, or restrictions on which specific unit executes which operation; an operation can be processed by any available unit, and only the cycle it is assigned to is significant.

To guarantee input integrity, the system ensures the following properties hold for all prerequisite rules $(a, b)$ provided in the input:
- The absolute difference between the operation identifiers, $|a - b|$, is strictly less than $n$.
- The product of the operation identifiers, $a \times b$, is no greater than $n^2$.

You must assign every operation to a cycle (from 1 to $T$) such that all precedence dependencies are satisfied and the number of operations in any cycle does not exceed the number of processing units $M$. If it is impossible to schedule all operations within the deadline under these conditions, you must report that the batch cannot be completed.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ must be completed before operation $b$ can begin.

## Output
Print `YES` then $n$ integers (the cycle assigned to each operation from $1$ to $n$, in the range $1 \dots T$); otherwise print `NO`.

## Example

**Input:**
```
4 2 3 3
1 2
1 3
2 4
```

**Output:**
```
YES
1 2 2 3
```
