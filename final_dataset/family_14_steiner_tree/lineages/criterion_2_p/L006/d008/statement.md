# Problem B — Simplicial Homology Optimization

Time limit: 2 s
Memory limit: 256 MB

## Description

You are designing a 1-dimensional simplicial complex $X$. 
The complex has $n$ 0-simplices (vertices), labeled 1 through $n$. 
You are given a critical subset $T$ consisting of $t$ distinct 0-simplices.

You have a catalog of $m$ available 1-simplices. Each 1-simplex connects 0-simplices $u$ and $v$, and requires a structural stabilization energy $w$.

Your goal is to select a subset of these 1-simplices, $C$, to form the complex $X$. The 0-simplices of $X$ are always the full set of $n$ vertices, while the 1-simplices of $X$ are exactly your chosen subset $C$.

Let $H_0(X; \mathbb{R})$ be the 0-th simplicial homology group of $X$ with real coefficients. 
The natural inclusion map $\iota: T \hookrightarrow X$ (where $T$ is viewed as a discrete subspace of $t$ points) induces a linear transformation on the homology groups, $\iota_*: H_0(T; \mathbb{R}) \to H_0(X; \mathbb{R})$.

You must select the subset $C$ such that the image of the induced map $\iota_*$ has a vector space rank of exactly 1.

You are given that $m = n - 1$. Furthermore, it is mathematically guaranteed that if you were to select all $m$ available 1-simplices, the resulting complex would have $\dim H_0(X; \mathbb{R}) = 1$ (meaning its 0-th Betti number $\beta_0$ is 1).

Determine the minimum total stabilization energy (the sum of $w$ for the 1-simplices in $C$) required to select a valid subset $C$ that satisfies the homological rank requirement for $T$.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1). The 0-simplices are indexed from 1 to **n**.
The second line lists **t** distinct integers representing the indices of the critical subset $T$.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate an available 1-simplex between $u$ and $v$ that can be stabilized at an energy cost of **w**.

## Output

Output a single integer representing the minimum possible total energy to select a subset of 1-simplices that satisfies the required homological property for $T$.

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