# Problem B — Exact Budget Selection (Small Prices)

Time limit: 2 s   Memory limit: 256 MB

## Description

A procurement officer reviews **n** line items, each with a positive price, and must hit a target **T** exactly. A plan selects a group of items (each at most once; empty group totals zero) whose prices sum to exactly T. In this catalogue the prices and the target are all modest, bounded well within a small range, so the set of reachable running totals stays compact and can be tracked directly. Decide whether some group sums exactly to T, and if so report one; otherwise report that no exact-total group exists.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 1000).
The second line contains **n** integers, the item costs, each between 1 and 100.
The third line contains a single integer **T** (0 ≤ T ≤ 500).

## Output

If some group of items has total cost exactly T, print `YES` on the first line, then on the second line print the 1-based indices of the chosen items separated by single spaces (in any order). If the chosen group is empty, leave the second line blank.

If no such group exists, print `NO`.

Any group whose costs sum to exactly T is accepted.

## Examples

### Example 1

**Input**
```
5
1 3 5 7 9
12
```

**Output**
```
YES
2 5
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
4
1 2 3 4
0
```

**Output**
```
YES

```

## Note

In Example 1, items 2 and 5 cost 3 and 9, which sum to 12. In Example 3, the empty group has total cost 0, matching the target.
