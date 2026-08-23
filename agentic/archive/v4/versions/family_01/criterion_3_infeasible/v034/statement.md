# Problem C — Incompatibility Certificate

Time limit: 2 s   Memory limit: 256 MB

A chemical repository has only two climate-controlled vaults, but allocating reagents to these vaults is known to be impossible. Your task is not to find a valid allocation, but to produce a certificate proving why two vaults are insufficient. It is guaranteed that there exists at least one group of three reagents where every pair within the group reacts dangerously when stored together. Any such group proves that two vaults cannot accommodate the inventory. Identify one such group.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of reagents and the number of reactive pairs, respectively.
Each of the next $m$ lines contains two integers $u$ $v$ — indicating that reagent $u$ and reagent $v$ are reactive with each other.
It is guaranteed that at least one such mutually reactive triple exists.

## Output
Print three integers $a\ b\ c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are reactive pairs. Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
