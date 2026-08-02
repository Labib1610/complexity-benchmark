# Network Interference Triad

Time limit: 2 s   Memory limit: 256 MB

A telecommunications provider operates a network of $n$ high-bandwidth relay stations, numbered from $1$ to $n$. Certain pairs of stations are linked by direct high-frequency transmission channels.

Engineers have discovered that when three stations are all pairwise connected to each other—that is, every station in the group of three shares a direct channel with the other two—a severe signal resonance interference occurs. It is known that the current network configuration contains at least one such group of three mutually connected stations.

Your goal is to identify one such group of three stations. If multiple such groups exist, report the one that is lexicographically smallest. That is, choose the triple $(a, b, c)$ with $a < b < c$ such that $a$ is minimized, ties broken by minimizing $b$, and further ties broken by minimizing $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n - 1) / 2, 2 \cdot 10^5)$), representing the number of relay stations and the number of direct transmission channels, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that there is a direct transmission channel between station $u$ and station $v$.
It is guaranteed that at least one group of three mutually connected stations exists.

## Output
Print three space-separated integers $a\ b\ c$ on a single line, where $a < b < c$, such that all three direct channels $(a, b)$, $(a, c)$, and $(b, c)$ are present in the network. If there are multiple valid triples, output the lexicographically smallest one.

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
