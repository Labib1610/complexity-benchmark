# Problem B — Cabling Every Site

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a cabling option at a given cost. **Every** site must end up connected to every other site through the cabling you install (directly or through intermediate sites).

Install a set of cabling options of minimum total cost so that all sites are connected. Report that minimum total cost.

## Input

The first line contains two integers **n** and **m** (1 ≤ n ≤ 200000, 0 ≤ m ≤ 200000).
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a cabling option joining sites u and v at cost w.
The cabling options are enough to connect all sites.

## Output

Print a single integer: the minimum total cost to connect all sites.

## Examples

### Example 1

**Input**
```
3 3
1 2 1
2 3 2
1 3 3
```

**Output**
```
3
```

### Example 2

**Input**
```
4 3
1 2 1
2 3 1
3 4 1
```

**Output**
```
3
```

### Example 3

**Input**
```
3 3
1 2 2
2 3 2
1 3 2
```

**Output**
```
4
```

## Note

In Example 1, using the two cheapest options (costs 1 and 2) already connects all three sites, for a total of 3.
