# Problem A — Concurrent Freight Dispatch over a Shared Corridor Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a directed network of hubs connected by one-way haulage lanes. The network is highly structured: every lane has a strict integer ceiling on the total number of containers it can carry per dispatch cycle, and all data is perfectly known in advance.

In the current cycle, there are $k$ distinct products to move. Each product operates entirely independently in terms of its logic: it has a specific origin hub, a specific destination hub, and a precise integer quantity of containers that must be delivered. There are no complex transit times, no empty repositioning rules, and no distance constraints to calculate. The only requirement is that the container count for each product is perfectly conserved at all intermediate hubs, meaning the number of containers of a specific product entering a hub equals the number leaving it (unless it is the product's origin or destination). At a product's origin, its net outflow equals its required quantity, and at its destination, its net inflow equals that quantity.

Because the products share the same physical infrastructure, the combined total of all containers (regardless of product) traversing a single lane cannot exceed that lane's integer ceiling. Furthermore, containers are indivisible physical units. All dispatch plans must therefore route only non-negative whole numbers of containers for each product on any given lane.

Given the strict integrality of the lane ceilings and the delivery requirements, determine if there is a valid whole-number dispatch plan that delivers every product's required quantity simultaneously, and if so, provide one.

## Input
The first line contains three integers $n$, $m$, and $k$ — the number of hubs, the number of directed lanes, and the number of distinct products.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$ — the origin hub, destination hub, and required container quantity for product $i$.
The next $m$ lines each contain three integers $u$, $v$, and $c$ — a one-way lane from hub $u$ to hub $v$ with a shared integer capacity of $c$ containers per cycle.

## Output
If all products can be concurrently delivered in whole containers without exceeding any lane's shared capacity, output `YES`. Then output $k$ lines. The $i$-th line must contain exactly $m$ integers, representing the number of containers of product $i$ routed along each of the $m$ lanes, strictly in the order the lanes were provided in the input.
If no such integer plan is possible, output `NO`.

## Example

### Input
```text
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
```text
YES
1 1 0 0 0
0 0 0 0 1
```
