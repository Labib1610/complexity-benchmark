# Transformation Network

Time limit: 1 s
Memory limit: 256 MB

A network consists of $n$ nodes. Each node must be assigned exactly one of two vector transformations:
- Transformation 1: $f(V) = M \cdot V + B_1$
- Transformation 2: $f(V) = M \cdot V + B_2$

where $V = \begin{pmatrix} x \\ y \end{pmatrix}$ is a 2D vector, $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $B_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$, and $B_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$.

There are $m$ links in the network. Each link connects two specific nodes $u$ and $v$. A link is considered stable if and only if the composition of the transformations assigned to its two endpoints (applied in either order) has no fixed points. That is, evaluating $f_u(f_v(V))$ must not produce $V$ for any vector $V$. If there exists even one vector $V$ such that $f_u(f_v(V)) = V$, the link is unstable and the entire configuration is invalid.

Your task is to determine whether there is an assignment of transformations (either 1 or 2) to all $n$ nodes such that every link in the network is stable. If multiple valid assignments exist, you must output the one that minimizes the sequence of assigned transformation numbers $s_1, s_2, \dots, s_n$ lexicographically.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a link connects node $u$ and node $v$.

## Output
If no stable assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \ldots, s_n$ (each being 1 or 2) representing the lexicographically smallest valid assignment.

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