# Problem C — Safety Audit Certificate

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility maintains a registry of $n$ personnel, labeled from $1$ to $n$. Due to operational hazards, certain pairs of personnel have an active safety restriction preventing them from being assigned to the same area.

A safety audit requires identifying a mutual conflict trio: a set of three distinct personnel members $a$, $b$, and $c$ such that an active safety restriction is recorded between every pair among the three (that is, between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$).

It is guaranteed that at least one such trio exists in the registry. Among all valid trios $(a, b, c)$ satisfying $a < b < c$, determine the one that is lexicographically smallest (minimizing $a$, then $b$, then $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of personnel and the number of active safety restrictions, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a mutual safety restriction between personnel $u$ and personnel $v$. No pair of personnel is listed more than once.

It is guaranteed that at least one valid trio exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $1 \le a < b < c \le n$ such that safety restrictions exist for $a$–$b$, $a$–$c$, and $b$–$c$. Output the lexicographically smallest such triple.

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
