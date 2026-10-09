# Problem A — Architectural Harmony

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a structural framework within a 3D architectural space. The space is defined by a grid where each coordinate (**x**, **y**, and **z**) ranges from 1 to **k**.

You are provided with a catalog of **t** available support struts. Each strut is designed to be installed at a specific grid location, given by its coordinates (**x**, **y**, **z**). No two available struts are designed for the exact same location.

You must select a subset of exactly **k** struts from the catalog to form a stable framework. To ensure proper load distribution, the framework must satisfy this strict non-alignment condition:
- No two chosen struts may share the same **x**-coordinate.
- No two chosen struts may share the same **y**-coordinate.
- No two chosen struts may share the same **z**-coordinate.

Determine whether it is possible to select a stable framework of exactly **k** struts from the catalog, and if so, report one valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the grid dimension, and the number of available struts. 
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an available strut at coordinates **x**, **y**, and **z**. No location is listed more than once.

## Output

If a stable framework of **k** struts exists, print `YES` on the first line, then print **k** lines, each containing the three coordinates `x y z` of one chosen strut. Any selection meeting the conditions is accepted; the struts may be printed in any order.

If no stable framework exists, print `NO`.

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

In Example 2, both available struts share the same **y**-coordinate (1). Choosing both would violate the non-alignment condition, so it is impossible to choose 2 valid struts.