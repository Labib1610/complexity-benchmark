# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The factory still has only two shifts, 1 and 2, but the roster is known to be hopeless. Your job is not to schedule — it is to certify the impossibility. It is guaranteed that there exists at least one group of three workers where every pair among those three is listed as an incompatible pair. Any such trio proves two shifts cannot suffice. Find and output the lexicographically smallest such trio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ $v$ ($1 \le u, v \le n$, $u \neq v$) representing an incompatible pair of workers.
It is guaranteed that at least one mutually incompatible trio exists.

## Output
Print three integers $a$, $b$, $c$ on one line with $a < b < c$ such that all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are listed as incompatible. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
