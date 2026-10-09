# Problem A — Microfluidic Manifold Routing for Additive Manufacturing

Time limit: 5 s   Memory limit: 256 MB

## Description
As part of a next-generation additive manufacturing pipeline, the system operates in three distinct phases: Layer Slicing, Manifold Routing, and UV Curing. You are responsible for programming the Manifold Routing phase.

In the initial Layer Slicing phase, the software identifies $k$ distinct resin compounds needed for the current layer. Each compound is assigned an injection valve, an ejection nozzle, and a required quantity of indivisible micro-batches.

During your phase—Manifold Routing—these micro-batches must be transported through a microfluidic manifold. The manifold is a system of valves connected by one-way capillary tubes. Because the fluids do not react with one another, they seamlessly share the available capacity of each tube. A common preliminary check in such systems is to evaluate the total aggregated flow from all injection valves to all ejection nozzles to ensure the network's overall capacity is sufficient. 

However, your routing algorithm must provide the complete detailed assignment. For any given tube, the sum of the micro-batches of all compounds passing through it cannot exceed the tube's rated capacity. Furthermore, the number of micro-batches of any given compound sent through any given tube must be a non-negative integer. You must track each compound individually to ensure it reaches its correct destination. For each compound, the routing must strictly conserve the number of micro-batches: at any valve that is not its specific injection or ejection point, the amount of that compound entering must exactly match the amount leaving. At its injection valve, the net outward movement of the compound must equal its required quantity, and at its ejection nozzle, the net inward movement must equal this same quantity.

Finally, in the UV Curing phase, the routed micro-batches are deposited and hardened. Your task is strictly limited to the Manifold Routing phase: you must produce a valid routing for all compounds that respects every tube's shared limit, or determine that the current layer's requirements cannot be met in a single cycle.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of valves, the number of capillary tubes, and the number of resin compounds.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$: the injection valve, ejection nozzle, and required number of micro-batches for compound $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$: representing a one-way capillary tube from valve $u$ to valve $v$ with a maximum capacity of $cap$ micro-batches.

## Output
If a valid routing is possible, print `YES` on the first line. Then, print $k$ lines. The $i$-th line should contain $m$ integers representing the number of micro-batches of compound $i$ routed through each capillary tube, given in the exact order the tubes appeared in the input.
If no such routing is possible, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 2
1 3 1
1 2 2
2 3 1
3 4 2
1 3 1
2 4 1
```

**Output:**
```
YES
1 0 1 1 1
1 1 0 0 0
```
