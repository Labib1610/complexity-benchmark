# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed grid of hubs connected by one-way haulage lanes. Each lane has
a strict ceiling on how many containers can traverse it per dispatch cycle, regardless of what is being
carried; this ceiling reflects the lane's rolling stock and cannot be exceeded. You are guaranteed that no lane has a ceiling that strictly exceeds the sum of the ceilings of all lanes in the grid.

In the current cycle there are several distinct products to move. Each product has its own origin hub,
its own destination hub, and a firm quantity — expressed in whole containers — that must be delivered in
full during this single cycle. You are additionally guaranteed that the required quantity for any single product is no greater than the total required quantity across all products. Crucially, all products draw on the **same** lanes: a lane's ceiling
applies to the combined container count of every product routed over it, so products compete for the
shared capacity even though they are otherwise independent. Container counts are indivisible, so the
number of containers of any given product sent along any given lane is a non-negative whole number.

Freight is conserved at every hub that is neither a product's origin nor its destination: for each
product separately, the containers of that product entering an intermediate hub must equal the containers
of that product leaving it. At a product's origin the net outflow of that product equals its required
quantity, and at its destination the net inflow equals that quantity. Empty repositioning, transit times,
and lane distances are outside the scope of this plan and should be ignored; only the per-lane ceilings,
the per-product conservation, and the per-product delivery quantities matter.

Produce a dispatch plan that delivers every product's full quantity while respecting every lane's shared
ceiling, or determine that the grid cannot carry all products together in one cycle. (Routing any single
product alone may be trivial; the difficulty is that the products must coexist on the shared lanes.)

## Input
Line 1: `n m k`.
Next `k` lines: `s_i t_i d_i`, where `s_i` is the origin, `t_i` is the destination, and `d_i` is the required quantity for product `i`.
Next `m` lines: `u v cap`, representing a directed lane from hub `u` to hub `v` with a ceiling of `cap`.

## Output
Print `YES` followed by `k` lines, each containing `m` integers representing product `i`'s container count on lane `j` (in the order the lanes were given in the input). If no such plan is possible, print `NO`.

## Example

### Input
```
4 5 2
1 4 10
2 3 5
1 2 10
2 4 10
1 3 5
3 4 5
2 3 5
```

### Output
```
YES
10 10 0 0 0
0 0 0 0 5
```
