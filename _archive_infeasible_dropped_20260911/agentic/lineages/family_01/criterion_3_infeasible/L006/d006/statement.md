# Problem C — Proof of Collusion

Time limit: 2 s
Memory limit: 256 MB

An auditor is analyzing $m$ transaction logs among $n$ regional suppliers (numbered $1$ to $n$). Each log entry involves a pair of suppliers. For any such pair, we define a "forward audit trail" originating from the smaller-numbered supplier and terminating at the larger-numbered supplier.

You already know that dividing these suppliers into two independent oversight tiers is hopeless. Your task is to provide a concrete proof of this impossibility by identifying a trio of suppliers who are completely deadlocked.

Specifically, you must find exactly three distinct suppliers $a$, $b$, and $c$ (where $a < b < c$) such that:
1. There is a forward audit trail from supplier $a$ to supplier $b$.
2. There is a forward audit trail from supplier $b$ to supplier $c$.
3. There is also a direct forward audit trail from supplier $a$ to supplier $c$, bypassing $b$.

This concentration of forward trails creates an unresolvable deadlock, preventing those three suppliers from being split across just two tiers.

Output the identifiers of these three suppliers. It is guaranteed that the records contain at least one such configuration.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 200000)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of suppliers involved in a transaction log entry.
It is guaranteed that at least one trio of suppliers satisfying the proof condition exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, representing the identifiers of the three suppliers. Output the lexicographically smallest such combination (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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