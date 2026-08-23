# Fluid Routing

Time limit: 1 s   Memory limit: 256 MB

A hydraulic system contains $n$ control valves, numbered 1 to $n$. Each valve must be attached to exactly one of two available pressure manifolds, labeled 1 and 2. 

To prevent pressure surges, the installation includes $m$ cross-link tubes. Each cross-link tube joins a specific pair of valves. For a cross-link to function safely, the two valves it joins must be attached to different manifolds. 

Your task is to assign each valve to a manifold such that all cross-link requirements are satisfied. When multiple valid routing configurations exist, you must output the one that produces the lexicographically smallest sequence of manifold choices $s_1, s_2, \dots, s_n$ (prioritizing manifold 1 for lower-numbered valves whenever possible). If no such configuration is physically possible, you must report this.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of valves joined by a cross-link tube.

## Output
If no valid configuration can be established, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid manifold assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```