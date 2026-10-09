# Problem A — Cabling the Required Sites

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a cabling option at a given cost. Among the sites, **t** are **required** and must all end up connected to each other through the cabling you install (directly or through intermediate sites). The remaining sites are optional relays: you may route cabling through them if it helps, or ignore them.

Install a set of cabling options of minimum total cost so that all required sites are connected. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t**. The number of sites **n** is a positive integer, bounded by the one hundred available land plots. The required sites **t** number at least one, but no more than the ten priority departments. The cabling options **m** count from zero up to the total possible connections between distinct sites.
The second line contains **t** distinct integers: the ids of the required sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w**: a cabling option joining distinct valid sites **u** and **v** at cost **w**. The cost is at least one, bounded by a one million dollar grant.
The cabling options are enough to connect all required sites.

## Output

Print a single integer: the minimum total cost to connect all required sites.

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

In Example 1, routing cabling through the optional relay site 4 (costs 1+1+1 = 3) is cheaper than joining the three required sites directly (which would cost 4). In Example 3 there is only one required site, so no cabling is needed.
