# Problem C — Ternary Cascade

Time limit: 2 s
Memory limit: 256 MB

In a chemical processing plant, certain pairs of substances will undergo a dangerous reaction if stored near each other. The plant's standard dual-containment bins can safely isolate any two reactive substances. However, this isolation method breaks down entirely if a "ternary cascade" occurs. A ternary cascade is defined as a set of three distinct substances where every possible pair among the three is reactive.

Your job is to identify a ternary cascade to prove that the current safety measures are inadequate. You are provided with a complete list of all interacting pairs (each listed pair represents a dangerous interaction). 

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of substances and the total number of interacting pairs. Substances are labeled from 1 to n.
Each of the next m lines contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v), denoting that substance u and substance v interact.
It is guaranteed that at least one set of three distinct substances exists such that all three pairwise interact.

## Output
Output three integers a, b, and c on a single line, separated by spaces, representing the labels of the substances involved in a ternary cascade. The labels must be printed in strictly increasing order (a < b < c).
If multiple ternary cascades exist, you must output the one that is lexicographically smallest. This means you must minimize a; if there is a tie, minimize b; and if there is still a tie, minimize c.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```