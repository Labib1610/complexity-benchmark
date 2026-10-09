# Problem B — Logistics Safeguards

Time limit: 1 s   Memory limit: 256 MB

## Description
Management of a logistics network must finalize the operational schedule for its $n$ transit hubs. Every hub $i$ must be assigned a phase state $s_i \in \{0, 1\}$.

Safety inspectors have completed $m$ vulnerability assessments. Each assessment provides two non-zero integer parameters $l_1$ and $l_2$. 

An assessment raises a critical failure if and only if the assigned phase states for the designated hubs $u = |l_1|$ and $v = |l_2|$ satisfy the following equality:
$$l_1 (2 s_u - 1) + l_2 (2 s_v - 1) = - (|l_1| + |l_2|)$$

Your task is to determine whether it is possible to assign a phase state $s_i \in \{0, 1\}$ to every hub such that zero critical failures occur across all $m$ assessments. If such a schedule can be formed, you must provide one.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Each of the following $m$ lines provides two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), representing the two parameters of a vulnerability assessment. 

Note that $l_1$ and $l_2$ in an assessment may refer to the same hub, with the same or opposite signs. A hub may appear in any number of assessments, and identical assessments may repeat.

## Output
If no safe schedule is possible, print a single line NO.

Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 0 or 1, representing the phase state $s_i$ for hub $i$) that form a valid schedule. Multiple valid schedules may exist; any one is accepted.

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