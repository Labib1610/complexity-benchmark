# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s
Memory limit: 256 MB

## Description
You are managing the logistics for a national distribution grid. The grid consists of $n$ distribution centers (hubs) and $m$ directional transit corridors. Each corridor has a fixed structural limit on the total volume of freight it can handle during a single operational shift.

A set of $k$ distinct cargo orders must be fulfilled during the next shift. Each order specifies an origin center, a destination center, and a precise quota of indivisible freight units that must be successfully relocated.

Freight routing must obey the following operational rules:
- **Conservation of Freight**: For any given order, at any center that is neither its origin nor its destination, the volume of units entering must exactly equal the volume of units exiting.
- **Origin and Destination Fulfillment**: For each order, the net volume of its units leaving its origin center (outgoing minus incoming) must exactly match its specified quota. Similarly, the net volume of its units entering its destination center (incoming minus outgoing) must exactly equal this quota.
- **Indivisibility**: All freight units are atomic; the volume of a specific order routed through any corridor must be a non-negative integer.
- **Shared Corridor Limits**: The corridors are shared among all orders. For any given corridor, the sum of the freight units across all orders routed through it cannot exceed the corridor's fixed structural limit.

To reflect real-world constraints, the test data guarantees the following properties:
- The total number of unique origin centers across all $k$ orders is at most $k$.
- The number of outgoing corridors directly departing from any single center never exceeds $m$.

Determine if there is a valid routing strategy that fulfills all $k$ orders simultaneously without violating any corridor limits. If such a strategy exists, you must also output the specific freight volumes assigned to each corridor.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of centers, corridors, and orders, respectively.
The following $k$ lines detail the cargo orders. The $i$-th line contains three integers $s_i$, $t_i$, and $d_i$, representing the origin center, the destination center, and the required freight quota for order $i$.
The final $m$ lines describe the transit corridors. The $j$-th line contains three integers $u_j$, $v_j$, and $c_j$, indicating a directional corridor from center $u_j$ to center $v_j$ with a structural limit of $c_j$ freight units.
Centers are indexed from 1 to $n$.

## Output
If all orders can be concurrently fulfilled, print `YES` on the first line. Following this, print $k$ lines. The $i$-th line must contain $m$ space-separated integers, where the $j$-th integer represents the volume of freight for order $i$ routed through the $j$-th corridor (in the exact order the corridors were provided in the input).
If no valid routing strategy can fulfill all orders, print `NO`.

## Example
### Input
```text
4 3 2
1 4 1
2 4 1
1 3 1
2 3 1
3 4 2
```
### Output
```text
YES
1 0 1
0 1 1
```
