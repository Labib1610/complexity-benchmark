# Problem C — Proof of Collusion

Time limit: 2 s
Memory limit: 256 MB

The auditor's database tracks $n$ regional suppliers and $m$ bilateral non-compete agreements. Each agreement binds a specific pair of suppliers. According to standard procedure, suppliers must be divided into exactly two independent oversight tiers. Any two suppliers bound by an agreement cannot be placed in the same tier, otherwise they would have the opportunity to collude.

It is already established that a valid two-tier division cannot be formed from this database. This failure is guaranteed to be caused by the existence of at least one group of exactly three suppliers who are all mutually bound by bilateral agreements with each other. In such a group, any attempt to assign the three suppliers to two tiers will force at least two of them into the same tier, violating the procedure.

Your task is to extract a concrete proof of this impossibility from the records by identifying one such group of three mutually bound suppliers. 

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the following $m$ lines contains two integers $u$ and $v$, representing a pair of suppliers who share a bilateral agreement.
It is guaranteed that at least one such group of three mutually bound suppliers exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These integers must represent a group of three suppliers such that the pairs $a$–$b$, $a$–$c$, and $b$–$c$ all share bilateral agreements. 

If there are multiple such groups, output the lexicographically smallest one (meaning the group with the smallest $a$; in case of a tie, the one with the smallest $b$; and if still tied, the smallest $c$).

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```
**Output:**
```
1 2 3
```

## Example 2
**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
**Output:**
```
1 2 4
```
