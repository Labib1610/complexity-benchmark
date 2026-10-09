# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A project requires **k** active crews to complete its tasks. To establish these crews, the coordinator has secured **k** specialists, **k** machinery units, and **k** distinct time windows. Within each category, the resources are indexed from 1 to **k**.

The coordinator has evaluated the compatibility of these resources and compiled a catalog of **t** approved operational blueprints. Each blueprint defines a specific combination of a specialist, a machinery unit, and a time window that can successfully work together.

To deploy the crews, you must select exactly **k** blueprints from the catalog. These selections must be completely independent: no specialist may be assigned more than once, no machinery unit may be used multiple times, and no time window may host more than one operation.

Determine if such a deployment is possible, and if so, report one valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of required crews and the number of approved blueprints.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an approved blueprint consisting of specialist **x**, machinery unit **y**, and time window **z**. No blueprint is listed more than once.

## Output

If it is possible to select **k** independent blueprints, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of a selected blueprint. Any valid selection of **k** blueprints that do not share resources is accepted; the blueprints may be printed in any order.

If no such selection is possible, print `NO`.

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

In Example 2, both approved blueprints require machinery unit 1, so it is impossible to select 2 blueprints without reusing a machinery unit.
