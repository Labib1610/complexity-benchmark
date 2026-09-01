# Problem A — Phase Resonance Protocol

Time limit: 2 s
Memory limit: 256 MB

A quantum communication grid consists of $n$ signal emitters (numbered 1 through $n$). To initialize the grid, each emitter must be assigned a discrete phase state: 1, 2, or 3. 

The grid infrastructure includes $m$ physical conduits, each of which bridges a specific pair of emitters. These conduits introduce a strict operational constraint: for any two emitters bridged by a conduit, the absolute difference between their assigned phase states must be strictly greater than zero to prevent a resonance cascade. You must determine a phase state assignment for all $n$ emitters that satisfies this condition for every conduit.

If no safe assignment is possible, you must indicate that the grid cannot be initialized. If multiple safe assignments exist, the protocol requires you to select the one that is lexicographically smallest. (Assignment $A$ is lexicographically smaller than assignment $B$ if, at the lowest emitter index where they differ, $A$ has a lower phase state value than $B$).

## Input
The first line contains two integers $n$ and $m$ — the number of emitters and the number of conduits (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n(n−1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$, $u \neq v$), representing the identifiers of two emitters bridged by a conduit.

## Output
If the grid cannot be initialized without a resonance cascade, output a single line containing `NO`.
If a safe assignment exists, output `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the phase state for each emitter from 1 to $n$. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```