# Problem A — Concurrent Freight Dispatch over a Shared Corridor System

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a system of warehouses connected by unidirectional transit segments. Each segment has a strict upper limit on how many intact crates can traverse it per operating phase. This limit applies to the combined physical count of all crates routed over the segment, regardless of which client they belong to.

In the upcoming phase, there are several distinct client contracts to fulfill. Each contract mandates moving a specific volume of crates—expressed as a whole number—from a source warehouse to a receiving warehouse. All contracts must be executed simultaneously over the shared system. Crates from different contracts compete for the same segment limits, meaning the sum of crates from all contracts on any single segment cannot exceed that segment's limit.

Crates cannot be dismantled; the number of crates allocated to any segment for any contract must be a non-negative integer. Furthermore, crates cannot be stored or discarded mid-journey. For any given contract, if a warehouse is neither its source nor its receiver, the total number of its crates entering the warehouse must equal the total number of its crates leaving it. At a contract's source warehouse, the number of its departing crates must exceed its arriving crates by exactly the required volume. Similarly, at its receiving warehouse, its arriving crates must exceed its departing crates by exactly the required volume.

Produce a dispatch plan that successfully executes every contract's required volume simultaneously without violating any segment's shared limit, or determine that the system cannot support all contracts in a single phase.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of warehouses, transit segments, and client contracts, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, specifying the source warehouse, the receiving warehouse, and the required volume of crates for the $i$-th contract.
The following $m$ lines each contain three integers $u$, $v$, and $c$, describing a unidirectional transit segment from warehouse $u$ to warehouse $v$ with a maximum limit of $c$ crates.

## Output
If a valid dispatch plan exists, print `YES` on the first line. Then, print $k$ lines. The $i$-th of these lines should contain $m$ integers, where the $j$-th integer represents the number of crates belonging to the $i$-th contract routed over the $j$-th transit segment (in the order segments are given in the input).
If no such plan exists, print `NO`.

## Example

### Input
```text
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 4 1
3 4 1
2 3 1
```

### Output
```text
YES
1 0 1 0 0
0 0 0 0 1
```
