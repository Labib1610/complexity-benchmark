# Ternary Quantum Coherence

Time limit: 2 s
Memory limit: 256 MB

A physics laboratory is working with a system of $n$ trapped ions. The scientists have performed a series of operations, successfully creating $m$ distinct two-particle entanglements. Each entanglement links a specific pair of ions.

The next phase of the experiment requires isolating a coherent ternary subsystem—a group of exactly three ions. For the subsystem to maintain the required quantum coherence, it must be completely interconnected: every ion in the chosen trio must share a two-particle entanglement with both of the other two ions in the trio.

You are provided with the log of the $m$ successful two-particle entanglements. It is guaranteed that the system contains at least one valid ternary subsystem. Your task is to identify the three ions that form it.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of trapped ions and the number of two-particle entanglements, respectively. The ions are assigned integer identifiers from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that the ion $u$ and the ion $v$ share an entanglement.

It is guaranteed that at least one valid ternary subsystem can be identified.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the identifiers of the three ions that form the subsystem. The identifiers must be printed in strictly increasing order ($a < b < c$).

If multiple such subsystems exist, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$).

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