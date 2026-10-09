# Problem A — Policy Consistency Enforcement

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a compliance policy for a system with $n$ distinct settings, indexed from 1 to $n$. Each setting can be toggled to either 'Enabled' or 'Disabled'. A complete system state is defined by the toggle values of all $n$ settings.

A specific set of $t$ settings are designated as *critical controls*. Your security objective is to ensure that in any permissible system state, all critical controls share the exact same toggle value (i.e., they are either all 'Enabled' or all 'Disabled').

To enforce this, you can implement *dependency constraints* from a provided vendor catalog. Each constraint in the catalog is defined by two settings, $u$ and $v$, and it dictates that setting $u$ and setting $v$ must have identical toggle values. A system state is considered permissible if it satisfies every constraint you have implemented.

You are given a list of $m$ available dependency constraints, each with an associated implementation cost. You need to select a subset of these constraints to implement such that any permissible system state is mathematically guaranteed to have uniform values across all $t$ critical controls.

Calculate the minimum total cost to implement a subset of constraints that achieves this security objective.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ t ≤ 10). The integer **t** is the number of critical controls.
The second line provides **t** distinct integers representing the indices of the critical controls.
The subsequent **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing an available constraint between setting **u** and setting **v** that costs **w** to implement.
It is guaranteed that implementing all available constraints would be sufficient to enforce the security objective.

## Output

Print a single integer: the minimum total cost to implement a valid subset of constraints.

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

In Example 1, implementing the constraints between settings (1, 4), (2, 4), and (3, 4) incurs a total cost of 1+1+1 = 3. Any permissible system state satisfying these three constraints must have setting 1 match setting 4, setting 2 match setting 4, and setting 3 match setting 4. Consequently, settings 1, 2, and 3 will all match setting 4, meaning they all share the exact same toggle value. This fulfills the security objective for the critical controls {1, 2, 3}. This is more economical than implementing a subset of constraints that does not involve setting 4 (which would cost at least 4).

In Example 3, there is only a single critical control. The security objective that all critical controls share the same toggle value is vacuously satisfied for any system state. Thus, an empty subset of constraints can be selected, resulting in a cost of 0.