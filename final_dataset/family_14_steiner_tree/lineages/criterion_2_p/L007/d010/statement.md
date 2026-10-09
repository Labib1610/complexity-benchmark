# Target Subspace Spanning

Time limit: 2 s   Memory limit: 256 MB

## Description

You are working with an $n$-dimensional vector space over the real numbers, defined by a standard basis $e_1, e_2, \ldots, e_n$.

You are provided with a catalog of $m$ available difference vectors. Each available vector is of the form $d = e_u - e_v$ (where $u \neq v$) and has an associated procurement cost of $w$. 

By the properties of vector spaces, the linear span of a vector $e_A - e_B$ inherently includes its negation $e_B - e_A$. Furthermore, if your procured vectors can linearly span both $e_A - e_B$ and $e_B - e_C$, their combined linear span will also include $e_A - e_C$ without requiring any additional vector procurements. It is guaranteed that the full catalog of $m$ available vectors spans the entire $(n-1)$-dimensional hyperplane of vectors whose coordinates sum to zero. This implies that the full catalog is sufficient to span the difference $e_x - e_y$ for any two basis vectors $e_x, e_y$ in the space.

A researcher has specified a target subset of $t$ basis vector indices, denoted as $T$. Your objective is to procure a subset of the available vectors such that for every pair of indices $a, b \in T$, the target vector $e_a - e_b$ lies within the linear span of your procured subset. You may procure available vectors involving basis vectors outside of $T$ if they are helpful in spanning the required target vectors.

Determine the minimum total procurement cost of a subset of available vectors that satisfies the researcher's requirement. Any available vector not strictly needed to span the required target vectors can be omitted.

## Input

The first line provides three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line provides $t$ distinct integers, representing the indices in the target subset $T$.
The next $m$ lines each contain three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), indicating an available difference vector $e_u - e_v$ with a procurement cost of $w$.

## Output

Output a single integer: the minimum total procurement cost of the selected subset of vectors.

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