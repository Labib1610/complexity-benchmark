# Shift Certificate Audit

Time limit: 2 s   Memory limit: 256 MB

A facility operates two non-overlapping work periods. Each employee is assigned to exactly one period. However, certain pairs of employees cannot be assigned to the same period due to operational restrictions.

Management needs to document why two work periods are strictly insufficient for the current set of employee restriction requirements. To do this, you must identify three employees who all mutually restrict one another. Because every pair among these three employees cannot share a period, no two-period allocation can accommodate all three of them simultaneously.

Among all valid groups of three mutually restricting employees, find the one that is lexicographically smallest. That is, if the three employee identifiers are listed in ascending order $a < b < c$, choose the triple that minimizes $a$ first, then $b$, and finally $c$.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1) / 2, 2 \cdot 10^5)$), representing the number of employees (numbered $1$ through $n$) and the total number of pairwise restrictions, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that employee $u$ and employee $v$ cannot share the same work period. Each restriction pair is listed at most once.

It is guaranteed that at least one such group of three mutually restricting employees exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$ such that all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are pairwise restrictions. Output the lexicographically smallest such triple (minimizing $a$, then $b$, then $c$).

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
