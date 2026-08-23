# Schedule Compatibility Assignment

Time limit: 2 s   Memory limit: 256 MB

An industrial facility manages a headcount of $n$ staff members, identified by numbers $1$ through $n$. The facility operates across three sequential time blocks designated as $1$, $2$, and $3$.

Certain pairs of staff members are flagged as mutually incompatible and cannot be assigned to work during the same time block. Every staff member must be assigned to exactly one of the three available time blocks such that no two mutually incompatible staff members share a time block.

If multiple valid schedule configurations exist, select the configuration that minimizes the assigned time block number of staff member 1; if ties remain, minimize for staff member 2, then staff member 3, and so on up to staff member $n$. If no valid configuration satisfies all incompatibility conditions, report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ — the headcount of staff members and the number of incompatible pairings ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that staff member $u$ and staff member $v$ are mutually incompatible.

## Output
If no valid schedule configuration exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the time block assigned to staff member $i$. Among all valid schedule configurations, output the sequence prioritized by the tie-breaking rule.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
