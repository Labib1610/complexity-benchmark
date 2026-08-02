# Transmitter Cross-Talk Audit

Time limit: 2 s   Memory limit: 256 MB

A regulatory body is conducting an audit of $n$ radio transmitters, indexed from $1$ to $n$. A set of $m$ pair-wise signal overlaps has been recorded; each overlap indicates that a specific pair of transmitters experiences mutual cross-talk and cannot operate on the same frequency channel.

The network provider claims that the entire network can be successfully operated using only two distinct frequency channels. The compliance team aims to refute this claim by identifying three distinct transmitters that all experience mutual cross-talk with one another—meaning every pair among these three transmitters overlaps.

At least one such mutual cross-talk triplet is guaranteed to exist in the recorded network data. To standardise compliance reports, you must locate the lexicographically smallest triplet of transmitter indices $(a, b, c)$ satisfying $a < b < c$ such that cross-talk occurs between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$) — the number of transmitters and the number of overlapping pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a cross-talk relationship between transmitter $u$ and transmitter $v$. No overlapping pair is listed more than once.
It is guaranteed that at least one triplet of mutually overlapping transmitters exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line ($a < b < c$) representing the lexicographically smallest triplet of mutually overlapping transmitters (minimizing $a$; then $b$; then $c$).

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
