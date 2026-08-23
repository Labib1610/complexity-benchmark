# Facility Collision Protocol Analysis

Time limit: 2 s   Memory limit: 256 MB

A research station monitors system conflicts among $n$ operational units, numbered $1$ through $n$. There are $m$ recorded direct conflict links between pairs of distinct units. A direct conflict link between unit $u$ and unit $v$ means $u$ and $v$ cannot operate simultaneously in the same zone.

The control center needs to identify a triplet of three distinct units $a, b, c$ with $a < b < c$ that are mutually in conflict with each other—meaning there is a direct conflict link between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

It is guaranteed that at least one such triplet exists. If there are multiple valid triplets, select the lexicographically smallest triple $(a, b, c)$—that is, the one with the smallest $a$, breaking ties with the smallest $b$, and further ties with the smallest $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \ne v$), representing a direct conflict link between unit $u$ and unit $v$.
It is guaranteed that at least one valid triplet exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($a < b < c$) on a single line representing the lexicographically smallest triplet of mutually conflicting units.

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
