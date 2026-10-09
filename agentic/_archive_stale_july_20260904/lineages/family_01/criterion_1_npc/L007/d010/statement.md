# Phase Configuration Protocol

Time limit: 2 s   Memory limit: 256 MB

A data center needs to assign a configuration state $c_u \in \{1, 2, 3\}$ to each of $n$ communication nodes.
There are $m$ interference links, each connecting a pair of nodes.

To evaluate the configuration, each state is associated with a $3 \times 3$ transformation matrix $A$:
- State 1 uses $A_1 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$
- State 2 uses $A_2 = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}$
- State 3 uses $A_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

For each of the $m$ links connecting a pair of nodes $u$ and $v$, the link's resonance score is defined as the trace of the matrix product $A_{c_u} A_{c_v}^T$, where $A_{c_v}^T$ is the transpose of $A_{c_v}$, and the trace of a matrix is the sum of its main diagonal elements. 
Because the trace of $A_{c_u} A_{c_v}^T$ equals the trace of $A_{c_v} A_{c_u}^T$, the score of a link is the same regardless of the order of $u$ and $v$.

The overall network is considered fully separated if and only if the sum of the resonance scores across all $m$ links is exactly $0$.

Your task is to determine if there exists a state assignment that makes the network fully separated. If at least one valid assignment exists, you must identify the one that is lexicographically smallest.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). These represent the total number of nodes and the number of interference links, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that node $u$ and node $v$ are connected by an interference link. Each pair of nodes is connected by at most one link.

## Output
If no fully separated assignment can be found, print `NO` on a single line.
If a valid assignment is possible, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$) representing the state assigned to each respective node. Among all valid configurations, the sequence of states you output must be the lexicographically smallest (i.e., comparing the state of node 1 first, then node 2, and so forth).

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