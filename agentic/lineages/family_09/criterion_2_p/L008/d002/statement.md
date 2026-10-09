# Problem B — Isolated Subsystems

Time limit: 2 s   Memory limit: 256 MB

## Description

A communications network consists of **n** nodes (numbered 1 to **n**) and **m** bidirectional cables. Each cable directly joins two nodes.

The network's architecture guarantees a structural property: it is possible to configure each cable with a one-way signal direction such that every node in the network acts either exclusively as a transmitter (all its connected cables send signals away from it) or exclusively as a receiver (all its connected cables bring signals toward it). Note that these signal directions are theoretical and are not provided in the input.

A subset of nodes is considered **completely isolated** if no two nodes in the subset are joined by a cable.

Given a target size **k**, determine whether a completely isolated subset of exactly **k** nodes can be chosen, and if so, output one such subset.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a cable between node **u** and node **v**. No cable is listed more than once, and the network is guaranteed to satisfy the transmitter/receiver property described above.

## Output

If a completely isolated subset of exactly **k** nodes exists, print `YES` on the first line. On the second line, print **k** distinct node numbers that form such a subset, separated by spaces. If multiple such subsets exist, any valid one will be accepted.

If no such subset can be formed, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

## Note

In Example 1, nodes 1 and 2 are not joined by any cable, so they form a completely isolated subset of size 2. In Example 3, the largest possible completely isolated subset contains only 2 nodes, making a target of 3 impossible.