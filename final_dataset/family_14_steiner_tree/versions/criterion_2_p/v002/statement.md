# Problem B — Activating the Critical Workstations (Non-Redundant Layout)

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility has **n** workstations (numbered 1..n). Certain pairs of workstations can be joined by a data link at a given activation cost. Among the workstations, **t** are **critical** and must all end up connected to each other through the links you activate (directly or through intermediate relay workstations).

In this facility the available data links are strictly non-redundant: they connect all workstations, there are exactly **n − 1** options, and between any two workstations there is exactly one possible routing sequence.

Activate a set of data links of minimum total cost so that all critical workstations are connected. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the critical workstations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a data link joining workstations u and v at cost w. The options form the non-redundant structure described above.

## Output

Print a single integer: the minimum total activation cost to connect all critical workstations.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1 the critical workstations 1 and 4 are joined only through 2 and 3, so all three links (5+1+2 = 8) are needed. In Example 2 there is one critical workstation, so no links are needed.
