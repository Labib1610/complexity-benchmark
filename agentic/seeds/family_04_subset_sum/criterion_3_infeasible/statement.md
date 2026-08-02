# Problem C — Exact Budget Selection (Negative Target)

Time limit: 1 s   Memory limit: 256 MB

## Description

A store offers **n** items for purchase. Item **i** has a positive cost. You are given a target budget **T** and must decide whether some group of items can be bought so that their costs add up to **exactly** T.

Each item may be chosen at most once. The group is allowed to be empty (an empty group has total cost 0).

Determine whether such a group exists, and if so report one.

## Input

The first line contains a single integer **n** (1 ≤ n ≤ 1000).
The second line contains **n** integers, the item costs, each between 1 and 1 000 000 000.
The third line contains a single integer **T** (−1 000 000 000 ≤ T ≤ −1).

## Output

If some group of items has total cost exactly T, print `YES` on the first line, then on the second line print the 1-based indices of the chosen items separated by single spaces (in any order).

If no such group exists, print `NO`.

## Examples

### Example 1

**Input**
```
3
5 10 15
-4
```

**Output**
```
NO
```

### Example 2

**Input**
```
4
1 2 3 4
-100
```

**Output**
```
NO
```

## Note

Every item cost is positive, so any group's total is at least 0.
