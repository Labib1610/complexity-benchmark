# Problem A — Concurrent Freight Dispatch over a Shared Corridor System

Time limit: 5 s   Memory limit: 256 MB

## Description
A national rail network consists of several stations connected by one-way tracks. Each track has a strict structural limit on the total number of wagons that can pass over it. This limit applies to the combined sum of all wagons, regardless of their contents.

Wagons are used to fulfill various transport orders. Each order is dedicated to a specific type of cargo. For any given order, at any station that is not its designated origin or destination, the number of incoming wagons carrying its cargo must perfectly match the number of outgoing wagons carrying its cargo. All wagons are indivisible units, meaning the number of wagons on any track for any order must be a non-negative integer. Crucially, all orders share the same network, meaning they compete for the limited capacity of the shared tracks.

Each order specifies an origin station, a destination station, and a required number of wagons. For a plan to be successful, the net outflow of an order's wagons at its origin must exactly equal this required number, and the net inflow at its destination must exactly equal this required number. Your task is to construct a routing plan that fulfills all orders simultaneously, without violating any track's structural limit or the conservation of wagons at intermediate stations. If it is impossible to fulfill all orders under these conditions, you must report that no such plan exists.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of stations, tracks, and orders, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the origin station, destination station, and required number of wagons for order $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way track from station $u$ to station $v$ with a capacity limit of $cap$.

## Output
If a valid routing plan exists, output `YES` on the first line. Then output $k$ lines, where the $i$-th line contains $m$ integers. Each integer represents the number of wagons for order $i$ routed along the corresponding track (in the same order the tracks were given in the input). If no such plan exists, output `NO`.

## Example

**Input**
```text
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 3 1
2 4 1
3 4 1
```

**Output**
```text
YES
0 1 0 0 1
0 0 1 0 0
```
