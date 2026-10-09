# Problem B — Cabling the Required Sites

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a cabling option at a given cost. The network of available cabling options connects all sites, there are exactly **n − 1** options in total, and between any two sites there is exactly one possible sequence of options that connects them.

Among all the sites, **t** are designated as **required**.

Your task is to install a set of cabling options of minimum total cost so that all required sites end up connected to each other (either directly or through intermediate relay sites). Report that minimum total cost.

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

In Example 1 the required sites 1 and 4 are joined only through 2 and 3, so all three options (5+1+2 = 8) are needed. In Example 2 there is one required site, so no cabling is needed.
