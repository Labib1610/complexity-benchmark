# Facility Mutual Incompatibility Audit

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates with a roster of $n$ personnel units, indexed $1$ through $n$. Due to strict safety protocols, management maintains a list of $m$ mutual incompatibility rules, where each rule indicates that two specific units cannot work together on the same assignment.

To prove that dividing the workforce into just two separate operational shifts is impossible, an auditor must present a mutual friction cluster of three distinct units where every pair within the cluster is bound by an explicit mutual incompatibility rule.

Among all valid three-unit clusters $(a, b, c)$ satisfying $1 \le a < b < c \le n$ where $(a,b)$, $(a,c)$, and $(b,c)$ are all mutually incompatible, your task is to find the one that is lexicographically smallest. That is, choose the cluster that minimizes $a$; if there is a tie, minimize $b$; if still tied, minimize $c$.

It is guaranteed that at least one such three-unit cluster exists in the provided log.

## Input
The first line contains two space-separated integers $n$ and $m$.
The workforce headcount $n$ ranges from a minimal operating squad of $3$ up to the facility's max unit capacity of $2000$.
The total rule count $m$ is at least $3$ and does not exceed the safety log system limit of $200,000$, nor does it exceed the maximum possible pairwise pairings $\frac{n(n-1)}{2}$.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a recorded mutual incompatibility rule between unit $u$ and unit $v$. No distinct pair of units is listed more than once.

It is guaranteed that at least one valid cluster exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($a < b < c$) on a single line representing the lexicographically smallest valid cluster.

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
