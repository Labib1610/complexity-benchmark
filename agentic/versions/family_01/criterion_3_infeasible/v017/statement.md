# Production Line Diagnostics

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates continuously using exactly two production lines. Certain pairs of manufacturing steps require a shared specialized calibration tool and therefore cannot be assigned to the same production line. The current batch of manufacturing steps cannot be distributed across the two lines without causing at least one tool collision.

Your diagnostic software must isolate a root cause of this allocation failure by identifying a set of three steps where every pair within the set requires a shared tool. Such a trio forms an unresolvable bottleneck, as no two of these three steps can be placed on the same line.

To ensure deterministic logging, if multiple such unresolvable trios exist, the system must output the one whose step identifiers are sequentially lowest.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of manufacturing steps and the number of tool collision pairs. Steps are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that step $u$ and step $v$ cannot be assigned to the same production line.
It is guaranteed that at least one set of three steps, where every pair collides, exists in the provided data.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the identifiers of the three steps where every pair collides. Output the combination that is sequentially lowest (the smallest possible value for $a$; in case of a tie, the smallest possible value for $b$; and finally the smallest possible value for $c$).

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
