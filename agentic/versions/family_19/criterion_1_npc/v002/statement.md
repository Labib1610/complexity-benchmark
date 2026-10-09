# Problem A — Concurrent Part Routing over a Shared Conveyor Layout

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing plant operates a directed layout of junctions connected by one-way conveyor belts. Each belt has a strict ceiling on how many parts can traverse it per production cycle, regardless of what is being carried; this ceiling reflects the belt's physical width and cannot be exceeded.

In the current cycle there are several distinct part types to move. Each part type has its own origin junction, its own destination junction, and a firm quantity — expressed in whole parts — that must be delivered in full during this single cycle. Crucially, all part types draw on the **same** belts: a belt's ceiling applies to the combined part count of every type routed over it, so part types compete for the shared capacity even though they are otherwise independent. Part counts are indivisible, so the number of parts of any given type sent along any given belt is a non-negative whole number.

Material is conserved at every junction that is neither a part type's origin nor its destination: for each type separately, the parts of that type entering an intermediate junction must equal the parts of that type leaving it. At a type's origin the net outflow of that type equals its required quantity, and at its destination the net inflow equals that quantity. Belt speeds, transit times, and physical distances are outside the scope of this plan and should be ignored; only the per-belt ceilings, the per-type conservation, and the per-type delivery quantities matter.

Produce a routing plan that delivers every part type's full quantity while respecting every belt's shared ceiling, or determine that the layout cannot carry all part types together in one cycle. (Routing any single type alone may be trivial; the difficulty is that the types must coexist on the shared belts.)

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of junctions, the number of conveyor belts, and the number of part types, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the origin junction, destination junction, and required quantity for part type $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a directed conveyor belt from junction $u$ to junction $v$ with a capacity ceiling of $cap$.

## Output
If a valid routing plan exists, print `YES` on the first line. Then print $k$ lines, each containing $m$ integers separated by spaces. The $i$-th line should represent the flow of part type $i$ on each of the $m$ belts, in the exact order the belts were given in the input.
If no such plan exists, print `NO`.

## Example 1

### Input
```text
4 3 2
1 3 1
2 4 1
1 2 1
2 3 1
3 4 1
```

### Output
```text
NO
```

## Example 2

### Input
```text
4 4 2
1 3 1
2 4 1
1 2 1
2 3 2
3 4 1
1 4 1
```

### Output
```text
YES
1 1 0 0
0 1 1 0
```
