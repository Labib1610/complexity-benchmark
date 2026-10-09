# Problem C — Contradictory System Parameters

Time limit: 2 s   Memory limit: 256 MB

## Description

You are verifying the constraints of a numerical configuration system. The system requires assigning a real-valued **start coordinate** and an **end coordinate** to various elements.

There are **j** independent indices. Each index $i$ (for $1 \le i \le j$) is associated with a primary element with a given parameter $p_{i,1}$ and a secondary element with a given parameter $p_{i,2}$.

A valid configuration must assign a start and end coordinate to every element such that all of the following rules are satisfied:
1. **Span:** For every element, its end coordinate minus its start coordinate exactly equals its given parameter ($p_{i,1}$ for primary, $p_{i,2}$ for secondary).
2. **Classification:** All primary elements are assigned to Class 1. All secondary elements are assigned to Class 2.
3. **Bounds:** Every element's start coordinate must be $\ge 0$, and its end coordinate must be $\le T$.
4. **Separation:** For any two distinct elements assigned to the same Class, the absolute difference between their coordinate sums must be at least the sum of their given parameters. (Specifically, if element A has coordinates $start_A, end_A$ and parameter $p_A$, and element B has coordinates $start_B, end_B$ and parameter $p_B$, then $|(start_A + end_A) - (start_B + end_B)| \ge p_A + p_B$).
5. **Precedence:** For every index $i$, the end coordinate of its primary element must be less than or equal to the start coordinate of its secondary element.

For every test input, it is guaranteed that no valid configuration exists. Your task is to output a short certificate that proves the rules are contradictory. 

To do this, you must identify the fundamental bottleneck by finding a specific subset of these rules that is already impossible to satisfy on its own. Exactly one of the following isolated rule subsets is guaranteed to be contradictory (even when all other rules and elements are ignored). Print the certificate for the unique subset that fails:

* `JOB i` (where **i** is a 1-based index, $1 \le i \le j$): The subset consisting only of Rules 1, 2, 3, and 5, enforced exclusively on the primary and secondary elements of index $i$. (All other rules, and all elements of other indices, are ignored).
* `LOAD c` (where **c** is either 1 or 2): The subset consisting only of Rules 1, 2, 3, and 4, enforced exclusively on the elements assigned to Class $c$. (All other rules, and all elements assigned to the other class, are ignored).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing $p_{i,1}$ and $p_{i,2}$ respectively for index $i$.

## Output

Print a single line containing either `JOB i` (where **i** is a 1-based index, $1 \le i \le j$) or `LOAD c` (where **c** is either 1 or 2), corresponding to the unique rule subset that remains impossible.

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

In Example 1, `JOB 1` is the correct certificate. If we only enforce the Span, Classification, Bounds, and Precedence rules for index 1, the end coordinate of its primary element and start coordinate of its secondary element must be ordered within the $100$ bound. This is mathematically impossible given their parameters.

In Example 2, `LOAD 1` is the correct certificate. If we only enforce the Span, Classification, Bounds, and Separation rules for Class 1, all four primary elements must satisfy the absolute difference inequality within the $150$ bound. This is impossible given their parameters.