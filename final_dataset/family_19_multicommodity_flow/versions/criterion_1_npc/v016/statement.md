# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed network of distribution centers connected by one-way transit corridors. Each corridor has a strict transit limit on how many standardized crates can traverse it per operational shift. This limit is dictated by the corridor's physical infrastructure and cannot be exceeded under any circumstances.

During the current shift, there are $k$ distinct freight contracts to fulfill. Each contract specifies its own origin center, its own destination center, and a firm volume—expressed in whole crates—that must be fully transported during this single shift. Crucially, all contracts draw on the **same** underlying infrastructure: a corridor's transit limit applies to the combined crate count of every contract routed through it. Contracts compete for the shared capacity even though their contents are independent. Crate counts are indivisible, meaning the number of crates for any given contract sent along any given corridor must be a non-negative integer.

Crate conservation applies at every distribution center that is neither a contract's origin nor its destination: for each contract evaluated independently, the number of crates belonging to that contract entering an intermediate center must exactly equal the number of crates of that contract leaving it. At a contract's origin, its net outflow must equal its required volume, and at its destination, its net inflow must equal that volume. 

To ensure grid stability, the national distributor's network strictly adheres to two structural invariants:
1. No single distribution center serves as the origin for more than $k$ distinct freight contracts.
2. The total number of corridor connections (inbound plus outbound) at any individual distribution center will never exceed $2m$, where $m$ is the total number of corridors in the grid.

Empty repositioning, travel times, and corridor lengths are outside the scope of this logistics plan and should be disregarded; only the per-corridor transit limits, the per-contract conservation rules, and the per-contract delivery volumes are relevant.

Produce a routing plan that fulfills every contract's full volume while respecting every corridor's shared transit limit, or determine that the network cannot support all contracts simultaneously in one shift.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of distribution centers, the number of corridors, and the number of freight contracts, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, specifying the origin center, destination center, and required crate volume for contract $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a directed corridor from center $u$ to center $v$ with a shared transit limit of $cap$.

## Output
If a valid routing plan exists, print `YES` on the first line. Then, print $k$ lines, each containing $m$ space-separated integers. The $j$-th integer on the $i$-th line must represent the number of crates for contract $i$ routed through corridor $j$ (corridors are indexed in the order they appear in the input).
If no such plan is possible, print `NO`.

## Example
### Input
```text
4 3 2
1 3 5
2 4 5
1 2 10
2 3 10
3 4 10
```

### Output
```text
YES
5 5 0
0 5 5
```
