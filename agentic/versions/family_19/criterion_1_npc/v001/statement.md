# Problem A — Concurrent Freight Dispatch over a Shared System

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a system of hubs connected by one-way haulage routes. Each route has a strict limit on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this limit reflects the route's rolling stock and cannot be exceeded.

In the current cycle there are several distinct products to move. Each product has its own starting hub, its own ending hub, and a firm quantity — expressed in whole containers — that must be delivered in full during this single cycle. Crucially, all products draw on the **same** routes: a route's limit applies to the combined container count of every product routed over it, so products compete for the shared limit even though they are otherwise independent. Container counts are indivisible, so the number of containers of any given product sent along any given route is a non-negative whole number.

Containers are preserved at every hub that is neither a product's starting hub nor its ending hub: for each product separately, the containers of that product entering an intermediate hub must equal the containers of that product leaving it. At a product's starting hub the total departures of that product minus its total arrivals equals its required quantity, and at its ending hub the total arrivals minus its total departures equals that quantity. Empty repositioning, transit times, and route distances are outside the scope of this plan and should be ignored; only the per-route limits, the per-product balance, and the per-product delivery quantities matter.

Produce a dispatch plan that delivers every product's full quantity while respecting every route's shared limit, or determine that the system cannot carry all products together in one cycle. (Routing any single product alone may be trivial; the difficulty is that the products must coexist on the shared routes.)

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of hubs, the number of routes, and the number of products, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the starting hub, ending hub, and required quantity in containers for product $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way route from hub $u$ to hub $v$ with a maximum limit of $cap$ containers.

## Output
If a valid dispatch plan exists, output `YES` on the first line. Then, output $k$ lines. The $i$-th of these lines should contain $m$ integers, where the $j$-th integer represents the number of containers of product $i$ sent along route $j$ (in the order the routes were given in the input).
If no such plan is possible, output `NO`.

## Example

**Input:**
```text
4 5 2
1 4 2
2 3 1
1 2 2
1 3 1
2 4 1
3 4 2
2 3 1
```

**Output:**
```text
YES
1 1 1 1 0
0 0 0 0 1
```
