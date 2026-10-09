# Freight Hub Upgrades

Time limit: 2 s   Memory limit: 256 MB

## Description

A regional railway network is composed of **N** stations and **E** track segments. It is possible to travel between any two stations using the available segments. 

The transport authority has selected **F** stations to serve as priority freight hubs. They need to reinforce a subset of the track segments to handle heavy industrial trains. The chosen subset of segments must allow cargo to be routed between any pair of freight hubs using only reinforced segments. Each track segment has a specific reinforcement cost. 

Calculate the minimum total cost to reinforce a valid subset of track segments.

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the identifiers of the freight hubs.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing a track segment between station **u** and station **v** with a reinforcement cost of **w**.

## Output

Print a single integer: the minimum total cost to reinforce track segments such that all freight hubs are connected to each other via reinforced tracks.

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