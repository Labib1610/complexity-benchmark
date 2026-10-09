# Problem C — Impossible Allocation: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A system attempts to allocate discrete elements from a linearly ordered universe $U = \{1, 2, \dots, T\}$. There are $j$ entities. For each entity $i$, the system must select two subsets of $U$: a subset $X_i$ containing exactly $p1_i$ elements, and a subset $Y_i$ containing exactly $p2_i$ elements.

A valid allocation must satisfy three structural axioms:
1. **Supremum-Infimum Separation:** For any single entity $i$, if $x \in X_i$ and $y \in Y_i$, then $x < y$.
2. **X-Orthogonality:** For any two distinct entities $i$ and $k$, the intersection of $X_i$ and $X_k$ is empty.
3. **Y-Orthogonality:** For any two distinct entities $i$ and $k$, the intersection of $Y_i$ and $Y_k$ is empty.

*(Note: An element $u \in U$ may simultaneously belong to $X_i$ and $Y_k$, provided this does not violate the separation axiom for their respective entities.)*

Every provided configuration is mathematically impossible to allocate—there is no valid way to choose the subsets to satisfy all axioms. Instead of attempting to generate the subsets, your task is to identify the bottleneck that proves the configuration is unachievable, providing a short certificate.

Exactly one of the following foundational requirements is broken. Output the applicable certificate:

- **Separation Failure:** For some entity $i$, there do not exist any two subsets $X_i, Y_i \subset U$ of the required sizes that satisfy the Supremum-Infimum Separation axiom. Output `JOB i` (where $i$ is the 1-based index of the entity).
- **X-Domain Exhaustion:** There is no way to choose subsets $X_1, \dots, X_j \subset U$ of the required sizes that satisfy the X-Orthogonality axiom. Output `LOAD 1`.
- **Y-Domain Exhaustion:** There is no way to choose subsets $Y_1, \dots, Y_j \subset U$ of the required sizes that satisfy the Y-Orthogonality axiom. Output `LOAD 2`.

You are guaranteed that exactly one of these requirements will be broken for the given input.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required number of elements for $X_i$ and $Y_i$ respectively (i.e., $p1_i$ and $p2_i$).

## Output

Print a single line: `JOB i` (for a separation failure) or `LOAD c` (for an exhaustion failure, where **c** is 1 for X-domain exhaustion or 2 for Y-domain exhaustion).

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

In Example 1, entity 1 requires subsets of size $|X_1| = 70$ and $|Y_1| = 60$. There is no way to select these from a universe of 100 elements such that every element in $X_1$ is strictly less than every element in $Y_1$, breaking the Supremum-Infimum Separation axiom. Thus `JOB 1` is the correct proof of impossibility. 

In Example 2, no single entity breaks the Separation axiom. However, the entities require $|X_i| = 50$ for all four entities. There is no way to select these mutually disjoint subsets (totaling 200 elements) from a universe of 150 elements, breaking the X-Orthogonality axiom. Thus `LOAD 1` is the correct output.