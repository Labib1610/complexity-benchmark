# Minimal Incompatibility Certificate

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility manages $n$ personnel units under strict operational safety guidelines. The management tracks $m$ pairwise non-coexistence conditions between units.

To formally demonstrate that dividing the workforce into just two distinct shifts is impossible, one must present a 3-element certificate: a subset of three units where every pair within the subset shares an explicit non-coexistence condition. Out of all $\binom{n}{3}$ possible combinations, your goal is to find the lexicographically smallest triplet $(a, b, c)$ that satisfies this criteria.

It is guaranteed that at least one such triplet exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) representing a non-coexistence condition between unit $u$ and unit $v$.
It is guaranteed that at least one valid certificate triplet exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$ representing the lexicographically smallest certificate triplet (minimizing $a$; breaking ties by smallest $b$; then by smallest $c$).

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
