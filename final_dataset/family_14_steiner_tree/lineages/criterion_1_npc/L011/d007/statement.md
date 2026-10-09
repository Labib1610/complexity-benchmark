# Problem A — State Synchronization

Time limit: 5 s
Memory limit: 256 MB

## Description

You are analyzing a system of **n** state variables, numbered 1 to **n**. The system allows you to enforce equality constraints between specific pairs of variables. There are **m** possible equality constraints you can enforce. Enforcing a constraint between variable **u** and variable **v** ensures they hold the same value and incurs a one-time computational cost of **w**. Constraints are symmetric.

A new integrity policy requires that a designated group of **t** *essential* variables must all be synchronized. You may include any number of other non-essential variables to act as intermediaries if it helps reduce the overall cost. 

Specifically, you must select a subset of variables **S** and a specific set of constraints **C** between variables in **S** to enforce. Your selection is valid if and only if it satisfies all of the following policy rules:
1. **Inclusion:** **S** must contain all **t** essential variables.
2. **Strict Unification:** The constraints in **C** must completely unify **S**. Formally, for every possible way to partition **S** into two non-empty disjoint sets **X** and **Y**, **C** must contain at least one constraint that requires a variable in **X** to equal a variable in **Y**.
3. **Minimal Dependency:** To prevent redundant synchronization cycles, the number of enforced constraints in **C** must be exactly one less than the total number of variables in **S** (i.e., $|C| = |S| - 1$).
4. **Intermediary Justification:** Every non-essential variable included in **S** must act as a true intermediary. Therefore, any non-essential variable in **S** must be directly involved in at least two constraints within **C**.

Your task is to find a valid selection of **S** and **C** that satisfies all policy rules while keeping the total computational cost of the enforced constraints in **C** to the absolute minimum.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).  
The second line lists **t** distinct integers representing the identifiers of the essential variables.  
Following this, there are **m** lines. Each line provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating that an equality constraint can be enforced between variable **u** and variable **v** for a computational cost of **w**.  
It is guaranteed that the available constraints provide at least one valid way to satisfy the policy for all essential variables.

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

In Example 1, enforcing the constraints between variable 4 and variables 1, 2, and 3 requires a total cost of 1 + 1 + 1 = 3. We select **S** = {1, 2, 3, 4} and **C** containing those three constraints. This satisfies all policy rules:
1. **Inclusion:** **S** contains all 3 essential variables (1, 2, and 3).
2. **Strict Unification:** The constraints strictly unify **S**. For instance, partitioning **S** into **X** = {1, 2} and **Y** = {3, 4} is bridged by the enforced constraint between 2 and 4.
3. **Minimal Dependency:** The number of constraints in **C** is 3, which is exactly $|S| - 1$ (4 - 1).
4. **Intermediary Justification:** The only non-essential variable in **S** is 4, which is involved in 3 constraints, satisfying the requirement of being involved in at least 2.

Utilizing variable 4 is more cost-effective than enforcing constraints exclusively among the essential variables, which would incur a cost of at least 4.

In Example 3, only one variable is designated as essential. We select **S** = {1} and **C** as an empty set of constraints. 
1. **Inclusion:** **S** contains the 1 essential variable.
2. **Strict Unification:** **S** is strictly unified because it is impossible to partition a one-element set into two non-empty sets.
3. **Minimal Dependency:** The number of constraints is 0, which is exactly $|S| - 1$ (1 - 1).
4. **Intermediary Justification:** There are no non-essential variables in **S**, so this rule is vacuously satisfied.

Thus, zero constraints need to be enforced, resulting in a cost of 0.