# Problem A — Integrating the Primary Nodes

Time limit: 5 s   Memory limit: 256 MB

## Description

A distributed computing cluster consists of a set of processing nodes. A specific subset of these nodes are designated as *primary* and must be fully integrated. Integration means that all primary nodes can exchange information with one another, either across a direct data channel or routed through a sequence of intermediate nodes.

You can deploy data channels between specific pairs of nodes, each requiring a certain deployment cost. You are allowed to deploy channels involving non-primary nodes if using them as routing intermediaries results in a lower overall expense. Non-primary nodes that are not helpful can be left disconnected.

Determine the absolute minimum total deployment cost required to ensure every primary node is integrated into a single communicating group.

## Input

The first line provides three integers: **n**, **m**, and **t**. The cluster is housed in a single rack with exactly 100 server bays, meaning the total number of processing nodes **n** is a positive integer that cannot exceed the number of bays. The number of potential data channels **m** can be as low as zero or as high as the theoretical limit where every pair of distinct nodes has exactly one potential channel between them. A dedicated hardware token is required for each primary node. The system possesses exactly 10 tokens, so the number of primary nodes **t** is a positive integer bounded by the token count.

The second line contains **t** distinct integers representing the identifiers of the primary nodes.

The following **m** lines each contain three integers **u**, **v**, and **w**, detailing a potential data channel that can link node **u** and node **v** at a deployment cost of **w**. Nodes are numbered sequentially starting from 1 up to **n**. It is guaranteed that **u** and **v** are distinct. The financial budget caps the cost **w** of any single channel at exactly one million, and every such cost is a positive integer. 

The given channels are always sufficient to successfully integrate all primary nodes.

## Output

Print a single integer: the minimum total deployment cost to integrate all primary nodes.

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

In Example 1, deploying channels through the non-primary node 4 (costs 1+1+1 = 3) is cheaper than linking the three primary nodes directly (which would cost 4). In Example 3 there is only one primary node, so no channels need to be deployed.
