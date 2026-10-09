# Problem B — State Vector Optimization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of $n$ variables $X_1, X_2, \dots, X_n$ where each $X_i \in \{0, 1\}$.
The system includes $m$ defined relations between pairs of variables.
The relations form a connected structure.
For each variable $i$, let $D_i$ be the total number of defined relations that involve variable $i$.

A state vector $X$ is considered **valid** if it satisfies the following equation:
$$ \sum_{j=1}^m (X_{u_j} - X_{v_j})^2 + \sum_{i=1}^n (2 - D_i) X_i = 2 $$
where the first sum is evaluated over all $m$ relations (each connecting $u_j$ and $v_j$), and the second sum is evaluated over all $n$ variables.

Additionally, a specific subset of $t$ critical variables must be set to 1 (that is, $X_k = 1$ for these variables).

Each relation $j$ has an associated positive penalty coefficient $W_j$.
The *evaluation cost* of a state vector is calculated as the sum of $W_j X_{u_j} X_{v_j}$ over all $m$ relations.
Your task is to determine the absolute minimum evaluation cost among all valid state vectors.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the indices of the critical variables.
Each of the next $m$ lines contains three integers $u$, $v$, and $W$ ($1 \le u, v \le n$, $u \neq v$, $1 \le W \le 1000000$), representing a relation between variable $u$ and variable $v$ with a penalty coefficient of $W$.
It is guaranteed that the relations form a connected structure.

## Output

Print a single integer: the minimum evaluation cost of a valid state vector.

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

In Example 1, the critical variables are 1 and 4. 
The relation counts are $D_1 = 1$, $D_2 = 2$, $D_3 = 2$, $D_4 = 1$.
If we set $X = [1, 0, 0, 1]$:
- The first sum (differences squared over all relations) is $(1-0)^2 + (0-0)^2 + (0-1)^2 = 2$.
- The second sum is $(2-1)(1) + (2-2)(0) + (2-2)(0) + (2-1)(1) = 2$.
The total sum is $2 + 2 = 4 \neq 2$. This state vector is invalid.
If we set $X = [1, 1, 1, 1]$:
- The first sum is $(1-1)^2 + (1-1)^2 + (1-1)^2 = 0$.
- The second sum is $(2-1)(1) + (2-2)(1) + (2-2)(1) + (2-1)(1) = 2$.
The total sum is $0 + 2 = 2$. This state vector is valid.
The evaluation cost is $5(1)(1) + 1(1)(1) + 2(1)(1) = 8$.

In Example 2, the only critical variable is 3. 
The relation counts are $D_1 = 1, D_2 = 2, D_3 = 2, D_4 = 2, D_5 = 1$.
If we set $X = [0, 0, 1, 0, 0]$:
- The first sum is $(0-0)^2 + (0-1)^2 + (1-0)^2 + (0-0)^2 = 2$.
- The second sum is $(2-2)(1) = 0$.
The total sum is $2 + 0 = 2$. This state vector is valid, and the evaluation cost is 0.

In Example 3, critical variables 1, 2, and 3 must all be 1 ($X = [1, 1, 1]$).
The relation counts are $D_1 = 1, D_2 = 2, D_3 = 1$.
- The first sum is $(1-1)^2 + (1-1)^2 = 0$.
- The second sum is $(2-1)(1) + (2-2)(1) + (2-1)(1) = 2$.
The total sum is $0 + 2 = 2$. This state vector is valid, and the evaluation cost is $4(1)(1) + 5(1)(1) = 9$.