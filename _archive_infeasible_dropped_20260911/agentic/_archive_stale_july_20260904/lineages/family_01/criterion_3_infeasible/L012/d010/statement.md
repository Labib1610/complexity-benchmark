# Problem C — Triadic Configurations

Time limit: 2 s
Memory limit: 256 MB

You are given a configuration of $n$ modules and a set of $m$ distinct bidirectional communication buses. Each bus connects a unique pair of modules. No bus connects a module to itself.

For any triplet of distinct modules $T = \{a, b, c\}$, we evaluate its structural stability by assigning a real-valued potential $P_u$ to each module $u \in T$. The triplet is considered *balanced* if it satisfies the following three equilibrium conditions:
- $E(a,b) \cdot P_b + E(a,c) \cdot P_c = 0$
- $E(b,a) \cdot P_a + E(b,c) \cdot P_c = 0$
- $E(c,a) \cdot P_a + E(c,b) \cdot P_b = 0$

Here, $E(u,v) = 1$ if a bus connects module $u$ and module $v$, and $E(u,v) = 0$ otherwise.

A triplet of modules $T$ is classified as *unresolvable* if the **only** assignment of potentials that achieves this balance is the trivial one: $P_a = 0$, $P_b = 0$, and $P_c = 0$. 

Your task is to identify the unresolvable triplet of modules. If multiple unresolvable triplets exist, you must report the lexicographically smallest one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of modules and the number of buses. Modules are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a bus between module $u$ and module $v$. It is guaranteed that all $m$ unordered pairs $\{u, v\}$ are distinct, and that at least one unresolvable triplet exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the identifiers of the modules that form the unresolvable triplet. 

The identifiers must be printed in ascending order ($a < b < c$). If there are multiple valid triplets, output the one that is lexicographically smallest. This means you should first minimize $a$; if there are ties, minimize $b$ among those ties; and if there are still ties, minimize $c$.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```
**Output:**
```
1 2 3
```

## Example 2
**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
**Output:**
```
1 2 4
```