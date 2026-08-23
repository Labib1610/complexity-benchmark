# Mutual Interference Triples

Time limit: 2 s   Memory limit: 256 MB

An industrial facility monitors a collection of $n$ registered electronic devices, indexed $1$ through $n$. Certain pairs of devices experience mutual interference, meaning they cannot safely transmit signals at the same time.

A safety audit requires identifying three distinct devices where every pair among the three experiences mutual interference. It is guaranteed that at least one such group of three devices exists in the facility network.

Your task is to find three device indices $a$, $b$, $c$ satisfying $a < b < c$ such that all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ interfere with each other. If there are multiple valid choices, output the lexicographically smallest triple — that is, the one that minimizes $a$, then minimizes $b$, and finally minimizes $c$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$) — the number of devices and the number of interference pairs, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that device $u$ and device $v$ interfere with each other. Each undirected pair of devices appears at most once in the input.

It is guaranteed that at least one triple of mutually interfering devices exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ ($1 \le a < b < c \le n$) on a single line representing the lexicographically smallest triple of mutually interfering devices.

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
