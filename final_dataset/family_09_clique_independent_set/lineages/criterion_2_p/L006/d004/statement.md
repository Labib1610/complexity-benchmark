# Problem B — Exact-Weight Logical Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of **n** boolean variables (numbered 1 to **n**) and **m** logical constraints. Each constraint links two specific variables. 

The system designers guarantee a specific structural property of this system: the variables can be perfectly divided into two categories, and every constraint connects one variable from each category; no constraint joins two variables in the same category. (You are not provided with this division into categories; you must infer it from the constraints if necessary).

Your task is to configure the system by setting exactly **k** of these variables to True (and the rest to False). The constraints dictate that for each linked pair of variables, they cannot both be set to True. Thus, no two variables selected to be True can share a constraint.

A valid True-assignment set is not restricted to being a subset of a single category; solutions may contain variables from both categories. In fact, some systems have a maximum possible number of True variables strictly larger than the size of either category. Feasibility must therefore be evaluated from the exact constraint structure, not from category sizes alone.

Given the target number **k**, determine if it is possible to choose exactly **k** distinct variables to be True without violating any constraint. If it is possible, output a valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a constraint between variable **u** and variable **v**. No constraint is listed more than once. The system is guaranteed to satisfy the two-category structural property described above.

## Output

If exactly **k** variables can be successfully selected to be True, print `YES` on the first line. On the second line, print the **k** distinct variable numbers that form your selection, separated by spaces. Any valid selection of **k** mutually constraint-abiding variables will be accepted.

If no such selection is possible, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```