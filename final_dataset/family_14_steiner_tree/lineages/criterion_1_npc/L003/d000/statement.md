# Problem A — Synchronizing the Core Components

Time limit: 5 s   Memory limit: 256 MB

## Description

A system has **n** components (numbered 1..n). Certain pairs of components can be synchronized by establishing a shared protocol at a given cost. Among the components, **t** are **core** and must all end up synchronized with each other (either directly or transitively through intermediate components). The remaining components are supplemental: you may establish protocols with them if it lowers the overall total, or ignore them.

Establish a set of shared protocols of minimum total cost so that all core components are synchronized with one another. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the core components.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a shared protocol establishing synchronization between components u and v at cost w.
The available protocols are enough to synchronize all core components.

## Output

Print a single integer: the minimum total cost to synchronize all core components.

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

In Example 1, establishing synchronization through the supplemental component 4 (costs 1+1+1 = 3) is cheaper than synchronizing the three core components directly (which would cost 4). In Example 3 there is only one core component, so no protocols are needed.
