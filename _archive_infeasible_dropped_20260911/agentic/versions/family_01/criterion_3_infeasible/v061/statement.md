# Fund Allocation Proof

Time limit: 2 s
Memory limit: 256 MB

A legal mediator is tasked with distributing an estate of $n$ properties between a primary and a secondary trust fund. However, there is a complication: certain properties have zoning incompatibilities, meaning they are strictly prohibited from being placed into the same fund.

The mediator has concluded that no valid allocation into the two funds is possible. To officially terminate the process, the mediator must submit a formal proof of impossibility. By law, this proof must consist of exactly three properties such that every possible pair formed from these three has a zoning incompatibility. Finding this configuration is sufficient to demonstrate that the estate cannot be legally allocated without violating the rules.

You are given the list of zoning incompatibilities. It is guaranteed that at least one such configuration of three properties exists. Your task is to find one to complete the documentation.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of properties and the number of zoning incompatibilities. The properties are numbered $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ — indicating that property $u$ and property $v$ have a zoning incompatibility.
It is guaranteed that there is at least one group of three properties that are all pairwise incompatible.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the three properties for the proof. The properties must be printed in ascending order ($a < b < c$). If there are multiple valid groups of three, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$).

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
