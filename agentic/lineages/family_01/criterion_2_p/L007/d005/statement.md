# Problem B — Network Configurations

Time limit: 1 s
Memory limit: 256 MB

A communication grid consists of $n$ radio towers. You need to assign each tower $i$ a protocol flag $f_i$, which must be chosen from the set $\{1, 2\}$. 

There are $m$ critical links between specific pairs of towers. 

To prevent catastrophic interference and signal dropping, the configuration must adhere to two strict safety regulations for every critical link connecting a tower $u$ and a tower $v$:
- High-Bandwidth Collision Rule: It is prohibited for both tower $u$ and tower $v$ to simultaneously be assigned flag 1.
- Low-Bandwidth Timeout Rule: It is prohibited for both tower $u$ and tower $v$ to simultaneously be assigned flag 2.

Determine if a valid assignment of protocol flags exists for all towers such that all critical links satisfy both safety regulations. If no such assignment is possible, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of towers connected by a critical link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $f_1 \dots f_n$ (each in $\{1,2\}$). 
If multiple valid assignments exist, you must resolve ties by choosing the assignment that assigns the smallest possible flag to tower 1. If ties remain, among those, choose the one that assigns the smallest possible flag to tower 2, and continue this sequential preference for smaller flags up to tower $n$ (this is equivalent to the lexicographically smallest valid assignment).

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```