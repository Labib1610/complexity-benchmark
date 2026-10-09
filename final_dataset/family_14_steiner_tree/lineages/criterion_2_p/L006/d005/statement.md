# Problem B — Equation Acquisition

Time limit: 2 s
Memory limit: 256 MB

## Description

You are working with a system of $n$ unknown real variables, $x_1, x_2, \dots, x_n$.

You are provided with a catalog of $m$ optional equations. Each available equation is of the form $x_u = x_v$ and has a specific acquisition cost.

Your objective focuses on a designated priority set of $t$ indices. You must acquire a subset of the available equations such that, for any valid assignment of real numbers to the variables that satisfies all of your acquired equations, it is mathematically guaranteed that $x_i = x_j$ for every pair of indices $i$ and $j$ in the priority set. You may acquire equations involving non-priority indices if they are useful for chaining logical deductions.

Determine the minimum total cost required to acquire a valid subset of equations that satisfies this condition for the priority set.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line lists **t** distinct integers representing the indices in the priority set.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate an available equation $x_u = x_v$ that can be acquired at a cost of **w**. It is guaranteed that if you were to acquire all **m** equations, the only satisfying assignments would be those where all **n** variables are equal.

## Output

Output a single integer representing the minimum possible total cost to acquire a subset of equations that guarantees $x_i = x_j$ for all priority indices $i$ and $j$.

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