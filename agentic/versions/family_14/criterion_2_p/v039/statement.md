# Problem B — Activating the Required Facilities

Time limit: 2 s   Memory limit: 256 MB

## Description

A regional hospital network manages **n** medical facilities (numbered 1..n). Certain pairs of facilities can be linked by a dedicated fiber-optic line at a given activation cost. Among the facilities, **t** operate as **critical data centers** and must all end up connected to each other through the lines you activate (directly or through intermediate relay facilities).

Due to the region's strict non-redundant conduit architecture, the available fiber-optic lines connect all facilities such that there are exactly **n − 1** possible lines, and between any two facilities there is exactly one possible route of lines.

Activate a set of fiber-optic lines of minimum total cost so that all critical data centers are connected. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the critical data centers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a fiber-optic line joining facilities u and v at activation cost w. The lines follow the architecture described above.

## Output

Print a single integer: the minimum total cost to connect all critical data centers.

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

In Example 1 the critical data centers 1 and 4 are joined only through 2 and 3, so all three lines (5+1+2 = 8) are needed. In Example 2 there is one critical data center, so no lines are needed.
