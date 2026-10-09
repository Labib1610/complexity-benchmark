# Component Assembly

Time limit: 2 s
Memory limit: 256 MB

## Description

You are analyzing a mathematical model consisting of **n** integer variables, numbered 1 to **n**. Initially, these variables are completely independent and can take any arbitrary values.

You are provided with a list of **m** optional constraints. Each constraint specifies that variable **u** must be strictly equal to variable **v**. Enforcing a constraint incurs a computational cost of **w**. 
The list of constraints is minimally exhaustive: there are exactly **m** = **n** − 1 available constraints, and if you were to enforce every single one of them, all **n** variables would be forced to take the exact same value.

Your objective is to enforce a subset of these constraints such that a specific list of **t** target variables are guaranteed to be equal to each other. Since the variables can initially take any arbitrary values, the only way to guarantee that two variables are equal is to link them through a sequence of enforced constraints. You do not care about the relationships between the remaining variables, though some may end up being equal to the target variables as a logical consequence of your chosen subset.

What is the minimum total computational cost (the sum of the costs of the enforced constraints) required to ensure all **t** target variables are equal?

## Input

The first line contains three integers **n**, **m**, and **t**. The number of variables is **n** (1 ≤ **n** ≤ 200000). The number of available constraints **m** is always exactly **n** − 1. The number of target variables **t** (1 ≤ **t** ≤ **n**).
The second line contains **t** distinct integers: the identifiers of the target variables.
Each of the next **m** lines contains three integers **u**, **v**, and **w**. These denote a constraint specifying that variable **u** and variable **v** must be equal (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), which costs **w** to enforce (1 ≤ **w** ≤ 1000000).

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