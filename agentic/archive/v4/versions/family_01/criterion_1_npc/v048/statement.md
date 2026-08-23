# Resource Allocation across Three Operational Windows

**Time limit:** 2 s  
**Memory limit:** 256 MB

An industrial facility operates across three distinct operational windows each day, labeled 1, 2, and 3. There are $n$ staff members who must each be assigned to exactly one operational window. Certain pairs of staff members have interpersonal conflicts and cannot be scheduled in the same window.

Your task is to determine whether it is possible to assign every staff member to an operational window such that no conflicting pair shares a window. If possible, find the valid assignment that yields the lexicographically smallest sequence of window assignments.

## Input
The first line of the input contains two integers $n$ and $m$.
* The total staff count $n$ satisfies $1 \le n \le 40$, constrained by the facility's safety ceiling of 40 occupants.
* The number of conflict pairs $m$ ranges from $0$ up to the maximum possible count of distinct pairs among the staff, $\frac{n(n-1)}{2}$.

Each of the next $m$ lines contains two distinct integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that staff member $u$ and staff member $v$ cannot share an operational window.

## Output
If no valid schedule exists that satisfies all conflict constraints, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), where $s_i$ denotes the window assigned to staff member $i$. If multiple valid schedules exist, output the one with the lexicographically smallest sequence $(s_1, s_2, \dots, s_n)$.

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
