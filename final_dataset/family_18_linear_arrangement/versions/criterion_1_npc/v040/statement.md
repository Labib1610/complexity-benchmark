# Problem A — Assembly Line Layout Validation

Time limit: 5 s   Memory limit: 256 MB

## Description
The automated schematic capture phase has just completed. It has generated a manifest of $n$ distinct electronic assemblies that must be integrated, along with a list of $m$ dedicated communication links required between specific pairs of these assemblies. 

Your task is the layout validation phase. The mechanical chassis provided for this integration features exactly $n$ mounting bays arranged in a single straight row. You must assign each assembly to exactly one bay, such that every bay receives exactly one assembly. The bays are numbered consecutively from 1 to $n$.

When two assemblies are required to communicate, a physical data cable must be routed between their respective bays. The chassis includes a straight cable channel running alongside the bays. The length of cable required for any single communication link is determined entirely by the distance between the two bays it connects. Specifically, if one assembly is placed in bay $x$ and the other in bay $y$, the cable length for that link is exactly $|x - y|$ units. 

The procurement department has allocated a total cable budget of $B$ units for the entire chassis. You must determine if there exists a valid assignment of all $n$ assemblies to the $n$ bays such that the sum of the cable lengths for all $m$ required links is at most $B$. 

If you find a valid layout, it will be passed to the fabrication phase where the cables will be cut and the assemblies installed according to your specifications. If no such layout exists, the chassis design will be rejected.

## Input
First line: three integers $n$, $m$, $B$. 
Each of the next $m$ lines: two integers $u$ $v$ — a required communication link between assembly $u$ and assembly $v$.

## Output
Print `YES` then a line with $n$ integers — the bay number (1..$n$, a permutation) assigned to assembly 1, 2, ..., $n$ — such that the total cable length is $\le B$. Otherwise print `NO`.

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
