# Operational Conflict Triad

Time limit: 2 s   Memory limit: 256 MB

A processing facility manages $n$ active materials, numbered $1$ through $n$. Operational guidelines list $m$ specific pairs of materials that trigger a critical reaction if placed together in the same containment vessel.

An auditor needs to document an irreconcilable conflict set consisting of three distinct materials $a, b,$ and $c$ (with $a < b < c$) such that every pair among the three is subject to a critical reaction when combined.

Among all valid choices of $(a, b, c)$, you must find the one that is lexicographically smallest. That is, choose the triple with the smallest index $a$; if there is a tie, the smallest index $b$; if still tied, the smallest index $c$. It is guaranteed that at least one such triple exists.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of materials and the number of conflicting pairs, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that a critical reaction exists between material $u$ and material $v$.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($a < b < c$) on a single line representing the lexicographically smallest triple of mutually conflicting materials.

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
