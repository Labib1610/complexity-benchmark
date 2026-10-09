# Problem B — Logistics Safeguards

Time limit: 1 s   Memory limit: 256 MB

## Description

A logistics network relies on $n$ transit hubs. Each hub must be permanently assigned one of two operational states for the upcoming shift: ACTIVE or DORMANT.

The network management has drawn up $m$ contingency plans. Each plan consists of exactly two proposed safeguards. A safeguard is a specification of a particular hub and the state it needs to be in. 

A contingency plan breaks down if and only if both of its proposed safeguards are rejected by the final configuration. Equivalently, a plan is secured when at least one of its two safeguards is met by the network's configuration. 

Your task is to determine whether there is a single, global assignment of states to all $n$ hubs such that no contingency plan breaks down. If such a configuration exists, provide one; otherwise, report that the requirements are mutually contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Each of the following $m$ lines provides two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), representing the two safeguards of a contingency plan. 

A positive integer $k$ indicates the safeguard requires hub $k$ to be ACTIVE. A negative integer $-k$ indicates the safeguard requires hub $k$ to be DORMANT. 

Note that $l_1$ and $l_2$ in a plan may refer to the same hub, with the same or opposite signs.

## Output
If no valid configuration exists, print a single line NO.

Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 0 or 1, representing DORMANT and ACTIVE respectively) that form a valid configuration. Multiple valid configurations may exist; any one is accepted.

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