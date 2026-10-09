# Problem B — Quantum Sensor Calibration

Time limit: 1 s
Memory limit: 256 MB

You are calibrating a network of $n$ quantum sensors. Each sensor $i$ must be configured with a measurement basis $b_i \in \{1, 2\}$. 
Each sensor processes a quantum state represented by an integer $x \in \{0, 1, 2, 3, 4\}$.

Choosing basis 1 configures the sensor to apply the state transformation $f_1(x) = (2x + 1) \bmod 5$.
Choosing basis 2 configures the sensor to apply the state transformation $f_2(x) = (3x + 2) \bmod 5$.

There are $m$ interference links between specific pairs of sensors. 
For a successful joint measurement across an interference link between sensor $u$ and sensor $v$, the combined effect of their transformations must be perfectly transparent. That is, if any state $x$ is processed sequentially by the transformation of sensor $u$ and then by the transformation of sensor $v$, the final state must evaluate back to exactly $x$, for all possible initial states $x \in \{0, 1, 2, 3, 4\}$.

Determine if a valid assignment of measurement bases exists for all sensors such that this transparency condition is satisfied for all interference links. If no such assignment is possible, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of sensors connected by an interference link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $b_1 \dots b_n$ (each in $\{1,2\}$). 
If multiple valid assignments exist, you must output the assignment that minimizes the sequence $b_1, b_2, \dots, b_n$ when it is interpreted as an $n$-digit base-3 integer (where $b_1$ is the most significant digit and $b_n$ is the least significant digit).

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