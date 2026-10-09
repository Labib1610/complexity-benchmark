# Problem B — Logistics Safeguards

Time limit: 1 s   Memory limit: 256 MB

## Description

Management of a logistics network must finalize the operational schedule for its $n$ transit hubs. For the upcoming shift, every hub will be designated as either ACTIVE or DORMANT.

Safety inspectors have completed $m$ vulnerability assessments. Each assessment highlights a pair of operational conditions. An individual condition specifies a required state for a particular hub. The inspectors have determined that a critical failure will occur if and only if the finalized schedule rejects both of the conditions highlighted in a given assessment.

Your task is to determine whether it is possible to assign a state to every hub such that zero critical failures occur across the network. If such a schedule can be formed, you must provide one.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Each of the following $m$ lines provides two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), representing the two conditions highlighted by a vulnerability assessment. 

A positive integer $k$ means the condition requires hub $k$ to be ACTIVE. A negative integer $-k$ means the condition requires hub $k$ to be DORMANT. 

Note that $l_1$ and $l_2$ in an assessment may refer to the same hub, with the same or opposite signs.

## Output
If no safe schedule is possible, print a single line NO.

Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 0 or 1, representing DORMANT and ACTIVE respectively) that form a valid schedule. Multiple valid schedules may exist; any one is accepted.

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