# Problem C — System of Inequalities: Certificate of Unsatisfiability

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given a target threshold $T$ and a set of $j$ elements. Each element $i$ (from $1$ to $j$) is associated with two positive integers, $p_{1,i}$ and $p_{2,i}$.

Consider the problem of assigning two non-negative real numbers, $S_i$ and $U_i$, to each element $i$ such that the following four conditions hold:
1. **Precedence:** For every element $i$, $S_i + p_{1,i} \le U_i$.
2. **First-stage separation:** For any pair of distinct elements $i$ and $k$, the open-ended intervals $[S_i, S_i + p_{1,i})$ and $[S_k, S_k + p_{1,k})$ do not intersect.
3. **Second-stage separation:** For any pair of distinct elements $i$ and $k$, the open-ended intervals $[U_i, U_i + p_{2,i})$ and $[U_k, U_k + p_{2,k})$ do not intersect.
4. **Threshold:** For every element $i$, $U_i + p_{2,i} \le T$.

For every test case in this problem, it is guaranteed that no such assignment of $S_i$ and $U_i$ exists. Your task is to provide a directly checkable certificate of unsatisfiability by identifying a specific relaxed subsystem of these constraints that is already impossible to satisfy on its own. 

Output a valid certificate of unsatisfiability from one of the two allowed forms below. It is guaranteed that at least one such certificate exists for every test case.

- `JOB i` : For the element at 1-based index $i$, the constraints $S_i \ge 0$, Precedence (1), and Threshold (4) cannot be simultaneously satisfied (ignoring all other elements and conditions).
- `LOAD c` : where $c \in \{1, 2\}$. 
  - If $c=1$, it certifies that the constraints $S_i \ge 0$, First-stage separation (2), and a modified threshold $S_i + p_{1,i} \le T$ for all $i$, cannot be simultaneously satisfied (ignoring $U_i$, $p_{2,i}$, and all other conditions). 
  - If $c=2$, it certifies that the constraints $U_i \ge 0$, Second-stage separation (3), and Threshold (4) for all $i$, cannot be simultaneously satisfied (ignoring $S_i$, $p_{1,i}$, and all other conditions).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the values of $p_{1,i}$ and $p_{2,i}$ for the $i$-th element.

## Output

Print a single line containing a valid certificate: `JOB i` or `LOAD c` as described above.

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

In Example 1, for element 1, the `JOB` subsystem requires $S_1 \ge 0$, $S_1 + 70 \le U_1$, and $U_1 + 60 \le 100$. This implies $S_1 \le -30$, which contradicts $S_1 \ge 0$. Thus, this subsystem is unsatisfiable for element 1, making `JOB 1` a valid certificate.

In Example 2, no single element violates the `JOB` subsystem. However, for `LOAD 1`, the subsystem requires placing four disjoint intervals of length 50 into the bounds $[0, 150]$. This requires a total length of 200, which cannot fit in a span of 150. Thus, this subsystem is unsatisfiable, making `LOAD 1` a valid certificate.