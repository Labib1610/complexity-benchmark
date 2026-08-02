# Industrial Shift Allocation Diagnostic

Time limit: 2 s   Memory limit: 256 MB

An industrial facility manages $n$ employees, assigned IDs from $1$ to $n$. A roster of pairwise conflicts prevents certain pairs of workers from sharing the same work shift.

The plant management wants to diagnose scheduling bottlenecks by finding a mutually conflicting trio: a set of three distinct employees where a direct conflict rule exists between every pair among them.

Given the list of pairwise conflict rules, find the triplet of IDs $(a, b, c)$ with $1 \le a < b < c \le n$ such that all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are recorded conflicts, and $(a, b, c)$ is lexicographically smallest (minimizing $a$, breaking ties by minimizing $b$, and then $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of workers and the number of recorded conflict rules, respectively.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a mutual conflict between worker $u$ and worker $v$.
It is guaranteed that at least one such triplet of mutually conflicting workers exists in the input.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line ($1 \le a < b < c \le n$) identifying the lexicographically smallest triplet where every pair among $a$, $b$, and $c$ has an explicit conflict restriction.

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
