# Equality Verification System

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of **N** variables, labeled 1 through **N**.

There are **E** available equality constraints. Each constraint asserts that two specific variables, **u** and **v**, are equal. Verifying a constraint incurs a known computational cost of **w**. It is guaranteed that if all **E** constraints were verified, they would collectively prove that all **N** variables are equal to one another.

A specific subset of **F** variables are designated as *critical*. You must select a subset of the available constraints to verify so that their combined assertions logically guarantee that all **critical** variables are equal to each other (via transitivity). You may verify constraints involving non-critical variables if they are useful in establishing the equality of the critical ones.

Determine the minimum total computational cost required to verify a subset of constraints that successfully proves all critical variables are equal. (If **F** = 1, no constraints need to be verified, so the minimum total cost is 0.)

## Input

The first line contains three integers **N**, **E**, and **F** (1 ≤ F ≤ N, 1 ≤ N ≤ 200000, E = N − 1).
The second line contains **F** distinct integers: the labels of the critical variables.
Each of the following **E** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ N, u ≠ v, 1 ≤ w ≤ 1000000), representing an available constraint asserting that variable **u** equals variable **v**, with a verification cost of **w**.

## Output

Print a single integer: the minimum total computational cost required to prove all critical variables are equal.

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