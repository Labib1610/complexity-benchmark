# Facility Duty Roster Allocation

Time limit: 2 s   Memory limit: 256 MB

A research facility needs to assign its $n$ staff members (indexed from $1$ to $n$) to daily duty shifts. Exactly three distinct work shifts are available, designated as $1$, $2$, and $3$. Every staff member must be assigned to exactly one of these shifts.

Due to operational conflict constraints, $m$ specific pairs of staff members cannot be assigned to the same duty shift.

Determine whether a valid duty shift assignment exists for all $n$ staff members such that no conflicting pair works the same shift. If multiple valid assignments exist, output the assignment sequence $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest (that is, comparing $s_1$ first, then $s_2$, and so on).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of staff members and the number of conflicting pairs.
Each of the next $m$ lines contains two space-separated integers $u\ v$ ($1 \le u, v \le n$, $u \neq v$), indicating that staff member $u$ and staff member $v$ cannot share a shift.

## Output
If no valid assignment exists, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the shift assigned to staff member $i$. Output the lexicographically smallest sequence among all valid assignments.

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