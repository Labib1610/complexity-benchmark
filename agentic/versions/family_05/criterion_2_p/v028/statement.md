# Drone Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A factory is building $k$ autonomous drones. Each drone is assembled from exactly three distinct components:
- A control board (numbered 1 to $k$)
- A sensor array (numbered 1 to $k$)
- A power module (numbered 1 to $k$)

To ensure stability, the factory has tested various configurations and produced a list of certified triples. Each triple specifies one control board, one sensor array, and one power module that can successfully operate together.

Before this assembly step, a firmware flashing process permanently locked each control board to exactly one sensor array. Furthermore, no two control boards were locked to the same sensor array. As a result, in the list of certified triples, any specific control board will always appear alongside the same sensor array, and distinct control boards will always appear with distinct sensor arrays.

Determine if it is possible to build exactly $k$ drones by choosing $k$ triples from the certified list such that every control board, every sensor array, and every power module from the inventory is used exactly once. If it is possible, output one such valid selection of triples.

## Input

The first line contains two integers $k$ and $t$ (1 ≤ $k$ ≤ 1200, 0 ≤ $t$ ≤ $k \cdot k$), representing the number of drones to build and the total number of certified triples.
Each of the following $t$ lines contains three integers $x$, $y$, and $z$ (1 ≤ $x, y, z$ ≤ $k$), representing a certified triple consisting of control board $x$, sensor array $y$, and power module $z$. 
No triple appears more than once in the input. The firmware lock guarantee holds: for any given $x$, all triples containing $x$ will have the same $y$, and no two different $x$ values will share the same $y$.

## Output

If exactly $k$ drones can be successfully assembled, print `YES` on the first line. Then, print $k$ lines, each containing the three integers `x y z` of a chosen certified triple, separated by spaces. The lines may be printed in any order. Any valid set of $k$ triples is acceptable.

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

In Example 2, both control boards only have certified configurations utilizing power module 1, meaning power module 2 can never be successfully integrated. Thus, building 2 complete drones is impossible.
