# Problem A — Spatial Dispersion

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a set of **t** valid anchor points in a 3-dimensional grid. The grid spans from 1 to **k** along the X, Y, and Z axes. 

Your objective is to select exactly **k** anchor points from the provided list to form a dispersed constellation. A constellation is valid if and only if every pair of selected points is separated by a non-zero distance along all three axes simultaneously. 

Formally, for any two distinct selected points $P = (P_x, P_y, P_z)$ and $Q = (Q_x, Q_y, Q_z)$, their coordinates must satisfy:
$\min(|P_x - Q_x|, |P_y - Q_y|, |P_z - Q_z|) \ge 1$

Determine if it is possible to form such a constellation. If it is, provide the coordinates of the **k** chosen points.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k). Here, **k** determines the bounds of the grid, and **t** is the number of valid anchor points available.

The next **t** lines each contain three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k). Each line describes the coordinates of a valid anchor point. No point appears more than once in the list.

## Output

If a valid constellation of exactly **k** points exists, output `YES` on the first line. Following this, output **k** lines, each containing three integers `x y z` corresponding to a chosen anchor point. The chosen points must strictly satisfy the condition that no two points share the same X-coordinate, no two share the same Y-coordinate, and no two share the same Z-coordinate. Any valid constellation is acceptable, and the points may be printed in any order.

If no such constellation exists, output `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

In Example 2, both valid anchor points share a Y-coordinate of 1. A constellation of exactly 2 points cannot be formed without reusing this Y-coordinate, which results in $|P_y - Q_y| = 0$ for the pair, violating the requirement that $\min(|P_x - Q_x|, |P_y - Q_y|, |P_z - Q_z|) \ge 1$.