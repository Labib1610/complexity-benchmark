# Problem C — Stellar Resonance

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a star system containing $n$ celestial bodies, identified by integers from 1 to $n$. Our observation logs indicate $m$ instances of gravitational resonance. Each instance of resonance occurs between a specific pair of celestial bodies and affects them symmetrically.

Theoretical models suggest that the system is unstable because it contains at least one set of three distinct bodies where every possible pair within those three is in resonance. 

Your task is to pinpoint three bodies that exhibit this mutual resonance. If there are multiple such sets of three bodies, you must report the one that is lexicographically first.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1) / 2, 2 \cdot 10^5)$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of celestial bodies that are in resonance. 
It is guaranteed that at least one mutually resonating set of three bodies exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are in resonance. Output the lexicographically smallest such set of three (smallest $a$; ties by smallest $b$; then smallest $c$).

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
