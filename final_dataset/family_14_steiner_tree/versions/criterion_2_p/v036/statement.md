# Fiber-Optic Upgrades for Research Centers

Time limit: 2 s   Memory limit: 256 MB

## Description

A university campus consists of **n** facilities. Specific pairs of facilities are linked by existing underground conduits. Installing fiber-optic cable in a conduit incurs a known labor and material cost.

The campus conduit network was built with minimal redundancy: between any two facilities, there is exactly one route of conduits connecting them. 

The administration has designated **t** specific facilities as high-priority research centers. The IT department must select a subset of conduits to wire with fiber-optics such that every research center can communicate with every other research center, either directly or by passing through intermediate wired facilities. 

Determine the absolute minimum total installation cost required to achieve this connectivity among all the research centers.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1), representing the number of facilities, the number of conduits, and the number of research centers respectively.

The second line contains **t** distinct integers: the identifiers of the facilities designated as research centers (facilities are numbered 1 to n).

Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating an underground conduit between facility u and facility v with an installation cost of w. 

## Output

Print a single integer: the minimum total installation cost to connect all research centers.

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

In Example 1, the research centers at facilities 1 and 4 can only communicate by routing through facilities 2 and 3, meaning all three conduits must be wired (costing 5 + 1 + 2 = 8). In Example 2, there is only one research center, so no communication network needs to be installed, resulting in a cost of 0.
