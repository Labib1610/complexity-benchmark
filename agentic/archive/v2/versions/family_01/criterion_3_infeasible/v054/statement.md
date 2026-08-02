# Facility Material Interference Report

Time limit: 2 s   Memory limit: 256 MB

A research center manages $n$ distinct chemical agents, identified by integers from $1$ to $n$. A safety registry tracks $m$ unordered pairs of agents that exhibit direct mutual interference when stored in proximity.

To document a complete mutual interference group of size three, the lab manager needs to find three distinct agents $a, b,$ and $c$ such that:
- $a < b < c$
- Agent $a$ and agent $b$ interfere with each other.
- Agent $a$ and agent $c$ interfere with each other.
- Agent $b$ and agent $c$ interfere with each other.

If multiple such triplets exist, choose the one that is lexicographically smallest. That is, minimize $a$; if tied, minimize $b$; if still tied, minimize $c$. At least one such triplet is guaranteed to exist.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), indicating the number of chemical agents and the number of interference pairs, respectively.
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that agent $u$ and agent $v$ interfere with each other. No pair of agents is listed more than once.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line, representing the lexicographically smallest triple with $a < b < c$ where all three pairs $(a, b)$, $(a, c)$, and $(b, c)$ are listed as interfering pairs in the registry.

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
