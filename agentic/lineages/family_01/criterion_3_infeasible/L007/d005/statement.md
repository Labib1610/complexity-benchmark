# Redundant Access Protocol

Time limit: 2 s   Memory limit: 256 MB

A secure facility has $m$ dual-key locks. There are $n$ distinct keys available, numbered 1 through $n$. Each lock is configured so that it can only be opened by inserting a specific combination of exactly two distinct keys.

To establish a new "redundant access protocol", the security team must identify exactly three distinct keys $a$, $b$, and $c$ (with $a < b < c$) such that every possible pair formed from these three keys can open a lock. Specifically, there must be a lock configured for keys $a$ and $b$, a lock for keys $b$ and $c$, and a lock for keys $a$ and $c$.

With up to 2000 keys, the lock configurations are extensive. It is guaranteed that at least one such group of three keys exists. You must identify it.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that a lock requires key $u$ and key $v$. 
It is guaranteed that at least one valid group of three keys exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ that satisfy the redundant access protocol. 
If multiple valid groups exist, output the one with the smallest value for $a$; if there is a tie, choose the one with the smallest value for $b$; and if still tied, the smallest value for $c$.

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