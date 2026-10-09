# Subspace Projection Penalty

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a high-dimensional linear system over **n** continuous variables, $x_1, x_2, \dots, x_n$. Initially, the variables are unconstrained, meaning the solution space is the full vector space $\mathbb{R}^n$.

To restrict this space, you can apply a predefined set of **m** available hyperplane constraints. The $i$-th available constraint, if selected, enforces the equation $x_u = x_v$. Applying this constraint to the system incurs a fixed structural penalty of $w$. 

When multiple constraints are applied, the solution space of the system becomes the intersection of the selected hyperplanes. 

You are given a list of **t** target axes (indices of specific variables). Your goal is to apply a subset of the available constraints such that, in the resulting solution space, the projection onto the **t** target axes has a dimension of exactly 1. 

(For clarity, the projection of the solution space onto the **t** target axes is the set of all vectors $(x_{c_1}, x_{c_2}, \dots, x_{c_t}) \in \mathbb{R}^t$ that can be extended to a valid solution $(x_1, \dots, x_n) \in \mathbb{R}^n$ satisfying all applied constraints.)

Determine the minimum total structural penalty incurred by selecting a subset of constraints that achieves this dimensional requirement.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the indices of the target axes.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available constraint $x_u = x_v$ and its structural penalty $w$.
The provided set of constraints is sufficient to reduce the projection dimension to 1.

## Output

Print a single integer: the minimum total structural penalty to achieve a projection dimension of exactly 1 on the target axes.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, applying the constraints involving variable 4 ($x_1=x_4$, $x_2=x_4$, and $x_3=x_4$ at a penalty of 1+1+1 = 3) restricts the solution space such that any valid solution must have $x_1 = x_2 = x_3 = x_4$. The projection of this solution space onto the target axes (1, 2, and 3) consists only of vectors where all three coordinates are equal ($x_1 = x_2 = x_3$). This forms a 1-dimensional subspace in $\mathbb{R}^3$. This incurs a lower penalty than applying the constraints directly between the target axes.

In Example 3, there is only one target axis. The projection of any non-empty solution space onto a single axis has a dimension of at most 1. Since the unconstrained solution space already projects to a 1-dimensional space on axis 1, no constraints need to be applied, and the minimum penalty is 0.