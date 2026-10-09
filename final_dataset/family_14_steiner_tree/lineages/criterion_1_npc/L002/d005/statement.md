# Problem A — Functional Kernels

Time limit: 5 s
Memory limit: 256 MB

## Description
Consider the vector space $\mathbb{R}^n$ consisting of vectors $x = (x_1, x_2, \dots, x_n)$.
You are provided with a pool of $m$ linear functionals. Each functional is defined by a pair of indices $(u, v)$ and maps any vector $x$ to $x_u - x_v$. Activating a specific functional incurs a one-time cost $w$.

A specific subset of $t$ indices have been designated as critical indices. Your objective is to activate a subset of the functionals such that their joint kernel (the intersection of the kernels of all activated functionals) is a subspace of the kernel of the functional $x \mapsto x_a - x_b$ for every pair of critical indices $a$ and $b$. 

Write a program to calculate the minimum total cost necessary to ensure this kernel subspace condition is met.

## Input
The first line contains three integers $n$, $m$, and $t$.
The dimension $n$ satisfies $1 \le n \le 100$. The number of available functionals $m$ satisfies $0 \le m \le n(n-1)/2$. The number of critical indices $t$ satisfies $1 \le t \le 10$.

The second line contains $t$ distinct integers: the critical indices.

Each of the next $m$ lines contains three integers $u$, $v$, and $w$, representing an available functional mapping $x \mapsto x_u - x_v$ that requires a cost of $w$. The integers $u$ and $v$ identify the two distinct dimensions involved ($1 \le u \le n$, $1 \le v \le n$, $u \neq v$). The cost $w$ satisfies $1 \le w \le 1000000$.

It is guaranteed that the available functionals are sufficient to ensure the condition can be met.

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
In Example 1, activating the functionals for $(1, 4)$, $(2, 4)$, and $(3, 4)$ incurs a cost of $1+1+1=3$. Their joint kernel consists of all vectors $x$ where $x_1 - x_4 = 0$, $x_2 - x_4 = 0$, and $x_3 - x_4 = 0$. Any such vector inherently satisfies $x_1 - x_2 = 0$, $x_2 - x_3 = 0$, and $x_1 - x_3 = 0$. Thus, the joint kernel is a subspace of the kernels for all pairs of the critical indices $1, 2$, and $3$. This is more cost-effective than activating the functionals defined solely on the critical indices, which would cost at least 4. 

In Example 3, with only one critical index, there are no pairs of distinct critical indices. The condition is vacuously satisfied without activating any functionals, resulting in a minimum cost of 0.