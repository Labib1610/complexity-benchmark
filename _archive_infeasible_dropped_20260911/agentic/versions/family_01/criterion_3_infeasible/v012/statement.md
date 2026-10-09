# Problem C — Proof of Collusion

Time limit: 2 s
Memory limit: 256 MB

An auditor is attempting to divide $n$ regional suppliers into exactly two independent oversight tiers. However, certain pairs of suppliers share bilateral non-compete agreements. Two suppliers with such an agreement cannot be placed in the same oversight tier, as they would collude to manipulate the audit.

The auditor already knows that a two-tier division is hopeless. Your task is not to attempt the division, but to provide a concrete proof of its impossibility. It is guaranteed that the records contain at least one group of exactly three suppliers who all share bilateral non-compete agreements with one another. Any such trio guarantees that two tiers are insufficient, as at least two of them would be forced into the same tier. Output one such trio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of suppliers who share a bilateral agreement.
It is guaranteed that at least one such trio of mutually agreeing suppliers exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ share bilateral agreements. Output the lexicographically smallest such trio (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
