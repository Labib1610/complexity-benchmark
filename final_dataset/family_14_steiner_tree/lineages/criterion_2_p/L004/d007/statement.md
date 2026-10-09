# Transposition Subgroup Orbit

Time limit: 2 s
Memory limit: 256 MB

## Description

You are analyzing the natural action of the symmetric group $S_n$ on the set of elements $X = \{1, 2, \dots, n\}$.

You are provided with a pool of $m$ optional subgroup generators. Each generator is a transposition that swaps elements $u$ and $v$ (leaving all other elements fixed) and has an associated inclusion cost $w$.

The pool of available generators is minimal and complete: there are exactly $m = n - 1$ transpositions available, and together they generate the entire symmetric group $S_n$.

Your objective is to select a subset of these transpositions to generate a subgroup $H$ of $S_n$. You must ensure that under the action of $H$ on $X$, a specific list of $t$ critical elements all belong to the exact same orbit. (That is, for any two critical elements $a$ and $b$, there must exist some permutation $\pi \in H$ such that $\pi(a) = b$). The orbits of the remaining non-critical elements do not matter.

What is the minimum total cost of the transpositions you must select to generate a subgroup $H$ that satisfies this orbit condition?

## Input

The first line contains three integers **n**, **m**, and **t**. The number of elements is **n** (1 ≤ **n** ≤ 200000). The number of available transpositions **m** is always exactly **n** − 1. The number of critical elements is **t** (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the critical elements.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These denote an optional transposition swapping **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), which costs **w** to include (1 ≤ **w** ≤ 1000000).

## Output

Print a single integer: the minimum total cost required.

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