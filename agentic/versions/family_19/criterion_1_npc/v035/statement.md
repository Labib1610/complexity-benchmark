# Problem A — Concurrent Freight Dispatch over a Shared Corridor Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed network of hubs connected by one-way haulage lanes. The system is designed around strict conservation principles: empty repositioning, transit times, and lane distances are completely excluded from the model, ensuring the routing logic remains straightforward and focused solely on capacity. Each lane has a strict ceiling on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this ceiling reflects the lane's rolling stock and cannot be exceeded.

In the current cycle there are several distinct products to move. Each product has its own origin hub, its own destination hub, and a firm, predetermined quantity — expressed in whole containers — that must be delivered in full during this single cycle. Because the quantities are fixed and each product is handled independently at the hubs, you can track their conservation separately. Crucially, all products draw on the **same** lanes: a lane's ceiling applies to the combined container count of every product routed over it, so products compete for the shared capacity. Container counts are indivisible, so the number of containers of any given product sent along any given lane is a non-negative whole number.

Freight is strictly conserved at every hub that is neither a product's origin nor its destination: for each product separately, the containers of that product entering an intermediate hub must exactly equal the containers of that product leaving it. At a product's origin the net outflow of that product equals its required quantity, and at its destination the net inflow equals that quantity. 

Produce a dispatch plan that delivers every product's full quantity while respecting every lane's shared ceiling, or determine that the network cannot carry all products together in one cycle. Because the flow of each product is conserved independently, the primary task is simply ensuring their combined totals fit within the shared lane capacities.

## Input
Line 1: Three integers $n$, $m$, and $k$, representing the number of hubs, lanes, and products.
Next $k$ lines: Three integers $s_i$, $t_i$, and $d_i$, representing the origin hub, destination hub, and required container quantity for product $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, representing a directed lane from hub $u$ to hub $v$ with a shared ceiling of $cap$ containers.

## Output
If a valid dispatch plan exists, print `YES` on the first line. Then print $k$ lines, each containing $m$ integers separated by spaces. The $i$-th line should list the number of containers of product $i$ routed over each of the $m$ lanes, in the exact order the lanes were given in the input.
If no valid plan can be formed, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 10
2 3 10
1 2 10
2 4 10
1 3 10
3 4 10
2 3 10
```

**Output:**
```
YES
10 10 0 0 0
0 0 0 0 10
```
