# Problem B — Production Line Configuration

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing plant operates $n$ distinct machines, each requiring calibration to either mode 1 or mode 0. To guarantee operational stability, the plant uses $m$ safety interlocks. Each interlock creates a dependency between a pair of machines based on specific reference conditions.

Determine if there is a way to calibrate all $n$ machines such that every safety protocol is satisfied. If such a plant-wide calibration is possible, provide one. Otherwise, indicate that a safe configuration is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$, where $|l_i| \le n$. These describe the reference conditions for an interlock. For a given $l_i$, if $l_i > 0$, the reference condition is machine $l_i$ in mode 1. If $l_i < 0$, the reference condition is machine $|l_i|$ in mode 0. 

The safety protocol enforced by each interlock dictates that whenever the machine for $l_1$ fails to match its reference condition, the machine for $l_2$ is strictly required to match its reference condition to prevent a shutdown. Because the interlocks are symmetric in their hardware wiring, this condition applies in reverse as well: whenever the machine for $l_2$ fails to match its reference condition, the machine for $l_1$ is strictly required to match its reference condition.

## Output
If there is no valid way to calibrate the machines without triggering a shutdown, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) representing the chosen mode for each machine from 1 to $n$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid calibrations may exist; any one is accepted. The same machine may be monitored by multiple interlocks.