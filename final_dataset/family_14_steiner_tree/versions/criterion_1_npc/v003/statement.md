# Problem A — Cabling the Required Sites

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a cabling option at a given cost. Among the sites, **t** are **required** and must all end up integrated. The required sites are considered integrated if a message can be passed between any two of them by hopping between pairs of sites that have an installed cabling option joining them. The remaining sites are optional relays: you may install options joining them if it helps route messages, or ignore them.

Install a set of cabling options of minimum total cost so that all required sites are integrated. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the required sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a cabling option joining sites u and v at cost w.
The provided cabling options are sufficient to integrate all required sites.

## Output

Print a single integer: the minimum total cost to integrate all required sites.

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

In Example 1, routing messages through the optional relay site 4 (costs 1+1+1 = 3) is cheaper than joining the three required sites directly (which would cost 4). In Example 3 there is only one required site, so no cabling is needed.
