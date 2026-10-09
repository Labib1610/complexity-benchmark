# Problem A — Production Run

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing plant is scheduled to deliver a production run of **k** integrated systems. The inventory provides the necessary parts, separated into chassis, power units, and logic units. There are exactly **k** distinct parts of each type, and the parts within each type are identified by serial numbers from 1 to **k**.

To build a single integrated system, the plant must combine one chassis, one power unit, and one logic unit. However, due to manufacturing tolerances, only specific groupings of parts will successfully integrate. You are provided with a catalog of verified groupings.

Your objective is to authorize a subset of exactly **k** groupings from the catalog such that every single chassis, power unit, and logic unit in the inventory is assigned to exactly one of the authorized systems.

Determine if the plant can complete the entire production run under these conditions, and if so, report one valid assignment.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of available parts of each type, and the number of verified groupings in the catalog.
Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), indicating that chassis **x**, power unit **y**, and logic unit **z** can be successfully integrated. No grouping appears more than once in the catalog.

## Output

If the production run can be completed, print `YES` on the first line. Following this, print **k** lines, each containing the three integers `x y z` representing the parts used for one authorized system. Any valid assignment that leaves no part unused is acceptable; the systems may be printed in any order.

If it is impossible to use all parts to build **k** systems, print `NO`.

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

In Example 2, both verified groupings require power unit 1, so power unit 2 can never be utilized.
