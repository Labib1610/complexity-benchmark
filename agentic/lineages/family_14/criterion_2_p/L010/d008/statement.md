# Subspace Basis Pricing

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working with vectors in an $n$-dimensional real vector space, where the coordinates are indexed from $1$ to $n$. Let $e_i$ denote the standard unit vector with a $1$ at position $i$ and $0$ elsewhere.

You are given a pool of $m$ available basis vectors. Each available vector is specified by two coordinate indices $u$ and $v$ and an associated price $w$, representing the vector $e_u - e_v$. The price to include this vector in your working set is $w$. 

You are mathematically guaranteed that if you were to include all $m$ available vectors, their linear span would contain all vectors of the form $e_i - e_j$ for any $1 \le i, j \le n$. The total number of available vectors $m$ is exactly $n - 1$.

A specific subset of $t$ coordinates are designated as target dimensions. 

You must select a subset of the available vectors to form a working set. Your working set must satisfy the following condition: for every pair of target dimensions $c_a$ and $c_b$, the difference vector $e_{c_a} - e_{c_b}$ must be in the linear span of your working set. 

Your objective is to determine the minimum possible total price of a working set that satisfies this requirement. (If there is only one target dimension, the requirement is vacuously satisfied by an empty working set, and the price is zero).

## Input

The first line provides three integers: $n$, $m$, and $t$. The vector space can have up to two hundred thousand dimensions ($1 \le n \le 200000$). The number of available vectors $m$ is always exactly $n - 1$. The number of target dimensions $t$ can range from one up to the entire space ($1 \le t \le n$).

The second line contains $t$ distinct integers representing the indices of the target dimensions.

Following this, there are $m$ lines, each detailing a single available vector with three integers: $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$). This represents the vector $e_u - e_v$ with price $w$. The price $w$ to include any single vector is at least one and does not exceed one million units ($1 \le w \le 1000000$).

## Output

Print a single integer: the minimum possible total price required to select a valid working set of vectors.

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

In Example 1, the target dimensions are 1 and 4. We must ensure $e_1 - e_4$ is in the linear span of our selected working set. By selecting the vectors $e_1 - e_2$ (price 5), $e_2 - e_3$ (price 1), and $e_3 - e_4$ (price 2), we can form the linear combination $e_1 - e_4 = (e_1 - e_2) + (e_2 - e_3) + (e_3 - e_4)$. The total price is 5 + 1 + 2 = 8. Because the available vectors are linearly independent, no cheaper subset spans this difference.

In Example 2, there is only one target dimension (dimension 3). Since there are no pairs of distinct target dimensions, the condition is vacuously satisfied by the empty set. The minimum possible total price is 0.