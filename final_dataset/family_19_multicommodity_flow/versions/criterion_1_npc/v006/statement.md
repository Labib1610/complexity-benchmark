# Problem A — Emergency Relief Dispatch over a Shared Supply Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A disaster response agency operates a network of staging areas connected by one-way supply routes. Each route has a strict maximum limit on how many supply pallets can traverse it per day, regardless of what is being carried; this limit reflects the availability of transport vehicles on that route and cannot be exceeded.

In the current day, there are several distinct categories of relief items to move. Each category has its own origin staging area, its own destination staging area, and a firm quantity — expressed in whole pallets — that must be delivered in full during this single day. Crucially, all categories draw on the **same** routes: a route's limit applies to the combined pallet count of every category routed over it, so categories compete for the shared transport capacity even though they are otherwise independent. Pallet counts are indivisible, so the number of pallets of any given category sent along any given route is a non-negative whole number.

Pallets are conserved at every staging area that is neither a category's origin nor its destination: for each category separately, the pallets of that category entering an intermediate staging area must equal the pallets of that category leaving it. At a category's origin, the net outflow of that category equals its required quantity, and at its destination, the net inflow equals that quantity. Empty repositioning, transit times, and route distances are outside the scope of this plan and should be ignored; only the per-route limits, the per-category conservation, and the per-category delivery quantities matter.

Produce a dispatch plan that delivers every category's full quantity while respecting every route's shared limit, or determine that the network cannot carry all categories together in one day.

## Input
Line 1: Three integers $n$ (staging areas), $m$ (routes), and $k$ (categories).
Next $k$ lines: Three integers $s_i$ (origin), $t_i$ (destination), and $d_i$ (pallets required) for category $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$ representing a directed route from $u$ to $v$ with a daily limit of $cap$ pallets.

## Output
Output `YES` followed by $k$ lines, each containing $m$ integers — category $i$'s pallet count on route $j$ (in the order routes were given in the input). If a valid dispatch plan is impossible, output `NO`.

## Example

**Input:**
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

**Output:**
```
YES
5 5 5 5 0
0 0 0 0 5
```
