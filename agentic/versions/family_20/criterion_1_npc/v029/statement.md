# Problem A — Rotating Maintenance Periods on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a trunk grid whose junctions are cable splice points. The grid has been engineered so
that **every** junction is a splice of **exactly a trio of** cables — the network has uniform connectivity at
every node. Maintenance is organised into three rotating service periods, and taking a cable offline
always consumes one whole period.

Safety rules forbid isolating a junction: at any splice point, no two of its connected cables may be serviced
in the same period, because a junction that loses multiple cables at once cannot maintain
continuity. Equivalently, the cables meeting at any junction must be spread across distinct
periods. The physical cable lengths, the materials, and which crews are assigned are all irrelevant to
the scheduling question — the only thing that binds is that cables sharing a junction never share a
period.

There are exactly three periods available and no more. Assign each cable in the grid one of the three
periods so that at every junction the connected cables occupy distinct periods, or determine
that three periods are provably insufficient for this grid. (Having only three periods for this uniform
network leaves no slack whatsoever — a single unavoidable clash makes the whole schedule
impossible.)

## Input
The first line has two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000).
Each of the next **m** lines has two integers u v (1 ≤ u < v ≤ n): a cable between junctions u and v.

## Output
If an assignment exists, print `YES`, then a line with **m** integers in {1,2,3} — the period of cable i
in input order (cables sharing a junction must differ). Otherwise print `NO`.

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
