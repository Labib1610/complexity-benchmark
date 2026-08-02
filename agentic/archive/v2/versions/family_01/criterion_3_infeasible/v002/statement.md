# Problem C — Signal Interference Audit

Time limit: 2 s   Memory limit: 256 MB

A telecom provider operates $n$ wireless relay stations, numbered $1$ to $n$. Due to overlapping frequency bands, certain pairs of stations experience mutual signal interference.

An audit requires identifying three distinct stations that all mutually interfere with one another—meaning every pair among the three interferes. It is guaranteed that at least one such set of three mutually interfering stations exists.

Your task is to find one such set.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of relay stations and the number of interfering pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that relay stations $u$ and $v$ mutually interfere.
It is guaranteed that at least one such set of three stations exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line with $a < b < c$ such that station $a$ interferes with $b$, $a$ interferes with $c$, and $b$ interferes with $c$.
Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
