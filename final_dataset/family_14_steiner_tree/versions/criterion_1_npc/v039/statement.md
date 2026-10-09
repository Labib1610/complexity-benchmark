# Problem A — Synchronizing the Critical Substations

Time limit: 5 s   Memory limit: 256 MB

## Description

A disaster recovery team manages a regional power grid consisting of **n** substations (numbered 1..n). Certain pairs of substations can be linked by restoring a transmission line at a given cost in labor hours. Among the substations, **t** serve critical hospitals and must all end up synchronized to each other through the transmission lines you restore (directly or through intermediate substations). The remaining substations are optional relays: you may route the synchronized grid through them if it reduces the total labor hours, or leave them inactive.

Determine a set of transmission lines to restore of minimum total cost so that all critical substations are synchronized. Report that minimum total cost.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the critical substations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a transmission line linking substations u and v at a cost of w labor hours.
The available lines are sufficient to synchronize all critical substations.

## Output

Print a single integer: the minimum total cost to synchronize all critical substations.

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

In Example 1, routing the synchronized grid through the optional relay substation 4 (costs 1+1+1 = 3) is cheaper than linking the three critical substations directly (which would cost 4). In Example 3 there is only one critical substation, so no lines need to be restored.
