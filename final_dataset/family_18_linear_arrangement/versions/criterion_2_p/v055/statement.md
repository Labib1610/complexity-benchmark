# Problem B — Fiber Laying for Pipeline Sensors

Time limit: 5 s   Memory limit: 256 MB

## Description
A pipeline monitoring system requires $n$ sensor nodes to be installed in a single underground trench. The trench features exactly $n$ discrete mounting bays, numbered sequentially from $1$ to $n$. Each sensor node must be assigned to exactly one bay, ensuring no bay is left empty.

Data flows through a centralized aggregation scheme: one master node exists, and every other node transmits directly to exactly one designated receiver node. This configuration connects all nodes into a single network without any cyclic data loops. A dedicated fiber optic strand must be laid between each node and its receiver. The length of the fiber strand required for a connection equals the absolute difference between the bay numbers of the two nodes. Multiple strands can run in parallel through any segment of the trench without interference.

The installation crew has a single continuous spool of fiber optic cable of total length $B$ to fulfill all connections. Determine a valid bay assignment for every node such that the sum of all fiber strand lengths is at most $B$, or report that the budget cannot be met.

## Input
The first line contains three integers $n$, $m$, and $B$. The integer $n$ represents the number of sensor nodes. The integer $m$ represents the number of fiber strands, which is exactly $n - 1$ (the number of nodes excluding the master node). The integer $B$ represents the total cable budget.
Each of the next $m$ lines contains two integers $u$ and $v$ (from $1$ to $n$), indicating a data transmission link between node $u$ and node $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers representing the bay assignments for nodes $1, 2, \dots, n$ respectively. Each integer must be between $1$ and $n$, and all $n$ integers must be distinct. If the budget cannot be met, print `NO`.

## Example

**Input:**
```
5 4 5
1 2
1 3
3 4
3 5
```

**Output:**
```
YES
2 1 4 3 5
```
