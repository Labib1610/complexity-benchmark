# Problem B — System Configuration

Time limit: 1 s   Memory limit: 256 MB

A cloud provider must configure the operation mode for $n$ database instances. The configuration requires assigning each instance $i$ an operation mode $s_i$, which must be chosen from the set $\{1, 2\}$.

Each instance $i$ maintains a state transformation matrix $M_i$, defined as:

$$ M_i = \begin{pmatrix} 3 & -4 \\ 2 & -3 \end{pmatrix}^{s_i} $$

Certain pairs of instances share a dedicated backup storage array. When two instances $u$ and $v$ share a backup array, the array synchronizes them by computing their combined transformation matrix $C_{u,v} = M_u \times M_v$.

To maintain system stability, the backup array's resonance detector requires that this combined matrix $C_{u,v}$ must not be equal to the $2 \times 2$ identity matrix $I$. Specifically, if $C_{u,v} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, the array will experience a feedback loop and synchronization will fail. 

You must assign a mode to each instance to satisfy all stability constraints, or determine that no such configuration exists. If multiple valid configurations exist, the automated deployment system requires the configuration whose sequence of mode assignments $s_1 \dots s_n$ is lexicographically smallest.

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