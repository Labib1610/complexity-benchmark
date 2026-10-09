# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description
During the commissioning of a control panel, engineers must configure a sequence of $n$ toggle switches. Each switch can be placed in an active (1) or inactive (0) position. The system is monitored by a set of $m$ safety protocols. Every protocol is defined by exactly two conditions, where a condition refers to a specific switch being in a specific position.

A safety protocol will register a critical fault if the panel's configuration violates both of its defined conditions simultaneously. Consequently, if a configuration fails to satisfy one condition of a protocol, the system inherently demands that the protocol's other condition is satisfied to prevent a fault. These interconnected dependencies can create extensive cascades of mandatory switch positions.

Your task is to determine whether it is possible to configure all $n$ switches such that zero critical faults are registered across the entire panel. If such a configuration is possible, you must provide one; otherwise, you must declare that the protocols cannot be satisfied.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of switches and the number of safety protocols, respectively.

Each of the following $m$ lines provides two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$), representing the two conditions for a protocol. A positive integer $+x$ indicates a condition where switch $x$ must be active (1), while a negative integer $-x$ indicates a condition where switch $x$ must be inactive (0). To prevent a fault, at least one of these two conditions must be present in the final configuration.

## Output
If there is no way to configure the switches without triggering a fault, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same switch index may appear in multiple protocols.
