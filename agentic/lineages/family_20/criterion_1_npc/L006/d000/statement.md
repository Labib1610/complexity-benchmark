# Problem A — Rotating Maintenance Phases on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a trunk grid whose junctions are cable splice points. The grid has been engineered so that each junction connects exactly a triad of cables. Maintenance is organised into three service phases, and taking a cable offline always consumes one whole phase.

Safety rules forbid isolating a junction: at any splice point, no two of its cables may be serviced in the same phase, because a junction that loses multiple cables at once cannot maintain continuity. Equivalently, the cables meeting at any junction must be spread across completely different phases. The physical cable lengths, the materials, and which crews are assigned are all irrelevant to the scheduling question — the only thing that binds is that cables terminating at the same junction never share a phase.

There are exactly three phases available and no more. Assign each cable in the grid one of the three phases so that at every junction all terminating cables occupy distinct phases, or determine that three phases are provably insufficient for this grid. (Having only three phases for a grid built entirely of triads leaves no slack whatsoever — a single unavoidable clash makes the whole schedule impossible.)

## Input
The first line has two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000).
Each of the next **m** lines has two integers u v (1 ≤ u < v ≤ n): a cable between junctions u and v.

## Output
If an assignment exists, print `YES`, then a line with **m** integers in {1,2,3} — the phase of cable i in input order (cables meeting at a junction must differ). Otherwise print `NO`.

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
