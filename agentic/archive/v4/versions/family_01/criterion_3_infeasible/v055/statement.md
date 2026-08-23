# Minimal Mutual Triplet

Time limit: 2 s   Memory limit: 256 MB

In a network of $n$ stations (numbered $1$ through $n$), pairs of stations can be directly linked by bidirectional communication channels. A total of $m$ distinct direct channels exist in the system.

A set of three distinct stations $a$, $b$, and $c$ forms a complete mutual triplet if a direct channel exists between every pair among them: between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$.

Given the network configuration, your task is to find the lexicographically smallest complete mutual triplet $(a, b, c)$ satisfying $1 \le a < b < c \le n$. That is, select the triplet that minimizes $a$, breaks ties by minimizing $b$, and breaks any further ties by minimizing $c$. At least one complete mutual triplet is guaranteed to exist.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 200000)$), representing the number of stations and the total number of channels, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a direct bidirectional channel between station $u$ and station $v$. No pair of stations appears more than once in the list.

It is guaranteed that at least one valid complete mutual triplet exists in the network.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line ($a < b < c$), representing the lexicographically smallest complete mutual triplet.

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
