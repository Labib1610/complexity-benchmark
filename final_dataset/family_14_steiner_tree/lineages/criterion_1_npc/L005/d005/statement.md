# Problem A — Constraint Activation

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a formal verification model consisting of **n** unknown integer variables, $x_1, x_2, \ldots, x_n$.

Within this model, a specific subset of **t** variables are designated as *focal variables*. Your objective is to guarantee that all **t** focal variables must take the exact same value. 

To do this, you can activate a selection of optional equality constraints. You are provided with a list of **m** available constraints. Each constraint specifies that two variables, $x_u$ and $x_v$, are equal ($x_u = x_v$). Activating this constraint incurs a computational cost of **w**. 

You may choose any combination of the available constraints to activate, paying the sum of their costs. Your chosen subset of constraints must logically entail that all **t** focal variables are equal. Specifically, in every possible assignment of integers to $x_1, \ldots, x_n$ that satisfies all of your activated constraints, the **t** focal variables must evaluate to the identical value.

You are permitted to activate constraints involving variables outside the focal set if they provide a more cost-effective way to establish the required entailment.

Determine the minimum total cost of a subset of constraints that logically guarantees all **t** focal variables are equal.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the indices of the focal variables.
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000). These represent an available constraint $x_u = x_v$ that can be activated for a cost of **w**.
It is guaranteed that it is possible to ensure all focal variables are equal using the available constraints.

## Output

Output a single integer representing the minimum total cost to logically guarantee that all **t** focal variables are equal.

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

In Example 1, activating the three constraints $x_1 = x_4$, $x_2 = x_4$, and $x_3 = x_4$ (total cost 1+1+1 = 3) logically entails that $x_1 = x_2 = x_3$. This is cheaper than activating constraints directly between the focal variables (which would cost 2+2=4). 
In Example 3, there is only one focal variable. It is vacuously guaranteed to equal itself, so no constraints need to be activated.