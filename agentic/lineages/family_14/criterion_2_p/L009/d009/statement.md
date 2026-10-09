# Subspace Span Optimization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working in an **N**-dimensional vector space over the real numbers. The space is parameterized by a standard basis $\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_N$.

You are given a catalog of **E** available shift vectors. Each shift vector has exactly two non-zero coordinates in the standard basis: a value of $1$ at coordinate **u** and a value of $-1$ at coordinate **v**. Purchasing this shift vector incurs a cost of **w**. (Multiplying a shift vector by $-1$ does not alter its generated linear span, so the assignment of $1$ and $-1$ to the two coordinates is interchangeable.)

It is guaranteed that the linear span of the entire catalog of **E** shift vectors has a dimension of exactly **N** - 1.

A specific subset of **F** coordinates are designated as *critical*. Your task is to select a subset of the available shift vectors to purchase such that, for any two critical coordinates $x$ and $y$, the vector $\mathbf{e}_x - \mathbf{e}_y$ is contained within the linear span of your purchased subset.

Determine the minimum total cost required to purchase a valid subset of shift vectors. (If **F** = 1, the empty set of vectors is sufficient, so the minimum total cost is 0.)

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the indices of the critical coordinates.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing an available shift vector with non-zero coordinates at **u** and **v**, and a purchase cost of **w**.

## Output

Print a single integer: the minimum total cost required to purchase a subset of shift vectors whose span satisfies the condition for all critical coordinates.

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