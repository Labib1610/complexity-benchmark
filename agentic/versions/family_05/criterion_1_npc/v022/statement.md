# Problem A — Data Cube Orthogonality

Time limit: 5 s   Memory limit: 256 MB

## Description

A data warehouse operates on a 3-dimensional coordinate grid with dimensions $X$, $Y$, and $Z$. The grid is perfectly symmetric, with each dimension indexed uniformly from 1 to $k$. 

You are provided with a list of $t$ active data nodes. Each active node is located at a specific coordinate $(x, y, z)$. 

To achieve balanced synchronization, the system requires you to activate exactly $k$ nodes from the provided list. Because the architecture is perfectly symmetric, an activation state is only valid if its projection onto each of the three coordinate axes is complete and uniform. In other words, across your $k$ chosen nodes, each $X$-coordinate from 1 to $k$ must be assigned exactly once, each $Y$-coordinate exactly once, and each $Z$-coordinate exactly once.

Since the system is uniformly bounded ($k$ nodes to cover $k$ indices in each of the 3 dimensions), your task is simply to find one such mutually orthogonal set of nodes if it exists, ensuring the data cube remains completely balanced.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 22$, $0 \le t \le k \cdot k \cdot k$): the dimension size and the number of active data nodes.
Each of the next $t$ lines contains three integers $x$, $y$, $z$ ($1 \le x, y, z \le k$), representing the coordinates of an active node. No coordinate triplet is listed more than once.

## Output

If a valid orthogonal synchronization of $k$ nodes exists, print `YES` on the first line. Then, print $k$ lines, each containing the three coordinates `x y z` of one chosen node. Any valid synchronization meeting the coordinate constraints is accepted; the nodes may be printed in any order.

If no valid synchronization exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both active nodes share the same $Y$-coordinate (1). Therefore, the $Y$-coordinate 2 can never be covered, making orthogonal synchronization impossible.
