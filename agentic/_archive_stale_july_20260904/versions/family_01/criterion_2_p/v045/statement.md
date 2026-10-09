# Problem B — Day and Night

Time limit: 1 s
Memory limit: 256 MB

The factory planning process requires dividing the workforce into two distinct operational periods, designated as Shift 1 and Shift 2. Human resources has collected employee data and identified specific pairs of personnel who cannot work together. Your task is to process this data: allocate every employee to exactly one of the two shifts so that no incompatible pair shares the same operational period. Once determined, this schedule will be forwarded to the payroll department. 

If a valid allocation cannot be achieved, you must indicate this. If it is possible, you must provide a valid schedule. To ensure a standardized result, if multiple valid schedules exist, you must output the one that is lexicographically smallest when the sequence of shift numbers ($1$ or $2$) for employees $1$ through $n$ is compared.

## Input
The first line contains two integers $n$ and $m$. The workforce size $n$ requires at least a single employee and is bounded by the factory's maximum capacity of $2 \cdot 10^5$ workers. The volume of incompatibility reports $m$ starts from zero and is capped at the same maximum capacity limit ($2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that employee $u$ and employee $v$ cannot share an operational period.

## Output
If there is no way to assign the shifts without violating an incompatibility, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, output $n$ space-separated integers $s_1 \dots s_n$ (where each $s_i \in \{1, 2\}$) representing the shift assigned to each employee. This sequence must be the lexicographically smallest valid assignment.

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
