# Workload-Balanced Cable Maintenance

Time limit: 5 s   Memory limit: 256 MB

## Description
A telecommunications utility is scheduling maintenance for its trunk network. The network consists of **n** splice junctions connected by **m** fiber-optic cables. The network topology is engineered to be uniformly three-way: every single junction acts as an endpoint for exactly three cables.

Maintenance must be completed using exactly three rotating service shifts. Each cable must be scheduled for maintenance during exactly one of these three shifts. Taking a cable offline consumes the entire shift.

To ensure network continuity and comply with union regulations, the final schedule must satisfy three strict conditions:
1. **Junction Continuity:** At any given junction, no two of its three connected cables may be taken offline during the same shift. The three cables meeting at any junction must be assigned to three distinct shifts.
2. **Active Redundancy:** During any of the three shifts, if we observe the cables that remain online, every junction in the network must retain exactly two active connections.
3. **Shift Equity:** The labor union mandates a perfectly balanced workload. Each of the three shifts must be allocated exactly **n**/2 cables, no more and no less.

You must determine if a valid maintenance schedule exists that satisfies all three conditions simultaneously. (Because the network leaves no slack, a single unavoidable clash makes the entire schedule impossible). 

## Input
The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ **u** < **v** ≤ **n**), representing a cable connecting junction **u** and junction **v**.

## Output
If a valid schedule exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} separated by spaces, representing the shift assigned to each cable in the order they were given in the input (cables sharing a junction must be assigned different shifts). If there are multiple valid schedules, you may output any of them.
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
