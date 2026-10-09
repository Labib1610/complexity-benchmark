# Freight Hub Upgrades

Time limit: 2 s   Memory limit: 256 MB

## Description

A regional railway network consists of **n** stations. The track layout guarantees that every station can be reached from any other, and there is exactly one sequence of direct track segments connecting any pair of stations. 

The transport authority has designated **t** of these stations as freight hubs. To support heavy cargo, the authority must upgrade a selection of track segments. The upgrades must ensure that every freight hub can route trains to every other freight hub using exclusively upgraded track segments. Each track segment has an associated upgrade cost. 

Determine the minimum total cost required to upgrade the necessary track segments.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the freight hubs.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a direct track segment between station **u** and station **v** with an upgrade cost of **w**.

## Output

Print a single integer: the minimum total cost to upgrade track segments such that all freight hubs are connected to each other via upgraded tracks.

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
