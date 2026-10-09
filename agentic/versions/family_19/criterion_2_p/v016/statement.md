# Commodity Routing over a Constrained Logistics System

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics operator needs to transport a specific commodity through a system of distribution centers (hubs) connected by one-way transit corridors. Each corridor has a strict upper limit on the number of units it can transport in a single operational cycle. This limit is due to fixed vehicle capacities that cannot be increased mid-cycle. A predetermined total volume of the commodity, measured in discrete units, must be transported from a designated starting center to a designated receiving center within one cycle.

For each corridor, the allocated number of units must be a non-negative integer that does not exceed the corridor's upper limit. At every center, except for the starting and receiving centers, the commodity must be perfectly conserved: the total number of units arriving must exactly equal the total number of units departing. No units may be stored or lost at these intermediate centers. At the starting center, the net outward shipments must exactly equal the predetermined total volume, and at the receiving center, the net inward shipments must exactly equal this same volume.

You may assume the system satisfies the following structural conditions:
1. For any single corridor in the system, its upper limit is no greater than the sum of the upper limits of all corridors combined.
2. The total number of incident corridors (incoming and outgoing combined) for any single distribution center is guaranteed not to exceed $2m$, where $m$ is the total number of corridors in the system.

All other operational details—such as empty vehicle repositioning, transit durations, corridor lengths, and the chronological sequence of unit movements—are irrelevant to this planning phase and must be ignored. Only the corridor limits, the conservation at intermediate centers, and the required end-to-end volume constrain the valid allocations.

Determine an allocation of units to corridors that successfully transports the required volume from the starting center to the receiving center without violating any corridor's limit. If no such allocation exists for a single cycle, you must report that it is impossible.

## Input
The first line contains three integers: $n$ (the number of centers), $m$ (the number of corridors), and $1$ (indicating a single commodity).
The second line contains three integers: $s$ (the starting center), $t$ (the receiving center), and $d$ (the required total volume).
The next $m$ lines each contain three integers: $u$, $v$, and $cap$, representing a one-way corridor from center $u$ to center $v$ with an upper limit of $cap$.

## Output
If the transport is possible, output `YES` on the first line, followed by a second line containing $m$ integers representing the allocated volume for each corridor in the exact order they were provided in the input.
If it is impossible, output `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
2 4 5
1 3 5
3 4 5
2 3 5
```

**Output:**
```
YES
5 5 5 5 0
```
