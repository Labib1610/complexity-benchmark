# Factory Roster Audit

Time limit: 2 s   Memory limit: 256 MB

## Description
Consider a factory workforce consisting of $n$ individual workers, labeled $1$ through $n$. Certain pairs of workers have documented mutual scheduling conflicts, meaning they cannot be assigned to work during the same shift. In this system, there are $m$ total pairwise conflicts logged. A conflict always involves two distinct workers, and conflict relationship is mutual.

It is guaranteed that within the workforce, there exists at least one group of three distinct workers where every two workers in the group have a logged conflict between them. To demonstrate why a simple two-shift arrangement fails, your task is to identify such a mutually conflicting group of three workers. Specifically, among all valid triplets $(a, b, c)$ with $a < b < c$ where $a$ conflicts with $b$, $a$ conflicts with $c$, and $b$ conflicts with $c$, you must find and report the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of workers and the number of pairwise conflicts, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating a pairwise conflict between worker $u$ and worker $v$.
It is guaranteed that at least one mutually conflicting group of three workers exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the lexicographically smallest triple of workers who all pairwise conflict with one another (that is, minimizing $a$, then $b$, then $c$).

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
