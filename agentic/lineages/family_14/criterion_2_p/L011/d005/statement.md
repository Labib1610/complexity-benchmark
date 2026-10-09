# Problem B — Cohesive Subset Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system of **n** modules, numbered 1 to **n**. You are given a list of **m** pairwise synergies between these modules. Each synergy involves two distinct modules and has a positive weight.

The **m** synergies are structured such that the entire system of **n** modules is fully *cohesive*. A subset of modules $K$ is defined as *cohesive* if, for every proper, non-empty subset $A \subset K$, there is at least one synergy that involves one module in $A$ and one module in $K \setminus A$. (A subset consisting of a single module has no such subsets $A$, and is inherently cohesive).

A specific set of **t** modules are designated as **critical modules**. Your objective is to select a subset of modules, called the **active subset**, satisfying the following conditions:
1. The active subset must include all **t** critical modules.
2. The active subset itself must be *cohesive*.

When you select the active subset, you trigger exactly those synergies that have BOTH of their modules within the active subset. Synergies that have one or zero modules in the active subset are not triggered.

The total cost of your selection is the sum of the weights of all triggered synergies. Determine the minimum total cost required to form a valid active subset.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the labels of the critical modules.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a synergy between module **u** and module **v** with a weight of **w**.

## Output

Output a single integer representing the minimum total cost of the triggered synergies.

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