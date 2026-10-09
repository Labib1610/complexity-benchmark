# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility employs $n$ workers, who are identified by integers from 1 to $n$. The facility operates continuously by utilizing exactly two distinct work periods: shift 1 and shift 2. Over time, management has compiled a list of $m$ specific pairs of workers who cannot collaborate effectively. A strict operational rule dictates that any two workers who form one of these incompatible pairs must be assigned to completely different work periods.

Your task is to determine whether the entire workforce can be distributed between the two shifts in complete compliance with this operational rule. If a compliant distribution exists, you must provide the specific assignment sequence $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$ is the shift assigned to worker $i$) that is lexicographically smallest. If no such distribution is possible, you must report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of workers who cannot collaborate.

## Output
If there is no way to assign the shifts without violating the operational rule, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each either 1 or 2), representing the lexicographically smallest valid assignment of shifts.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
