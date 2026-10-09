# Problem B — System Configuration

Time limit: 1 s   Memory limit: 256 MB

A cloud provider must configure the operation mode for $n$ database instances. The configuration requires assigning each instance $i$ an operation mode $s_i$, which must be chosen from the set $\{1, 2\}$.

Each instance $i$ operates using a state transformation matrix $M_i$. The matrix depends on the assigned mode:
- If $s_i = 1$, $M_i = \begin{pmatrix} -8 & -5 & 4 & 5 \\ -10 & -6 & 5 & 6 \\ -16 & -10 & 8 & 10 \\ -10 & -6 & 5 & 6 \end{pmatrix}$

- If $s_i = 2$, $M_i = \begin{pmatrix} 6 & 1 & -2 & -2 \\ 10 & -4 & -2 & 0 \\ 10 & 13 & -6 & -10 \\ 13 & -12 & -1 & 4 \end{pmatrix}$

The system includes $m$ shared backup storage arrays, each connecting two specific database instances. A backup array continuously monitors the joint state of its two connected instances, $u$ and $v$. The array processes data by multiplying their state transformation matrices together.

A critical feedback loop occurs if a matrix product evaluates to the $4 \times 4$ zero matrix $Z$ (the matrix where all 16 elements are 0). To ensure stability, the configuration must guarantee that for every backup array connecting instances $u$ and $v$, the product of their matrices is not equal to $Z$. The backup array checks both data flow directions, so the stability requirement is that neither $M_u \times M_v$ nor $M_v \times M_u$ may equal $Z$.

You must assign a mode to each instance to satisfy all stability constraints across all backup arrays, or determine that no such configuration exists. If multiple valid configurations exist, the automated deployment system requires the configuration whose sequence of mode assignments $s_1 \dots s_n$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of database instances and the number of shared backup arrays.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that instances $u$ and $v$ share a backup array.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid configuration.

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