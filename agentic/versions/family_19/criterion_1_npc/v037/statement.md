# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed grid of hubs connected by one-way haulage lanes. Each lane has a strict physical limit on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this limit is dictated by the lane's available rolling stock and cannot be breached.

In the current cycle there are several distinct products to move. Each product has its own origin hub, its own destination hub, and a firm target — a specific physical count of whole containers — that must be delivered in full during this single cycle. Crucially, all products draw on the **same** lanes: the total physical count of all containers from all products routed over a lane is bounded by that lane's rolling stock limit, so products compete for the shared capacity even though they are otherwise independent. Container counts are indivisible, so the number of containers of any given product sent along any given lane must be a count of zero or more whole containers.

Freight is conserved at every hub that is neither a product's origin nor its destination: for each product separately, the physical count of containers of that product entering an intermediate hub must exactly match the count leaving it. At a product's origin the net outflow of that product must match its target number of containers, and at its destination the net inflow must match that target. Empty repositioning, transit times, and lane distances are outside the scope of this plan and should be ignored; only the rolling stock limits, the per-product conservation, and the per-product delivery targets matter.

Produce a dispatch plan that delivers every product's full target while respecting every lane's shared rolling stock limit, or determine that the grid cannot carry all products together in one cycle. (Routing any single product alone may be trivial; the difficulty is that the products must coexist on the shared lanes.)

## Input
Line 1: `n m k`. 
Next `k` lines: `s_i t_i d_i`. 
Next `m` lines: `u v cap` (directed link u->v).

## Output
`YES` then `k` lines, each with `m` integers — commodity i's flow on link j (input order); or `NO`.

## Example

### Input
```text
4 4 2
1 4 1
2 3 1
1 2 1
2 3 1
3 4 1
1 4 1
```

### Output
```text
YES
0 0 0 1
0 1 0 0
```
