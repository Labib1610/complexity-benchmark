# Problem C — Surge Analysis

Time limit: 2 s   Memory limit: 256 MB

A facility operates $n$ devices, which must be powered by either a primary circuit or a secondary circuit. Each device must be wired to exactly one of these circuits.

Certain pairs of devices draw too much current and will cause a surge if they are wired to the same circuit. You are given a list of $m$ such pairs.

Your task is to identify three distinct devices $a, b,$ and $c$ (with $a < b < c$) such that the given list of pairs includes:
- A pair consisting of Device $a$ and Device $b$, which requires them to be on different circuits.
- A pair consisting of Device $b$ and Device $c$, which requires them to be on different circuits.
- A pair consisting of Device $a$ and Device $c$, which requires them to be on different circuits.

Output the trio with the smallest possible value for $a$; in the event of a tie, the smallest possible value for $b$; and finally the smallest possible value for $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of devices that would cause a surge if placed on the same circuit.
It is guaranteed that at least one trio satisfying the criteria exists.

## Output
Print three integers $a$, $b$, and $c$, separated by spaces, on a single line.

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
