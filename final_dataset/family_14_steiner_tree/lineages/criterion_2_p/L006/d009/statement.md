# Problem B — Subspace Projection Optimization

Time limit: 2 s
Memory limit: 256 MB

## Description

You are working in an $n$-dimensional Euclidean space $\mathbb{R}^n$ with the standard orthonormal basis $e_1, e_2, \dots, e_n$. 
You are given a target subset $T$ consisting of $t$ distinct basis indices.

You have a catalog of $m$ available coordinate transformations. Transformation $i$ is a swap operator $S_{u_i, v_i}$ that exchanges the $u_i$-th and $v_i$-th coordinates of any vector in $\mathbb{R}^n$ and leaves all other coordinates unchanged. Activating this transformation requires an energy cost of $w_i$.

When you select a subset $C$ of these transformations, you define a subspace $V_C$ consisting of all vectors that are strictly invariant under every transformation in $C$. That is:
$V_C = \{ x \in \mathbb{R}^n \mid S_{u,v}(x) = x \text{ for all } S_{u,v} \in C \}$

Let $\pi_C : \mathbb{R}^n \to V_C$ denote the orthogonal projection onto the invariant subspace $V_C$. 
Your goal is to select a subset of transformations $C$ such that for any two indices $a, b \in T$, their corresponding basis vectors have the exact same projection onto $V_C$. In other words, you must ensure that $\pi_C(e_a) = \pi_C(e_b)$ for all $a, b \in T$.

You are given that $m = n - 1$. Furthermore, it is mathematically guaranteed that if you were to select all $m$ available transformations, the resulting subspace $V_C$ would be exactly 1-dimensional (specifically, the line spanned by the all-ones vector).

Determine the minimum total energy (the sum of $w_i$ for the transformations in $C$) required to select a valid subset $C$ that satisfies the projection requirement for all indices in $T$.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1). The basis coordinates are indexed from 1 to **n**.
The second line lists **t** distinct integers representing the indices of the target subset $T$.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate an available swap transformation between coordinates $u$ and $v$ that can be activated at an energy cost of **w**.

## Output

Output a single integer representing the minimum possible total energy to select a subset of transformations that satisfies the projection requirement for $T$.

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