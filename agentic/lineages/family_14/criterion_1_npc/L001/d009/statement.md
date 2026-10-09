# Problem A — Quotient Space Constraints

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing an $n$-dimensional vector space $V$ over the real numbers, defined by a standard basis $E = \{e_1, e_2, \dots, e_n\}$. 
Your specific objective is to enforce a condition on a critical subset of $t$ target basis vectors, identified by their indices $c_1, c_2, \dots, c_t$.

To do this, you can apply linear constraints to the space. You are provided with a list of $m$ available constraints. Each constraint specifies two basis vectors, $e_u$ and $e_v$, and an activation cost of $w$. 
When you activate a constraint, you permanently enforce the equation $e_u = e_v$. This effectively quotients the vector space by the one-dimensional subspace spanned by the vector $(e_u - e_v)$. 

You must select a subset of these available constraints to activate such that, in the resulting quotient space, the $t$ target basis vectors $e_{c_1}, e_{c_2}, \dots, e_{c_t}$ all map to the exact same vector. 
You may freely activate constraints involving any basis vectors in $E$ (not just the target ones) if doing so yields a lower total activation cost. 

Determine the minimum total activation cost required to ensure all $t$ target basis vectors map to the same vector in the quotient space. (If $t=1$, no constraints are needed, so the minimum cost is 0).

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of dimensions in the vector space, the number of available constraints, and the number of target basis vectors.
The second line contains **t** distinct integers $c_1, c_2, \dots, c_t$: the indices of the target basis vectors.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that the constraint $e_u = e_v$ can be activated for a cost of w.
It is guaranteed that the available constraints are sufficient to ensure all target basis vectors map to the same vector.

## Output

Print a single integer: the minimum total activation cost.

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

In Example 1, the target basis vectors are $e_1, e_2$, and $e_3$. You can activate the constraints $e_1 = e_4$, $e_2 = e_4$, and $e_3 = e_4$ for a total cost of 1+1+1 = 3. 
In the resulting quotient space, since $e_1 = e_4$, $e_2 = e_4$, and $e_3 = e_4$, it follows logically that $e_1 = e_2 = e_3$. All target vectors map to the same vector. 
Alternatively, you could activate the constraints $e_1 = e_2$ and $e_2 = e_3$ for a total cost of 2+2 = 4 to achieve $e_1 = e_2 = e_3$. The minimum cost is 3.

In Example 3, there is only one target basis vector ($t=1$), so no constraints are needed. The minimum cost is 0.