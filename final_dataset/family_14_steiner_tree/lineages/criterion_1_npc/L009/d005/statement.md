# Problem A — Basis Alignment Procurement

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a vector space with a fixed standard basis $x_1, x_2, \ldots, x_n$. Within this space, a specific set of $t$ basis vectors are designated as objective targets.

You are tasked with procuring a collection of difference vectors to form a subspace. You can select from a provided catalog of available difference vectors. Each catalog entry allows you to add the vector $x_u - x_v$ to your collection for a specified procurement expense. Selecting $x_u - x_v$ also makes $x_v - x_u$ available via scalar multiplication by $-1$, so each input pair behaves as an undirected option.

Your goal is to select a subset of the available difference vectors such that for any two objective targets $x_a$ and $x_b$, their difference $x_a - x_b$ is contained within the linear span of your selected collection.

Calculate the minimum total expense required to procure a set of difference vectors that satisfies this spanning condition for all objective targets.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ t ≤ 10). The integer **t** is the number of objective targets.
The second line provides **t** distinct integers representing the indices of these objective targets.
The subsequent **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing a catalog entry that provides the vector $x_u - x_v$ for a procurement expense of **w**.
It is guaranteed that the available options are sufficient to satisfy the condition for all objective targets.

## Output

Print a single integer: the minimum total expense to satisfy the condition for all objective targets.

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

In Example 1, procuring the vectors $x_1 - x_4$, $x_2 - x_4$, and $x_3 - x_4$ (costing 1+1+1 = 3) is more economical than spanning the differences among the three objective targets using vectors that do not involve $x_4$ (which would cost 4). In Example 3, there is only a single objective target, so the condition is already satisfied with an empty subset, so the cost is 0.