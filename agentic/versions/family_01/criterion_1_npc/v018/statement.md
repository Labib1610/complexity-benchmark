# Problem A — Schedule Allocation

Time limit: 2 s
Memory limit: 256 MB

In a manufacturing facility, the workforce consists of $n$ employees. Over time, interpersonal issues have developed, resulting in a known list of incompatible employee pairs. The facility's operations are divided into three distinct daily schedules, which are designated by the numbers 1, 2, and 3. Management enforces a strict policy for organizing the workforce: any two employees who are listed as incompatible must be assigned to different schedules. Furthermore, every employee must be placed into exactly one of these three schedules.

Your task is to determine whether it is possible to distribute the employees according to these rules. If it is possible, you must find the specific valid distribution that is lexicographically smallest when represented as a sequence of schedule numbers (meaning the schedule number for employee 1 is minimized, first and foremost, then employee 2, and so on).

## Input
The first line contains two integers $n$ and $m$ — the number of employees and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of employees who are incompatible.

## Output
If there is no way to assign schedules that satisfies all rules, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the schedule assigned to employee $i$. If there are multiple valid assignments, output the one whose sequence $s_1, s_2, \dots, s_n$ is lexicographically smallest.

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
