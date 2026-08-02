# Problem A — Exact Budget Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

A store offers **n** items for purchase. Item **i** has a positive cost. You are given a target budget **T** and must decide whether some group of items can be bought so that their costs add up to **exactly** T.

Each item may be chosen at most once. The group is allowed to be empty (an empty group has total cost 0).

Determine whether such a group exists, and if so report one.

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
