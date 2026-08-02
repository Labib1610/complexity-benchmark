# Sensor Network Phase Calibration

Time limit: 1 s   Memory limit: 256 MB

An experimental physics facility operates a network of $n$ sensors, numbered $1$ through $n$. Each sensor must be configured to operate in one of two distinct phase settings, labeled $1$ or $2$.

Due to local electromagnetic coupling, certain pairs of sensors experience severe cross-talk if they share the same phase setting. There are $m$ such mutually interfering pairs. You are tasked with determining whether it is possible to set every sensor to setting $1$ or $2$ such that no interfering pair shares the same setting.

If one or more valid configurations exist, select the configuration sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest. If no valid configuration exists, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of sensors and the number of interference constraints, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), specifying that sensor $u$ and sensor $v$ must not be assigned the same phase setting.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid configuration.

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
