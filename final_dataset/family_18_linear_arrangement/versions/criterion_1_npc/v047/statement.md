# Problem A — Signal Routing on a Linear Backplane

Time limit: 5 s   Memory limit: 256 MB

## Description
The automated schematic capture phase has just completed. It has generated a manifest of $n$ distinct electronic modules that must be integrated, along with a list of $m$ dedicated communication traces required between specific pairs of these modules. 

Your task is the layout validation phase. The mechanical chassis provided for this integration features a linear backplane with exactly $n$ mounting slots arranged in a single straight row. You must assign each module to exactly one slot, such that every slot receives exactly one module. The slots are numbered consecutively from 1 to $n$. To satisfy mechanical balancing constraints, the layout must ensure that the sum of the slot numbers assigned to all $n$ modules is exactly $\frac{n(n+1)}{2}$.

When two modules are required to communicate, a physical data cable must be routed between their respective slots. The chassis includes a straight cable channel running alongside the slots. The length of cable required for any single communication trace is determined entirely by the distance between the two slots it connects. Specifically, if one module is placed in slot $x$ and the other in slot $y$, the cable length for that trace is exactly $|x - y|$ units. Due to the physical dimensions of the chassis, no single cable can ever exceed a length of $n-1$ units.

Additionally, to comply with the chassis power distribution limits, the input is guaranteed to satisfy the property that the aggregate number of trace terminations across all modules is exactly $2m$. 

The procurement department has allocated a total cable budget of $B$ units for the entire chassis. You must determine if there exists a valid assignment of all $n$ modules to the $n$ slots such that the sum of the cable lengths for all $m$ required traces is at most $B$. 

If you find a valid layout, it will be passed to the fabrication phase where the cables will be cut and the modules installed according to your specifications. If no such layout exists, the chassis design will be rejected.

## Input
The first line contains three integers $n$, $m$, and $B$. 
Each of the next $m$ lines contains two integers $u$ and $v$ — a required communication trace between module $u$ and module $v$.

## Output
Print `YES` then a line with $n$ integers — the slot number (1..$n$, a permutation) assigned to module 1, 2, ..., $n$ — such that the total cable length is $\le B$. Otherwise print `NO`.

## Example

**Input:**
```
5 4 4
1 3
3 5
5 2
2 4
```

**Output:**
```
YES
1 4 2 5 3
```
