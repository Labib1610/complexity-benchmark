# Problem A — Eclipse Protocol Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A satellite has $n$ internal subsystems. During the upcoming eclipse, each subsystem must be explicitly commanded to either the ACTIVE or STANDBY state. There is no intermediate state.

The science team has scheduled $m$ observation protocols for the eclipse. Each protocol defines exactly three acceptable operational conditions. A condition specifies a particular subsystem and requires it to be either ACTIVE or STANDBY. 

A protocol is successfully executed if at least one of its three conditions is met by the satellite's overall state. If none of the three conditions are met, the protocol fails. Determine if there is a single, static configuration of all $n$ subsystems that successfully executes all $m$ protocols simultaneously. If such a configuration exists, output it; otherwise, report that the schedule is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines describes one protocol using three non-zero integers $c_1$, $c_2$, and $c_3$.
The absolute value $|c_i|$ identifies the subsystem ($1 \le |c_i| \le n$).
A positive integer means the condition requires the subsystem to be ACTIVE.
A negative integer means the condition requires the subsystem to be STANDBY.
The same subsystem may be referenced more than once within the same protocol.

## Output
If no single configuration can execute all protocols, print NO on a single line.
Otherwise, print YES on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i$ is the state of subsystem $i$ ($1$ for ACTIVE, $0$ for STANDBY). Any valid configuration is accepted.

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
