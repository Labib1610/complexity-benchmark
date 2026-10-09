# Problem A — Network Phase Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A power utility manages a regional transmission network consisting of junction points connected by high-voltage lines. The network architecture dictates that every junction point acts as a hub for exactly three connecting lines. Because of this strict architectural rule, the total number of lines in any valid network is exactly one and a half times the number of junction points, and the count of junction points is necessarily an even number. The system records a minimum of two junction points, and its database capacity can handle a maximum of two thousand junction points.

To conduct routine inspections, the utility schedules three distinct service phases. Inspecting a line takes exactly one full phase. A critical safety protocol requires that no junction point is ever severely isolated during a phase. Specifically, if two or more lines connected to the same junction are undergoing inspection simultaneously, the junction loses electrical continuity. Therefore, all three lines meeting at any given junction must be assigned to completely different service phases.

Determine if it is possible to assign every line to one of the three available phases without violating the safety protocol, and if so, provide a valid schedule.

## Input
The first line of the input contains two integers **n** and **m**, representing the number of junction points and the number of lines, respectively. These values conform to the architectural rules and capacity limits described above.
Following this, there are **m** lines. Each line contains two integers **u** and **v** (1 ≤ u < v ≤ n), indicating that a high-voltage line connects junction point **u** and junction point **v**.

## Output
If a valid service schedule exists, print `YES` on the first line. On the second line, output **m** integers separated by spaces, where each integer is 1, 2, or 3. The $i$-th integer represents the service phase assigned to the $i$-th line as they appear in the input. If no such schedule is possible with only three phases, print `NO`.

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
