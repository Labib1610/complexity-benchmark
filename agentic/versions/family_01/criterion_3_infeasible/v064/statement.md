# Synchronized Triad Discovery

Time limit: 2 s   Memory limit: 256 MB

A high-frequency trading platform consists of $n$ execution nodes numbered from $1$ to $n$. Across this infrastructure, exactly $m$ active bidirectional fiber lines connect distinct pairs of nodes.

An auditing mechanism needs to locate a closed loop of three distinct nodes—that is, three nodes where a direct fiber line exists between every pair among the three.

It is guaranteed that at least one such closed group of three nodes exists within the network.

Your objective is to find one such node index triplet $(a, b, c)$ satisfying $a < b < c$. If there are multiple qualifying triplets, choose the lexicographically smallest one (the one that minimizes $a$; if tied, minimizes $b$; if still tied, minimizes $c$).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of execution nodes and the number of active fiber lines, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that a bidirectional fiber line connects node $u$ and node $v$. No pair of nodes is connected by more than one line.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line, representing the node indices of the lexicographically smallest qualifying triplet with $a < b < c$.

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
