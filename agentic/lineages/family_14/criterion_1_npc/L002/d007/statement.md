# Problem A — Orthogonal Constraint

Time limit: 5 s
Memory limit: 256 MB

## Description
Let $\mathbb{R}^n$ be the standard $n$-dimensional Euclidean space. 
A specific subset of $t$ coordinates from $\{1, 2, \dots, n\}$ are designated as target coordinates. Let $L$ be the subspace of $\mathbb{R}^n$ consisting of all vectors whose components at the target coordinates are all equal to each other. That is, $L = \{ x \in \mathbb{R}^n \mid x_a = x_b \text{ for all target coordinates } a \text{ and } b \}$.

You are provided with a pool of $m$ candidate vectors. Each candidate vector is specified by a pair of distinct indices $(u, v)$ and has a value of $1$ at coordinate $u$, a value of $-1$ at coordinate $v$, and $0$ at all other coordinates. Activating a specific candidate vector incurs a one-time cost $w$.

Your objective is to activate a subset of the candidate vectors, forming a set $S$, such that the orthogonal complement of $S$ is a subspace of $L$. Recall that the orthogonal complement of $S$ is defined as $S^\perp = \{ x \in \mathbb{R}^n \mid x \cdot y = 0 \text{ for all } y \in S \}$.

Write a program to calculate the minimum total cost necessary to ensure this condition is met.

## Input
The first line contains three integers $n$, $m$, and $t$.
The dimension $n$ satisfies $1 \le n \le 100$. The number of candidate vectors $m$ satisfies $0 \le m \le n(n-1)/2$. The number of target coordinates $t$ satisfies $1 \le t \le 10$.

The second line contains $t$ distinct integers: the target coordinates.

Each of the next $m$ lines contains three integers $u$, $v$, and $w$, representing a candidate vector with $1$ at coordinate $u$ and $-1$ at coordinate $v$, which requires an activation cost of $w$. The integers $u$ and $v$ identify the two distinct coordinates involved ($1 \le u \le n$, $1 \le v \le n$, $u \neq v$). The cost $w$ satisfies $1 \le w \le 1000000$.

It is guaranteed that the available candidate vectors are sufficient to ensure the condition can be met.

## Output
Print a single integer: the minimum total cost to ensure the target condition is met.

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
In Example 1, the target coordinates are 1, 2, and 3. The subspace $L$ consists of all vectors $x \in \mathbb{R}^4$ such that $x_1 = x_2 = x_3$.
If we activate the candidate vectors for $(1, 4)$, $(2, 4)$, and $(3, 4)$, the set $S$ contains three vectors.
The orthogonal complement $S^\perp$ is the set of vectors $x$ satisfying $x_1 - x_4 = 0$, $x_2 - x_4 = 0$, and $x_3 - x_4 = 0$.
Any vector in $S^\perp$ must therefore have $x_1 = x_2 = x_3 = x_4$. Since this implies $x_1 = x_2 = x_3$, we have $S^\perp \subseteq L$.
The cost of this selection is $1+1+1=3$. This is more cost-effective than activating the candidate vectors defined solely on the target coordinates, which would cost at least 4.

In Example 3, with only one target coordinate, there are no pairs of distinct target coordinates to constrain. The subspace $L$ is exactly $\mathbb{R}^3$. The condition $S^\perp \subseteq L$ is vacuously satisfied even if $S$ is empty (where $S^\perp = \mathbb{R}^3$). Thus, no candidate vectors need to be activated, resulting in a minimum cost of 0.