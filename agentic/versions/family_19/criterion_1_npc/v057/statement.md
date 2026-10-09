# Problem A — WCS Middleware: Steady-State Routing

Time limit: 5 s   Memory limit: 256 MB

## Description
In a modern automated fulfillment center, operations are orchestrated through a three-stage pipeline. First, the Inventory Management System (IMS) analyzes overnight orders and generates a relocation manifest. Second, a middleware routing engine determines if the physical conveyor network can support the manifest. Third, the Warehouse Control System (WCS) reads the routing engine's output and mechanically actuates the diverters to execute the plan. 

Your task is to implement the second stage: the middleware routing engine. 

The physical network consists of $n$ transfer zones connected by $m$ unidirectional conveyor segments. Because all items are packed in uniform standard totes, the conveyors treat them interchangeably. The structural limit of any conveyor segment is measured purely by the total number of totes traversing it per cycle, regardless of what the totes contain.

The IMS manifest provides $k$ distinct relocation batches. For each batch, a precise number of totes must be moved from a specific induction zone to a specific destination zone. 

To produce a valid configuration for the WCS, your engine must satisfy these conditions:
- The number of totes of any batch assigned to any conveyor segment must be a non-negative whole number.
- At any zone that is neither the induction nor the destination for a particular batch, the number of incoming totes for that batch must exactly balance the number of outgoing totes for that batch.
- At a batch's induction zone, the outgoing totes for that batch minus the incoming totes for that batch must equal the IMS manifest target.
- At a batch's destination zone, the incoming totes for that batch minus the outgoing totes for that batch must equal the IMS manifest target.
- For any conveyor segment, the sum of totes across all $k$ batches routed over it must not exceed its structural limit.

Determine if the WCS can be configured to execute the IMS manifest. If it is possible, generate the routing matrix required by the WCS.

## Input
The first line contains three integers $n$, $m$, and $k$ — the number of transfer zones (numbered $1$ to $n$), conveyor segments, and relocation batches.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the induction zone, destination zone, and target number of totes for batch $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a unidirectional conveyor segment from zone $u$ to zone $v$ with a structural limit of $cap$ totes per cycle.

## Output
If a valid routing matrix exists, print `YES` on the first line. Then print $k$ lines. The $i$-th of these lines must contain $m$ integers, representing the number of totes of batch $i$ routed over each of the $m$ conveyor segments, in the exact order the segments appeared in the input. If no such matrix is possible, print `NO`.

## Example
**Input:**
```
4 5 2
1 4 10
3 2 10
1 2 10
1 3 10
3 2 10
2 4 10
3 4 10
```

**Output:**
```
YES
10 0 0 10 0
0 0 10 0 0
```
