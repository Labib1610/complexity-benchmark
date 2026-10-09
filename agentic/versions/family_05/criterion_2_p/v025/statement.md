# Orbital Refit Program

Time limit: 2 s
Memory limit: 256 MB

## Description

An orbital station must refit exactly **k** starships. There are three categories of assets, each containing exactly **k** items:

- **k** starships, numbered 1 to k,
- **k** reactor modules, numbered 1 to k,
- **k** refit gantries, numbered 1 to k.

A complete refit operation requires pairing exactly one starship, one reactor module, and one refit gantry. You are provided with a catalog of **t** certified operational triplets `(s, r, g)`.

Due to prior integration phases, **each starship is already permanently paired with exactly one distinct reactor module**. Therefore, for any given starship, all certified triplets will feature the exact same reactor module, and no two starships will ever use the same reactor module.

To comply with safety regulations, the catalog guarantees the following structural conditions:
- The number of certified triplets containing any specific refit gantry is at most **k**.
- For every certified triplet `(s, r, g)`, the inequality **s + r + g ≤ 3k** holds.

Your task is to select exactly **k** certified triplets such that every starship, every reactor module, and every refit gantry is utilized in **exactly one** chosen triplet. Determine whether this is possible, and if so, report one valid set of triplets.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of items in each category and the number of certified triplets.
Each of the next **t** lines contains three integers **s**, **r**, **g** (1 ≤ s, r, g ≤ k), representing a certified triplet. No triplet is listed more than once. For each starship, every listed triplet uses the same reactor module, and different starships use different reactor modules.

## Output

If a valid selection of **k** triplets exists, print `YES` on the first line, then print **k** lines, each containing the three members `s r g` of one chosen triplet (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

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
