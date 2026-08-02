# Operational Shift Assignment

Time limit: 2 s   Memory limit: 256 MB

A facility manages a team of $n$ staff members, labeled $1$ through $n$. Each staff member must be assigned to one of three available work shifts: shift $1$, shift $2$, or shift $3$.

There are $m$ specified pairs of staff members who have interpersonal conflicts and cannot be assigned to the same shift. 

Determine whether a valid shift schedule exists such that no conflicting pair of staff members works during the same shift. If one or more valid schedules exist, find the schedule that yields the lexicographically smallest sequence of shift choices when listed in order from staff member $1$ to staff member $n$.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of staff members and the number of conflicting pairs, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that staff member $u$ and staff member $v$ have a conflict and cannot share the same shift.

## Output
If no valid shift schedule exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ represents the shift assigned to staff member $i$. Among all valid assignments, output the one that is lexicographically smallest.

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
