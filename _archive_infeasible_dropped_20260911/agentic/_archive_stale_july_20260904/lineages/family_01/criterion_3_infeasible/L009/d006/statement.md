# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The laboratory protocol requires isolating reactive materials to prevent hazards. Certain pairs of materials are documented as mutually volatile.

Your task is to identify a certificate of instability. A certificate consists of exactly three distinct materials that satisfy two strict rules:
1. The trio is not completely inert: there is at least one mutually volatile pair among the three materials.
2. The trio exhibits reactive symmetry: for any material in the trio, if it is mutually volatile with at least one of the other two materials in the trio, it must be mutually volatile with both of them.

It is guaranteed that the provided registry contains at least one such certificate.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a mutually volatile pair.
It is guaranteed that a certificate of three materials exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the materials of a certificate. Output the lexicographically smallest such certificate (smallest $a$; ties by smallest $b$; then smallest $c$).

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