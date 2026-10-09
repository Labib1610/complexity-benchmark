# Problem B — Plant Routing Guidelines

Time limit: 1 s   Memory limit: 256 MB

## Description

A chemical plant operates a manifold of $n$ flow-control valves. Each valve must be configured to either state 1 (routing to the reactor) or state 0 (routing to the bypass).

The plant's safety protocol consists of $m$ hardware interlocks. Each interlock is wired to monitor two specific valve states, represented in the system by two non-zero integers. An integer $v > 0$ means the interlock monitors valve $v$ for state 1. An integer $v < 0$ means the interlock monitors valve $|v|$ for state 0.

Because of its physical wiring, an interlock triggers a plant shutdown if and only if neither of the two valve states it monitors is present in the configuration. Your task is to determine if there is a single combination of states for all $n$ valves that prevents any interlocks from triggering a shutdown. If such a combination exists, you must provide it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$, with $|l_i| \le n$. These represent the two valve states monitored by a single interlock.

## Output
If no combination of valve states can prevent a shutdown, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in $\{0, 1\}$) representing a valid configuration of the $n$ valves.

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
Multiple valid combinations may exist; providing any one is accepted. The same valve state may be monitored by multiple interlocks, and a single interlock may monitor the exact same valve state twice.
