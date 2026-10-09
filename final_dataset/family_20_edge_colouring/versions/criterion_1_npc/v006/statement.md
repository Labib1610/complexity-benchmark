# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a trunk grid whose junctions are cable splice points. The grid has been engineered so that every junction is a splice of exactly three cables. Maintenance is organised into three rotating service windows, and taking a cable offline always consumes one whole window.

Safety rules forbid isolating a junction: at any splice point, no two of its three cables may be serviced in the same window, because a junction that loses two of its cables at once cannot maintain electrical continuity. 

There are exactly three windows available. Assign each cable in the grid one of the three windows so that at every junction the three incident cables occupy distinct windows, or determine that three windows are insufficient for this grid.

## Input
The first line has two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of junctions and cables.
Each of the next **m** lines has two integers u v (1 ≤ u < v ≤ n): a cable between junctions u and v.

## Output
If an assignment exists, print `YES`, then a line with **m** integers in {1,2,3} — the window of cable i in input order. Otherwise print `NO`.

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
