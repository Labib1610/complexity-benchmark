# Problem A — Freight Corridor Allocation

Time limit: 5 s   Memory limit: 256 MB

## Description
A national rail authority coordinates train movements across $n$ switching yards connected by $m$ directional track corridors. Each corridor has a strict daily signaling allowance that limits the total number of cars it can safely process, regardless of which order they belong to. 

The authority must fulfill $k$ distinct freight orders today. Each order requires moving an exact number of intact cars from a specific loading yard to an unloading yard. Because train cars cannot be disassembled, the number of cars from any given order assigned to a corridor must be a non-negative whole number. 

Cars from a specific order do not spontaneously appear or disappear en route. At any yard other than an order's designated loading or unloading site, the volume of cars from that order entering the yard must exactly match the volume leaving it. At the loading yard, the number of departing cars for the order minus any arriving cars for that order must equal the required freight amount. Conversely, at the unloading yard, arriving cars minus departing cars for that order must equal the required amount. Because all orders share the same track infrastructure, the sum of cars from all orders routed over a single corridor cannot exceed that corridor's allowance.

Determine if there is a daily routing schedule that fulfills all $k$ freight orders simultaneously without exceeding any corridor's allowance. If such a schedule exists, provide the exact number of cars from each order to route over each corridor.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of switching yards, track corridors, and freight orders.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the loading yard, the unloading yard, and the fixed number of cars required for order $i$.
The final $m$ lines each contain three integers $u_j$, $v_j$, and $c_j$, representing a directional track corridor from yard $u_j$ to yard $v_j$ with a daily allowance of $c_j$ cars.

## Output
If no valid routing schedule exists, output `NO`.
Otherwise, output `YES` on the first line. Then, output $k$ lines. The $i$-th of these lines must contain $m$ space-separated integers, where the $j$-th integer represents the number of cars from order $i$ routed over the $j$-th corridor (following the exact order the corridors were provided in the input).

## Example

### Input
```
4 5 2
1 4 2
1 3 1
1 2 2
2 4 2
1 3 2
3 4 2
2 3 1
```

### Output
```
YES
2 2 0 0 0
0 0 1 0 0
```
