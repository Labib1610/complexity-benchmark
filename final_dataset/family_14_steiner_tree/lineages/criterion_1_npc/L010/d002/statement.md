# Problem A — Cabling the Priority Locations

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus infrastructure project involves **n** sites, numbered 1 through **n**. You have a catalog of potential cabling segments that can be laid between specific pairs of sites, each with a known installation expense. The project mandate requires that a specific subset of **t** sites, designated as priority locations, must be able to exchange data with one another.

You must select which cabling segments to install to establish this data exchange capability. Data can traverse any sequence of installed segments, meaning non-priority sites can freely act as transit points. Determine the absolute minimum total installation expense required to satisfy the mandate.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers identifying the priority locations.
The next **m** lines each provide three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), showing that a cabling segment can be laid between site **u** and site **v** for an expense of **w**.
It is guaranteed that it is possible to satisfy the mandate using the provided options.

## Output

Output a single integer representing the minimum total expense to ensure all priority locations can exchange data.

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

In Example 1, using site 4 as a transit point (which costs 1+1+1 = 3) is more cost-effective than linking the three priority locations directly (which would cost 4). In Example 3, there is only one priority location, so no segments need to be installed.