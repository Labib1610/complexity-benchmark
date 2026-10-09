# Problem C — Protocol Inadequacy

Time limit: 2 s   Memory limit: 256 MB

A regulatory agency is auditing a warehouse that stores various chemical compounds, labeled 1 through $n$. Certain pairs of these compounds are highly reactive and must never be stored together.

The warehouse currently operates using a safety protocol that divides its floor space into exactly two separate isolation zones. The inspectors suspect this protocol is fundamentally inadequate. To legally mandate the construction of additional zones, they must provide a concrete demonstration that a two-zone system cannot possibly prevent all reactions. Specifically, they need to find a triad of three compounds such that all three are mutually reactive with one another (every pair among the three is reactive). If such a triad exists, it is impossible to place them into just two zones without putting at least one reactive pair together.

Your task is to identify one such triad. The agency's preliminary analysis guarantees that at least one such group of three compounds exists in the warehouse.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of chemical compounds and the number of known reactive pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of compounds that are reactive with each other.
It is guaranteed that at least one set of three mutually reactive compounds exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are reactive. You must output the lexicographically smallest such set (meaning the one with the smallest $a$; if there is a tie, the one with the smallest $b$; and if still tied, the smallest $c$).

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
