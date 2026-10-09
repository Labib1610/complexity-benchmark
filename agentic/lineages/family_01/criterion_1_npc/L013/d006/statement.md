# Quantum Resonance Synthesis

Time limit: 2 s   Memory limit: 256 MB

You are configuring a network of $n$ quantum resonance emitters. Each emitter $i$ (where $1 \le i \le n$) must be assigned an excitation state $e_i$, chosen from the discrete energy levels $\{1, 2, 3\}$.

The network's stability is constrained by $m$ proximity conditions. Each condition specifies two emitters, identified by their indices $u$ and $v$, which share a quantum entanglement channel. To avoid destructive interference, their assigned states must form a linearly independent configuration with their indices.

Specifically, for each condition specifying emitters $u$ and $v$, you construct the $2 \times 2$ channel matrix:
$$ \begin{bmatrix} u & v \\ u e_u & v e_v \end{bmatrix} $$
For the entanglement channel to remain stable, this matrix must be invertible. That is, its determinant must not be exactly zero. You must ensure this requirement holds for all $m$ conditions.

Your task is to determine whether there exists a global assignment of excitation states for all $n$ emitters such that all $m$ proximity conditions are satisfied simultaneously. If such an assignment exists, you must provide one. Providing any single valid assignment is sufficient, even if multiple exist.

## Input
The first line contains two integers $n$ and $m$ — the total number of emitters and the number of proximity conditions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating a condition that the emitters $u$ and $v$ must satisfy the matrix invertibility requirement.

## Output
If it is impossible to assign excitation states to all emitters such that every condition is satisfied, print a single line containing `NO`.
If it is possible, print `YES` on the first line. On the second line, print $n$ integers $e_1, e_2, \dots, e_n$ separated by spaces, where each $e_i \in \{1, 2, 3\}$ indicates the excitation state assigned to emitter $i$. You only need to supply one valid assignment, even if multiple are possible.

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