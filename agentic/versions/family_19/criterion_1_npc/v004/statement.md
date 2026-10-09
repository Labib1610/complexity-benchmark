# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed grid of hubs connected by one-way haulage lanes. Each lane has a strict integer capacity on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this capacity reflects the lane's rolling stock and cannot be exceeded.

In the current cycle there are several distinct products to move. Each product has its own origin hub, its own destination hub, and a firm quantity — expressed in exact integers — that must be delivered in full during this single cycle. Crucially, all products draw on the **same** lanes: a lane's integer capacity applies to the combined container count of every product routed over it, so products share the network even though they are otherwise independent. Container counts are indivisible, so the number of containers of any given product sent along any given lane is a non-negative whole number.

Because all lane capacities and product requirements are purely integral, freight is conserved perfectly at every hub that is neither a product's origin nor its destination: for each product separately, the exact integer count of containers entering an intermediate hub must equal the containers leaving it. At a product's origin the net outflow of that product equals its required quantity, and at its destination the net inflow equals that quantity. Empty repositioning, transit times, and lane distances are outside the scope of this plan and should be ignored; only the integer capacities, the per-product conservation, and the exact delivery quantities matter.

Produce a dispatch plan that delivers every product's full quantity while respecting every lane's shared capacity, or determine that the grid cannot carry all products together in one cycle. (Routing any single product alone is highly tractable due to these integer properties; the task is simply to coordinate the products on the shared lanes.)

## Input
Line 1: Three integers $n$, $m$, and $k$, representing the number of hubs, lanes, and products respectively.
Next $k$ lines: Three integers $s_i$, $t_i$, and $d_i$, representing the origin hub, destination hub, and required integer quantity for product $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, representing a directed lane from hub $u$ to hub $v$ with the given integer capacity.

## Output
If a valid dispatch plan exists, print `YES` on the first line. Then, print $k$ lines, each containing $m$ integers separated by spaces. The $i$-th line should represent the flow of the $i$-th product across each of the $m$ lanes, given in the exact order the lanes appeared in the input.
If no such plan is possible, print `NO`.

## Example

**Input:**
```
4 4 2
1 4 1
1 4 1
1 2 1
2 4 1
1 3 1
3 4 1
```

**Output:**
```
YES
1 1 0 0
0 0 1 1
```
