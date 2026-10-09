# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description
A control panel features $n$ binary switches that must be configured prior to a system test. The commissioning team has provided $m$ operational requirements. Each requirement dictates that out of a specific pair of switch states, at least one state must be active during the test. A switch state refers to a particular switch being set to a specific polarity (either ON or OFF). 

Your task is to determine whether it is possible to configure all $n$ switches simultaneously such that every single one of the $m$ requirements is fulfilled. If such a configuration exists, you must provide it. If no global configuration can satisfy all requirements simultaneously, you must report that the system is unconfigurable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of switches and the number of requirements, respectively.
Each of the following $m$ lines contains two non-zero signed integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$). For each requirement, the absolute value indicates the switch index, and the sign indicates the required polarity (positive for ON, negative for OFF). At least one of the two specified polarities must be matched by the final switch configuration.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing a valid assignment, where $1$ denotes ON and $0$ denotes OFF.

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
Multiple valid configurations may exist; any one of them is accepted. The same switch may be referenced in multiple requirements.