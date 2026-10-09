# Problem A — Automated Distribution Center Routing

Time limit: 5 s   Memory limit: 256 MB

## Description
An automated distribution center moves pallets between junction points using one-way conveyor belts. Each conveyor belt has a structural limit on how many pallets it can safely support during a single operating shift. This limit applies to the physical total of all pallets on that belt, no matter who they belong to.

During the upcoming shift, several client orders must be fulfilled. Each order consists of a specific number of unbroken pallets that must travel from a designated intake dock to a designated loading ramp.

Because the pallets are solid objects, the quantity of any order routed over any belt must be a non-negative whole number. At any junction point that is not a designated intake dock or loading ramp for a specific order, the total number of pallets of that order entering the junction must exactly equal the number exiting it. No pallets can be stored long-term at junctions, and no pallets can be lost. Furthermore, for each client order, the exact number of pallets dispatched from its intake dock must reach its loading ramp.

You must determine exactly how many pallets of each client order to route over each conveyor belt so that all orders are completely fulfilled without exceeding the structural limit of any belt. If the center's belts cannot support the combined requirements, you must detect this.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of junction points (numbered $1$ to $n$), conveyor belts, and client orders.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$: the intake dock, the loading ramp, and the required number of pallets for order $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$: a one-way conveyor belt from junction $u$ to junction $v$ with a structural limit of $cap$ pallets.

## Output
If all orders can be fulfilled, print `YES` on the first line. Then, print $k$ lines. The $i$-th of these lines must contain $m$ integers, where the $j$-th integer is the number of pallets for client order $i$ routed over the $j$-th conveyor belt (in the exact order the belts were given in the input).
If the requirements cannot be met, print exactly `NO`.

### Example

**Input**
```text
4 5 2
1 4 2
2 3 1
1 2 2
2 4 2
1 3 1
3 4 1
2 3 1
```

**Output**
```text
YES
2 2 0 0 0
0 0 0 0 1
```
