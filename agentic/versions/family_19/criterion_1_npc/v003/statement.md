# Problem A — Concurrent Freight Dispatch over a Shared Corridor System

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a system of hubs connected by one-way haulage lanes. Each lane has a strict ceiling on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this ceiling reflects the lane's rolling stock and cannot be exceeded.

In the current cycle there are several distinct products to move. Each product has its own origin hub, its own destination hub, and a firm quantity — expressed in whole containers — that must be delivered in full during this single cycle. Crucially, all products draw on the **same** lanes: a lane's ceiling applies to the combined container count of every product routed over it, so products compete for the shared capacity even though they are otherwise independent. Container counts are indivisible, so the number of containers of any given product sent along any given lane is a non-negative whole number.

Freight is conserved at every hub that is neither a product's origin nor its destination: for each product separately, the containers of that product entering an intermediate hub must equal the containers of that product leaving it. At a product's origin the net outflow of that product equals its required quantity, and at its destination the net inflow equals that quantity. Empty repositioning, transit times, and lane distances are outside the scope of this plan and should be ignored; only the per-lane ceilings, the per-product conservation, and the per-product delivery quantities matter.

Produce a dispatch plan that delivers every product's full quantity while respecting every lane's shared ceiling, or determine that the system cannot carry all products together in one cycle. (Routing any single product alone may be straightforward; the difficulty is that the products must coexist on the shared lanes.)

## Input
Line 1: `n` (hubs), `m` (lanes), `k` (products).
Next `k` lines: `s_i` (origin), `t_i` (destination), `d_i` (quantity) for each product `i`.
Next `m` lines: `u` `v` `cap` (a one-way lane from hub `u` to hub `v` with ceiling `cap`).

## Output
`YES` followed by `k` lines, each containing `m` integers — the number of containers of product `i` sent over lane `j` (in the order lanes were given in the input); or `NO`.

## Example
**Input:**
```
4 5 2
1 4 1
2 3 1
1 2 1
2 4 1
1 3 1
3 4 1
2 3 1
```

**Output:**
```
YES
1 1 0 0 0
0 0 0 0 1
```
