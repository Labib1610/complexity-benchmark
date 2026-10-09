# Problem C — Orthogonal Support Diagnostics

Time limit: 2 s   Memory limit: 256 MB

## Description

We are analyzing systems of binary vectors. For a given dimension $T$ and a collection of $j$ elements, we must assign to each element $k \in \{1, \dots, j\}$ two binary vectors, $v_k$ and $w_k$, both of length $T$ (with indices running from $1$ to $T$).

Any valid assignment of these vectors must satisfy the following rules:
1. **Hamming Weight:** For all $k \in \{1, \dots, j\}$, the number of $1$s in $v_k$ must be exactly $p_{1,k}$, and the number of $1$s in $w_k$ must be exactly $p_{2,k}$.
2. **Support Separation:** For all $k \in \{1, \dots, j\}$, the highest index where $v_k$ contains a $1$ must be strictly less than the lowest index where $w_k$ contains a $1$.
3. **v-Orthogonality:** For any two distinct elements $k, m \in \{1, \dots, j\}$ (where $k \neq m$), the dot product $v_k \cdot v_m$ must be exactly $0$.
4. **w-Orthogonality:** For any two distinct elements $k, m \in \{1, \dots, j\}$ (where $k \neq m$), the dot product $w_k \cdot w_m$ must be exactly $0$.

For every given input, it is mathematically guaranteed that no valid assignment of vectors exists. You are tasked with determining why. Exactly one of the following two fundamental contradictions will be present in the input, and you must output the corresponding certificate:

- `JOB i` (where $i \in \{1, \dots, j\}$): The system of constraints formed by rules 1 and 2 is intrinsically inconsistent for the single index $i$ on its own. (If multiple indices fit this description, you may output any one of them).
- `LOAD c` (where $c \in \{1, 2\}$): The system of constraints formed by rule 1 and the orthogonality rule for family $c$ (rule 3 for $c=1$, rule 4 for $c=2$) is intrinsically inconsistent when applied to the entire collection of $j$ indices. (If both families fit this description, you may output either one).

*(Note: the certificate prefixes `JOB` and `LOAD` are retained for compatibility with legacy systems).*

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required Hamming weights for vectors $v_k$ and $w_k$, respectively. Elements are implicitly numbered 1 to **j**.

## Output

Print a single line containing the certificate: either `JOB i` or `LOAD c`.

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

In Example 1, **T** = 100. For element 1, we must construct binary vectors $v_1$ and $w_1$ of length 100. The Hamming weight rule requires $v_1$ to have 70 ones and $w_1$ to have 60 ones. The support separation rule requires the highest index of a 1 in $v_1$ to be strictly less than the lowest index of a 1 in $w_1$. This forces the two vectors to place their 1s in completely disjoint segments of indices, requiring at least $70 + 60 = 130$ available positions. Since the vectors only have length 100, this is impossible. Thus, `JOB 1` proves the inconsistency.

In Example 2, **T** = 150. For family 1, the v-orthogonality rule requires that for any pair of vectors $v_k$ and $v_m$, their dot product is 0. Since they are binary vectors, this means no two vectors can have a 1 at the same index. Each of the 4 vectors must contain exactly 50 ones, requiring 200 distinct indices in total. This cannot be satisfied within a vector of length 150. Thus, `LOAD 1` proves the inconsistency.