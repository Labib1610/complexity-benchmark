# Problem C — Server Loop Analysis

Time limit: 2 s   Memory limit: 256 MB

A high-availability computing network consists of $n$ servers numbered $1$ through $n$, connected by $m$ direct two-way communication links. Each link directly connects two distinct servers.

A diagnostic protocol requires identifying a tightly interconnected cluster of three servers: three distinct servers $a$, $b$, and $c$ such that every pair among them is directly connected by a communication link (that is, direct links exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$).

It is guaranteed that at least one such three-server cluster exists in the network.

Find the valid triple $a, b, c$ with $a < b < c$ that is lexicographically smallest. That is, choose the triple that minimizes $a$; if there is a tie, minimizes $b$; if there is still a tie, minimizes $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of servers and the number of communication links, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a direct two-way communication link between server $u$ and server $v$.
It is guaranteed that at least one valid triple exists.

## Output
Print three space-separated integers $a\ b\ c$ on a single line with $a < b < c$, representing the lexicographically smallest triple of servers where all three pairwise direct links exist.

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
