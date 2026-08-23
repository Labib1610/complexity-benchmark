# Multi-Facility Synchronous Triad

Time limit: 2 s   Memory limit: 256 MB

A research consortium consists of $n$ distinct facilities, indexed from $1$ to $n$. Across the consortium, certain pairs of facilities maintain a direct, two-way data-sharing channel.

The organization needs to form a three-way audit panel consisting of three distinct facilities $a$, $b$, and $c$ (with indices satisfying $1 \le a < b < c \le n$) such that every pair of facilities within the panel has an active direct channel—meaning a channel exists between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

It is guaranteed that at least one such three-facility panel exists. If there are multiple valid sets of three facilities, select the triple $(a, b, c)$ that is lexicographically smallest. That is, choose the triple that minimizes $a$; if tied, minimizes $b$; if still tied, minimizes $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of facilities and the number of direct data-sharing channels, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a direct two-way channel between facility $u$ and facility $v$.

No pair of facilities is listed more than once in the input. At least one valid triple exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line, where $1 \le a < b < c \le n$, representing the lexicographically smallest triple of mutually connected facilities.

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
