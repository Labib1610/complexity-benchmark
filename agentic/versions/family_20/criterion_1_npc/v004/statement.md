# Problem A — Rotating Maintenance Windows on the Uniform Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a highly regular trunk grid whose junctions are cable splice points. The grid has been strictly engineered so that **every** junction is a splice of **exactly three** cables — the network's topology is perfectly uniform, being exactly three-way at every single node. Maintenance is organised into three rotating service windows, and taking a cable offline always consumes one whole window.

Safety rules forbid isolating a junction: at any splice point, no two of its three cables may be serviced in the same window, because a junction that loses two of its three cables at once cannot maintain continuity. Equivalently, the three cables meeting at any junction must be spread across three different windows. The physical cable lengths, the materials, and which crews are assigned are all irrelevant to the scheduling question — the only thing that binds is the strict topological regularity that cables sharing a junction never share a window.

There are exactly three windows available and no more. Exploit the perfect 3-way uniformity of the grid to assign each cable one of the three windows so that at every junction the three incident cables occupy three distinct windows, or determine that three windows are provably insufficient. (While the strict regularity often allows schedules to fall neatly into place without slack, a single unavoidable clash makes the whole schedule impossible.)

## Input
The first line has two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000).
Each of the next **m** lines has two integers u v (1 ≤ u < v ≤ n): a cable between junctions u and v.

## Output
If an assignment exists, print `YES`, then a line with **m** integers in {1,2,3} — the shift of cable i in input order (adjacent cables must differ). Otherwise print `NO`.

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
