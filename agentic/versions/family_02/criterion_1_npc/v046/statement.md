# Problem A — Facility Pressure Test Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
During the commissioning of a facility, a pressure test requires configuring $n$ manual isolation valves. Every valve must be locked in either the OPEN or CLOSED position; no intermediate states are allowed. 

The safety system enforces $m$ distinct interlock checks. Each check monitors exactly three valve conditions, where a condition specifies a particular valve and its required position (OPEN or CLOSED). A check passes if at least one of its three monitored conditions is met. 

The same valve may be monitored by multiple checks in conflicting positions, and may even appear multiple times within a single check. Determine if there is a single global configuration for all $n$ valves that passes all $m$ checks simultaneously, and if so, output it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
The following $m$ lines each represent one interlock check. Each line contains three non-zero integers $c_1, c_2, c_3$, where the absolute value $|c_i|$ represents the valve number ($1 \le |c_i| \le n$). A positive integer means the condition requires the valve to be OPEN, while a negative integer means the condition requires the valve to be CLOSED.

## Output
If no configuration can satisfy all checks simultaneously, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $v_1, v_2, \dots, v_n$ separated by spaces (each in $\{0, 1\}$), where $v_i = 1$ if valve $i$ is OPEN, and $v_i = 0$ if valve $i$ is CLOSED. If multiple valid configurations exist, any of them will be accepted.

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
