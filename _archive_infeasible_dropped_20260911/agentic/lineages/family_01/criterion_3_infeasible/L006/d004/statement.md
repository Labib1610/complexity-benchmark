# Problem C — Proof of Collusion

Time limit: 2 s
Memory limit: 256 MB

An auditor is attempting to divide regional suppliers (identified by integers $1$ through $n$) into exactly two independent oversight tiers. However, the records contain bilateral non-compete agreements, each between a specific pair of suppliers. Two suppliers sharing such an agreement cannot be placed in the same oversight tier, as they would collude to manipulate the audit.

The auditor already knows that a two-tier division is hopeless for the given records. Your task is not to attempt the division, but to provide a concrete proof of its impossibility. To do this, you must find three distinct agreements in the provided records that involve exactly three distinct suppliers in total. This tight concentration of agreements creates an unresolvable deadlock, preventing those three suppliers from being split across just two tiers.

Output the identifiers of these three suppliers. It is guaranteed that the records contain at least one such configuration.

## Input
The first line contains two integers $n$ and $m$. The supplier headcount $n$ ranges from a minimum of $3$ up to the corporate roster limit of exactly $2000$. The agreement count $m$ is at least $3$, and is bounded by either the maximum possible number of unique pairs among the $n$ suppliers, or the system's hard capacity of exactly $200000$ agreements, whichever is strictly smaller.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of suppliers who share a bilateral agreement. (Each pair appears at most once in the records).
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