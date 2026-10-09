# Problem B — Interference-Free Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

A wireless network consists of **n** nodes (numbered 1 to **n**) and **m** known interference links. Each link indicates that two specific nodes will interfere if both are activated.

Due to a hardware restriction, every node is configured to use one of two available radio channels. You are not given these configurations, but it is guaranteed that interference links only ever exist between nodes configured to different channels. Nodes on the same channel never have an interference link between them.

A set of nodes is **interference-free** if no two nodes in the set share an interference link.

Given a target size **k**, determine whether an interference-free set of exactly **k** nodes exists. If such a set exists, you must also provide one valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing an interference link between node **u** and node **v**. No link is listed more than once. The links are guaranteed to follow the two-channel structure described above (every link is between nodes on different channels).

## Output

If an interference-free set of **k** nodes exists, print `YES` on the first line. On the second line, print **k** distinct node numbers forming such a set, separated by spaces. If there are multiple valid sets, any of them will be accepted.

If no such set exists, print `NO`.

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
