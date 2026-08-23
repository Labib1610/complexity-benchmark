# Problem A — Shift Allocation Protocol

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates three daily shifts, numbered 1, 2, and 3. There are $n$ employees, and management has compiled a list of incompatible employee pairs who cannot work the same shift.

The allocation process evaluates employees in numerical order (from 1 to $n$). For each employee, the system prefers to assign shift 1, then shift 2, and finally shift 3. Your goal is to determine a sequence of shifts $s_1, s_2, \dots, s_n$ that respects these local priorities as much as possible while ensuring no incompatible employees share a shift. Formally, among all completely valid schedules, you must find and output the one that is lexicographically smallest.

If no combination of assignments can separate all incompatible pairs across the three shifts, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n(n-1)/2$) — the number of employees and the number of incompatible pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of incompatible employees.

## Output
If a valid schedule cannot be formed, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the shift assigned to each employee. This sequence must be the lexicographically smallest valid assignment.

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
