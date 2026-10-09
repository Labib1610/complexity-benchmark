# Orbital Reflection Synchrony

Time limit: 1 s   Memory limit: 256 MB

A satellite network consists of $n$ orbital modules, numbered $1$ through $n$. You must assign each module an operating mode, represented by the integer $1$ or $2$.

Each mode corresponds to a specific $3 \times 3$ transformation matrix:
- Mode 1 corresponds to the matrix $M_1 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$.
- Mode 2 corresponds to the matrix $M_2 = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 2 & 1 \end{pmatrix}$.

The network's synchronization is governed by $m$ telemetry channels. Each channel connects a specific pair of modules. For a channel to function correctly, the matrix product of the two modules' transformation matrices must have a trace (the sum of the elements on the main diagonal) exactly equal to $11$. 

Because the trace of a product of two square matrices is independent of the order of multiplication (i.e., $\text{Tr}(A B) = \text{Tr}(B A)$), the order in which the two modules' matrices are multiplied does not matter. If the trace of their product evaluates to any value other than $11$, the telemetry channel fails.

Your task is to assign an operating mode ($1$ or $2$) to each of the $n$ modules so that every telemetry channel functions correctly. If multiple valid assignments are possible, you must output the lexicographically smallest valid sequence of modes. If no such assignment is possible, you must report that it cannot be done.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), representing the indices of a pair of modules connected by a telemetry channel.

## Output
If it is impossible to configure the modules to satisfy all channels, output a single line with NO.
If it is possible, output YES on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1,2\}$) giving the lexicographically smallest valid sequence of modes.

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