# Problem C — Tri-Core Synchronization

Time limit: 2 s   Memory limit: 256 MB

A distributed computing network consists of $n$ microservices, numbered 1 through $n$. There are $m$ dedicated bidirectional communication channels, each directly linking a specific pair of microservices.

Your task is to provision a tri-core processing cluster. A valid cluster requires exactly three distinct microservices such that all three are directly connected to each other by the communication channels (i.e., every pair within the chosen group of three must share a dedicated bidirectional link). 

It is guaranteed that the network's topology contains at least one such group of three microservices.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating a bidirectional channel between microservice $u$ and microservice $v$. 
It is guaranteed that at least one valid cluster of three microservices exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the IDs of the microservices in the cluster, sorted such that $a < b < c$. 
If there are multiple valid clusters, output the lexicographically smallest one (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

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
