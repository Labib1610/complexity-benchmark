# Quantum State Configuration

Time limit: 1 s   Memory limit: 256 MB

You are calibrating a quantum array containing $n$ interacting particles. Each particle must be stabilized by assigning it a spin state, which must be chosen as either $1$ or $2$.

The array's stability is dictated by $m$ entanglement links between specific pairs of particles. When two particles are linked, their spin states must be complementary to prevent destructive interference. Specifically, if an entanglement link connects particle $u$ and particle $v$, their assigned spin states $s_u$ and $s_v$ must satisfy the equation $s_u + s_v = 3$. 

Your task is to determine whether it is possible to assign a valid spin state to every particle in the array such that all entanglement constraints are satisfied.

## Input
The first line contains the number of particles, $n$, and the number of entanglement links, $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$). The particles are indexed from $1$ to $n$.
The next $m$ lines each contain two integers $u$ and $v$ — representing an entanglement link between particle $u$ and particle $v$.

## Output
If no valid spin state assignment exists, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the spin state assigned to each particle. If there are multiple valid assignments, output the one whose sequence of states is lexicographically smallest.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
