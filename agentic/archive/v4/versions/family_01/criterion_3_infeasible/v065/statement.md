# Maritime Logistics: Primary Mutual Alliance Triad

Time limit: 2 s   Memory limit: 256 MB

A global maritime agency oversees $n$ commercial ports, indexed from $1$ to $n$. Across these ports, there are $m$ active shipping channels, each providing a direct two-way transport connection between two distinct ports.

To form an efficient local supply loop, the agency seeks a mutual alliance triad—a set of three distinct ports $a$, $b$, and $c$ (ordered such that $1 \le a < b < c \le n$) where every pair among the three is connected by a direct shipping channel. Thus, direct channels must exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

To prioritize scheduling, the agency must identify the primary triad. This is the valid triple $(a, b, c)$ with $a < b < c$ that is lexicographically smallest; that is, it minimizes $a$, breaks ties by minimizing $b$, and breaks further ties by minimizing $c$.

It is guaranteed that at least one such triad exists in the shipping network.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), denoting the number of ports and active shipping channels, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a direct two-way shipping channel between port $u$ and port $v$. No channel is listed more than once, and no channel connects a port to itself.

It is guaranteed that at least one mutual alliance triad exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the lexicographically smallest primary triad.

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
