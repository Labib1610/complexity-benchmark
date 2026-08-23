# High-Availability Storage Quorum

Time limit: 2 s   Memory limit: 256 MB

To ensure zero downtime, a cloud provider is building a new storage tier requiring groups of exactly three servers to act as a single logical unit. You are given a fleet of $n$ servers, labeled $1$ to $n$.

Not all servers can synchronize with each other. Network constraints allow direct synchronization only across $m$ specific two-way connections. For a three-server group to function reliably, it must survive the unexpected loss of any one of its members. This means that regardless of which specific server in the group experiences a hardware failure, the surviving pair must have a pre-existing direct synchronization connection between them. If even one possible single-server failure scenario leaves a disconnected pair, the group cannot be formed.

Given the list of all valid two-way connections, find three servers that can safely form this group. It is guaranteed that the provided network allows for at least one such group to be formed.

## Input
The first line provides the number of servers $n$ ($3 \le n \le 2000$) and the number of valid two-way connections $m$ ($3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$). This signifies that a direct synchronization connection exists between server $u$ and server $v$. Each connection is listed at most once.

## Output
Print three space-separated integers $a$, $b$, and $c$, ordered such that $a < b < c$, representing the identifiers of the chosen servers. If there are multiple valid groups, output the one that is lexicographically smallest (i.e., prefer the smallest $a$; in case of a tie, the smallest $b$; and then the smallest $c$).

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