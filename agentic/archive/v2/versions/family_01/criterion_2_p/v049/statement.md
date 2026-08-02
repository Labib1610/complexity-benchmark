# Workforce Shift Assignment

Time limit: 1 s   Memory limit: 256 MB

In an enterprise workforce management system, $n$ employees (numbered $1$ through $n$) need to be assigned to one of two operational shifts, designated as shift $1$ and shift $2$.

Certain pairs of employees have operational conflicts and cannot work the same shift. You are given $m$ such conflict pairs. An assignment is valid if:
1. Each employee $i$ is assigned a shift $s_i \in \{1, 2\}$.
2. No two conflicting employees receive the same shift assignment.
3. For every connected cluster of conflicting relationships, the employee with the minimum ID in that cluster is assigned to shift $1$.

If at least one valid assignment exists, identify the lexicographically smallest sequence $s_1, s_2, \dots, s_n$. Otherwise, report that no valid schedule exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m 
\le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that employee $u$ and employee $v$ have an operational conflict.

## Output
If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
