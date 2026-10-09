# Problem C — Cross-Referenced Flags

Time limit: 2 s
Memory limit: 256 MB

You are auditing a strict access-control system containing $n$ user profiles, numbered $1$ to $n$. Each profile maintains exactly $n$ boolean permission flags, which are all initially set to `false`.

The system logs $m$ mutual authorizations. Each authorization is a pair $(u, v)$, which updates the system by setting flag $v$ in profile $u$ to `true`, and setting flag $u$ in profile $v$ to `true`.

A critical security vulnerability occurs if there is a "tri-level escalation". This happens when three distinct profile IDs $a$, $b$, and $c$ (with $a < b < c$) satisfy the following state:
1. In profile $a$, flag $b$ and flag $c$ are both `true`.
2. In profile $b$, flag $c$ is `true`.

Because authorizations are mutual, this configuration creates a closed loop of permissions among the three profiles.

You must identify the profiles involved in this vulnerability. It is guaranteed that the log produces at least one such configuration.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 200000)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of profiles that mutually authorized each other.
It is guaranteed that at least one tri-level escalation exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, representing the IDs of the three profiles. Output the lexicographically smallest such combination (smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```