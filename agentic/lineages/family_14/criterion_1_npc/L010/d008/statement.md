# Problem A — Exhibition Mandates

Time limit: 5 s   Memory limit: 256 MB

## Description

An exhibition features **n** distinct blank canvases, numbered 1 to **n**. Each canvas is to be painted with a single solid color.

An art critic offers a collection of **m** optional equality mandates. Each mandate applies to a specific pair of canvases, **u** and **v**, and requires a legal fee of **w** to enact. If you pay the fee to enact a mandate, any legally compliant painting of the exhibition must assign the exact same color to canvas **u** and canvas **v**.

You are provided a list of **t** centerpiece canvases. Your objective is to enact a subset of mandates such that, in every legally compliant painting of the exhibition, all **t** centerpiece canvases are forced to be painted the exact same color as each other. You may enact mandates involving any of the **n** canvases to achieve this consequence.

Determine the absolute minimum total legal fee required to enact such a subset of mandates.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the identifiers of the centerpiece canvases.
The next **m** lines each provide three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that the equality mandate between canvas **u** and canvas **v** is available for a legal fee of **w**.
It is guaranteed that enacting all available mandates would force all centerpiece canvases to be painted the same color.

## Output

Output a single integer representing the minimum total legal fee required.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, enacting the equality mandates between canvas 4 and canvases 1, 2, and 3 costs 1 + 1 + 1 = 3. Under these three mandates, any legally compliant painting must assign canvases 1, 2, and 3 the same color (because they must all match canvas 4). This costs less than enacting the mandates directly among 1, 2, and 3 (which would cost 2 + 2 = 4).

In Example 3, with only one centerpiece canvas, no mandate is needed to ensure it matches itself, so the minimum fee is 0.