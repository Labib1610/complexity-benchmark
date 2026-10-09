# Basis Span Optimization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing an **n**-dimensional vector space with a standard basis $v_1, v_2, \dots, v_n$.

There is a proposed set of **m** difference vectors. Each proposed vector is defined by a pair of basis elements **u** and **v**, representing the vector $v_u - v_v$, and has an associated computational cost **w** to include in your working set. You are guaranteed that **m** = **n** − 1, and that the full set of **m** proposed vectors spans the entire (**n**−1)-dimensional subspace of vectors whose coordinates sum to zero.

You are given a set of **t** target indices. You must select a subset of the proposed difference vectors such that, for any pair of target indices **a** and **b**, the vector $v_a - v_b$ is contained within the linear span (over the real numbers) of your selected subset. You may include proposed vectors that do not directly involve the target indices if they help satisfy this requirement.

Find the minimum total cost of a selected subset of difference vectors that satisfies this requirement. The total cost of a subset is the sum of the computational costs **w** of the vectors it contains.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1). The proposed vectors strictly satisfy the spanning guarantee described above.
The second line contains **t** distinct integers: the target indices.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a proposed vector $v_u - v_v$ that requires a cost of **w** to include.

## Output

Print a single integer: the minimum total cost of a subset of vectors whose span contains $v_a - v_b$ for all target indices **a** and **b**.

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