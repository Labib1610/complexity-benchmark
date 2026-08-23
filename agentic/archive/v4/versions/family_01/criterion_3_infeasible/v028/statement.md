# Network Security Audit: Triad Detection

Time limit: 2 s   Memory limit: 256 MB

A cloud platform consists of $n$ microservices, indexed from $1$ to $n$, connected by $m$ bidirectional communication channels. Each channel connects two distinct microservices.

An architectural security risk occurs whenever three distinct microservices $a, b, c$ form a fully interconnected cluster—that is, direct channels exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$. System invariants guarantee that every channel connects two different microservices, that no two microservices share duplicate channels, and that at least one such mutually connected group of three microservices exists.

Your task is to identify the lexicographically smallest triple of microservice identifiers $(a, b, c)$ with $a < b < c$ that forms a fully interconnected cluster. 

Tuple $(a_1, b_1, c_1)$ is lexicographically smaller than $(a_2, b_2, c_2)$ if $a_1 < a_2$, or if $a_1 = a_2$ and $b_1 < b_2$, or if $a_1 = a_2$, $b_1 = b_2$, and $c_1 < c_2$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of microservices and the number of channels.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a bidirectional channel between microservice $u$ and microservice $v$.

It is guaranteed that at least one fully interconnected cluster of three microservices exists.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line ($a < b < c$) representing the lexicographically smallest triple of microservices that are pairwise connected by channels.

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
