# Problem B — Vector Span Optimization

Time limit: 2 s
Memory limit: 256 MB

## Description

You are working in an $n$-dimensional Euclidean space $\mathbb{R}^n$ with the standard orthonormal basis $e_1, e_2, \dots, e_n$. 
You are given a target subset $T$ consisting of $t$ distinct basis indices.

You have a catalog of $m$ available difference vectors. Vector $i$ is defined as $d_i = e_{u_i} - e_{v_i}$. Activating this vector requires an energy cost of $w_i$.

Your goal is to select a subset $C$ of these available vectors such that for any two indices $a, b \in T$, the difference between their corresponding basis vectors, $e_a - e_b$, lies entirely within the linear span of the selected subset $C$. In other words, $e_a - e_b$ must be expressible as a linear combination of the vectors in $C$ for all $a, b \in T$.

You are given that $m = n - 1$. Furthermore, it is mathematically guaranteed that if you were to select all $m$ available vectors, their linear span would have a dimension of exactly $n - 1$.

Determine the minimum total energy (the sum of $w_i$ for the vectors in $C$) required to select a valid subset $C$ that satisfies the spanning requirement for all indices in $T$.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1). The basis coordinates are indexed from 1 to **n**.
The second line lists **t** distinct integers representing the indices of the target subset $T$.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate an available vector $d = e_u - e_v$ that can be activated at an energy cost of **w**.

## Output

Output a single integer representing the minimum possible total energy to select a subset of vectors that satisfies the spanning requirement for $T$.

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