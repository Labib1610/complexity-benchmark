# Problem C — Inconsistent Real System

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of inequalities over the real numbers. For a given set of parameters, the system seeks real variables $U_{i,1}, V_{i,1}, U_{i,2}, V_{i,2}$ for each $i \in \{1 \dots j\}$ satisfying the following constraints:

For all $i \in \{1 \dots j\}$:
1. $V_{i,1} = U_{i,1} \cdot 2^{p_{i,1}}$
2. $V_{i,2} = U_{i,2} \cdot 2^{p_{i,2}}$
3. $U_{i,1} \ge 1$
4. $U_{i,2} \ge 1$
5. $V_{i,1} \cdot V_{i,2} \le 2^T$

For all pairs $i, k \in \{1 \dots j\}$ with $i \neq k$:
6. $(V_{i,1} - U_{k,1})(V_{k,1} - U_{i,1}) \le 0$
7. $(V_{i,2} - U_{k,2})(V_{k,2} - U_{i,2}) \le 0$

In this specific problem, it is guaranteed that **no real solution exists** for the given inputs. Your task is to output a simple proof (a certificate) demonstrating which structural obstruction makes the system unsolvable.

It is guaranteed that the inconsistency in each test case is caused by exactly one of the following two isolated subsystems having no real solution. You must determine which subsystem is inconsistent and output the corresponding certificate. If the description applies to multiple valid certificates, any single one is acceptable.

- **Local Contradiction:** For a single index **i**, the subsystem consisting only of constraints 1, 2, 3, 4, and 5 for that specific $i$ has no real solution.
  Output format: `JOB i` (where **i** is the 1-based index of the parameter pair).

- **Global Contradiction:** For a single index **c** (**c** $\in \{1, 2\}$), the subsystem formed by the variables $U_{1,c}, V_{1,c}, \dots, U_{j,c}, V_{j,c}$ subject to the following constraints has no real solution:
  - Constraint 1 (if $c=1$) or Constraint 2 (if $c=2$) applied to all $i \in \{1 \dots j\}$.
  - Constraint 3 (if $c=1$) or Constraint 4 (if $c=2$) applied to all $i \in \{1 \dots j\}$.
  - Constraint 6 (if $c=1$) or Constraint 7 (if $c=2$) applied to all pairs $i \neq k$.
  - The additional bounding constraint $V_{i,c} \le 2^T$ for all $i \in \{1 \dots j\}$.
  Output format: `LOAD c` (where **c** is exactly 1 or 2).

## Input

The first line specifies two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
The subsequent **j** lines each provide exactly **2** integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the parameters $p_{i,1}$ and $p_{i,2}$ respectively for the $i$-th index.

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

In Example 1, for index 1, the local subsystem is:
1. $V_{1,1} = U_{1,1} \cdot 2^{70}$
2. $V_{1,2} = U_{1,2} \cdot 2^{60}$
3. $U_{1,1} \ge 1$
4. $U_{1,2} \ge 1$
5. $V_{1,1} \cdot V_{1,2} \le 2^{100}$

From constraints 1 and 3, $V_{1,1} \ge 2^{70}$. From constraints 2 and 4, $V_{1,2} \ge 2^{60}$. Multiplying these gives $V_{1,1} \cdot V_{1,2} \ge 2^{130}$. However, constraint 5 requires $V_{1,1} \cdot V_{1,2} \le 2^{100}$. Since $2^{130} > 2^{100}$, these constraints are mutually inconsistent. Thus `JOB 1` is a valid certificate.

In Example 2, for $c=1$, the global subsystem requires finding four pairs $(U_{i,1}, V_{i,1})$ for $i \in \{1, 2, 3, 4\}$ such that:
- $V_{i,1} = U_{i,1} \cdot 2^{50}$
- $U_{i,1} \ge 1$
- $(V_{i,1} - U_{k,1})(V_{k,1} - U_{i,1}) \le 0$ for all $i \neq k$
- $V_{i,1} \le 2^{150}$

The quadratic constraint ensures that the open intervals $(U_{i,1}, V_{i,1})$ and $(U_{k,1}, V_{k,1})$ cannot intersect, which forces the variables to be strictly ordered. If we order them such that $U_{1,1} \le U_{2,1} \le U_{3,1} \le U_{4,1}$, the non-intersecting condition implies $V_{1,1} \le U_{2,1}$, $V_{2,1} \le U_{3,1}$, and $V_{3,1} \le U_{4,1}$. 
By chaining these inequalities, the lowest possible value for the maximum upper bound among the four pairs would be $V_{4,1} \ge 2^{200}$. However, the bounding constraint requires all $V_{i,1} \le 2^{150}$. Since $2^{200} > 2^{150}$, the subsystem has no real solution. Thus `LOAD 1` is a valid certificate.