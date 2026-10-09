# Server Synchronization States

Time limit: 1 s
Memory limit: 256 MB

You are configuring a network of $n$ server nodes. Each node $i$ must be assigned an operational tier $x_i \in \{1, 2\}$.

The nodes are connected by a set of $m$ bidirectional sync channels. For a channel connecting node $u$ and node $v$, we construct a characteristic state matrix:
$$M_{u,v} = \begin{pmatrix} x_u & 1 \\ -1 & x_v \end{pmatrix}$$
The channel's resonance is defined as the determinant of this matrix $M_{u,v}$.

The network's overall resonance is defined as the product of the resonances of all $m$ channels. (If the network has no channels, the overall resonance is considered to be 1). To prevent data bottlenecks while maintaining hardware limits, the network is considered perfectly balanced if and only if its overall resonance is exactly $3^m$.

Your task is to determine a valid tier assignment for all $n$ nodes such that the network is perfectly balanced. If there are multiple valid ways, you must output the assignment that produces the lexicographically smallest sequence of operational tiers $x_1, x_2, \dots, x_n$. If it is impossible to satisfy the requirement, report that no such assignment exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a sync channel exists between node $u$ and node $v$.

## Output
If there is no valid tier assignment, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $x_1, x_2, \dots, x_n$, representing the lexicographically smallest valid sequence of operational tiers.

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