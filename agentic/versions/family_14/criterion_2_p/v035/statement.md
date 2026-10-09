# Optimal Subset Selection for Required Site Connectivity

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a cabling option at a given cost. Among the sites, **t** are **required** and must all end up connected to each other through the cabling you install (directly or through intermediate relay sites).

You must choose a subset of the **m** available cabling options to install. With 2^m possible subsets to consider, your goal is to identify a valid subset that connects all **t** required sites while minimizing the sum of the costs of the chosen options. The **m** available cabling options connect all sites such that there are exactly **n − 1** options, and between any two sites there is exactly one possible cabling route.

Report the minimum total cost of such a subset.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the required sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a cabling option joining sites u and v at cost w.

## Output

Print a single integer: the minimum total cost to connect all required sites.

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

In Example 1, the required sites 1 and 4 are joined only through 2 and 3, so all three options (5+1+2 = 8) must be included in the chosen subset. In Example 2, there is one required site, so an empty subset of options is sufficient.
