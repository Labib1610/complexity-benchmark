# Guild Triad Discovery

Time limit: 2 s   Memory limit: 256 MB

A historical archive contains records for $n$ distinct merchant guilds, indexed from $1$ to $n$. Over the centuries, certain pairs of guilds established formal bilateral trade treaties.

Historians are researching the formation of regional economic blocks. Specifically, they wish to identify a set of three distinct guilds where every pair among the three shares a formal bilateral trade treaty. It is known from historical records that at least one such group of three mutually linked guilds exists.

Your task is to identify one such set of three guilds. If there are multiple qualifying sets of three guilds, select the one that produces the lexicographically smallest triple $(a, b, c)$ when ordered such that $a < b < c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), denoting the number of merchant guilds and the number of bilateral trade treaties, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that merchant guild $u$ and merchant guild $v$ share a bilateral trade treaty.
It is guaranteed that at least one triple of mutually linked guilds exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the index numbers of the three guilds that pairwise share treaties.
Output the lexicographically smallest such triple (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
