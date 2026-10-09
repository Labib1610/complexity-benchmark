# Problem A — Equality Constraint Minimization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are given a system of **n** variables, denoted $x_1, x_2, \ldots, x_n$. You are also given a target subset of **t** variables that must be guaranteed to hold the same value.

To enforce this, you can activate bidirectional equality constraints. The system has **m** available equality constraints. The $i$-th available constraint, if activated, enforces that $x_u = x_v$ and costs $w$ to activate.

Because equality is transitive, if you activate $x_a = x_b$ and $x_b = x_c$, it automatically enforces $x_a = x_c$. You may activate any combination of available constraints, including those involving variables outside the target subset, if doing so helps enforce the required condition for the target variables at a lower total cost.

Determine the minimum total activation cost such that for every assignment of values to the **n** variables satisfying the activated constraints, all **t** target variables are guaranteed to be equal.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the indices of the target variables.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available equality constraint between variable $x_u$ and variable $x_v$ at activation cost $w$.
The available constraints are sufficient to ensure all target variables are equal.

## Output

Print a single integer: the minimum total activation cost to ensure all target variables are equal.

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

In Example 1, activating the constraints involving variable 4 ($x_1 = x_4$, $x_2 = x_4$, and $x_3 = x_4$ at a cost of 1+1+1 = 3) ensures that variables 1, 2, and 3 are equal. This is cheaper than activating the constraints directly between the target variables. In Example 3, there is only one target variable, so no constraints need to be activated and the minimum cost is 0.