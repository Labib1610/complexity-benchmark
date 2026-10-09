# Quantum Resonance Synthesis

Time limit: 2 s   Memory limit: 256 MB

You are configuring a network of $n$ quantum resonance emitters. Each emitter $i$ (where $1 \le i \le n$) must be assigned an excitation state $e_i$, chosen from the discrete energy levels $\{1, 2, 3\}$.

The network contains $m$ entanglement channels, each connecting a specific pair of emitters $u$ and $v$. 
For any active channel between emitters $u$ and $v$, their interaction is governed by a double-well potential function:
$W(e_u, e_v) = (e_u - e_v)^4 - 5(e_u - e_v)^2 + 7$

The overall stability of the quantum network is determined by its total interaction energy, which is the sum of the potentials across all $m$ channels. For the network to achieve perfect resonance, this total interaction energy must be exactly equal to $3m$.

Your task is to determine whether there exists a global assignment of excitation states for all $n$ emitters such that the total interaction energy is exactly $3m$. If such an assignment exists, you must provide one. Providing any single valid assignment is sufficient, even if multiple exist.

## Input
The first line contains two integers $n$ and $m$ — the total number of emitters and the number of entanglement channels ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating a channel between emitters $u$ and $v$.

## Output
If it is impossible to assign excitation states to all emitters such that the total energy is exactly $3m$, print a single line containing `NO`.
If it is possible, print `YES` on the first line. On the second line, print $n$ integers $e_1, e_2, \dots, e_n$ separated by spaces, where each $e_i \in \{1, 2, 3\}$ indicates the excitation state assigned to emitter $i$. You only need to supply one valid assignment.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```