# Problem B — Cabling the Required Sites (Single-Path Network)

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a cabling option at a given cost. Among the sites, **t** are **required** and must all end up connected to each other through the cabling you install (directly or through intermediate relay sites).

In this campus the available cabling options form a single-path network: they connect all sites, there are exactly **n − 1** options, and between any two sites there is exactly one possible cabling route.

Install a set of cabling options of minimum total cost so that all required sites are connected. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t**. The total number of sites **n** is at least one and tops out at the campus maximum capacity of 200000. The number of required sites **t** is anywhere from a single site up to the entire campus, and the number of available cabling options **m** is exactly one fewer than the number of sites.
The second line contains **t** distinct integers: the ids of the required sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. This represents a cabling option joining distinct sites **u** and **v** (both valid site ids from 1 up to **n**) at cost **w**. The cost is at least 1 and at most the campus department budget limit of 1000000. The options form the layout described above.

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

This is the same minimum-cabling problem as Problem A. The only difference is that the cabling options form a single-path network, which makes an efficient exact solution possible. In Example 1 the required sites 1 and 4 are joined only through 2 and 3, so all three options (5+1+2 = 8) are needed. In Example 2 there is one required site, so no cabling is needed.
