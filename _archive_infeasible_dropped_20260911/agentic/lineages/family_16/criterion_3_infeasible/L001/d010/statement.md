# Problem C — Inconsistent Real System

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with analyzing a specific system of inequalities over the positive real numbers. For a given set of input parameters, the system attempts to find positive real-valued variables $U_{i,1}, V_{i,1}, U_{i,2}, V_{i,2}$ for each index $i \in \{1 \dots j\}$ that satisfy the following constraints:

For every $i \in \{1 \dots j\}$:
1. $\int_{U_{i,1}}^{V_{i,1}} \frac{1}{x} dx = p_{i,1} \ln 2$
2. $\int_{U_{i,2}}^{V_{i,2}} \frac{1}{x} dx = p_{i,2} \ln 2$
3. $U_{i,1} \ge 1$
4. $U_{i,2} \ge 1$
5. $V_{i,1} \cdot V_{i,2} \le 2^T$

For all pairs of distinct indices $i, k \in \{1 \dots j\}$ (where $i \neq k$):
6. The open intervals $(U_{i,1}, V_{i,1})$ and $(U_{k,1}, V_{k,1})$ are disjoint on the real line.
7. The open intervals $(U_{i,2}, V_{i,2})$ and $(U_{k,2}, V_{k,2})$ are disjoint on the real line.

For the provided test cases, it is mathematically guaranteed that **no real solution exists**. Your objective is to output a simple proof (a certificate) identifying the structural obstruction that renders the system unsolvable.

The inconsistency in each test case is guaranteed to arise because exactly one of the two following isolated subsystems has no real solution. You must determine which subsystem is inconsistent and output its corresponding certificate. If multiple valid certificates exist within the applicable category, any single correct one is accepted.

- **Local Contradiction:** There is a single index **i** where the subsystem restricted solely to constraints 1, 2, 3, 4, and 5 for that specific $i$ admits no real solution.
  Output format: `JOB i` (where **i** is the 1-based index of the parameters).

- **Global Contradiction:** There is a single index **c** (**c** $\in \{1, 2\}$) where the subsystem formed by the variables $U_{1,c}, V_{1,c}, \dots, U_{j,c}, V_{j,c}$ under the following constraints admits no real solution:
  - Constraint 1 (if $c=1$) or Constraint 2 (if $c=2$) applied to all $i \in \{1 \dots j\}$.
  - Constraint 3 (if $c=1$) or Constraint 4 (if $c=2$) applied to all $i \in \{1 \dots j\}$.
  - Constraint 6 (if $c=1$) or Constraint 7 (if $c=2$) applied to all pairs $i \neq k$.
  - The additional bounding constraint $V_{i,c} \le 2^T$ for all $i \in \{1 \dots j\}$.
  Output format: `LOAD c` (where **c** is exactly 1 or 2).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains exactly **2** integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the parameters $p_{i,1}$ and $p_{i,2}$ for the $i$-th index.

## Output

Print exactly one line containing a valid certificate from the applicable category: either `JOB i` or `LOAD c`. When printing `LOAD c`, the value of **c** must be exactly 1 or 2.

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

In Example 1, for index 1, the local subsystem requires:
1. $\int_{U_{1,1}}^{V_{1,1}} \frac{1}{x} dx = 70 \ln 2$
2. $\int_{U_{1,2}}^{V_{1,2}} \frac{1}{x} dx = 60 \ln 2$
3. $U_{1,1} \ge 1$
4. $U_{1,2} \ge 1$
5. $V_{1,1} \cdot V_{1,2} \le 2^{100}$

Summing the first two constraints gives $\int_{U_{1,1}}^{V_{1,1}} \frac{1}{x} dx + \int_{U_{1,2}}^{V_{1,2}} \frac{1}{x} dx = 130 \ln 2$.
Since $U_{1,1} \ge 1$ and $U_{1,2} \ge 1$, we have $\int_{1}^{V_{1,1}} \frac{1}{x} dx \ge \int_{U_{1,1}}^{V_{1,1}} \frac{1}{x} dx$ and similarly for the second process.
Thus, $\int_{1}^{V_{1,1}} \frac{1}{x} dx + \int_{1}^{V_{1,2}} \frac{1}{x} dx \ge 130 \ln 2$.
By properties of logarithms, this evaluates to $\ln(V_{1,1}) + \ln(V_{1,2}) \ge 130 \ln 2$, meaning $\ln(V_{1,1} \cdot V_{1,2}) \ge \ln(2^{130})$, which implies $V_{1,1} \cdot V_{1,2} \ge 2^{130}$.
This contradicts constraint 5, which requires $V_{1,1} \cdot V_{1,2} \le 2^{100}$. Thus `JOB 1` is a valid certificate.

In Example 2, for $c=1$, the global subsystem requires finding four pairs $(U_{i,1}, V_{i,1})$ for $i \in \{1, 2, 3, 4\}$ such that:
- $\int_{U_{i,1}}^{V_{i,1}} \frac{1}{x} dx = 50 \ln 2$
- $U_{i,1} \ge 1$
- The open intervals $(U_{i,1}, V_{i,1})$ are pairwise disjoint.
- $V_{i,1} \le 2^{150}$

The disjointness of the four open intervals dictates that they can be ordered sequentially on the real line. Let the sorted intervals correspond to indices $a, b, c, d$ such that $1 \le U_{a,1} < V_{a,1} \le U_{b,1} < V_{b,1} \le U_{c,1} < V_{c,1} \le U_{d,1} < V_{d,1} \le 2^{150}$.
We can integrate $1/x$ over this entire span:
$\int_{1}^{2^{150}} \frac{1}{x} dx \ge \int_{U_{a,1}}^{V_{a,1}} \frac{1}{x} dx + \int_{U_{b,1}}^{V_{b,1}} \frac{1}{x} dx + \int_{U_{c,1}}^{V_{c,1}} \frac{1}{x} dx + \int_{U_{d,1}}^{V_{d,1}} \frac{1}{x} dx$.
The left side evaluates to $150 \ln 2$.
The right side is the sum of the four individual integrals, which is $50 \ln 2 + 50 \ln 2 + 50 \ln 2 + 50 \ln 2 = 200 \ln 2$.
This requires $150 \ln 2 \ge 200 \ln 2$, which is false. Thus the subsystem has no real solution, making `LOAD 1` a valid certificate.