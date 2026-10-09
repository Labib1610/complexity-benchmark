# Problem B — Enforcing Variable Equivalence

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working with a system of $n$ continuous variables, numbered $1$ to $n$. You have a list of $m$ possible equality constraints. Each constraint enforces that two specific variables are strictly equal ($x_u = x_v$) and comes with an activation cost $w$.

It is guaranteed that $m = n - 1$, and that if you were to activate all $m$ constraints, the resulting system of equations would logically force all $n$ variables to take the exact same value.

You are given a subset of $t$ target variables. Your task is to select a subset of the available constraints to activate such that the chosen constraints logically imply that all $t$ target variables must be equal to one another. Assume the variables can take arbitrary real values, meaning equality can only be established through direct transitive links. (If $t=1$, this condition is trivially satisfied without activating any constraints).

Find the minimum possible total activation cost of the chosen constraints.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the indices of the target variables.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \ne v$, $1 \le w \le 1000000$), representing an available constraint $x_u = x_v$ with an activation cost of $w$. The constraints satisfy the global property described above.

## Output

Print a single integer: the minimum total activation cost required to ensure all target variables are equal.

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

In Example 1, the target variables are 1 and 4. To logically enforce $x_1 = x_4$, we must activate all three constraints: $x_1 = x_2$, $x_2 = x_3$, and $x_3 = x_4$. The total cost is $5 + 1 + 2 = 8$. 

In Example 2, there is only one target variable, so the condition that all targets equal one another is trivially met at a cost of $0$.
