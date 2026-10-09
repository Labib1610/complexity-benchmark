# Problem A — Concurrent Freight Dispatch over a Shared Corridor System

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a system of hubs. Between certain pairs of hubs, there are one-way haulage lanes. Each lane has a strict ceiling on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this ceiling reflects the lane's rolling stock and cannot be exceeded.

In the current cycle there are several distinct products to move. Each product has its own origin hub, its own destination hub, and a firm quantity — expressed in whole containers — that must be delivered in full during this single cycle. Crucially, all products draw on the **same** lanes: a lane's ceiling applies to the combined container count of every product routed over it, so products compete for the shared capacity even though they are otherwise independent. Container counts are indivisible, so the number of containers of any given product sent along any given lane is a non-negative whole number.

Freight is conserved at every hub that is neither a product's origin nor its destination: for each product separately, the containers of that product entering an intermediate hub must equal the containers of that product leaving it. At a product's origin the net outflow of that product equals its required quantity, and at its destination the net inflow equals that quantity. Empty repositioning, transit times, and lane distances are outside the scope of this plan and should be ignored; only the per-lane ceilings, the per-product conservation, and the per-product delivery quantities matter.

Produce a dispatch plan that delivers every product's full quantity while respecting every lane's shared ceiling, or determine that the system cannot carry all products together in one cycle. (Routing any single product alone may be trivial; the difficulty is that the products must coexist on the shared lanes.)

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of hubs, lanes, and products, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the origin hub, destination hub, and required container quantity for product $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way lane from hub $u$ to hub $v$ with a capacity ceiling of $cap$.

## Output
If a valid dispatch plan exists, output `YES` on the first line. Then output $k$ lines, where the $i$-th line contains $m$ integers representing the number of containers of product $i$ routed along each of the $m$ lanes (in the same order the lanes were given in the input). If no such plan exists, output `NO`.

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
