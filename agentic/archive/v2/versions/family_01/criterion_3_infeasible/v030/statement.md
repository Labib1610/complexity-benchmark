# Frequency Interference Analysis

Time limit: 2 s   Memory limit: 256 MB

## Description
Consider a monitoring facility tracking $n$ active signal channels, numbered from $1$ through $n$. Due to overlapping frequency bands, certain pairs of channels experience severe mutual interference.

A system log records $m$ distinct unordered pairs of channels that interfere with each other. A critical fault mode occurs when three distinct channels $a$, $b$, and $c$ form a fully interconnected group—that is, channel $a$ interferes with $b$, channel $a$ interferes with $c$, and channel $b$ interferes with $c$.

Your task is to identify one such fault group of three channels. If multiple such groups exist, report the triple $(a, b, c)$ with $1 \le a < b < c \le n$ that is lexicographically smallest (minimizing $a$ first; if tied, minimizing $b$; if still tied, minimizing $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of signal channels and the total number of interference pairs.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating a mutual interference pair between channel $u$ and channel $v$.

It is guaranteed that no pair is reported more than once and that at least one such group of three mutually interfering channels exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line separated by spaces such that $a < b < c$ and all three channel pairs $(a, b)$, $(a, c)$, and $(b, c)$ are present in the interference log. Output the lexicographically smallest triple under the tie-breaking rule.

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
