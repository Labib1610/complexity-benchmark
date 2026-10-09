# Problem B — Quantum Sensor Calibration

Time limit: 1 s
Memory limit: 256 MB

You are calibrating a network of $n$ quantum sensors. Each sensor $i$ must be configured with a measurement basis $b_i \in \{1, 2\}$. 
The basis chosen dictates the observable matrix applied by the sensor:
- Choosing basis 1 configures the sensor with the Pauli-X matrix: $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$
- Choosing basis 2 configures the sensor with the Pauli-Z matrix: $Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$

There are $m$ entanglement links between specific pairs of sensors. 
For a successful joint measurement across an entanglement link between sensor $u$ and sensor $v$, their configured observable matrices, denoted $O_u$ and $O_v$, must anti-commute. That is, they must satisfy the matrix equation $O_u O_v + O_v O_u = \mathbf{0}$, where $\mathbf{0}$ is the $2 \times 2$ zero matrix.

Determine if a valid assignment of measurement bases exists for all sensors such that the observability condition is satisfied for all entanglement links. If no such assignment is possible, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of sensors connected by an entanglement link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $b_1 \dots b_n$ (each in $\{1,2\}$). 
If multiple valid assignments exist, you must resolve ties by choosing the assignment that assigns the smallest possible basis to sensor 1. If ties remain, among those, choose the one that assigns the smallest possible basis to sensor 2, and continue this sequential preference for smaller bases up to sensor $n$ (this is equivalent to the lexicographically smallest valid assignment).

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