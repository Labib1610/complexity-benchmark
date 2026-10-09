# Optimal Subnetwork Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

A distributed computing grid consists of **n** processing nodes and **m** bidirectional data links. Each data link has a specific activation cost.

A specialized computational task requires the collaboration of a specific subset of **t** nodes, designated as the "active set". To allow these nodes to coordinate, you must select a subset of the data links to activate. 

You must ensure that all **t** nodes of the active set are mutually reachable using only the chosen links (they may route data through intermediate nodes, which do not themselves need to be in the active set). Out of the $2^m$ possible link activation states, your objective is to find a valid configuration that minimizes the sum of the activation costs of the chosen links. 

The grid's physical topology consists of exactly **m** = **n** − 1 links, arranged such that there is exactly one valid sequence of links between any given pair of processing nodes. 

Determine the minimum total activation cost required to establish full communication among the active set.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the active set nodes.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a data link between node **u** and node **v** with an activation cost of **w**. The links follow the structural property described above.

## Output

Print a single integer: the minimum total activation cost required to connect all nodes in the active set.

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

In Example 1, the active set consists of nodes 1 and 4. The only way to connect them is to activate the links between 1 and 2, 2 and 3, and 3 and 4. The total cost is 5 + 1 + 2 = 8. In Example 2, there is only one node in the active set, so no links need to be activated and the required cost is 0.
