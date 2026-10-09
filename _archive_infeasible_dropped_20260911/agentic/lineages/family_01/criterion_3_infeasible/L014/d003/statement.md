# Problem C — Quantum Entanglement Conflict

Time limit: 2 s   Memory limit: 256 MB

A quantum monitoring station tracks $n$ qubits. Due to overlapping states, certain pairs of qubits experience phase resonance. This resonance destabilizes their superposition unless they are assigned to different isolation tiers. The station currently only has two isolation tiers available for assignment. 

The proposed quantum configuration cannot be stabilized. The tracking data contains at least one group of three distinct qubits where every qubit in the group experiences resonance with both of the other two. Because all three mutually resonate, it is impossible to safely distribute them across merely two isolation tiers.

Your task is to identify one such group of three qubits to serve as proof of the configuration's instability.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of qubits and the number of resonating pairs, respectively.
The qubits are identified by integers from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ — the numeric identifiers of two qubits that experience resonance.
The input data will always contain at least one group of three qubits that all mutually resonate.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$. These three qubits must mutually resonate (i.e., the pair $a$ and $b$, the pair $a$ and $c$, and the pair $b$ and $c$ must each appear in the input, in any order, as a resonating pair). 
If there are multiple such groups, output the one with the smallest value for $a$. If there is a tie, choose the one with the smallest value for $b$. If a tie still persists, choose the one with the smallest value for $c$.

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