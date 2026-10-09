# Problem A — Concurrent Freight Dispatch

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics operator manages a network of $n$ distribution centers. The network includes $m$ one-way shipping routes, each connecting a specific pair of centers. Every route has a strict daily quota, representing the maximum total number of cargo containers it can transport across all operations, dictated by vehicle availability.

During the current operational shift, $k$ delivery contracts must be fulfilled. Each contract requires the transportation of a specific number of intact containers from a designated source center to a designated destination center.

You must determine a valid routing schedule that fully satisfies all $k$ contracts simultaneously. The schedule must strictly adhere to the following rules:
- Containers are indivisible entities. The number of containers assigned to any route for any contract must be a non-negative integer.
- All contracts share the same network infrastructure. For any given shipping route, the sum of containers assigned to it across all $k$ contracts cannot exceed that route's daily quota.
- For any contract, at any distribution center that is neither its source nor its destination, the total number of containers arriving for that contract must exactly equal the total number of containers departing for that contract.
- For any contract, at its source center, the number of departing containers minus the number of arriving containers for that contract must exactly equal the contract's required volume.
- For any contract, at its destination center, the number of arriving containers minus the number of departing containers for that contract must exactly equal the contract's required volume.

To reflect the structural limits of the logistics network, the input guarantees the following properties:
- **Hub Degree Guarantee**: No individual distribution center serves as the starting point for more than $m$ shipping routes, nor as the destination for more than $m$ shipping routes.
- **Quota Subadditivity Guarantee**: No single shipping route has a daily quota that strictly exceeds the total sum of the daily quotas of all $m$ shipping routes combined.

Determine if there exists a valid assignment of containers to routes that fulfills all $k$ contracts without exceeding any route's quota. If it is possible, you must also provide the exact assignment.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of distribution centers, shipping routes, and delivery contracts.
The following $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the source center, the destination center, and the required number of containers for the $i$-th contract.
The next $m$ lines each contain three integers $u$, $v$, and $c$, indicating a one-way shipping route from center $u$ to center $v$ with a daily quota of $c$ containers.

## Output
If it is possible to fulfill all contracts, output `YES` on the first line. Then, output $k$ lines. The $i$-th of these lines should contain $m$ integers, representing the number of containers for the $i$-th contract assigned to each of the $m$ shipping routes, in the exact order the routes were given in the input.
If it is impossible, output `NO`.

## Example

### Input
```text
4 5 2
1 4 2
2 3 1
1 2 2
2 3 2
3 4 2
1 3 1
2 4 1
```

### Output
```text
YES
1 0 1 1 1
0 1 0 0 0
```
