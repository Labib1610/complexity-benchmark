# Problem A — Subspace Spanning

Time limit: 5 s
Memory limit: 256 MB

## Description
Consider an $n$-dimensional vector space with a standard basis $e_1, e_2, \dots, e_n$.
You are offered $m$ difference vectors, each of the form $e_u - e_v$ for some basis vectors $e_u$ and $e_v$. Acquiring a specific difference vector incurs a one-time cost. 

A specific subset of $t$ indices have been designated as target indices. Your objective is to select a set of difference vectors to acquire such that for any two target indices $a$ and $b$, the vector $e_a - e_b$ lies within the linear span of the acquired set. You are permitted to acquire difference vectors that involve non-target indices; if utilizing them as intermediate basis components reduces the overall cost, it is a valid strategy.

Write a program to calculate the minimum total cost necessary to ensure all required vectors $e_a - e_b$ are in the span of the acquired set.

## Input
The first line contains three integers $n$, $m$, and $t$.
The number of dimensions $n$ satisfies $1 \le n \le 100$. The number of available vectors $m$ satisfies $0 \le m \le n(n-1)/2$. The number of target indices $t$ satisfies $1 \le t \le 10$.

The second line contains $t$ distinct integers: the target indices.

Each of the next $m$ lines contains three integers $u$, $v$, and $w$, representing an available difference vector $e_u - e_v$ that requires a cost of $w$. The integers $u$ and $v$ identify the two distinct dimensions involved ($1 \le u \le n$, $1 \le v \le n$, $u \neq v$). The cost $w$ satisfies $1 \le w \le 1000000$.

It is guaranteed that the available vectors are sufficient to ensure the target condition can be met.

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
In Example 1, acquiring the vectors $e_1 - e_4$, $e_2 - e_4$, and $e_3 - e_4$ (which requires a cost of 1+1+1 = 3) allows $e_1 - e_2$, $e_2 - e_3$, and $e_1 - e_3$ to be formed via linear combinations. This is more cost-effective than acquiring vectors that only involve the three target indices directly (which would require a cost of 4). 
In Example 3, with only one target index, there are no target pairs that require acquiring any vector, so the minimum cost is 0.