# Problem A — Rotating Maintenance Periods on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
In perfectly balanced infrastructure networks, structural uniformity often allows for highly efficient operational schedules. A utility operates a trunk grid where junctions act as cable splice points. The grid has been engineered for maximum regularity: every single junction connects exactly three cables. 

Maintenance must be scheduled across exactly three rotating service periods. Because the network has perfectly uniform connectivity, the schedule must achieve perfect load balancing. At any junction, the three connected cables must be distributed exactly one per period. If two cables at the same junction were serviced simultaneously, the junction would lose multiple connections, violating safety rules. Thus, the periods assigned to the cables meeting at any junction must be mutually distinct (periods 1, 2, and 3).

The physical properties of the grid are irrelevant; only the topology matters. Since the number of junctions is always even and the total number of cables is exactly 1.5 times the number of junctions, the periods can often be distributed perfectly. Your task is to determine whether this perfectly regular grid admits such a balanced assignment, and if so, to output one.

## Input
The first line contains two integers $n$ and $m$, where $n$ is the number of junctions (always even, $2 \le n \le 2000$) and $m$ is the number of cables ($m = 3n/2$).
Each of the following $m$ lines provides two integers $u$ and $v$ ($1 \le u < v \le n$), representing a cable connecting junction $u$ and junction $v$.

## Output
If a balanced schedule exists, print `YES` on the first line. On the second line, print $m$ integers from the set $\{1, 2, 3\}$, where the $i$-th integer is the period assigned to the $i$-th cable in the input order. (Cables sharing a junction must be assigned different periods). If no such exact distribution is possible, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
