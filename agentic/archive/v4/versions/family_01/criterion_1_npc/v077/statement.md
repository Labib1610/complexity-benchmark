# Shift Roster Allocation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates three distinct daily shifts, designated by numerical codes 1, 2, and 3. The plant employs $n$ individual staff members. Certain pairs of staff members share incompatibilities and must not be scheduled during the same operational shift.

Management requires a schedule that places every staff member into exactly one shift such that no incompatible pair shares a shift. Furthermore, to satisfy union rules, every assigned shift number must be an integer between 1 and 3 inclusive, and no staff member may be assigned to more than one shift.

If multiple valid shift rosters exist, management requires the schedule that yields the lexicographically smallest sequence of shift choices $(s_1, s_2, \dots, s_n)$ (comparing $s_1$ first, then $s_2$, and so forth). If no compliant assignment is possible, report this condition.

## Input
The first line of input contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), denoting the number of staff members and the number of incompatible pairs, respectively.

The following $m$ lines each contain two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that staff member $u$ and staff member $v$ are incompatible.

## Output
If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$, where $s_i \in \{1, 2, 3\}$ represents the shift assigned to staff member $i$. Output the lexicographically smallest valid assignment if multiple exist.

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
