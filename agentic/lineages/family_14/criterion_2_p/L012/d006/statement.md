# Quadratic Penalty Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

A system state is represented by a vector $x = (x_1, x_2, \dots, x_n) \in \mathbb{R}^n$. Exactly $t$ of these coordinates are designated as **Target Dimensions**.

You are provided with a collection of $m$ available quadratic penalty operators. Each operator $P(x)$ enforces a constraint between two specific coordinates and takes the form $(x_u - x_v)^2$. Activating an operator incurs a specific scalar cost. The complete collection of $m$ available operators is sufficient to guarantee that if their sum evaluates to zero, then all $n$ coordinates of $x$ must be identical. Furthermore, this collection contains exactly $m = n - 1$ operators, which is the exact rank required to enforce this one-dimensional solution space.

You must select a subset of these operators to activate. Let $F(x)$ be the sum of your selected operators. Your selection must satisfy the following condition: for any state vector $x$ such that $F(x) = 0$, the values of $x$ at all $t$ Target Dimensions must be identical. (When $t=1$, this condition imposes no additional restriction on the selected subset).

Your objective is to determine the minimum total activation cost required to select a valid subset of operators meeting this condition.

## Input

The first line contains three integers: $n$, $m$, and $t$.
- $n$ is the total number of coordinates in the state vector. There is at least 1 coordinate and at most 200000.
- $m$ is the number of available operators, which is exactly $n - 1$.
- $t$ is the number of Target Dimensions, which is at least 1 and at most $n$.

The second line contains $t$ distinct integers: the indices of the Target Dimensions (from 1 to $n$).

Each of the next $m$ lines details an available operator with three integers: $u$, $v$, and $w$.
- $u$ and $v$ are distinct coordinate indices (from 1 to $n$) linked by the operator $(x_u - x_v)^2$.
- $w$ is the cost to activate this operator. This cost is a positive integer not exceeding 1000000.

These $m$ lines form the exact structure described above, guaranteeing a one-dimensional solution space when all operators are active.

## Output

Print a single integer: the minimum total activation cost required to ensure all Target Dimensions are equal whenever the sum of the selected operators is zero.

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

In Example 1, the Target Dimensions 1 and 4 can only be forced to take identical values when $F(x)=0$ by activating all three operators (costs 5 + 1 + 2 = 8). In Example 2, there is only one Target Dimension. Since a single coordinate always equals itself, no operators need to be activated, resulting in a minimum cost of 0.