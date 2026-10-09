# Problem A — Preventing Phase Collisions in Quantum Circuits

Time limit: 5 s   Memory limit: 256 MB

## Description
A quantum computing matrix consists of $n$ nodes and $m$ bidirectional entanglement channels between pairs of nodes. Severing a channel requires a specific amount of energy. 

Among the $n$ nodes, $k$ are designated as primary anchors. Each anchor is initialized with a mutually incompatible quantum state. If any two primary anchors remain capable of interacting—meaning there is a sequence of unsevered channels connecting them—their states will collapse, destroying the matrix. Nodes that are not primary anchors hold neutral states; their final placement does not matter as long as they do not act as a bridge between different primary anchors.

To stabilize the matrix, you must sever a set of channels such that no two primary anchors can interact. The total energy expended to sever the channels must not exceed the available energy budget $B$. 

Determine if it is possible to achieve this stabilization within the energy budget. If so, provide a valid set of channels to sever. If there are multiple valid sets within the budget, any of them will be accepted.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$.
The second line contains $k$ distinct integers, representing the identifiers of the primary anchors.
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating an entanglement channel between node $u$ and node $v$ that requires $w$ units of energy to sever.

## Output
If stabilization is possible within the budget, output `YES` on the first line. On the second line, output the number of severed channels $c$. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a severed channel. 
If it is impossible to stabilize the matrix within the budget, output `NO`.

## Example 1

**Input:**
```text
5 6 3 15
1 3 5
1 2 4
2 3 5
3 4 3
4 5 4
1 5 6
2 4 8
```

**Output:**
```text
YES
3
1 2
4 5
1 5
```

## Example 2

**Input:**
```text
5 6 3 10
1 3 5
1 2 4
2 3 5
3 4 3
4 5 4
1 5 6
2 4 8
```

**Output:**
```text
NO
```
