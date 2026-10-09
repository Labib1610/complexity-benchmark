# Problem A — Shift Allocation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates continuously using three daily shifts, designated 1, 2, and 3. You are tasked with assigning each of the $n$ employees to exactly one of these shifts.

To maintain productivity, certain pairs of employees who perform redundant tasks or have personal disagreements cannot be scheduled on the same shift. In many practical scenarios, the workforce can largely be partitioned between the first two primary shifts, utilizing the third shift only when necessary to accommodate any remaining incompatibilities. Since you are not asked to balance the shift sizes, minimize the use of the third shift, or optimize any other metric, the assignment conditions are highly flexible. You only need to find a single feasible schedule.

Your objective is to determine if there is any valid assignment of employees to the three shifts such that no two incompatible employees work at the same time, and to output one such schedule if it exists.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of employees and the number of incompatible pairs.
Following this are $m$ lines, each containing two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that employee $u$ and employee $v$ cannot be assigned to the same shift. Each incompatible pair is listed at most once.

## Output
If there is no way to assign all employees to the three shifts without violating an incompatibility constraint, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ is the shift assigned to employee $i$. If multiple valid schedules exist, you may output any of them.

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
