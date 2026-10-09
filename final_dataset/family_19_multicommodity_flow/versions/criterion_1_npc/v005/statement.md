# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed grid of hubs connected by one-way haulage lanes. Each lane is equipped with a fixed fleet of transport vehicles. Since each vehicle can haul exactly one container per dispatch cycle, a lane's vehicle count dictates the maximum total number of containers that can traverse it, regardless of what is being carried.

In the current cycle there are several distinct products to move. Each product has its own origin hub, its own destination hub, and a firm quantity — expressed in whole containers — that must be delivered in full during this single cycle. Crucially, all products draw on the **same** lanes: a lane's vehicle fleet must handle the combined container count of every product routed over it, so products compete for the shared capacity even though they are otherwise independent. Containers cannot be subdivided and a lane cannot transport a deficit of cargo, meaning the count of containers for any product on any lane must be counted in whole units from zero upwards.

Freight is conserved at every hub that is neither a product's origin nor its destination: for each product separately, the containers of that product entering an intermediate hub must equal the containers of that product leaving it. At a product's origin the net outflow of that product equals its required quantity, and at its destination the net inflow equals that quantity. Empty repositioning, transit times, and lane distances are outside the scope of this plan and should be ignored; only the per-lane vehicle counts, the per-product conservation, and the per-product delivery quantities matter.

Produce a dispatch plan that delivers every product's full quantity while respecting every lane's shared vehicle fleet, or determine that the grid cannot carry all products together in one cycle. (Routing any single product alone may be trivial; the difficulty is that the products must coexist on the shared lanes.)

## Input
Line 1: `n m k`. 
Next `k` lines: `s_i t_i d_i`. 
Next `m` lines: `u v cap` (directed link `u`->`v`, where `cap` is the vehicle count).

## Output
`YES` then `k` lines, each with `m` integers — commodity `i`'s flow on link `j` (input order); or `NO`.

## Example
### Input
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

### Output
```
YES
1 1 0 0 0
0 0 0 0 1
```
