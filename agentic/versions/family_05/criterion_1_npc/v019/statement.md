# Problem A — Architectural Harmony

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing an installation using a set of available decorative blocks. Every block is defined by three attributes: its shape, its color, and its material. Each attribute is represented by an integer from 1 to **k**.

You are given a catalog of **t** specific blocks that are currently in stock. No two blocks in the catalog have the exact same combination of shape, color, and material.

You must choose a subset of exactly **k** blocks from the catalog to form a "perfect collection". A collection is considered perfect if it satisfies all of the following conditions:
- Every shape from 1 to **k** is represented exactly once among the chosen blocks.
- Every color from 1 to **k** is represented exactly once among the chosen blocks.
- Every material from 1 to **k** is represented exactly once among the chosen blocks.

Determine whether it is possible to select a perfect collection from the stock, and if so, report one valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of distinct values for each attribute, and the number of blocks in stock. 
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a block in stock with shape **x**, color **y**, and material **z**. No block type is listed more than once.

## Output

If a perfect collection of **k** blocks exists, print `YES` on the first line, then print **k** lines, each containing the three attributes `x y z` of one chosen block. Any selection meeting the conditions is accepted; the blocks may be printed in any order.

If no perfect collection exists, print `NO`.

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

In Example 2, both available blocks have color 1, so color 2 can never be included in the collection.
