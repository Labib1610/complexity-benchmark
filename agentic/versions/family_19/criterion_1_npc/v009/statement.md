# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed grid of hubs connected by one-way haulage lanes. Each lane has a strict ceiling on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this ceiling reflects the lane's rolling stock and cannot be exceeded. Container counts are indivisible, so the number of containers of any given category sent along any given lane is a non-negative whole number.

Freight is conserved at every hub that is neither a category's origin nor its destination: for each category separately, the containers of that category entering an intermediate hub must equal the containers of that category leaving it. Empty repositioning, transit times, and lane distances are outside the scope of this plan and should be ignored; only the per-lane ceilings, the per-category conservation, and the per-category delivery quantities matter.

In the current cycle there are several distinct products to move, each acting as a separate category. Each product has its own origin hub, its own destination hub, and a firm quantity — expressed in whole containers — that must be delivered in full during this single cycle. At a product's origin the net outflow of that product equals its required quantity, and at its destination the net inflow equals that quantity. Crucially, all products draw on the same lanes: a lane's ceiling applies to the combined container count of every product routed over it, so products compete for the shared capacity even though they are otherwise independent.

Produce a dispatch plan that delivers every product's full quantity while respecting every lane's shared ceiling, or determine that the grid cannot carry all products together in one cycle. (Routing any single product alone may be trivial; the difficulty is that the products must coexist on the shared lanes.)

## Input
Line 1: Three integers $n$ (number of hubs), $m$ (number of lanes), and $k$ (number of products).
Next $k$ lines: Three integers $s_i$ (origin), $t_i$ (destination), and $d_i$ (quantity) for product $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, representing a directed lane from hub $u$ to hub $v$ with the given capacity ceiling.

## Output
If a valid dispatch plan exists, print `YES` on the first line. Then print $k$ lines, each containing $m$ space-separated integers. The $j$-th integer on the $i$-th of these lines must represent the number of containers of product $i$ sent along lane $j$ (where lanes are indexed 1 to $m$ in the order they appear in the input).
If no such plan is possible, print `NO`.

## Example

### Input
```
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 3 1
2 4 1
3 4 1
```

### Output
```
YES
0 1 0 0 1
0 0 1 0 0
```
