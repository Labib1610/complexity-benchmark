# Problem C — Tri-Resonance

Time limit: 2 s   Memory limit: 256 MB

A communication system utilizes $n$ frequency bands. During testing, $m$ specific unordered pairs of bands were flagged as producing cross-talk when active simultaneously. 

For any subset of bands $S$, let $C(S)$ be the number of flagged pairs whose elements both belong to $S$. 
The engineers need to identify a tri-resonance, which is defined as a subset $S$ of exactly three distinct bands such that $C(S) = 3$. 

With up to 2000 bands, there are over a billion possible 3-band subsets to evaluate. You must efficiently search the space to find one tri-resonant subset. It is guaranteed that the system is flawed and at least one such subset exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that the pair of bands $\{u, v\}$ produces cross-talk. 
It is guaranteed that at least one tri-resonant subset exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the bands in a tri-resonant subset. 
If multiple valid subsets exist, output the one with the smallest value for $a$; if there is a tie, choose the one with the smallest value for $b$; and if still tied, the smallest value for $c$.

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