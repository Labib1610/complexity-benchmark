# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a trunk grid whose junctions are cable splice points. The grid has been engineered with strict uniformity: every junction serves as an endpoint for an identical number of cables. 

Maintenance is organised into rotating service windows. The total number of available windows is strictly limited to equal the number of cables meeting at any single junction. Taking a cable offline always consumes one whole window. 

Safety rules forbid destabilising a junction: at any splice point, no two of its connected cables may be serviced during the same window. Because the number of windows exactly matches the number of cables at each junction, this means that every cable meeting at a given junction must be assigned a completely different service window. The physical cable lengths, the materials, and which crews are assigned are all irrelevant to the scheduling question — the only thing that binds is that cables sharing a junction never share a window.

Assign each cable in the grid to one of the available windows so that all safety rules are satisfied, or determine that the available windows are provably insufficient for this grid. 

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of junctions and the total number of cables, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), indicating that a cable connects junction $u$ and junction $v$.

## Output
If a valid assignment exists, print `YES`, followed by a line containing $m$ integers. Each integer must correspond to the service window assigned to the cable in the order they appear in the input. Windows are numbered sequentially starting from $1$ up to the total number of available windows. If no such assignment is possible, print `NO`.

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
