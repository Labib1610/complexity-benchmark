# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates in two daily shifts: shift 1 and shift 2. Each of the $n$ staff members must be assigned to exactly one of these shifts.

Certain tasks require specialized equipment. There are $m$ pairs of staff members who rely on the same unique piece of equipment. To ensure the equipment is properly utilized across the day without overlapping, exactly one staff member from each such pair must be assigned to shift 1, and the other must be assigned to shift 2.

You must determine a valid shift assignment for all staff members that satisfies all equipment requirements, or report that no such schedule is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a pair of staff members who share equipment.

## Output
If no valid shift schedule exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $s_1, \dots, s_n$ (each $s_i \in \{1, 2\}$), where $s_i$ is the shift assigned to staff member $i$. If there are multiple valid schedules, output the one that is lexicographically smallest.

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