# Problem A — Database Compliance Routing

Time limit: 5 s   Memory limit: 256 MB

## Description

A banking network operates **n** independent transaction databases (numbered 1 to **n**). To comply with international regulations, a specific subset of **t** databases must be fully synchronized.

Two databases can be synchronized by deploying a continuous replication link between them. Deploying a link between a specific pair of databases requires purchasing a dedicated hardware bridge for a one-time cost.

Synchronization is transitive: if database A is linked to database B, and B is linked to C, then A and C are also synchronized.

You need to purchase a set of hardware bridges such that all **t** regulated databases are synchronized with each other. You may choose to link non-regulated databases if routing the synchronization through them results in a lower total hardware cost.

Find the minimum total cost of hardware bridges required to achieve full synchronization among the regulated databases.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the regulated databases.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a feasible replication link between database **u** and database **v** that costs **w** to deploy.
The available links are guaranteed to be sufficient to satisfy the compliance requirement.

## Output

Print a single integer: the minimum total cost to purchase a set of hardware bridges satisfying the compliance requirement.

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

In Example 1, linking regulated databases 1, 2, and 3 with the non-regulated database 4 (costs 1+1+1 = 3) is cheaper than deploying links to synchronize the three regulated databases directly with each other (which would incur a cost of 4). In Example 3, there is only one regulated database, so no links need to be deployed.
