# Problem B — Minimal Constraint System Simplification

Time limit: 2 s   Memory limit: 256 MB

## Description

You are optimizing a system of **n** real-valued variables, numbered 1 to **n**, and **m** equality conditions. Each condition enforces $x_u = x_v$ for two distinct variables and has an associated retention cost.

A subset of variables **S** is considered *monolithic* if every possible assignment of real numbers to the variables in **S** that satisfies all conditions linking two variables that are both in **S** results in all variables in **S** sharing a single common value. (A subset containing exactly one variable is inherently monolithic). Initially, the full set of **n** variables is monolithic.

You may simplify the system by performing a sequence of variable eliminations. In a single step, you permanently discard exactly one variable, which safely drops any equality conditions involving it. However, your elimination sequence must satisfy two strict safety regulations:
1. You may never eliminate any of the **t** *mandated variables*, as they are required for the final system.
2. After every individual elimination step, the subset of remaining variables must still be *monolithic*. If discarding a variable would allow an assignment where the remaining conditions are satisfied but the remaining variables take on two or more distinct values, that variable cannot be eliminated at that time.

You can stop the elimination process at any point, including making no eliminations at all. Your objective is to determine the minimum possible total retention cost of the equality conditions that remain in the system when you finish.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the indices of the mandated variables.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating an equality condition between variable **u** and variable **v** with a retention cost of **w**.

## Output

Output a single integer representing the minimum possible total retention cost of the remaining equality conditions after a valid sequence of eliminations.

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