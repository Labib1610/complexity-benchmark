# Problem C — Unconnectable Site

Time limit: 1 s   Memory limit: 256 MB

## Description

A campus has **n** sites (numbered 1..n). Certain pairs of sites can be joined by a cabling option at a given cost. Among the sites, **t** are **required** and must all end up connected to each other through the cabling you install.

In the input you are given, at least one required site has **no cabling option at all touching it**. Such a site cannot be connected to anything, so the required sites can never all be connected.

Report the smallest id among the required sites that have no cabling option touching them.

## Input

The first line contains three integers **n**, **m**, and **t** (2 ≤ n ≤ 200000, 0 ≤ m ≤ 200000, 1 ≤ t ≤ n).
The second line contains **t** distinct integers: the ids of the required sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a cabling option joining sites u and v at cost w.
It is guaranteed that at least one required site has no cabling option touching it.

## Output

Print a single integer: the smallest id among the required sites with no cabling option touching them.

## Examples

### Example 1

**Input**
```
3 1 2
1 3
1 2 4
```

**Output**
```
3
```

### Example 2

**Input**
```
4 2 2
2 4
1 2 3
1 3 3
```

**Output**
```
4
```

## Note

In Example 1, required site 3 appears in no cabling option, so it can never be connected.
