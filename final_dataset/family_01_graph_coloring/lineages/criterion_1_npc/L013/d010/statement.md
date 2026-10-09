# Quantum Resonance Synthesis

Time limit: 2 s   Memory limit: 256 MB

You are configuring a network of $n$ quantum resonance emitters. Each emitter $i$ (where $1 \le i \le n$) must be assigned an excitation state $e_i \in \{1, 2, 3\}$.

The network contains $m$ bidirectional entanglement channels. We represent the network structure using an $n \times n$ matrix $A$, where $A_{u,v} = A_{v,u} = 1$ if there is a channel between emitters $u$ and $v$, and $0$ otherwise (with $A_{i,i} = 0$).

We define the state matrix $X$ as an $n \times n$ diagonal matrix where the diagonal entry $X_{i,i} = e_i$ for all $1 \le i \le n$, and all off-diagonal entries are $0$.

The overall stability of the quantum network is governed by the resonance matrix $C$, calculated as:
$C = X^2 A + A X^2 + X A X - 6(X A + A X) + 11 A$

For the network to achieve perfect resonance, $C$ must be exactly the $n \times n$ zero matrix (i.e., all entries of $C$ must be $0$).

Your task is to determine whether there exists an assignment of excitation states $e_1, e_2, \dots, e_n$ for all $n$ emitters such that the network resonance matrix $C$ is exactly the zero matrix. If such an assignment exists, you must provide one. Providing any single valid assignment is sufficient, even if multiple exist.

## Input
The first line contains two integers $n$ and $m$ — the total number of emitters and the number of channels ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating a channel between emitters $u$ and $v$.

## Output
If it is impossible to assign excitation states to all emitters such that $C$ is the zero matrix, print a single line containing `NO`.
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