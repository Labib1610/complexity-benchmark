# Problem A — Subspace Basis Procurement

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing an $n$-dimensional vector space over the finite field GF(2). Let $b_1, b_2, \ldots, b_n$ denote the standard basis vectors of this space. Within this domain, a specific set of $t$ indices are designated as priority coordinates.

You are tasked with procuring a subset of vectors from a provided catalog. Each catalog entry allows you to add a specific vector of the form $b_u + b_v$ to your chosen subset for a specified procurement expense. Note that since the field is GF(2), addition is commutative and $b_u + b_v$ is identical to $b_v + b_u$.

Your goal is to select a subset of the available catalog entries. Let $S$ be the set of vectors you have procured, and let $V$ be the subspace spanned by $S$ over GF(2). You must ensure that for every pair of priority coordinates $x$ and $y$, the vector $b_x + b_y$ is contained in the subspace $V$. You may freely utilize vectors involving non-priority coordinates to help span the required vectors; they act as valid intermediate components in linear combinations.

Calculate the minimum total expense required to procure a subset of catalog entries that satisfies this condition.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ t ≤ 10). The integer **t** is the number of priority coordinates.
The second line provides **t** distinct integers representing the identities of these priority coordinates.
The subsequent **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing a catalog entry that provides the vector $b_u + b_v$ for a procurement expense of **w**.
It is guaranteed that the available catalog options are sufficient to construct a subspace containing $b_x + b_y$ for all pairs of priority coordinates $x$ and $y$.

## Output

Print a single integer: the minimum total expense to satisfy the condition for all priority coordinates.

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

In Example 1, procuring the vectors $b_1 + b_4$, $b_2 + b_4$, and $b_3 + b_4$ incurs a total expense of 1+1+1 = 3. The subspace spanned by these three vectors over GF(2) contains $b_1 + b_2$ (since $(b_1 + b_4) + (b_2 + b_4) = b_1 + b_2$), $b_2 + b_3$, and $b_1 + b_3$. Consequently, the condition is fulfilled for the priority coordinates 1, 2, and 3. This is more economical than selecting a subset of vectors that do not involve coordinate 4 (which would cost at least 4).

In Example 3, there is only a single priority coordinate. The condition that for every pair of priority coordinates $x$ and $y$, $b_x + b_y$ belongs to the subspace is vacuously satisfied by an empty subset of vectors, resulting in a cost of 0.