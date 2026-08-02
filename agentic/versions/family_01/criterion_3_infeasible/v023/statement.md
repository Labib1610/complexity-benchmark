# Mutual Connection Audit

Time limit: 2 s   Memory limit: 256 MB

A digital communications grid consists of $n$ network hubs numbered from $1$ to $n$. Exactly $m$ bidirectional communication links operate between pairs of distinct hubs.

A security protocol requires identifying a tight cluster of three hubs—specifically, a group of three distinct hubs where every pair within the group is directly connected by a link.

It is guaranteed that at least one such group of three mutually connected hubs exists in the grid.

Your task is to identify one such triplet of hub labels $(a, b, c)$ satisfying $a < b < c$. If multiple such triplets exist, output the lexicographically smallest one (the one with the smallest $a$; if tied, the smallest $b$; if still tied, the smallest $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of hubs and the number of active links, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that a bidirectional communication link exists between hub $u$ and hub $v$. No pair of hubs is connected by more than one link.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line, representing the hub indices of the lexicographically smallest mutually connected triplet with $a < b < c$.

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
