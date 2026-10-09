# Problem A — Linking the Mandatory Facilities

Time limit: 5 s   Memory limit: 256 MB

## Description

A complex has **n** facilities (numbered 1..n). Certain pairs of facilities can be joined by a pipeline segment at a given expense. Among the facilities, **t** are **mandatory** and must all end up linked to each other through the segments you establish (directly or through intermediate facilities). The remaining facilities are optional intermediaries: you may pass pipelines through them if it helps, or ignore them.

Establish a set of pipeline segments of minimum total expense so that all mandatory facilities are linked. Report that minimum total expense.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the mandatory facilities.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a pipeline segment joining facilities u and v at expense w.
The available pipeline segments are enough to link all mandatory facilities.

## Output

Print a single integer: the minimum total expense to link all mandatory facilities.

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

In Example 1, passing pipelines through the optional intermediary facility 4 (expenses 1+1+1 = 3) is cheaper than joining the three mandatory facilities directly (which would cost 4). In Example 3 there is only one mandatory facility, so no pipeline is needed.
