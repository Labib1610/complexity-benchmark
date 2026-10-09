# Problem A — Zero Sum Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a mathematical function $f(x_1, x_2, \dots, x_n)$ where each variable $x_i$ is restricted to taking a value of either $0$ or $1$.

The function is defined as the sum of $m$ specific terms. Each term is the product of two distinct variables, $x_u \cdot x_v$. (If $m=0$, the function has no terms and evaluates to $0$ for all assignments.)

You need to determine if there exists an assignment of values to the $n$ variables such that exactly $k$ variables are set to $1$, and the overall function evaluates to exactly $0$.

## Input

The first line contains three integers $n$, $m$, and $k$ (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next $m$ lines contains two integers $u$ and $v$ (1 ≤ u, v ≤ n, u ≠ v), indicating that the product $x_u \cdot x_v$ is one of the terms in the sum. No term is listed more than once.

## Output

If a valid assignment exists, print `YES` on the first line, then on the second line print the $k$ distinct indices of the variables that are set to $1$, separated by spaces. Any valid assignment meeting the criteria is accepted.

If no such assignment exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```