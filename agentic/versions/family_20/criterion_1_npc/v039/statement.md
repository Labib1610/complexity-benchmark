# Problem A — Scheduling Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a trunk grid whose junctions are cable splice points. The grid is constructed so that every junction connects exactly three cables. The utility must generate a complete maintenance schedule before the annual inspection. 

The maintenance cycle consists of exactly three rotating service windows. During maintenance, a cable is completely depowered, which consumes one whole window. To prevent localized blackouts, a junction must always have at least two active cables connected to it. Because every junction connects exactly three cables, no two of its incident cables may be depowered in the same window. Consequently, the three cables meeting at any junction must be assigned to three different windows.

Assign each cable in the grid to one of the three windows so that at every junction the three connected cables occupy distinct windows, or determine that three windows are insufficient for this grid.

## Input
The first line has two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of junctions and cables.
Each of the next **m** lines has two integers u v (1 ≤ u < v ≤ n): a cable between junctions u and v.

## Output
If a valid assignment exists, print `YES`, then a line with **m** integers in {1,2,3} — the window assigned to cable i in input order. Otherwise print `NO`.

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
