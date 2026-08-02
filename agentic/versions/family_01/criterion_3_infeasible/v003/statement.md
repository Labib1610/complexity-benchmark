# Problem C — Mutual Interference Certificate

Time limit: 2 s   Memory limit: 256 MB

A complex system consists of $n$ processing units numbered from $1$ to $n$. Certain pairs of units suffer from mutual hardware interference when operated together. You are given a list of $m$ unordered pairs of units that directly interfere with one another.

To certify that a specific operational configuration is impossible under two-frequency multiplexing, you must identify a set of three distinct units where every pair among them directly interferes with each other. 

It is guaranteed that at least one such group of three units exists. Your task is to find the lexicographically smallest triple $(a, b, c)$ with $a < b < c$ such that $a$ and $b$ interfere, $a$ and $c$ interfere, and $b$ and $c$ interfere. Lexicographically smallest means choosing the triple with the smallest possible value of $a$; if there is a tie, choosing the one with the smallest $b$; if there is still a tie, choosing the one with the smallest $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \ne v$), indicating that units $u$ and $v$ directly interfere with each other.
It is guaranteed that at least one such mutually interfering triple exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the lexicographically smallest triple of mutually interfering units.

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
