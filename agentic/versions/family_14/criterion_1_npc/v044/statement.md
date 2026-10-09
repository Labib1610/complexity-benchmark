# Problem A — Core Infrastructure

Time limit: 5 s   Memory limit: 256 MB

## Description

A regional grid contains **n** stations. A specific subset of **t** stations are designated as *core* stations, while the rest are *auxiliary* stations. You are provided with a list of potential bidirectional links that can be activated between pairs of stations, each with a specific activation cost.

In many network designs, one might simply activate the shortest paths between all pairs of core stations. However, because paths can share links, the true minimum cost often involves finding optimal intersection points (auxiliary stations) where multiple routes can merge. Given that **t** is at most 10, the number of such intersections is strictly bounded, meaning the final activated network will structurally be a small union of paths. 

Your objective is to select a subset of links to activate such that a signal can travel from any core station to any other core station, using only the activated links. Auxiliary stations are not required to be connected unless they are functioning as cost-effective relays.

Determine the absolute minimum total cost of links that must be activated to achieve full connectivity among all core stations.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the core stations (stations are numbered from 1 to n).
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a link can be activated between station **u** and station **v** for a cost of **w**.
It is guaranteed that the available links are sufficient to connect all core stations.

## Output

Print a single integer: the minimum total activation cost to interconnect all core stations.

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

In Example 1, routing the connections through the auxiliary station 4 (costing 1+1+1 = 3) is cheaper than linking the three core stations directly (which would cost 4). In Example 3, there is only one core station, so no links need to be activated.
