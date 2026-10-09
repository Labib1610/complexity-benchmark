# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility operates a trunk grid where various cables meet at splice junctions. The network's layout is strictly uniform: every junction serves as a connection point for exactly three cables.

Maintenance work on these cables is organized into distinct service shifts. There are exactly three such shifts available. When a cable is serviced, it is taken offline for the entirety of its assigned shift.

To maintain network continuity, safety protocols dictate that no junction may have more than one of its cables offline during any single shift. Because every junction connects exactly three cables, and there are exactly three shifts, this rule means that at any given junction, all three of its connected cables must be scheduled for completely different shifts. Physical lengths and crew logistics are not considered; the only restriction is this strict separation of shifts at every junction.

Given the layout of the grid, perfectly distributing the service shifts might not always be achievable. You must assign each cable to one of the three available shifts such that the safety protocols are satisfied everywhere, or prove that no such schedule exists for the given network.

## Input
The first line contains two integers **n** and **m** (where **n** is even, **m** = 3**n**/2, and 2 ≤ **n** ≤ 2000), representing the number of junctions and cables, respectively.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), specifying a cable between junction **u** and junction **v**.

## Output
If a valid schedule exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} — the shift assigned to each cable, in the same order the cables were specified in the input. If no such schedule is possible, print `NO`.

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
