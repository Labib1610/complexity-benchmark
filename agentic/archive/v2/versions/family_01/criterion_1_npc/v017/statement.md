# Factory Operations Pipeline: Shift Partitioning Module

Time limit: 2 s   Memory limit: 256 MB

## Description
As part of an automated facility management workflow, employee scheduling is executed in three consecutive phases:
1. *Constraint Aggregation*: The system compiles a list of paired personnel who cannot be present on the factory floor simultaneously due to safety regulations.
2. *Duty Assignment (Current Phase)*: Every employee must be assigned to exactly one of three available operational shifts (designated as 1, 2, or 3). An assignment is valid if no two conflicting personnel share the same shift assignment. If valid assignments exist, the system requires the lexicographically smallest sequence of shift numbers to ensure deterministic pipeline execution downstream. If no valid partition exists, execution halts.
3. *Audit & Logging*: The generated assignment is forwarded to the compliance logging module.

Your task is to implement Phase 2 of this workflow. Given the total number of employees and the list of pairwise conflicts, determine whether a valid assignment of shifts 1, 2, or 3 exists. If impossible, report `NO`. Otherwise, output `YES` followed by the lexicographically smallest sequence of shift numbers assigned to employees 1 through $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of employees and the number of conflicting pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that employee $u$ and employee $v$ cannot share a shift.

## Output
If no valid shift assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ where $s_i \in \{1, 2, 3\}$ represents the shift assigned to employee $i$. If multiple valid shift assignments exist, output the one that is lexicographically smallest (i.e., comparing $s_1$ first, then $s_2$, and so on).

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
