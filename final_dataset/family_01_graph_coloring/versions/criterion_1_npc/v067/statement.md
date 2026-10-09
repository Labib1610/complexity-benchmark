# Problem A — Factory Roster Regulations

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility employs $n$ technicians. The human resources department maintains a registry of personnel incompatibilities, which consists entirely of mutual friction records between specific pairs of individuals. According to the facility's strict operational guidelines, any two technicians who share a friction record must never be present during the same work period. The facility's daily schedule is divided into three distinct work periods, designated simply as 1, 2, and 3.

Given the registry of friction records, your objective is to determine whether it is possible to assign each of the $n$ technicians to exactly one of the three work periods without violating the operational guidelines. If such an allocation is possible, you must also provide a valid assignment.

## Input
The first line contains two integers $n$ and $m$ — the number of technicians and the number of friction records ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of technicians with a friction record.

## Output
If no valid schedule exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the work period assigned to technician $i$. Any valid schedule will be accepted.

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
