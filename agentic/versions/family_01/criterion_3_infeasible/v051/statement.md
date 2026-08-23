# Problem C — Containment Instability

Time limit: 2 s
Memory limit: 256 MB

In a hazardous materials storage facility, certain pairs of chemical compounds are known to be highly reactive when exposed to each other. The facility's safety protocols are designed to manage simple reactive pairs using isolated dual-containment bins. However, the safety protocols are entirely bypassed if a specific instability arises. This instability occurs when it is possible to find three distinct compounds such that the first reacts with the second, the second reacts with the third, and the third reacts with the first.

Your task is to identify one such set of three compounds to demonstrate that the current storage protocols are insufficient. You are given a list of all reactive pairs. It is guaranteed that the inventory contains at least one such instability.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of compounds and the number of reactive pairs, respectively. Compounds are numbered from 1 to n.
Each of the following m lines contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v), indicating that compound u and compound v are reactive. Reactivity is mutual.
It is guaranteed that at least one such instability exists.

## Output
Print three integers a, b, and c on a single line, separated by spaces, representing the identifiers of the three compounds involved in the instability. The identifiers must be printed in increasing order (a < b < c).
If there are multiple such sets of three compounds, output the one that is lexicographically smallest. That is, minimize a; in case of a tie, minimize b; and if still tied, minimize c.

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
