# Protocol Compliance Check

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ operating modules, indexed from $1$ to $n$. Due to power constraints, certain pairs of modules share a bidirectional mutual interference link.

An audit flag is raised if there exists a set of three distinct modules $a$, $b$, and $c$ such that a mutual interference link exists between every pair among them: between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

It is guaranteed that at least one such group of three modules exists. Output the triple of indices $a$, $b$, and $c$ satisfying $1 \le a < b < c \le n$ that is lexicographically smallest. That is, choose the valid triple that minimizes $a$; if there is a tie, minimize $b$; if still tied, minimize $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of operating modules and the number of mutual interference links.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a mutual interference link between module $u$ and module $v$. No unordered pair of modules is listed more than once.

It is guaranteed that at least one valid triple exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($1 \le a < b < c \le n$) representing the lexicographically smallest triple of mutually interfering modules.

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
