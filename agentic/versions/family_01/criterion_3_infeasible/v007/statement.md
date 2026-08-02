# Problem C — Frequency Audit

Time limit: 2 s   Memory limit: 256 MB

A telecommunication agency is auditing a network of $n$ broadcast stations, numbered $1$ through $n$. Due to signal overlap, certain pairs of stations interfere with one another and cannot operate on the same frequency channel.

The network operator claims that the entire network can operate using only two frequency channels without any interference. To disprove this claim, auditors need to locate three distinct stations that mutually interfere with each other—meaning every pair among the three has signal interference.

It is guaranteed that at least one such group of three mutually interfering stations exists in the network. Find the lexicographically smallest triple of station identifiers $(a, b, c)$ with $a < b < c$ such that $a$ interferes with $b$, $a$ interferes with $c$, and $b$ interferes with $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$) — the number of stations and the number of interfering pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that station $u$ and station $v$ interfere with each other. No interfering pair is listed more than once.
It is guaranteed that at least one mutually interfering triple exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$ representing the lexicographically smallest triple of mutually interfering stations (minimizing $a$; then $b$; then $c$).

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
