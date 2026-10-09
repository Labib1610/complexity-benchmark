# Difference Vector Spanning

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working in an $n$-dimensional real vector space with the standard basis $e_1, e_2, \dots, e_n$. A specific subset of $t$ indices from $1$ to $n$ are designated as **Target Dimensions**.

You are provided with a collection of $m$ candidate difference vectors. Each candidate vector is defined by two distinct indices $u$ and $v$, and takes the form $d = e_u - e_v$. Including a candidate vector in your active set incurs a specific scalar cost.

The complete collection of $m$ available candidate vectors spans the entire $(n-1)$-dimensional subspace of vectors whose coordinates sum to zero. Furthermore, this collection contains exactly $m = n - 1$ vectors.

You must select a subset of these candidate vectors. Your selection must satisfy the following condition: for any pair of Target Dimensions $a$ and $b$, the difference vector $e_a - e_b$ must be expressible as a linear combination (with real coefficients) of your selected candidate vectors. (When $t=1$, this condition imposes no restrictions, as no pairs exist).

Your objective is to determine the minimum total cost required to select a valid subset of candidate vectors meeting this condition.

## Input

The first line contains three integers: $n$, $m$, and $t$.
- $n$ is the dimension of the vector space. There is at least 1 dimension and at most 200,000.
- $m$ is the number of available candidate vectors, which is exactly $n - 1$.
- $t$ is the number of Target Dimensions, which is at least 1 and at most $n$.

The second line contains $t$ distinct integers: the indices of the Target Dimensions (from 1 to $n$).

Each of the next $m$ lines details an available candidate vector with three integers: $u$, $v$, and $w$.
- $u$ and $v$ are the distinct indices (from 1 to $n$) defining the vector $e_u - e_v$.
- $w$ is the cost to include this vector. This cost is a positive integer not exceeding 1,000,000.

These $m$ lines form the exact structure described above, guaranteeing the full collection spans the zero-sum subspace.

## Output

Print a single integer: the minimum total cost required to ensure all required difference vectors between Target Dimensions are in the span of the selected subset.

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

In Example 1, the Target Dimensions are 1 and 4. The required difference vector $e_1 - e_4$ can only be expressed as a linear combination by including all three candidate vectors, since $(e_1 - e_2) + (e_2 - e_3) + (e_3 - e_4) = e_1 - e_4$. The minimum cost is therefore 5 + 1 + 2 = 8. 

In Example 2, there is only one Target Dimension. Since no pairs of Target Dimensions exist, no candidate vectors need to be included, resulting in a minimum cost of 0.