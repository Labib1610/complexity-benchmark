# Problem C — Impossible Domains: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A mathematical solver is attempting to construct a family of distance-preserving functions. Let $j$ be the number of items. For each item $i \in \{1 \dots j\}$, the solver must construct two functions, $f_{i,1}$ and $f_{i,2}$, mapping from closed intervals to the real numbers. 

Specifically, the required domains for the two functions are $f_{i,1}: [0, p_{i,1}] \to \mathbb{R}$ and $f_{i,2}: [0, p_{i,2}] \to \mathbb{R}$. Each function must be an isometry. That is, for any $u, v$ in the domain of $f_{i,c}$, the function must satisfy $|f_{i,c}(u) - f_{i,c}(v)| = |u - v|$.

The constructed functions must strictly satisfy three constraints:
1. **Domain Bounding:** For all $i \in \{1 \dots j\}$ and $c \in \{1, 2\}$, the range (image) of $f_{i,c}$ must be entirely contained within the closed interval $[0, T]$.
2. **Pointwise Precedence:** For every item $i$, and for all real numbers $x \in [0, p_{i,1}]$ and $y \in [0, p_{i,2}]$, the inequality $f_{i,1}(x) \le f_{i,2}(y)$ must hold.
3. **Intersection Cardinality:** For a fixed component $c$ (where $c \in \{1, 2\}$), the ranges of the functions across all $j$ items must not overlap significantly. That is, for any distinct items $i \neq m$, the intersection of the range of $f_{i,c}$ and the range of $f_{m,c}$ must contain at most one real number.

You are analyzing logs from failed systems where a valid complete assignment of these functions is mathematically impossible. For every provided test case, exactly one of the following isolated conditions is inherently impossible to satisfy. Output the code for the one that applies:
- `JOB i` — It is mathematically impossible to find isometries $f_{i,1}$ and $f_{i,2}$ for item **i** (1-indexed) that simultaneously satisfy Domain Bounding and Pointwise Precedence, even if we completely ignore Intersection Cardinality and all other items.
- `LOAD c` — It is mathematically impossible to find isometries $f_{1,c}, \dots, f_{j,c}$ for component **c** (where **c** $\in \{1, 2\}$) that simultaneously satisfy Domain Bounding and Intersection Cardinality, even if we completely ignore Pointwise Precedence and the other component.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the domain lengths $p_{i,1}$ and $p_{i,2}$ for the first and second function of the item, respectively.

## Output

Print a single line containing the applicable certificate: either `JOB i` or `LOAD c`.

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