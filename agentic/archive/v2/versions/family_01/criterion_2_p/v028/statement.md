# Sensor Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

A remote monitoring station consists of $n$ sensors numbered from $1$ to $n$. Exactly two operating channels, labeled $1$ and $2$, are available for configuration.

Due to physical proximity, certain pairs of sensors experience severe interference if operated on the same channel. You are given $m$ pairs of sensors that interfere with each other. Every such pair must be assigned distinct channels.

Determine whether it is possible to assign a channel ($1$ or $2$) to every sensor such that no interfering pair shares the same channel. If possible, find the valid channel sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of sensors and the number of interference pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — an interference pair between sensor $u$ and sensor $v$.

## Output
If no valid channel assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
