# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description
A control panel features $n$ binary switches that must be configured prior to a system test. The commissioning team has provided $m$ hardware interlocks. Each interlock coordinates two expected positions (either ON or OFF) across a pair of switches.

An interlock restricts the configuration by establishing a conditional dependency. If the first switch is placed in the opposite of its expected position, the interlock engages and strictly requires the second switch to be placed in its expected position. Because the mechanism is symmetric, if the second switch is placed in the opposite of its expected position, it requires the first switch to be placed in its expected position. If both switches are placed in their expected positions, the interlock remains dormant and imposes no restrictions.

Your task is to determine whether a global configuration exists for all $n$ switches such that every interlock is satisfied (meaning no interlock's requirements are violated). If such a configuration exists, you must provide it. If no such configuration is possible, you must report that the system is unconfigurable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of switches and the number of interlocks, respectively.

Each of the following $m$ lines contains two non-zero signed integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$). For each expected position, the absolute value indicates the switch index. A positive integer defines an expected position of ON, while a negative integer defines an expected position of OFF. The two expected positions in an interlock may refer to the same switch, and may be identical or opposite.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing a valid configuration, where $1$ denotes ON and $0$ denotes OFF.

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
Multiple valid configurations may exist; any one of them is accepted. The same switch may be monitored by multiple interlocks.