# Resonant Hazard Identification

Time limit: 2 s   Memory limit: 256 MB

An industrial automated facility manages $n$ processing units, identified by integers from $1$ to $n$. A total of $m$ recorded interference entries document pairs of units that experience hardware resonance when operating simultaneously.

A hazard state arises when three distinct units $a, b, c$ with $a < b < c$ form a fully mutual interference set—meaning an interference entry exists for every pair among them: $(a,b)$, $(a,c)$, and $(b,c)$.

It is guaranteed that at least one such set of three units exists. Your task is to identify the lexicographically smallest hazard set. Specifically, select the valid triple $(a, b, c)$ with $a < b < c$ that has the minimum value of $a$; if there are ties, select the one with the minimum $b$; if ties still persist, select the one with the minimum $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating an interference entry between unit $u$ and unit $v$.
It is guaranteed that at least one valid set of three units exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line separated by spaces ($a < b < c$), representing the lexicographically smallest triple of mutually interfering processing units.

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
