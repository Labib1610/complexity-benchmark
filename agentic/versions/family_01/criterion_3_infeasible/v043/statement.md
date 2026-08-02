# Mutual Interference Certificate

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ processing modules labeled $1$ through $n$. Between certain pairs of modules, direct cross-talk interference occurs when both modules are active. You are provided with a list of $m$ distinct unordered pairs of modules that experience this direct cross-talk.

An operational safety audit requires identifying three distinct modules $a, b, c$ with $a < b < c$ such that every pair among them directly interferes with one another—that is, direct cross-talk occurs between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

Among all valid triples $(a, b, c)$ satisfying this condition, you must determine the one that is lexicographically smallest. Lexicographically smallest means choosing a triple that minimizes $a$; in case of a tie, minimizes $b$; and if a tie still remains, minimizes $c$.

It is guaranteed that at least one such mutually interfering triple exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \ne v$), indicating that modules $u$ and $v$ directly interfere with each other.
It is guaranteed that at least one mutually interfering triple exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line separated by spaces ($a < b < c$), representing the lexicographically smallest triple of mutually interfering modules.

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
