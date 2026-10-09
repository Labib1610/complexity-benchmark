# Priority Site Connectivity

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a link at a given cost. Among the sites, **t** are **priority** and must all end up connected to each other through the links you establish (directly or through intermediate sites).

In this campus the available link options form a specific layout: they connect all sites, there are exactly **n − 1** options, and between any two sites there is exactly one possible route without revisiting any site.

Establish a set of links of minimum total cost so that all priority sites are connected. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the priority sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a link joining sites u and v at cost w. The options form the layout described above.

## Output

Print a single integer: the minimum total cost to connect all priority sites.

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

In Example 1 the priority sites 1 and 4 are joined only through 2 and 3, so all three links (5+1+2 = 8) are needed. In Example 2 there is one priority site, so no links are needed.
