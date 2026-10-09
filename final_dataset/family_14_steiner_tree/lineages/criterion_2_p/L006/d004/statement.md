# Problem B — Subspace Acquisition

Time limit: 2 s
Memory limit: 256 MB

## Description

You are working in the vector space $\mathbb{R}^n$ with the standard basis vectors $e_1, e_2, \dots, e_n$.

You are provided with a catalog of **m** available vectors. Each available vector is defined by a pair of indices $(u, v)$ and takes the form $e_u - e_v$. 

The catalog of **m** vectors forms a basis for the subspace of all vectors in $\mathbb{R}^n$ whose coordinates sum to zero. This means that if you acquire all **m** vectors, their linear span will contain every vector $e_i - e_j$ for $1 \le i, j \le n$, but omitting even one vector from the catalog would strictly reduce the dimension of the space they span.

Your objective focuses on a designated priority set of **t** indices. You must purchase a subset of the available vectors such that for every pair of indices $i$ and $j$ in the priority set, the vector $e_i - e_j$ is contained within the linear span of your purchased subset. You may purchase vectors involving non-priority indices if they are useful for constructing the required vectors through linear combinations.

Each vector in the catalog has a specific purchase cost. Determine the minimum total cost required to acquire a valid subset of vectors that satisfies the spanning condition for all pairs in the priority set.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line lists **t** distinct integers representing the indices in the priority set.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate an available vector $e_u - e_v$ that can be purchased at a cost of **w**. It is guaranteed that the given **m** vectors satisfy the basis property described above.

## Output

Output a single integer representing the minimum possible total cost to purchase a subset of vectors whose span contains $e_i - e_j$ for all priority indices $i$ and $j$.

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