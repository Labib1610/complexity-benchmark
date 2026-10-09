# Problem A — Shift Allocation on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a trunk grid where junctions are linked by cables. The maintenance cycle is strictly divided into a morning shift, an afternoon shift, and a night shift. The grid has been uniformly engineered such that the number of cables meeting at any junction is exactly equal to the total number of shifts in the maintenance cycle.

Taking a cable offline consumes an entire shift. Safety rules forbid isolating a junction: at any splice point, no two of its connected cables may be serviced during the same shift, as a junction losing multiple connections at once cannot maintain continuity. Consequently, the cables meeting at any given junction must be spread completely across the available shifts. 

The physical cable lengths, materials, and crew assignments are irrelevant to the scheduling question—the only constraint is that cables sharing a junction cannot share a maintenance shift.

You must assign a shift to each cable in the grid so that the safety rules are respected at every junction, or determine that the shifts are provably insufficient for this grid. Leaving a cable unassigned is not permitted. 

## Input
The first line contains two integers representing the number of junctions and the number of cables. The junction count is an even number; a grid must have at least a single pair of junctions to form a connection, and the utility's district limits cap the junction count at a maximum of two thousand. Because of the uniform grid engineering, the cable count is exactly the junction count multiplied by the number of daily shifts, then divided by two.

Each of the following lines contains two integers identifying the two junctions connected by a cable, with the numerically smaller junction identifier listed first. Junction identifiers start from one and go up to the total number of junctions.

## Output
If a valid maintenance schedule exists, print `YES`, followed by a line with a space-separated sequence of integers corresponding to the shift assignment of each cable, in the exact order the cables appear in the manifest. Use `1` for the morning shift, `2` for the afternoon shift, and `3` for the night shift. If no such schedule is possible, print `NO`.

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
