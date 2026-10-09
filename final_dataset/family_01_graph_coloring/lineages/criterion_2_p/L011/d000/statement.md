# Phase Configuration

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates continuously through two distinct production phases, labeled 1 and 2. The facility houses $n$ industrial machines. Due to the electrical wiring, $m$ specific pairs of machines are connected to the same local power sub-panel. If two machines sharing a sub-panel are active during the same production phase, they will overload the circuit. Consequently, such pairs must be scheduled in different phases.

You must determine whether it is possible to assign each machine to exactly one of the two phases without causing any power overloads. If a safe configuration is possible, the plant's automated control system requires a standardized output. Specifically, the resulting sequence of $n$ phase assignments must be lexicographically smallest, meaning that the system prefers placing machines in phase 1 over phase 2, prioritizing the machine with the lowest ID, then the second lowest, and so forth.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of machines and the number of shared sub-panel connections.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that machine $u$ and machine $v$ share a power sub-panel.

## Output
If there is no way to assign the phases without an overload, output a single line containing `NO`.
If a safe assignment exists, output `YES` on the first line. On the second line, output $n$ space-separated integers, where the $i$-th integer (either 1 or 2) represents the phase assigned to machine $i$. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
