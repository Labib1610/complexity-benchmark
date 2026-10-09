# Problem B — Logical Harmonization

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a constraint satisfaction engine that manages **n** distinct integer variables, labeled 1 to **n**. You are given a list of proposed equality constraints. Each constraint, if enforced, guarantees that a specific pair of variables will always hold the identical value. The full list of proposed constraints is comprehensive enough that, if every single one were active, all **n** variables would be forced to share one identical value.

Within this system, a subset of **t** variables are designated as **observable variables**. Your objective is to enforce a subset of the proposed constraints such that all observable variables are logically guaranteed to take the same value as one another. This guarantee can be established directly by enforcing a constraint between two observable variables, or transitively through a series of enforced constraints involving other variables (which might not be observable variables themselves).

Enforcing each proposed constraint requires a specific amount of computational overhead. Determine the minimum total overhead required to enforce a valid subset of constraints that logically binds all observable variables to the same value.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the labels of the observable variables.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that an equality constraint can be enforced between variable **u** and variable **v** with a computational overhead of **w**.

## Output

Output a single integer representing the minimum total computational overhead needed to ensure all observable variables are guaranteed to hold the same value.

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