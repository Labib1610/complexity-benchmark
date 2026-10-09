# Problem C — Impossibility Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of linear inequalities over $4j$ real variables. For a given set of parameters, the system requires assigning four real numbers—$x_i, y_i, u_i,$ and $v_i$—for each index $i \in \{1 \dots j\}$ such that all of the following conditions are simultaneously satisfied:

1. **Span 1:** $y_i - x_i = p_{i,1}$
2. **Span 2:** $v_i - u_i = p_{i,2}$
3. **Chain:** $u_i \ge y_i$
4. **Separation 1:** For any $i \neq k$, either $y_i \le x_k$ or $y_k \le x_i$
5. **Separation 2:** For any $i \neq k$, either $v_i \le u_k$ or $v_k \le u_i$
6. **Global Bounds:** $x_i \ge 0$ and $v_i \le T$ for all $i$

In this specific problem, **no valid assignment of variables exists** that can satisfy the system for the given inputs. Your task is to output a simple proof (a certificate) demonstrating why the system is structurally impossible to solve.

It is guaranteed that the impossibility in each test case is caused by exactly one of the following two reasons. You must determine which reason applies and output the corresponding certificate. If the applicable reason offers multiple valid certificates, any single one is acceptable.

- **Local Contradiction:** For a single index **i**, there exist no real values $x_i, y_i, u_i, v_i$ that satisfy conditions 1, 2, 3, and 6. (In other words, the chain for index $i$ cannot fit within the global bounds, even if conditions 4 and 5 are completely ignored for all variables).
  Output format: `JOB i` (where **i** is the 1-based index of the parameter pair).

- **Global Contradiction:** For a single dimension **c** (**c** $\in \{1, 2\}$), there exist no values for the $2j$ variables in that dimension that satisfy the span, separation, and dimension-specific bounds. Specifically, if $c=1$, no $x_i, y_i$ satisfy condition 1, condition 4, and the bounds $x_i \ge 0$ and $y_i \le T$ for all $i$. If $c=2$, no $u_i, v_i$ satisfy condition 2, condition 5, and the bounds $u_i \ge 0$ and $v_i \le T$ for all $i$. (In other words, the separation requirements force the variables out of bounds, even if condition 3 is completely ignored).
  Output format: `LOAD c` (where **c** is exactly 1 or 2).

## Input

The first line specifies two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
The subsequent **j** lines each provide exactly **2** integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the required spans $p_{i,1}$ and $p_{i,2}$ respectively for the $i$-th index.

## Output

Output exactly one line containing a valid certificate from the applicable category: either `JOB i` or `LOAD c`. If printing `LOAD c`, then **c** must be exactly 1 or 2.

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, for index 1, condition 1 gives $y_1 = x_1 + 70$. Condition 3 gives $u_1 \ge y_1$. Condition 2 gives $v_1 = u_1 + 60$. Combining these yields $v_1 \ge x_1 + 130$. Since condition 6 requires $x_1 \ge 0$, we must have $v_1 \ge 130$, which contradicts the requirement $v_1 \le 100$. Thus `JOB 1` is a valid certificate.
In Example 2, for dimension 1, the separation condition requires the intervals $[x_i, y_i)$ to be non-overlapping. The sum of their spans $y_i - x_i$ is 200. It is impossible to place non-overlapping intervals of total length 200 such that all $x_i \ge 0$ and all $y_i \le 150$. Thus `LOAD 1` is a valid certificate.