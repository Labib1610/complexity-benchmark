# Problem A — Signal Router Integration

Time limit: 2 s   Memory limit: 256 MB

## Description

A telecommunications facility manages $n$ signal routers. Prior to deployment, every router must be permanently locked into one of two routing modes: primary (represented by 1) or secondary (represented by 0). No router may remain unconfigured.

During the integration phase, the facility runs $m$ automated safety protocols. Each protocol monitors exactly three router states. A monitored state is given as a non-zero integer $x$: a positive value $x > 0$ indicates the protocol is monitoring router $x$ for the primary mode, while a negative value $x < 0$ indicates it is monitoring router $|x|$ for the secondary mode. A monitored state is considered present if the router is configured to the specified mode, and absent if it is configured to the opposite mode.

A safety protocol triggers a system halt if and only if all three of its monitored states are absent. A protocol that does not halt the system imposes no further restrictions. Routers are often monitored by multiple protocols, potentially for conflicting modes across different protocols.

Your objective is to determine whether it is possible to configure every router such that zero safety protocols trigger a system halt. If it is possible, you must output one such valid configuration.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero integers $v_1, v_2, v_3$, with $|v_i| \le n$. These represent the three states monitored by that protocol.

## Output
If no valid configuration exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i$ is the mode assigned to router $i$. Any valid configuration is accepted.

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
Each protocol monitors exactly three states. The same router index may appear more than once within a single protocol.
