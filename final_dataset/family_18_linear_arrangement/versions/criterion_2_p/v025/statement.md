# Linear Rail Module Integration

Time limit: 5 s
Memory limit: 256 MB

## Description
An engineering team is installing $n$ processing modules along a single straight rail. The rail has $n$ mounting bays, numbered $1$ through $n$. Each module must be assigned to exactly one bay, such that no two modules share a bay.

The modules must communicate to maintain system stability. There are $m$ communication tethers, each connecting a specific pair of modules. The communication network is built as a minimal integrated framework: it connects all modules together into a single unified grid, and contains absolutely no redundant pathways (removing any tether would isolate some modules from others).

The signal degradation over a tether is proportional to the physical distance between its two modules. Specifically, if a tether connects a module in bay $x$ and a module in bay $y$, its degradation is $|x - y|$. The team has a maximum allowable total degradation of $B$, which is the sum of the degradations of all $m$ tethers.

To ensure compliance with safety regulations, the input configurations are guaranteed to satisfy two additional structural conditions:
1. The modules can be partitioned into two distinct sets such that every tether connects a module in the first set to a module in the second set.
2. The total number of modules that are connected to an odd number of tethers is an even number.

Determine a valid bay assignment for all $n$ modules such that the total degradation does not exceed $B$. If no such assignment is possible, report that it cannot be done.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, representing a tether between module $u$ and module $v$.
(It is guaranteed that $m = n - 1$).

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer is the bay number (from $1$ to $n$) assigned to module $i$. If multiple valid assignments exist, any assignment that satisfies the total degradation limit is acceptable.
If no such assignment is possible, print `NO`.

## Example
**Input:**
```text
5 4 6
1 2
1 3
1 4
1 5
```

**Output:**
```text
YES
3 1 2 4 5
```
