# Operator Network

Time limit: 1 s
Memory limit: 256 MB

A network consists of $n$ nodes. Each node must be assigned exactly one of two linear operators on $\mathbb{R}^2$:
- Operator 1: $T_1(\mathbf{x}) = A \mathbf{x}$, where $A = \begin{pmatrix} 1 & 4 \\ 2 & 5 \end{pmatrix}$
- Operator 2: $T_2(\mathbf{x}) = B \mathbf{x}$, where $B = \begin{pmatrix} 5 & -4 \\ -2 & 1 \end{pmatrix}$

There are $m$ links in the network. Each link connects two specific nodes $u$ and $v$. A link is considered stable if and only if the composed operator $T_{u,v} = T_u \circ T_v$ (applied in either order, as they commute) is self-adjoint with respect to the standard inner product.

Specifically, the combined operator $T_{u,v}$ must satisfy the following equation for all vectors $\mathbf{x}, \mathbf{y} \in \mathbb{R}^2$:

$$ \mathbf{y}^\mathsf{T} T_{u,v}(\mathbf{x}) = T_{u,v}(\mathbf{y})^\mathsf{T} \mathbf{x} $$

where $^\mathsf{T}$ denotes the vector transpose.

If there exists even one pair of vectors $\mathbf{x}, \mathbf{y}$ where this equality fails, the link is unstable and the entire configuration is invalid.

Your task is to determine whether there is an assignment of operators (either 1 or 2) to all $n$ nodes such that every link in the network is stable. If multiple valid assignments exist, you must output the one that minimizes the sequence of assigned operator numbers $s_1, s_2, \dots, s_n$ lexicographically.

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