# Network Overlap Audit

Time limit: 2 s   Memory limit: 256 MB

A data center monitors $n$ processing nodes, numbered $1$ to $n$, and tracks direct links between them. A set of $m$ distinct bidirectional links is recorded.

An investigation requires finding three nodes $a, b, c$ ($a < b < c$) that form a fully interconnected group—meaning direct links exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

It is guaranteed that at least one such group of three nodes exists in the system. Find and report the lexicographically smallest triple $(a, b, c)$ satisfying this property (i.e., smallest $a$; if tied, smallest $b$; if still tied, smallest $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a direct bidirectional link between node $u$ and node $v$.

It is guaranteed that at least one fully interconnected group of three nodes exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$ representing the lexicographically smallest triple of mutually connected nodes.

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
