# Minimal Bottleneck Diagnostic

Time limit: 2 s   Memory limit: 256 MB

An automated control system coordinates $n$ operational units, numbered $1$ through $n$. Due to physical signal overlap, certain pairs of units suffer from severe mutual interference and cannot be active concurrently. The control log contains $m$ recorded interference pairs.

To diagnose multi-unit scheduling deadlocks across the entire system architecture, the diagnostic monitor searches for minimal cyclic interference patterns. Specifically, a group of three distinct units where every pair within the group interferes with each other represents a fundamental localized bottleneck.

Your task is to identify one such bottleneck: a tuple of unit identifiers $(a, b, c)$ with $a < b < c$ such that all three pairwise links—$(a, b)$, $(a, c)$, and $(b, c)$—are present in the interference registry. If several such tuples exist, you must output the lexicographically smallest one (minimizing $a$, breaking ties by minimizing $b$, and then $c$).

It is guaranteed that at least one such mutually interfering three-unit group exists in the input.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) indicating an interference link between unit $u$ and unit $v$.
It is guaranteed that at least one mutually interfering three-unit group exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line ($a < b < c$) representing the lexicographically smallest mutually interfering tuple.

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
