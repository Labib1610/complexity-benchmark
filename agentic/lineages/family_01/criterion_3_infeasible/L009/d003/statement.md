# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The laboratory protocol requires isolating reactive materials by assigning them to two separate storage units so that neither unit contains a mutually volatile pair. However, the provided registry of mutually volatile pairs indicates that such a safe allocation might not always be possible.

Your task is to identify a minimal certificate of this instability. A certificate consists of exactly three materials with the following property: there is no way to assign each of these three materials to one of two separate storage units such that both units remain completely free of mutually volatile pairs. It is guaranteed that the provided registry contains at least one such certificate.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a mutually volatile pair.
It is guaranteed that a certificate of three materials exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the materials of a minimal certificate. Output the lexicographically smallest such certificate (smallest $a$; ties by smallest $b$; then smallest $c$).

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