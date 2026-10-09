# Problem A — Secure Data Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

An enterprise operates a network consisting of **n** distinct server nodes, labeled uniquely from 1 to **n**. Within this network, there are **m** potential bidirectional communication links that can be established. Each potential link connects a specific pair of nodes and requires a known activation expense to be provisioned.

Among the **n** nodes, a specific subset of **t** nodes has been designated as critical. The remaining nodes are standard nodes. Any node, whether critical or standard, is capable of forwarding information between any activated links connected to it.

The enterprise must ensure that information can flow between all critical nodes. This means that every critical node must be able to exchange data with every other critical node via some sequence of activated links. You must select a subset of the potential links to activate such that this connectivity condition for the critical nodes is met, while keeping the sum of the activation expenses as low as possible. Determine this minimum total expense.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the critical nodes.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a potential link between nodes **u** and **v** with an activation expense of **w**.
It is guaranteed that the available potential links are sufficient to interconnect all critical nodes.

## Output

Print a single integer: the minimum total activation expense required to interconnect all critical nodes.

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

In Example 1, activating links through the standard node 4 (expense 1+1+1 = 3) is cheaper than directly linking the three critical nodes (which would cost 2+2 = 4). In Example 3, there is only one critical node, so no links need to be activated.
