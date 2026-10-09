# Optimal Linear Unit Placement

Time limit: 5 s
Memory limit: 256 MB

## Description
You are tasked with optimizing the physical layout of a monitoring installation. There are $n$ distinct monitoring units that must be assigned to $n$ discrete mounting slots arranged in a single straight line. Each slot can hold exactly one unit. This means there are $n!$ possible spatial configurations to evaluate, as every permutation of units to slots produces a different layout.

The units communicate with each other through a set of $m$ dedicated reporting links. Each link connects a specific pair of units. When deployed, a link requires a physical cable whose length is strictly determined by the distance between the two units' assigned slots. Specifically, if two linked units are placed in slots $i$ and $j$, the cable length required for that link is $|i - j|$. 

Your goal is to search this space of permutations and find a configuration where the sum of the lengths of all cables does not exceed a strict total budget $B$. There are no individual limits on any single cable; only the aggregate sum matters. The $m$ links are structured such that every unit is reachable from any other, and there are exactly enough links to achieve this without forming any closed loops.

You must determine if any valid assignment exists within the budget $B$, and if so, provide one such configuration.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of units, the number of reporting links, and the total cabling budget, respectively.

The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that a reporting link exists between unit $u$ and unit $v$. It is guaranteed that $m = n - 1$.

## Output
If there is a valid placement, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer represents the slot position (from $1$ to $n$) assigned to unit $i$. This must be a permutation of the integers from $1$ to $n$.

If no such placement exists, print `NO`.

## Example

### Input
```
5 4 5
1 2
1 3
2 4
2 5
```

### Output
```
YES
4 2 5 1 3
```
