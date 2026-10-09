# Problem A — Phase II: Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
The national distributor's weekly planning workflow consists of three phases. In Phase I, analysts forecast the required product quantities and assess the strict ceilings on how many containers can traverse each one-way haulage lane per dispatch cycle. This phase has just concluded, providing the current cycle's requirements over the directed grid of hubs.

You must now execute Phase II: generating the dispatch plan. There are several distinct products to move. Each product has its own origin hub, its own destination hub, and a firm quantity — expressed in whole containers — that must be delivered in full during this single cycle. Crucially, all products draw on the **same** lanes: a lane's ceiling applies to the combined container count of every product routed over it, so products compete for the shared capacity even though they are otherwise independent. Container counts are indivisible, so the number of containers of any given product sent along any given lane is a non-negative whole number.

Freight is conserved at every hub that is neither a product's origin nor its destination: for each product separately, the containers of that product entering an intermediate hub must equal the containers of that product leaving it. At a product's origin the net outflow of that product equals its required quantity, and at its destination the net inflow equals that quantity. Empty repositioning, transit times, and lane distances are handled in Phase III (driver scheduling) and should be ignored here; only the per-lane ceilings, the per-product conservation, and the per-product delivery quantities matter for Phase II.

Produce a Phase II dispatch plan that delivers every product's full quantity while respecting every lane's shared ceiling, or determine that the grid cannot carry all products together in one cycle. The output of your Phase II plan will be passed directly to Phase III.

## Input
Line 1: Three integers `n`, `m`, and `k`, representing the number of hubs, haulage lanes, and distinct products.
Next `k` lines: Three integers `s_i`, `t_i`, and `d_i`, representing the origin hub, destination hub, and required quantity for product `i`.
Next `m` lines: Three integers `u`, `v`, and `cap`, representing a directed lane from hub `u` to hub `v` with a shared capacity ceiling of `cap`.

## Output
If a valid Phase II plan exists, output `YES` followed by `k` lines. Each line must contain `m` integers representing product `i`'s container count on lane `j` (in the order the lanes were given in the input). If no such plan exists, output `NO`.

## Example

**Input**
```text
4 5 2
1 4 1
2 3 1
1 2 1
2 4 1
2 3 1
3 4 1
1 3 1
```

**Output**
```text
YES
1 1 0 0 0
0 0 1 0 0
```
