# Policy Contradiction

Time limit: 2 s
Memory limit: 256 MB

An external auditor is attempting to divide $n$ corporate accounts (labeled $1$ through $n$) into two distinct risk classifications. However, the audit logs reveal $m$ specific pairs of accounts that have co-mingled funds. According to the regulatory policy, any two accounts that have co-mingled funds cannot be assigned to the same risk classification.

The regulatory policy is known to be structurally impossible to satisfy for the given accounts. Your objective is to generate a minimal proof of this impossibility. To do this, you must find a triad of three distinct accounts such that every pair of accounts within this triad has co-mingled funds. The existence of such a triad strictly prevents the two-classification division. 

It is guaranteed that at least one such triad exists. Furthermore, the following structural properties are guaranteed to hold for the given audit data:
- No account is involved in co-mingling relationships with more than $n-1$ distinct other accounts.
- The total sum of co-mingling relationships, when counted per-account across all $n$ accounts, is exactly $2m$.
- Any account that forms part of a valid triad will always appear in at least two relationships in the input.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The next $m$ lines each contain two integers $u$ and $v$ — a pair of accounts that have co-mingled funds.
It is guaranteed that at least one triad of mutually co-mingled accounts exists.

## Output
Output three integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the labels of the three accounts in the triad, such that the pairs $a$ and $b$, $a$ and $c$, and $b$ and $c$ all have co-mingled funds. 
If there are multiple such triads, output the one that is lexicographically smallest (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```
