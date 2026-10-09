# Axiom Selection

Time limit: 2 s
Memory limit: 256 MB

## Description

You are analyzing a formal logical system containing **n** propositions, numbered 1 to **n**. Each proposition can evaluate to either True or False.

You are given a pool of **m** optional axioms. Each axiom establishes a logical equivalence between two propositions **u** and **v** (meaning they must both be True or both be False). Adopting an axiom into your system incurs a computational cost of **w**. 
The pool of axioms is minimally complete: there are exactly **m** = **n** − 1 available axioms, and if you were to adopt all of them, the entire system would admit exactly two valid truth assignments (one where all **n** propositions are True, and one where all are False).

Your objective is to adopt a subset of these axioms such that a specific list of **t** critical propositions are unconditionally synchronized. That is, in any valid truth assignment that satisfies all axioms in your adopted subset, the **t** critical propositions must all hold the exact same truth value as each other. You do not care about the truth values of the remaining propositions, as long as the adopted axioms are satisfied.

What is the minimum total cost of axioms you must adopt to ensure this property for the **t** critical propositions?

## Input

The first line contains three integers **n**, **m**, and **t**. The number of propositions is **n** (1 ≤ **n** ≤ 200000). The number of available axioms **m** is always exactly **n** − 1. The number of critical propositions **t** (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the critical propositions.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These denote an optional axiom establishing the equivalence of proposition **u** and proposition **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), which costs **w** to adopt (1 ≤ **w** ≤ 1000000).

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