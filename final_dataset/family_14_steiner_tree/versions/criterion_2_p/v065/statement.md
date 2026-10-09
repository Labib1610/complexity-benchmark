# Data Synchronization Pipelines

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud computing environment consists of **n** server clusters. Certain pairs of clusters are connected by bidirectional data pipelines. Activating a pipeline for synchronization incurs a specific latency cost.

The pipeline architecture is designed such that there is exactly one non-repeating sequence of pipelines between any two server clusters. Furthermore, the architecture guarantees the following properties for every valid environment:
- The total number of available pipelines is strictly less than the number of server clusters.
- The sum of activation costs for all pipelines in the entire environment does not exceed $2 \times 10^{11}$.
- Activating any possible subset of pipelines will never create a closed loop.

A specific group of **t** server clusters has been designated to host a distributed database. You must select a subset of pipelines to activate so that all **t** database clusters can synchronize with each other. Two database clusters can synchronize if there is a sequence of activated pipelines connecting them, possibly routing through other clusters (which may or may not be database clusters themselves).

Find the absolute minimum total latency cost of the activated pipelines that ensures full connectivity among all **t** database clusters.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1), representing the number of clusters, the number of pipelines, and the number of database clusters respectively.

The second line contains **t** distinct integers: the identifiers of the clusters designated as database clusters (clusters are numbered 1 to n).

Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a pipeline between cluster **u** and cluster **v** with an activation cost of **w**. 

## Output

Print a single integer: the minimum total activation cost to connect all database clusters.

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

In Example 1, the database clusters at 1 and 4 can only synchronize by routing through clusters 2 and 3. Thus, all three pipelines must be activated, yielding a cost of 5 + 1 + 2 = 8. In Example 2, there is only one database cluster, so no pipelines need to be activated, resulting in a cost of 0.
