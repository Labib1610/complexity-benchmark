# Matrix Null Space Optimization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are constructing an **N** $\times$ **N** real symmetric matrix $M$, which is initially the zero matrix.

You are given a catalog of **E** available update operations. Each update is defined by two distinct indices **u** and **v**. Purchasing this update adds a specific rank-1 matrix $U$ to $M$. The matrix $U$ has elements $U_{u,u} = 1$, $U_{v,v} = 1$, $U_{u,v} = -1$, and $U_{v,u} = -1$, with all other entries being $0$. Purchasing this update incurs a cost of **w**.

It is guaranteed that if you purchase the entire catalog of **E** updates, the resulting matrix $M$ will have exactly one eigenvalue equal to $0$, and its corresponding eigenspace (the null space) will be spanned by the all-ones vector $(1, 1, \dots, 1)^T$.

A specific subset of **F** indices are designated as *target* indices. Your task is to select a subset of the available updates to purchase such that, in the resulting matrix $M$, every vector $\mathbf{x} = (x_1, x_2, \dots, x_N)^T$ in the null space of $M$ satisfies the condition $x_a = x_b$ for all target indices $a$ and $b$.

Determine the minimum total cost required to purchase a valid subset of updates. (If **F** = 1, purchasing no updates is sufficient, as the condition holds vacuously, meaning the minimum total cost is 0.)

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the target indices.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing an available update defined by indices **u** and **v**, and a purchase cost of **w**.

## Output

Print a single integer: the minimum total cost required to purchase a subset of updates whose resulting matrix satisfies the condition for all target indices.

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