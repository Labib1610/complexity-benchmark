# Problem C — Network Triad Discovery

Time limit: 2 s   Memory limit: 256 MB

Consider a data processing network with $n$ units labeled $1$ through $n$, connected by $m$ bidirectional communication channels. Each channel establishes a direct link between two distinct units. No pair of units is connected by more than one channel.

Within this infrastructure, three distinct units $a$, $b$, and $c$ form a mutually connected triad if direct channels exist between $a$ and $b$, between $b$ and $c$, and between $a$ and $c$. The network configuration is such that at least one mutually connected triad is present.

Among all valid mutually connected triads, we order the three unit labels such that $a < b < c$. Your task is to identify the triad that is lexicographically smallest. That is, select the tuple $(a, b, c)$ that minimizes $a$; if multiple such tuples share the minimum $a$, minimize $b$; and if a tie still remains, minimize $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of units and the number of channels, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a direct bidirectional channel between unit $u$ and unit $v$.
It is guaranteed that at least one valid triad exists.

## Output
Print three space-separated integers $a\ b\ c$ on a single line with $a < b < c$, representing the lexicographically smallest mutually connected triad.

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
