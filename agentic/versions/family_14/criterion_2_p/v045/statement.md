# Distribution Network Optimization

Time limit: 2 s   Memory limit: 256 MB

## Description

A logistics corporation oversees a network of depots. Specific pairs of these depots are joined by transport corridors, each carrying a distinct yearly upkeep cost. A designated group of these depots act as primary distribution centers. The corporation plans to fund the upkeep of a chosen set of corridors to guarantee that cargo can be routed between any two primary distribution centers, either directly or by passing through other depots, using strictly the funded corridors. The objective is to find the lowest possible total yearly upkeep cost for this chosen set.

The existing corridor network provides a route between any two depots in the system. However, the infrastructure is entirely devoid of redundancy: the closure of even a single corridor would permanently sever the connection between at least one pair of depots. 

## Input

The first line contains three integers: the total number of depots, the number of transport corridors, and the number of primary distribution centers. The logistics database allocates memory for up to two hundred thousand depots. The corridor count is structurally dictated by the exact minimum number of connections required to link all depots into a single network. The number of distribution centers can be as small as one, or as large as the entire set of depots.

The second line contains distinct integers: the identifiers of the primary distribution centers.

Each of the remaining lines contains three integers describing a transport corridor: the two distinct depot identifiers it connects, and its yearly upkeep cost. Depot identifiers are positive integers that do not exceed the total depot count. The upkeep cost is a positive integer, and a government regulation caps it at exactly one million per corridor.

## Output

Print a single integer: the minimum total upkeep cost required to ensure every primary distribution center can reach every other primary distribution center using only the funded corridors. (If the network has only one primary distribution center, no corridors require funding, resulting in a cost of zero.)

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
