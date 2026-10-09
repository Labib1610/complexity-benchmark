# Problem B — Factory Tuning

Time limit: 1 s   Memory limit: 256 MB

The factory requires each of its $n$ machines to be set to a power mode $s_i \in \{1, 2\}$. There are $m$ interference links between specific pairs of machines.

To evaluate a configuration of power modes, the factory calculates two types of potentials:
- For each machine $i$, its *node potential* is defined as $d_i \cdot s_i^2$, where $d_i$ is the number of interference links connected to machine $i$.
- For each interference link between machine $u$ and machine $v$, its *edge potential* is defined as $2 \cdot s_u \cdot s_v$.

The system's *total harmonic potential* is the sum of the node potentials of all $n$ machines, minus the sum of the edge potentials of all $m$ links.

A legacy controller accepts the configuration if and only if the total harmonic potential is exactly equal to $m$.

You must assign a power mode to every machine such that the configuration is accepted by the controller.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a linked pair of machines.

## Output
If no valid assignment of modes exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment. (An assignment $s$ is lexicographically smaller than $t$ if at the first index $i$ where they differ, $s_i < t_i$.)

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