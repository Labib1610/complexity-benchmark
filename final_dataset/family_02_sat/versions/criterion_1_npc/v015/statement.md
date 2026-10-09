# Control Panel Commissioning

Time limit: 2 s   Memory limit: 256 MB

## Description

A control panel contains **n** toggle switches. Prior to operation, each switch must be set to either the ACTIVE or INACTIVE state. The panel is wired with **m** safety interlocks. Each interlock enforces exactly three switch requirements. A requirement dictates that a specific switch must be in a specific state. An interlock operates safely if and only if at least one of its three requirements is satisfied by the current configuration. Your objective is to determine whether there exists a single configuration for all **n** switches that satisfies every interlock simultaneously. If a valid configuration exists, you must provide it; otherwise, you must declare the system over-constrained.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the following **m** lines describes one safety interlock using three non-zero integers $l_1, l_2, l_3$ ($|l_i| \le n$).
A positive integer $x$ specifies a requirement that switch $x$ is ACTIVE.
A negative integer $-x$ specifies a requirement that switch $x$ is INACTIVE.
The same switch may be referenced multiple times within the same interlock.

## Output
If no configuration can satisfy all interlocks, print a single line containing `NO`.
If a valid configuration exists, print `YES` on the first line.
On the second line, print **n** integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{0, 1\}$ represents the state of switch $i$ (1 for ACTIVE, 0 for INACTIVE).
Any valid configuration will be accepted.

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
