# Problem A — Simultaneous Freight Routing over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics system consists of a set of distribution centers connected by one-way transit corridors. We are tasked with executing a simultaneous dispatch cycle for several distinct consignments.

Each consignment is defined by its starting center, its target center, and the exact volume of indivisible freight pallets that must be transported. Because the centers operate on a strict cross-docking model, pallets cannot be permanently stored at intermediate locations. For any specific consignment, a center that is neither its starting nor target location must have the number of arriving pallets of that consignment perfectly match the number of departing pallets. For the starting center, the number of departing pallets minus any arriving pallets of that consignment must exactly equal the required volume. Conversely, at the target center, the number of arriving pallets minus departing pallets must exactly equal the required volume.

All consignments share the same physical grid. Each one-way corridor has a structural limit that dictates the absolute maximum number of pallets it can handle during the cycle. If you tally up the pallets from every consignment traveling through a specific corridor, this combined figure cannot exceed the corridor's limit. Furthermore, pallets can only travel in the designated direction of a corridor, meaning negative pallet counts on a corridor are impossible.

You must determine if there is a routing strategy that successfully delivers every consignment's required volume in whole pallets under these physical restrictions, and if so, output the strategy.

## Input
The first line provides three integers $n$, $m$, and $k$ — the number of distribution centers, the number of one-way transit corridors, and the number of consignments.
The following $k$ lines detail the consignments. Each line gives three integers $s_i$, $t_i$, and $d_i$ — the starting center, the target center, and the required volume of pallets for consignment $i$.
The final $m$ lines detail the corridors. Each line gives three integers $u$, $v$, and $c$ — indicating a one-way corridor from center $u$ to center $v$ which can handle a maximum of $c$ pallets in total.

## Output
If a valid routing of whole pallets exists that satisfies all conditions, print `YES`. Following this, print $k$ lines. The $i$-th line should contain exactly $m$ integers, detailing the number of pallets of consignment $i$ assigned to each of the $m$ corridors, following the exact order the corridors appeared in the input.
If no such routing is possible, print `NO`.

## Example

### Input
```text
4 5 2
1 4 1
2 3 1
1 2 1
2 4 1
1 3 1
3 4 1
2 3 1
```

### Output
```text
YES
1 1 0 0 0
0 0 0 0 1
```
