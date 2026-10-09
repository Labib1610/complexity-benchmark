# Cabling the Required Sites (Infrastructure Upgrade)

Time limit: 2 s   Memory limit: 256 MB

## Description

The campus infrastructure upgrade is a three-stage process. In the first stage, surveyors mapped out the campus of **n** sites (numbered 1..n) and identified feasible cabling options between certain pairs of sites at a given cost. They verified that the available cabling options connect all sites and contain no redundant loops: there are exactly **n − 1** options, meaning between any two sites there is exactly one possible cabling route.

You are responsible for the second stage. Among the sites, **t** are **required** and must all end up connected to each other through the cabling you install (directly or through intermediate relay sites). Your task is to select a set of cabling options of minimum total cost so that all required sites are connected.

In the third stage, the procurement department will use the minimum total cost you report to order the necessary materials before installation begins. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the required sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a cabling option joining sites u and v at cost w. The options form the structure described above.

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

In Example 1 the required sites 1 and 4 are joined only through 2 and 3, so all three edges (5+1+2 = 8) are needed. In Example 2 there is one required site, so no cabling is needed.
