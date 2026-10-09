# Valve Network Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description
A fluid processing facility operates $n$ distinct valves. Each valve must be permanently configured to either an OPEN (1) or CLOSED (0) position. No intermediate positions are supported.

During system analysis, $m$ operational vulnerabilities were cataloged. Each vulnerability is characterized by a set of three specific valve states. For example, a vulnerability might list valve 2 as OPEN, valve 5 as CLOSED, and valve 7 as OPEN.

A vulnerability is successfully mitigated if the facility's actual overall configuration matches at least one of the three valve states associated with it. If the facility's configuration fails to match all three of the specified states for a given vulnerability, a system failure is triggered.

The facility's piping topology imposes the following guarantees on the vulnerability catalog:
- The total sum of the valve indices (the absolute values $|v_i|$) across all $m$ vulnerabilities will never exceed $108,000$.
- For any single vulnerability, the numerical difference between the highest and lowest valve indices referenced is strictly less than $90$.

Your task is to determine whether there exists a global configuration for all $n$ valves that mitigates every single cataloged vulnerability simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the subsequent $m$ lines contains three non-zero signed integers $v_1, v_2, v_3$, with $|v_i| \le n$.
A positive integer $x$ indicates that the vulnerability lists valve $x$ as OPEN. A negative integer $x$ indicates that the vulnerability lists valve $|x|$ as CLOSED.

## Output
If no universally safe configuration exists, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \dots, c_n$ (each in $\{0, 1\}$), where $c_i$ represents the state of valve $i$ (1 for OPEN, 0 for CLOSED). If multiple safe configurations exist, any of them will be accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each vulnerability lists exactly three states. The same valve may be listed more than once in a single vulnerability.
