# Steering Panel Selection

Time limit: 2 s   Memory limit: 256 MB

A research institute manages $n$ researchers, numbered $1$ to $n$. Certain pairs of researchers have active collaboration history. There are $m$ such pairwise collaboration links.

The institute needs to select a 3-member steering panel consisting of distinct researchers $a, b, c$ ($a < b < c$) such that every pair among them has a collaboration link (specifically, links exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$). Additionally, compliance regulations stipulate that the sum of the identification numbers of the panel members, $a + b + c$, must be strictly less than $3n$.

It is guaranteed that at least one valid 3-member steering panel exists. If multiple such panels exist, choose the lexicographically smallest one (minimizing $a$; breaking ties by minimizing $b$; then by $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), denoting a pairwise collaboration link between researcher $u$ and researcher $v$.
It is guaranteed that at least one valid panel exists.

## Output
Print three space-separated integers $a\ b\ c$ ($a < b < c$) representing the lexicographically smallest valid steering panel.

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
