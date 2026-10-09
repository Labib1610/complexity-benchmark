# Problem A — Backplane Slot Assignment

Time limit: 5 s
Memory limit: 256 MB

## Description
A new control vault requires $n$ hardware modules to be installed into a linear backplane. The backplane features exactly $n$ uniform slots, numbered sequentially from $1$ to $n$. Each module must be assigned to exactly one slot, resulting in a perfect one-to-one mapping (a permutation) of modules to slots.

The modules are interconnected by $m$ identical, point-to-point data links. Because the backplane is a straight line, the physical length of the wire required for a link between a module in slot $x$ and a module in slot $y$ is simply the absolute difference in their slot numbers, $|x - y|$. The routing architecture is strictly linear and uncapacitated: wires can overlap freely, and there are no per-link length limits or routing bottlenecks. The cost is driven solely by this simple 1D distance metric.

Procurement has allocated a grand total wire budget $B$ for the entire system. Because the cost function is merely the sum of the absolute differences of the assigned slot indices, the problem relies entirely on finding a suitable permutation. In many configurations, placing heavily connected modules centrally and pushing leaf modules to the edges reduces the overall displacement. 

You must determine if there exists an assignment of modules to slots such that the total wire length over all $m$ links does not exceed $B$. If it is feasible, you must output a valid assignment.

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of modules, the number of data links, and the total wire budget. 
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a data link between module $u$ and module $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers representing the assigned slot numbers (from $1$ to $n$) for modules $1, 2, \dots, n$ respectively. If there are multiple valid assignments, any one is acceptable.
If no such assignment can satisfy the budget, print `NO`.

## Example
### Input
```
4 3 4
1 2
1 3
1 4
```

### Output
```
YES
2 1 3 4
```
