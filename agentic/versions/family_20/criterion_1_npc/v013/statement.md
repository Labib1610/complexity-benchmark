# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a highly regular trunk grid. The grid is engineered with strict local uniformity: every junction connects exactly three cables. Because of this perfect structural balance, a grid with $n$ junctions always contains exactly $3n/2$ cables, and $n$ is always guaranteed to be an even number.

Maintenance is organised into three rotating service windows. Each cable must be scheduled in exactly one window. To maintain continuous service, a strict safety rule applies at the junctions: no two cables meeting at the same junction can be scheduled in the same window.

Because there are exactly three windows and exactly three cables per junction, this safety rule forces a perfectly balanced local schedule. At every single junction, the three incident cables must be distributed perfectly across the windows—one to window 1, one to window 2, and one to window 3. The exact match between the local junction degree and the number of available windows means there is zero slack in the schedule at any junction. 

While this strict local perfection might suggest a straightforward repeating pattern, the global topology of the grid can sometimes prevent a valid schedule. Your task is to assign each cable to one of the three windows such that adjacent cables always receive different windows, or determine that the grid's topology makes this impossible.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of junctions and the number of cables.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), representing a cable between junction $u$ and junction $v$. The input is guaranteed to describe a grid where every junction has exactly three incident cables.

## Output
If a valid maintenance schedule exists, print `YES` on the first line. On the second line, print $m$ integers from $\{1, 2, 3\}$, representing the window assigned to each cable in the order they appear in the input. If multiple valid assignments exist, you may output any of them.
If no such schedule is possible, print `NO`.

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
