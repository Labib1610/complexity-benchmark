# Problem C — Diagnostic Triplet Search

Time limit: 2 s   Memory limit: 256 MB

Consider a communication system with $n$ distinct endpoints numbered $1$ through $n$. There are $m$ bidirectional links present, where each link directly connects two distinct endpoints. No pair of endpoints is connected by more than one direct link.

A group of three distinct endpoints $x$, $y$, and $z$ is called a *triplet cluster* if a direct link exists between $x$ and $y$, between $y$ and $z$, and between $x$ and $z$. The network configuration guarantees that at least one triplet cluster exists.

Every triplet cluster can be uniquely represented as a sequence $(a, b, c)$ such that $a < b < c$. We compare two such sequences $(a_1, b_1, c_1)$ and $(a_2, b_2, c_2)$ lexicographically: $(a_1, b_1, c_1)$ is smaller than $(a_2, b_2, c_2)$ if $a_1 < a_2$; or if $a_1 = a_2$ and $b_1 < b_2$; or if $a_1 = a_2$, $b_1 = b_2$, and $c_1 < c_2$.

Your objective is to identify the lexicographically smallest sequence $(a, b, c)$ with $a < b < c$ corresponding to a valid triplet cluster.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$) — the number of endpoints and the number of links, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a direct link between endpoint $u$ and endpoint $v$.
It is guaranteed that at least one valid triplet cluster exists.

## Output
Print three space-separated integers $a\ b\ c$ on a single line with $a < b < c$, representing the lexicographically smallest sequence corresponding to a triplet cluster.

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
