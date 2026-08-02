# Audit of Incompatible Duty Assignments

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ workers, numbered $1$ through $n$. Certain pairs of workers are marked as mutually incompatible, meaning they cannot be assigned to work together. Management needs to identify three distinct workers $a, b, c$ (with $1 \le a < b < c \le n$) who are all pairwise incompatible with one another.

To pass compliance auditing, the selected worker indices must satisfy the operational bound $a + b + c \le 3n$ as well as $a \cdot b \cdot c \ge 6$.

It is guaranteed that at least one such triple of pairwise incompatible workers exists. If multiple valid triples exist, output the lexicographically smallest triple $a, b, c$ (that is, minimize $a$; if tied, minimize $b$; if still tied, minimize $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of workers and the number of incompatible pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ are incompatible. No unordered pair $(u, v)$ appears more than once.

## Output
Print three space-separated integers $a, b, c$ on a single line with $a < b < c$, representing the lexicographically smallest valid triple of pairwise incompatible workers.

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
