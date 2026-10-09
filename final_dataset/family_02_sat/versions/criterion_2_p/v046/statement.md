# Problem B — Paired Toggle Contracts

Time limit: 1 s   Memory limit: 256 MB

## Description

A build system is configured by setting $n$ toggles to either an active (1) or inactive (0) state. The system's requirements are defined by $m$ compatibility contracts. Each contract lists exactly two required toggle states. A positive index indicates the toggle must be active, while a negative index indicates it must be inactive. For the build to proceed, every contract must have at least one of its two listed states fulfilled by the final configuration. Because each contract pairs exactly two states, failing to fulfill one side of the contract strictly enforces the fulfillment of the other. You must determine if there is a global assignment of the $n$ toggles that satisfies all $m$ contracts simultaneously, and output a valid assignment if one exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$, representing the two states in a contract. The absolute value of each integer is at most $n$ ($|l_i| \le n$).

## Output
If there is no valid configuration that satisfies all contracts, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing a valid configuration for the toggles in order from $1$ to $n$.

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
Multiple valid configurations may exist; any one is accepted. The same toggle may appear in multiple contracts.
