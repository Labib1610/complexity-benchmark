# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description
A control panel features $n$ binary switches that must be configured prior to a system test. The commissioning team has provided $m$ safety rules. Each rule monitors a pair of target switch settings. A target setting is defined by a switch index and a desired position (either ON or OFF). 

A safety rule triggers a system fault if and only if the panel's final configuration contradicts both of its monitored target settings at the same time. If the configuration matches one or both of the target settings, the rule remains silent.

Your task is to determine whether a global configuration exists for all $n$ switches such that zero system faults are triggered. If such a configuration exists, you must provide it. If no such configuration is possible, you must report that the system is unconfigurable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of switches and the number of safety rules, respectively.
Each of the following $m$ lines contains two non-zero signed integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$). For each target setting, the absolute value indicates the switch index. A positive integer indicates a target setting of ON, while a negative integer indicates a target setting of OFF. The two target settings in a rule may refer to the same switch, and may be identical or opposite.

## Output
If no fault-free configuration exists, print a single line containing `NO`.
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
Multiple valid configurations may exist; any one of them is accepted. The same switch may be monitored by multiple rules.