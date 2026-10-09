# Production Schedule

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant runs continuously, dividing its daily operations into three distinct production shifts, designated as 1, 2, and 3. Every machine operator on the payroll must be assigned to exactly one of these three shifts.

The human resources department maintains a list of past safety incidents. Each record documents a conflict between a specific pair of operators. To ensure a safe working environment, any two operators who are listed together in an incident record are strictly forbidden from working during the same shift. 

You must determine if there is a way to assign every operator to a shift such that no safety rules are violated. If a valid schedule is possible, you must provide one.

## Input
The first line of the log contains two integers $n$ and $m$. The integer $n$ represents the headcount of machine operators. The facility employs at least one operator, while the strict upper limit on $n$ is dictated by the exactly 40 individual employee lockers available on site. The integer $m$ represents the number of safety incident records. This value ranges from zero up to the theoretical maximum where every distinct pair of operators has exactly one incident on file.

Each of the following $m$ lines provides two integers $u$ and $v$, identifying a pair of operators (who are numbered 1 through $n$) that share an incident record and therefore cannot be assigned to the same shift.

## Output
If it is impossible to distribute the operators across the three shifts without violating the safety rules, output a single line containing NO.
If it is possible, output YES on the first line. On the second line, output $n$ integers separated by spaces. The $i$-th integer must be 1, 2, or 3, indicating the shift assigned to operator $i$. If multiple valid schedules exist, any of them will be accepted.

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
