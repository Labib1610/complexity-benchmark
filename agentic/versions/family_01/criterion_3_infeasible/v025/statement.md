# Platform Mutual Audit Group

Time limit: 2 s   Memory limit: 256 MB

A computer network consists of $n$ servers, numbered $1$ through $n$. Certain pairs of servers share a direct bidirectional link.

Security policies require identifying a group of three servers that are all directly linked to one another—that is, three distinct servers where every pair within the group shares a direct link. You are guaranteed that at least one such group of three servers exists in the network.

Your goal is to find the triple of server indices $(a, b, c)$ with $1 \le a < b < c \le n$ such that direct links exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

To standardize reporting, if there are multiple such triples, choose the one that is lexicographically smallest. That is, choose the triple that minimizes $a$; if there is a tie, minimize $b$; if still tied, minimize $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of servers and the number of direct links, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) indicating a direct bidirectional link between server $u$ and server $v$.

No pair of servers is listed more than once. It is guaranteed that at least one valid triple exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the lexicographically smallest triple of mutually linked servers.

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
