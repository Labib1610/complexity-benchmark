# Problem B — Minimal Constraint System Simplification

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with simplifying a system of **n** variables, numbered 1 to **n**, and **m** two-way constraints. Each constraint links two distinct variables and has a known evaluation cost.

The initial system is fully *coupled*. A set of variables is considered *coupled* if it is impossible to partition it into two non-empty groups such that no constraint links a variable in the first group to a variable in the second group. (A set consisting of a single variable cannot be partitioned and is inherently coupled). Because the system is fully coupled and has exactly **m = n − 1** constraints, there is exactly one sequence of constraints linking any two variables.

You may perform a sequence of variable eliminations to simplify the system. In a single elimination step, you permanently discard exactly one variable, which safely drops any constraints linked to it. However, your elimination sequence must satisfy two strict safety regulations:
1. You may never eliminate any of the **t** *target variables*, as they are required for the final output.
2. After every individual elimination step, the set of remaining variables must still be *coupled*. If discarding a variable would cause the remaining variables to lose coupling (i.e., they could then be partitioned into two unlinked groups), that variable cannot be eliminated at that time.

You can stop the elimination process at any point, including making no eliminations at all. Your objective is to determine the minimum possible total evaluation cost of the constraints that remain in the system when you finish.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the labels of the target variables.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a constraint between variable **u** and variable **v** with an evaluation cost of **w**.

## Output

Output a single integer representing the minimum possible total evaluation cost of the remaining constraints after a valid sequence of eliminations.

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