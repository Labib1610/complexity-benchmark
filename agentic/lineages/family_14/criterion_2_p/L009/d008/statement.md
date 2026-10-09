# Subspace Span Optimization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working in an **N**-dimensional vector space over the real numbers. The space has a standard basis consisting of **N** independent basis vectors, denoted as $\mathbf{b}_1, \mathbf{b}_2, \dots, \mathbf{b}_N$.

You are given a catalog of **E** available difference vectors. Each difference vector is defined by a pair of indices **u** and **v**, and takes the form $\mathbf{d} = \mathbf{b}_u - \mathbf{b}_v$. Purchasing this vector for your set incurs a cost of **w**. (Note that purchasing $\mathbf{b}_u - \mathbf{b}_v$ is equivalent to purchasing $\mathbf{b}_v - \mathbf{b}_u$, as their linear span is identical; the order of the indices does not matter).

It is guaranteed that if you were to purchase all **E** available difference vectors, their linear span would contain the difference $\mathbf{b}_x - \mathbf{b}_y$ for any $1 \le x, y \le N$.

A specific subset of **F** basis vectors are designated as *target* vectors. Your task is to select a subset of the available difference vectors to purchase such that the linear span of your purchased subset contains the vector $\mathbf{b}_x - \mathbf{b}_y$ for every pair of target vectors $\mathbf{b}_x$ and $\mathbf{b}_y$.

Determine the minimum total cost required to purchase a valid subset of difference vectors. (If **F** = 1, no vectors need to be purchased, so the minimum total cost is 0.)

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the indices of the target basis vectors.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing an available difference vector $\mathbf{b}_u - \mathbf{b}_v$ with a purchase cost of **w**.

## Output

Print a single integer: the minimum total cost required to purchase a subset of difference vectors whose span satisfies the condition for all target vectors.

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