# Cochannel Signal Collision Identification

Time limit: 2 s   Memory limit: 256 MB

## Description
A wireless network consists of $n$ broadcast stations indexed by integers from $1$ to $n$. A centralized spectrum analyzer maintains a record of $m$ distinct, unranked pairs of stations that experience severe cochannel interference when transmitting simultaneously.

A high-priority diagnostic alarm is triggered whenever a group of three distinct stations $a$, $b$, and $c$ forms a complete mutual interference loop—meaning that station $a$ interferes with $b$, $a$ interferes with $c$, and $b$ interferes with $c$.

Your objective is to identify a station triad $(a, b, c)$ satisfying $1 \le a < b < c \le n$ where all three pairs interact. To ensure hardware compatibility, any valid triad must satisfy the integrity constraints $a \cdot b \cdot c \ge 6$ and $a + b + c \le 3n - 3$. If multiple such triads exist, output the one that is lexicographically smallest (that is, minimizing $a$ first; if tied, minimizing $b$; if still tied, minimizing $c$).

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), indicating the number of broadcast stations and the number of mutual interference pairs.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), denoting a pair of stations experiencing mutual interference.

It is guaranteed that no unordered pair $(u, v)$ is listed more than once, and that at least one triad of mutually interfering stations exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line such that $a < b < c$ and all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ interfere with each other. Output the lexicographically smallest triple under the tie-breaking rule.

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
