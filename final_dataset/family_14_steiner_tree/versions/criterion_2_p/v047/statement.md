# Problem B — Secure Fiber Provisioning

Time limit: 2 s
Memory limit: 256 MB

## Description

A corporate campus consists of **n** facilities. There are **m** potential fiber-optic trenches that can be activated. Each trench connects two distinct facilities and requires a specific installation cost. The full set of proposed trenches provides a connected network, meaning it is possible to route data between any two facilities if all trenches are activated.

The company has identified **t** critical facilities that must be able to share data with one another. Your objective is to select a subset of the proposed trenches to activate such that every critical facility can transmit data to every other critical facility (transmission may relay through any number of intermediate facilities, which do not themselves need to be critical).

To comply with network topology regulations, your selection must satisfy two additional requirements:
1. The activated subset of trenches must not contain any closed loops (a sequence of distinct trenches that starts and ends at the same facility).
2. The total number of activated trenches in your subset must be strictly less than **n**.

Determine the minimum total installation cost required to activate a valid subset of trenches meeting all requirements. If a critical facility is the only one (i.e., **t** = 1), the cost is 0.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers representing the identifiers of the critical facilities.
The following **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). This indicates a potential trench between facility **u** and facility **v** with an installation cost of **w**. It is guaranteed that activating all **m** trenches would fully connect the **n** facilities.

## Output

Output a single integer representing the minimum total installation cost to connect all critical facilities while satisfying the topology regulations.

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
