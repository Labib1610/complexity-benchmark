# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory administration needs to divide its $n$ employees into two distinct operational periods, designated as period 1 and period 2. 

Throughout the facility, there are $m$ specific workstations, each utilized by exactly two employees. To ensure smooth operations and avoid overlap, the two employees sharing any single workstation must be scheduled during different operational periods.

Your task is to determine if it is possible to assign every employee to either period 1 or period 2 under these conditions. If multiple valid schedules exist, you must provide the one that is lexicographically smallest when represented as a sequence of $n$ period assignments.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of employees and the number of shared workstations, respectively. Employees are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that employee $u$ and employee $v$ share a workstation.

## Output
If it is impossible to schedule the employees according to the requirements, print a single line containing `NO`.
If a valid schedule exists, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the period assigned to each employee from $1$ to $n$. This sequence must be the lexicographically smallest among all valid assignments.

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
