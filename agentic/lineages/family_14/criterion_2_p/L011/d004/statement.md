# Problem B — Active Zone Connectivity

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a communication network for **n** sites, labeled 1 to **n**. You are given a list of **m** potential undirected cabling options. Each option connects two sites and has a specific construction cost.

The **m = n - 1** options form a fully connected network over sites 1 to **n**: all sites are connected and there is exactly one path between any two sites.

A subset of **t** sites are designated as **required sites**. Your objective is to choose cabling options of minimum total cost so that all required sites are connected (possibly through non-required sites).

To formally define your selection, you must designate a subset of sites to act as the **active zone**. This active zone must satisfy the following conditions:
1. It must include all **t** required sites.
2. The chosen cabling options will be EXACTLY those options that have BOTH of their endpoints within the active zone.
3. These chosen options must successfully connect all sites in the active zone into a single connected component.

The total cost of your network is the sum of the construction costs of the chosen options. Determine the minimum total cost required to form a valid active zone that connects all required sites.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the labels of the required sites.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating an undirected cabling option between site **u** and site **v** with a cost of **w**.

## Output

Output a single integer representing the minimum total cost of the chosen options.

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