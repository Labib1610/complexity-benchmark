# Problem A — Variable Unification

Time limit: 5 s
Memory limit: 256 MB

## Description

An algebraic system consists of **n** distinct variables, identified by integers from 1 to **n**. You are given a set of **m** allowed bidirectional unification operations. Each operation can unify a specific pair of variables, and applying it incurs a known computational penalty.

A theoretical framework requires that a specific subset of **t** variables—designated as *invariant variables*—must be reduced to the exact same algebraic value. Two variables are guaranteed to have the same value if they are directly unified, or if their identical value can be established transitively through a sequence of other unified variables.

When satisfying this framework, you are not restricted to only applying operations that involve the invariant variables. Any of the remaining non-invariant variables may be unified as intermediate steps; unifying them is entirely optional but may be advantageous if it reduces the overall computational penalty.

Your task is to select a subset of the allowed unification operations to apply such that all invariant variables are guaranteed to hold the same value, while keeping the total computational penalty of the selected operations to the absolute minimum.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).  
The second line lists **t** distinct integers representing the identifiers of the invariant variables.  
Following this, there are **m** lines. Each line provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating that a unification operation can be applied between variable **u** and variable **v** for a computational penalty of **w**.  
It is guaranteed that the allowed operations provide at least one valid way to unify all invariant variables.

## Output

Output a single integer representing the minimum possible total computational penalty required to satisfy the framework's requirement.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, applying the operations that unify variable 4 with variables 1, 2, and 3 requires a total penalty of 1 + 1 + 1 = 3. This successfully ensures the invariant variables (1, 2, and 3) share the same value. Utilizing variable 4 as a transitive intermediary is more cost-effective than applying operations solely among the invariant variables, which would incur a penalty of at least 4. 

In Example 3, only one variable is designated as invariant. Since no operations are needed to ensure a single variable shares a value with itself, zero operations are applied, resulting in a penalty of 0.