# Drone Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing facility is producing $k$ autonomous drones. A complete drone requires a chassis, a navigation unit, and a battery. The facility has exactly $k$ of each component type in inventory, with each type serialized from 1 to $k$.

To guarantee flight stability, engineers have compiled a catalog of tested schematics. Each schematic lists one chassis, one navigation unit, and one battery that function correctly together.

Earlier in the production line, a welding process permanently fused each chassis to a navigation unit. This process ensured that each chassis was attached to exactly one navigation unit, and no navigation unit was attached to more than one chassis. Because of this, any schematic in the catalog featuring a particular chassis will always list the exact same navigation unit, and no two different chassis will ever be listed with the same navigation unit.

Your task is to determine if it is possible to assemble exactly $k$ drones by selecting $k$ schematics from the catalog so that every chassis, every navigation unit, and every battery from the inventory is utilized exactly once. If possible, provide one such valid selection of schematics.

## Input

The first line contains two integers $k$ and $t$ (1 ≤ $k$ ≤ 1200, 0 ≤ $t$ ≤ $k \cdot k$), representing the number of drones to build and the total number of tested schematics.
Each of the following $t$ lines contains three integers $x$, $y$, and $z$ (1 ≤ $x, y, z$ ≤ $k$), representing a schematic that combines chassis $x$, navigation unit $y$, and battery $z$. 
No schematic appears more than once in the input. The welding guarantee holds: for any given $x$, all schematics containing $x$ will have the same $y$, and no two different $x$ values will share the same $y$.

## Output

If exactly $k$ drones can be successfully assembled, print `YES` on the first line. Then, print $k$ lines, each containing the three integers `x y z` of a chosen schematic, separated by spaces. The lines may be printed in any order. Any valid set of $k$ schematics is acceptable.

If it is impossible to assemble $k$ drones under these conditions, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both chassis only have tested schematics utilizing battery 1, meaning battery 2 can never be successfully integrated. Thus, building 2 complete drones is impossible.
