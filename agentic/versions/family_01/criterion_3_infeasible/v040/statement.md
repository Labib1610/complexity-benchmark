# Task Force Formation

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ personnel, numbered $1$ through $n$. Due to strict operational rules, certain pairs of personnel have direct cross-audit requirements. There are $m$ such pairwise relations.

A 3-person audit committee consists of three distinct personnel $a, b, c$ ($a < b < c$) such that every pair among them has a direct cross-audit requirement (that is, cross-audit requirements exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$). You need to find such a committee.

It is guaranteed that at least one valid 3-person audit committee exists. If multiple such committees exist, choose the one that is lexicographically smallest (smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$) representing a pairwise cross-audit requirement between worker $u$ and worker $v$.
It is guaranteed that at least one valid triple exists.

## Output
Print three integers $a\ b\ c$ on a single line with $a < b < c$ such that all three pairs $a\text{--}b$, $a\text{--}c$, and $b\text{--}c$ have cross-audit requirements. Output the lexicographically smallest such triple.

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
