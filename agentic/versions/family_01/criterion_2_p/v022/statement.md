# Problem B — Resonance Cascade Mitigation

Time limit: 1 s
Memory limit: 256 MB

A high-energy particle accelerator contains $n$ magnetic confinement nodes. We must assign an operational mode to each node. The configuration of the accelerator is defined by a state vector $S = (s_1, s_2, \dots, s_n)$.

A state space of $2^n$ potential configurations exists, and we must find a vector that satisfies all stability criteria. In a generalized framework, the domain of operational modes could be large. For this specific hardware instance, the domain is restricted, and each node's mode must be chosen such that $s_i \in \{1, 2\}$.

The stability of the accelerator is governed by a set of $m$ interference constraints. Each constraint is defined by a pair of indices $u$ and $v$, indicating that the nodes at these positions are strongly coupled. To prevent a cascade failure, any valid configuration vector must ensure that $s_u \neq s_v$ for every coupled pair.

Your objective is to determine if there exists at least one valid state vector among the $2^n$ possibilities that satisfies all $m$ constraints simultaneously. If multiple valid state vectors exist, the automated control system requires the lexicographically smallest valid configuration vector to initialize the sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a constraint between node $u$ and node $v$.

## Output
If no valid state vector exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2\}$), representing the lexicographically smallest valid state vector.

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
