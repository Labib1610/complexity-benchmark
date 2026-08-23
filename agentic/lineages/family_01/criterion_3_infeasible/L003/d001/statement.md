# Problem C — Chemical Safety Audit

Time limit: 2 s   Memory limit: 256 MB

A chemical manufacturing plant has an inventory of $n$ distinct reagents, numbered 1 through $n$. Through testing, they have identified $m$ specific combinations of two reagents that produce a highly exothermic reaction when mixed.

The safety protocol requires identifying a "Type-3 Hazard", which occurs when three specific reagents are brought together such that any two out of the three would react exothermically on their own. It is a known fact about this inventory that at least one Type-3 Hazard can be formed.

Your task is to process the list of reactive pairs and identify one such set of three reagents.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of reagents that react exothermically.
It is guaranteed that at least one Type-3 Hazard exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ produce exothermic reactions. Output the lexicographically smallest such set (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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