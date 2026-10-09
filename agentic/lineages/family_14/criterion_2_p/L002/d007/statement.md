# Null Space Target Component Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing an unknown vector $x \in \mathbb{R}^n$. The $i$-th component of $x$ is denoted as $x_i$.

There is a pool of $m$ available row vectors. Each available row vector $r$ is specified by two indices $u$ and $v$, representing a vector with $1$ at position $u$, $-1$ at position $v$, and $0$ everywhere else. Activating this row vector requires a cost of $w$. You are guaranteed that the $m \times n$ matrix formed by activating all $m$ available row vectors has a null space of exactly dimension 1, spanned by the vector of all ones.

You are given a target set of $t$ indices. You must select a subset of the available row vectors to form a matrix $B$. Your goal is to ensure that for every vector $x$ in the null space of $B$ (i.e., for every $x$ such that $Bx = \mathbf{0}$), the values of $x_i$ for all target indices $i$ are identical to each other. You may select row vectors involving non-target indices if they are necessary to satisfy this algebraic requirement.

Find the minimum total activation cost of a selected subset of row vectors that achieves this. The total cost is the sum of the activation costs $w$ of the row vectors you choose to include in $B$.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$). The available row vectors strictly satisfy the null space dimension guarantee described above.
The second line contains $t$ distinct integers: the target indices.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing an available row vector with $1$ at position $u$ and $-1$ at position $v$, which requires a cost of $w$ to activate.

## Output

Print a single integer: the minimum total cost of a subset of row vectors whose resulting matrix null space forces all target components to be equal.

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