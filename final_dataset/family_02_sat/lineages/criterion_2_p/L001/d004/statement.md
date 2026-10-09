# Problem B — Logistics Safeguards

Time limit: 1 s   Memory limit: 256 MB

## Description

Management of a logistics network must finalize the operational schedule for its $n$ transit hubs. Every hub $i$ must be assigned a phase state $P(i) \in \{0, 1\}$.

Safety inspectors have completed $m$ vulnerability assessments. Each assessment provides two parameters $l_1$ and $l_2$. For any parameter $v$, we define its target requirement $R(v) = 1$ if $v > 0$, and $R(v) = 0$ if $v < 0$. The hub it refers to is $|v|$.

An assessment is considered *exposed* if the assigned phase of the hub for its first parameter does not match its target requirement, AND the assigned phase of the hub for its second parameter also does not match its target requirement. In other words, an assessment with parameters $l_1$ and $l_2$ is exposed if and only if $P(|l_1|) \neq R(l_1)$ and $P(|l_2|) \neq R(l_2)$.

A critical failure occurs if there is at least one exposed assessment in the network. Your task is to determine whether it is possible to assign a phase state to every hub such that zero exposed assessments occur. If such a schedule can be formed, you must provide one.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$). For clarity, $n$ is up to 100000 and $m$ is up to 200000.

Each of the following $m$ lines provides two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), representing the two parameters of a vulnerability assessment. 

Note that $l_1$ and $l_2$ in an assessment may refer to the same hub, with the same or opposite signs. A hub may appear in any number of assessments, and identical assessments may repeat.

## Output
If no safe schedule is possible, print a single line NO.

Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 0 or 1, representing the phase state $P(i)$ for hub $i$) that form a valid schedule. Multiple valid schedules may exist; any one is accepted.

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