# Problem B — Quantum Sensor Calibration

Time limit: 1 s
Memory limit: 256 MB

You are calibrating a network of $n$ quantum sensors. Each sensor $i$ must be configured with a measurement basis $b_i \in \{1, 2\}$. 
Choosing basis 1 configures the sensor with the calibration matrix: 
$C_1 = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$

Choosing basis 2 configures the sensor with the calibration matrix: 
$C_2 = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$

There are $m$ interference links between specific pairs of sensors. 
For a successful joint measurement across an interference link between sensor $u$ and sensor $v$, their configured matrices, denoted $C_u$ and $C_v$, must combine to form a non-singular system. That is, the matrix sum $C_u + C_v$ must be invertible (its determinant must be non-zero).

Determine if a valid assignment of measurement bases exists for all sensors such that the invertibility condition is satisfied for all interference links. If no such assignment is possible, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of sensors connected by an interference link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $b_1 \dots b_n$ (each in $\{1,2\}$). 
If multiple valid assignments exist, you must output the lexicographically smallest valid assignment (i.e., resolve ties by preferring basis 1 over basis 2 for sensor 1, then for sensor 2, and so on).

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