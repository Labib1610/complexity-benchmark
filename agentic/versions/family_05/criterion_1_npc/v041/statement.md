# Problem A — Banquet Planning

Time limit: 5 s   Memory limit: 256 MB

## Description

A banquet requires the preparation of **k** full dining sequences. You have a pantry stocked with **k** distinct starters (identified by numbers 1 through **k**), **k** distinct centerpieces (1 through **k**), and **k** distinct finales (1 through **k**).

The head chef has provided a catalog of approved culinary trios. Each trio specifies a starter, a centerpiece, and a finale that harmonize perfectly.

Your task is to select exactly **k** trios from the catalog to form the dining sequences. A selection is valid only if no two chosen trios share a starter, no two share a centerpiece, and no two share a finale.

Determine whether a valid selection can be made, and if so, report one such selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of dining sequences required and the number of approved trios in the catalog.
Each of the next **t** lines contains three integers **s**, **c**, and **f** (1 ≤ s, c, f ≤ k), describing an approved trio consisting of starter **s**, centerpiece **c**, and finale **f**. No trio is listed more than once in the catalog.

## Output

If a valid selection of **k** trios exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers **s** **c** **f** of one chosen trio. The chosen trios may be printed in any order.

If no valid selection exists, print `NO`.

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

In Example 2, both approved trios require centerpiece 1. Thus, any selection of two trios from the catalog would unavoidably share a centerpiece, making a valid selection impossible.
