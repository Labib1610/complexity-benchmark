# Problem A — Signal Router Integration

Time limit: 2 s   Memory limit: 256 MB

## Description

A telecommunications facility manages a network of $n$ signal routers. Prior to deployment, every single router must be permanently locked into one of two routing modes: active (represented by 1) or passive (represented by 0). No router may remain unconfigured.

During the integration phase, the facility runs $m$ automated safety protocols. Each protocol observes exactly three specific router conditions. An observed condition is defined by a non-zero integer $x$: a positive value $x > 0$ means the protocol requires router $x$ to be in the active mode, while a negative value $x < 0$ means it requires router $|x|$ to be in the passive mode. An observed condition is considered fulfilled if the router is configured to the required mode, and unfulfilled if it is configured to the opposite mode.

A safety protocol triggers a system halt if and only if all three of its observed conditions are unfulfilled. A protocol that does not halt the system imposes no further restrictions. Routers are often observed by multiple protocols, potentially requiring conflicting modes across different protocols.

Your objective is to determine whether it is possible to configure every router such that zero safety protocols trigger a system halt. If it is possible, you must output one such valid configuration.

## Input
The first line contains two integers $n$ and $m$. The facility consists of exactly 6 physical racks, each capable of holding 15 routers, meaning $n$ is at least 1 and at most the facility's total router capacity. The integration system allocates memory for exactly 16 protocol banks, each fitting 25 protocols, meaning $m$ is non-negative and at most the total protocol capacity of these banks.

Each of the next $m$ lines contains three non-zero integers $v_1, v_2, v_3$, representing the three conditions observed by that protocol. The absolute value of any $v_i$ will not exceed $n$.

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
Each protocol observes exactly three conditions. The same router index may appear more than once within a single protocol.
