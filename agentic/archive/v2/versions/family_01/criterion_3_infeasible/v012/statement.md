# Problem C — Chemical Instability Report

Time limit: 2 s   Memory limit: 256 MB

A chemical repository stores $n$ hazardous compounds, labeled from $1$ to $n$. Safety logs record $m$ distinct incompatible pairs of compounds that produce dangerous reactions whenever they share a containment vessel.

To prove that a simple two-vessel separation strategy cannot safely partition all compounds, a safety inspector needs to identify three compounds that are pairwise incompatible—meaning every pair among the three produces a reaction.

You are given the list of all incompatible pairs. Your task is to locate three compounds $a, b, c$ with $a < b < c$ such that $a$ and $b$ are incompatible, $a$ and $c$ are incompatible, and $b$ and $c$ are incompatible. If multiple such triplets exist, output the lexicographically smallest one (the one with the smallest $a$; if tied, the smallest $b$; if still tied, the smallest $c$). It is guaranteed that at least one such triplet exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of compounds and the number of incompatible pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that compound $u$ and compound $v$ are mutually incompatible.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line such that $a < b < c$ and all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are incompatible. Output the lexicographically smallest such triple.

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
