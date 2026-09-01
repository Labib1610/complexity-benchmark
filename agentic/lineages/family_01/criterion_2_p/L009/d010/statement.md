# Problem B — Network Channels

Time limit: 1 s
Memory limit: 256 MB

You are configuring a network of $n$ communication nodes. Each node $i$ must be assigned a channel capacity $c_i$ belonging to the set $\{1, 2\}$.

The network contains $m$ interference links. Each link connects exactly two specific nodes. 
To maintain a balanced network, we define a stability condition for each link. For a link connecting node $u$ and node $v$, imagine constructing a rectangular grid containing $c_u$ rows and $c_v$ columns of square cells.
The configuration is considered stable if and only if, for every interference link in the network, the total number of distinct contiguous rectangular subgrids (of any valid dimensions, from $1 \times 1$ up to $c_u \times c_v$, where two subgrids are distinct if they occupy a different set of cells in the grid) is exactly 3.

You must assign a channel capacity to each of the $n$ nodes so that this stability requirement is met for all links. If no such assignment is possible, you must report it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two nodes connected by a single interference link.

## Output
If no valid capacity assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $c_1, \dots, c_n$ (each $c_i \in \{1, 2\}$), where $c_i$ is the capacity assigned to node $i$. If there are multiple valid assignments, output the one that is lexicographically smallest. An assignment sequence $A$ is lexicographically smaller than $B$ if, at the first index $i$ where they differ, $A_i < B_i$.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```