# Problem C — Tripartite Alliance

Time limit: 2 s
Memory limit: 256 MB

In a sprawling galaxy, there are $n$ star systems and $m$ established hyperspace trade routes. Each trade route is bidirectional and connects two different star systems. 

A "Tripartite Alliance" is a special economic agreement formed by exactly three distinct star systems. For the alliance to be valid, all three star systems must have direct hyperspace trade routes connecting each of them to the other two. That is, if the systems in the alliance are $a$, $b$, and $c$, there must be an active route between $a$ and $b$, a route between $a$ and $c$, and a route between $b$ and $c$.

Your task is to identify a Tripartite Alliance. The galaxy's routing data is complex, but the hyperspace registry confirms that the current configuration guarantees the presence of at least one such alliance.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of star systems and the number of trade routes. Star systems are numbered from $1$ to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating a bidirectional trade route between star system $u$ and star system $v$. It is guaranteed that at most one route exists between any specific pair of star systems, and that at least one Tripartite Alliance exists in the network.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the star systems in the alliance. You must list them in ascending order ($a < b < c$).

If there are multiple valid alliances, output the lexicographically smallest one. An alliance $(a_1, b_1, c_1)$ is lexicographically smaller than $(a_2, b_2, c_2)$ if $a_1 < a_2$; or if $a_1 = a_2$ and $b_1 < b_2$; or if $a_1 = a_2$, $b_1 = b_2$, and $c_1 < c_2$.

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
