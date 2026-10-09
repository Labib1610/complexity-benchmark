# Critical Offset Span

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of $n$ abstract state variables, denoted $x_1, x_2, \dots, x_n$.

You have access to a pool of $m$ potential offset constraints. Each constraint is defined by two indices $u$ and $v$ and an activation cost $w$, representing the linear expression $x_u - x_v$. The cost to include this constraint in your active set is $w$.

You are mathematically guaranteed that the full pool of $m$ constraints forms a basis for the relative difference space of the variables. Specifically, their linear span (over the real numbers) contains the expression $x_i - x_j$ for all $1 \le i, j \le n$, and the total number of available constraints $m$ is exactly $n - 1$. Because they form a basis, the expression $x_i - x_j$ for any two variables can be constructed as a unique linear combination of the available constraints.

A specific subset of $t$ variables are designated as critical variables.

You must select a subset of the available constraints to form your active set. Your active set must satisfy the following condition: for every pair of critical variables $c_a$ and $c_b$, the difference expression $x_{c_a} - x_{c_b}$ must be within the linear span of your active set.

Your objective is to determine the minimum possible total cost of an active set that satisfies this requirement.

If there is only one critical variable ($t = 1$), the condition is vacuously satisfied by an empty active set, and the minimum cost is $0$.

## Input

The first line provides three integers: $n$, $m$, and $t$. The number of variables is bounded by $1 \le n \le 200000$. The number of constraints $m$ is always exactly $n - 1$. The number of critical variables $t$ satisfies $1 \le t \le n$.

The second line contains $t$ distinct integers representing the indices of the critical variables.

Following this, there are $m$ lines, each detailing a single constraint with three integers: $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$). This represents the constraint $x_u - x_v$ with activation cost $w$. The cost $w$ to activate any single constraint satisfies $1 \le w \le 1000000$.

## Output

Print a single integer: the minimum possible total activation cost required to select a valid active set of constraints.

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

In Example 1, the critical variables are 1 and 4. We must ensure $x_1 - x_4$ is in the linear span of our active set. By selecting the constraints $x_1 - x_2$ (cost 5), $x_2 - x_3$ (cost 1), and $x_3 - x_4$ (cost 2), we can form the linear combination $x_1 - x_4 = (x_1 - x_2) + (x_2 - x_3) + (x_3 - x_4)$. The total cost is 5 + 1 + 2 = 8. Because the constraints form a basis, no cheaper subset spans this difference.

In Example 2, there is only one critical variable (variable 3). Since there are no pairs of distinct critical variables, the condition is vacuously satisfied by the empty set. The minimum possible total cost is 0.