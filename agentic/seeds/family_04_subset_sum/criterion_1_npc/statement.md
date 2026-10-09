# Problem A — Exact Budget Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A procurement officer reviews **n** line items, each with a positive price, and must hit an audited target **T** to the exact unit — not over, not under. A purchase plan selects a group of items (each at most once; the empty group totals zero) whose prices sum to **exactly** T. Discounts, delivery, and categories are irrelevant; only the prices and the exact target matter. The prices here span a very wide range, so the reachable totals do not fill the interval densely and there is no modular shortcut. Decide whether some group of items sums exactly to T, and if so report one such group; otherwise report that no exact-total group exists.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 40).
The second line contains **n** integers, the item costs, each between 1 and 1 000 000 000.
The third line contains a single integer **T** (0 ≤ T ≤ 40 000 000 000).

## Output

If some group of items has total cost exactly T, print `YES` on the first line, then on the second line print the 1-based indices of the chosen items separated by single spaces (in any order). If the chosen group is empty, leave the second line blank.

If no such group exists, print `NO`.

Any group whose costs sum to exactly T is accepted.

## Examples

### Example 1

**Input**
```
5
3 34 4 12 5
9
```

**Output**
```
YES
3 5
```

### Example 2

**Input**
```
3
2 4 6
5
```

**Output**
```
NO
```

### Example 3

**Input**
```
1
7
7
```

**Output**
```
YES
1
```

## Note

In Example 1, items 3 and 5 cost 4 and 5, which sum to 9.
