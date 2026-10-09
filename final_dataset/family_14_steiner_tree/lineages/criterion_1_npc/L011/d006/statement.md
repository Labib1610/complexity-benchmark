# Problem A — State Synchronization

Time limit: 5 s
Memory limit: 256 MB

## Description

You are analyzing a system of **n** state variables, numbered 1 to **n**. The system allows you to enforce equality constraints between specific pairs of variables. There are **m** possible equality constraints you can enforce. Enforcing a constraint between variable **u** and variable **v** ensures they hold the same value and incurs a one-time computational cost of **w**. Constraints are symmetric.

A subset of variables **S** is defined as a *strictly unified subset* if the constraints completely contained within **S** guarantee that all variables in **S** must hold the same value. Formally, for every possible way to partition **S** into two non-empty disjoint sets **X** and **Y** (such that **X** ∪ **Y** = **S**), there must be at least one enforced constraint that requires a variable in **X** to equal a variable in **Y**.

A new integrity policy requires that a designated group of **t** *essential* variables must all be part of the same strictly unified subset.

You may include any number of other non-essential variables in this subset if enforcing constraints involving them helps reduce the overall cost. Your task is to select a set of constraints to enforce such that there exists at least one strictly unified subset containing all **t** essential variables, while keeping the total computational cost of the enforced constraints to the absolute minimum.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).  
The second line lists **t** distinct integers representing the identifiers of the essential variables.  
Following this, there are **m** lines. Each line provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating that an equality constraint can be enforced between variable **u** and variable **v** for a computational cost of **w**.  
It is guaranteed that the available constraints provide at least one valid way to form a strictly unified subset containing all essential variables.

## Output

Output a single integer representing the minimum possible total computational cost required to satisfy the integrity policy.

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

In Example 1, enforcing the constraints between variable 4 and variables 1, 2, and 3 requires a total cost of 1 + 1 + 1 = 3. The subset **S** = {1, 2, 3, 4} forms a strictly unified subset. For instance, if we partition **S** into **X** = {1, 2} and **Y** = {3, 4}, the enforced constraint between 2 and 4 requires a variable in **X** to equal a variable in **Y**. Any valid partition of **S** will have at least one enforced constraint crossing between its two sets. This subset successfully contains the essential variables 1, 2, and 3. Utilizing variable 4 in the subset is more cost-effective than enforcing constraints exclusively among the essential variables, which would incur a cost of at least 4.

In Example 3, only one variable is designated as essential. A subset consisting of just this single variable (**S** = {1}) satisfies the condition for being strictly unified because it is impossible to partition a one-element set into two non-empty sets. This results in all variables in the set sharing the same value. Thus, zero constraints need to be enforced, resulting in a cost of 0.