# Problem C — Mutual Interference Certificate

Time limit: 2 s   Memory limit: 256 MB

A high-performance computing facility manages $n$ processing nodes labeled from $1$ to $n$. Due to signal cross-talk, specific pairs of nodes exhibit dual-way interference whenever both are active. You are given a list of $m$ distinct pairs of nodes that suffer from direct interference.

A stability failure occurs whenever three distinct nodes $a$, $b$, and $c$ are chosen such that every pair among them experiences direct interference. To log the earliest potential stability failure, you must locate the lexicographically smallest triple $(a, b, c)$ satisfying $1 \le a < b < c \le n$ where nodes $a$ and $b$ interfere, nodes $a$ and $c$ interfere, and nodes $b$ and $c$ interfere.

Lexicographical comparison requires minimizing $a$ first; if multiple valid triples share the same $a$, choose the one that minimizes $b$; if ties still remain, choose the one that minimizes $c$. It is guaranteed that at least one such mutually interfering triple exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \ne v$), denoting that nodes $u$ and $v$ directly interfere with each other. No pair of nodes is listed more than once.
It is guaranteed that at least one triple of mutually interfering nodes exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($a < b < c$) representing the lexicographically smallest triple of mutually interfering nodes.

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
