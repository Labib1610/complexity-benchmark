# Definite Integral Deduction

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing an unknown integrable function $f(x)$ evaluated at $n$ distinct reference points $X_1, X_2, \ldots, X_n$ on the real line.

You are provided with a catalog of $m = n - 1$ available definite integral evaluations. Each available evaluation provides the exact numerical value of $\int_{X_u}^{X_v} f(x) dx$ (where $u \neq v$) and requires $w$ compute hours to perform. 

By the fundamental properties of definite integrals, $\int_B^A f(x) dx = -\int_A^B f(x) dx$, and if you know the values of $\int_A^B f(x) dx$ and $\int_B^C f(x) dx$, you can deduce $\int_A^C f(x) dx$ without any additional compute. It is guaranteed that the full catalog of $n-1$ available evaluations is sufficient to deduce the integral of $f(x)$ between any two reference points in the entire set of $n$ points.

A researcher has specified a target subset of $t$ reference point indices, denoted as $T$. Your objective is to select a subset of the available evaluations such that you can deduce the exact value of $\int_{X_a}^{X_b} f(x) dx$ for every pair of indices $a, b \in T$. You may select evaluations involving points outside of $T$ if they are helpful in deducing the required target integrals.

Determine the minimum total compute hours required to perform a subset of evaluations that satisfies the researcher's requirement. Any evaluation not strictly needed to deduce the required target integrals can be omitted.

## Input

The first line provides three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line provides $t$ distinct integers, representing the indices in the target subset $T$.
The next $m$ lines each contain three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), indicating an available definite integral evaluation $\int_{X_u}^{X_v} f(x) dx$ with a compute cost of $w$ hours.

## Output

Output a single integer: the minimum total compute hours of the selected subset of evaluations.

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