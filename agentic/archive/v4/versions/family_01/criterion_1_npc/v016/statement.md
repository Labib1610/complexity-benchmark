# Problem A — Shift Scheduling Under Friction

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates continuous production across 3 available work shifts, identified by integers 1, 2, and 3. There are $n$ personnel, indexed from 1 to $n$. Operational logs indicate that $m$ specific pairs of personnel experience workplace friction and must never be scheduled onto the same shift.

Your objective is to assign every employee to exactly one shift such that no pair with logged friction shares a shift. Any shift may host anywhere from 0 to $n$ employees, provided no two conflicting workers end up on the same shift. If an employee experiences no friction with anyone, that employee may be placed on any shift from 1 to 3, subject to global validity and optimization criteria.

If at least one valid schedule exists, identify the one that yields the lexicographically smallest list of assigned shifts $(s_1, s_2, \dots, s_n)$. That is, when comparing two valid assignments, the preferred assignment is the one with the smaller shift number at the first index where they differ.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of personnel and the number of friction pairs, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that employee $u$ and employee $v$ have workplace friction and cannot share a shift. No friction pair is listed more than once.

## Output
If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ denotes the assigned shift for employee $i$. If multiple valid schedules exist, output the one that is lexicographically smallest.

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
