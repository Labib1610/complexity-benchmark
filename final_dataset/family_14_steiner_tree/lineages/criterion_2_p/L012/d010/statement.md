# Subspace Nullity Enforcement

Time limit: 2 s   Memory limit: 256 MB

## Description

You are optimizing a linear transformation represented by an $n \times n$ symmetric matrix $M$. Initially, $M$ is a zero matrix.

You are given a sequence of $m$ available update operations. Each operation is defined by a pair of indices $(u, v)$ and an associated cost $w$. If you choose to apply this operation, you incur the cost $w$ and update the matrix $M$ as follows:
- $M_{u, u}$ increases by 1
- $M_{v, v}$ increases by 1
- $M_{u, v}$ decreases by 1
- $M_{v, u}$ decreases by 1

You are also given a set of $t$ required indices. Your objective is to choose a subset of the $m$ operations to apply such that the resulting matrix $M$ enforces a specific property on its null space. Specifically, for any vector $x = (x_1, x_2, \dots, x_n)^T \in \mathbb{R}^n$ that satisfies the equation $M x = 0$, it must be guaranteed that all components of $x$ corresponding to the required indices are equal. That is, if $p_1, p_2, \dots, p_t$ are the required indices, then $x_{p_1} = x_{p_2} = \dots = x_{p_t}$ for all $x$ in the null space of $M$.

When $t=1$, the minimum total cost is 0.

It is guaranteed that $m = n - 1$. Furthermore, if you were to apply all $m$ available operations, the null space of the resulting matrix $M$ would consist exactly of the vectors where all $n$ components are equal.

Find the minimum total cost of a subset of operations that achieves the objective.

## Input

The first line contains three integers: $n$, $m$, and $t$.
- $n$ is the dimension of the matrix. There is at least 1 and at most 200,000.
- $m$ is the number of available operations, which is exactly $n - 1$.
- $t$ is the number of required indices, which is at least 1 and at most $n$.

The second line contains $t$ distinct integers: the required indices (from 1 to $n$).

Each of the next $m$ lines details an available operation with three integers: $u$, $v$, and $w$.
- $u$ and $v$ are the distinct matrix indices (from 1 to $n$) updated by the operation.
- $w$ is the cost to apply this operation. This cost is a positive integer not exceeding 1,000,000.

## Output

Print a single integer: the minimum total cost to apply a subset of operations satisfying the null space condition for the required indices.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the required indices are 1 and 4. To ensure that any vector $x$ satisfying $Mx = 0$ has $x_1 = x_4$, all three operations must be applied. The total cost is 5 + 1 + 2 = 8.

In Example 2, there is only one required index. With one required index, no operation is required, so the minimum cost is 0.