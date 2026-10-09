# Subspace Spanning Cost

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working in the vector space $\mathbb{R}^n$, with the standard basis vectors denoted as $e_1, e_2, \dots, e_n$. 
You are given a target set of **t** indices, called the *focus indices*. You need to ensure that you can generate the difference vector $e_a - e_b$ for every pair of focus indices **a** and **b**.

You have a catalog of **m** available basis operations. Each operation is defined by a pair of indices (**u**, **v**) and provides the vector $e_u - e_v$. Acquiring this vector into your chosen subset incurs a cost of **w**. 

Your goal is to choose a subset of these **m** available vectors such that every required difference vector $e_a - e_b$ (for all focus indices **a**, **b**) lies within the linear span of your chosen subset. 

You must find the minimum possible total cost (the sum of the costs of the chosen vectors) to achieve this.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **n** ≤ 200000, **m** = **n** - 1, 1 ≤ **t** ≤ **n**).

The second line provides **t** distinct integers representing the focus indices.

The subsequent **m** lines each contain three integers **u**, **v**, and **w**. These values describe an available vector $e_u - e_v$ (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**) that incurs a cost of **w** (1 ≤ **w** ≤ 1000000). It is guaranteed that the linear span of all **m** available vectors contains the vector $e_x - e_y$ for all $1 \le x, y \le n$.

## Output

Print a single integer indicating the minimum total cost required to ensure the difference vectors between all pairs of focus indices are within the linear span of the chosen subset.

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

In Example 1, the focus indices are 1 and 4. We require the vector $e_1 - e_4$ to be in the linear span of our chosen subset. The only way to form $e_1 - e_4$ is by taking the sum of the vectors $e_1 - e_2$, $e_2 - e_3$, and $e_3 - e_4$. Thus, all three vectors (costing 5 + 1 + 2 = 8) must be chosen. 

In Example 2, there is only one focus index, so no difference vectors need to be spanned. The minimum cost is 0.