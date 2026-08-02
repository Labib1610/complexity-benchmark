# High-Risk Clearance Conflicts

Time limit: 2 s   Memory limit: 256 MB

A security facility tracks clearance conflicts between $n$ personnel IDs, numbered $1$ through $n$. You are given a list of $m$ distinct pairs of personnel IDs that are directly in conflict with each other.

A critical security vulnerability arises whenever three personnel IDs form a mutually conflicting set. Specifically, you need to find three distinct IDs $a$, $b$, and $c$ satisfying $a < b < c$ such that:
- $a$ and $b$ are in conflict,
- $a$ and $c$ are in conflict, and
- $b$ and $c$ are in conflict.

It is guaranteed that at least one such set of three IDs exists in the system. If there are multiple such sets, find the lexicographically smallest triple $(a, b, c)$. That is, select the triple that minimizes $a$, breaks ties by minimizing $b$, and breaks further ties by minimizing $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \ne v$), indicating that personnel ID $u$ and personnel ID $v$ are directly in conflict.
It is guaranteed that at least one valid triple exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($a < b < c$) on a single line representing the lexicographically smallest set of three mutually conflicting personnel IDs.

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
