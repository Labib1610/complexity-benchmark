# Subspace Basis Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working with a vector space constructed from $n$ orthogonal basis vectors $\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n$.

You are provided with a generator pool of $m = n - 1$ distinct transition vectors. Each transition vector is defined by a pair of indices $u$ and $v$ ($u \neq v$), representing the vector $\mathbf{e}_u - \mathbf{e}_v$, and has a specific activation cost $w$.

It is guaranteed that the full pool of available transition vectors spans the entire $(n-1)$-dimensional subspace defined by the equation $\sum_{i=1}^n x_i = 0$.

A researcher has specified a target subset of $t$ indices, denoted as $T$. Your objective is to select a subset of the available transition vectors such that their linear span contains the vector $\mathbf{e}_a - \mathbf{e}_b$ for every pair of distinct indices $a, b \in T$. Note that the linear span of your selected vectors may also contain transition vectors involving indices outside of $T$, which is permissible and often necessary to establish the required vectors.

Determine the minimum total activation cost of a subset of transition vectors that must be selected to satisfy the researcher's requirement. Any transition vector not strictly needed to span the required target vectors can be omitted.

## Input

The first line provides three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line provides $t$ distinct integers, representing the indices in the target subset $T$.
The next $m$ lines each contain three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), indicating an available transition vector $\mathbf{e}_u - \mathbf{e}_v$ with an activation cost of $w$.

## Output

Output a single integer: the minimum total activation cost of the selected subset of transition vectors.

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