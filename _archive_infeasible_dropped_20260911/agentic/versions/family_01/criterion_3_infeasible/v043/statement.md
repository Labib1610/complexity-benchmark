# Certificate of Deadlock

Time limit: 2 s
Memory limit: 256 MB

The manufacturing plant is strictly limited to operating two daily shifts. However, the current personnel constraints are known to be completely unworkable. Your task is not to attempt an assignment, but to provide a formal justification of why it fails.

To prove that a two-shift schedule is unworkable, you must identify a deadlock configuration consisting of three distinct employees. Within this trio, the first employee is restricted from operating simultaneously with the second employee, the first employee is also restricted from operating simultaneously with the third employee, and the second employee is restricted from operating simultaneously with the third employee. Because only two shifts exist, any assignment would force at least two of these three individuals into the same shift, violating the restrictions.

You are guaranteed that at least one such trio exists in the provided data. Find and output one such trio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of employees and the number of restrictions, respectively. Employees are numbered from $1$ to $n$.
Each of the following $m$ lines provides two integers $u$ and $v$, meaning employee $u$ and employee $v$ are restricted from operating simultaneously.
It is guaranteed that at least one deadlock configuration of three employees exists.

## Output
Print three integers $a$, $b$, $c$ on a single line, separated by spaces, representing the three employees in the deadlock configuration. You must format your output such that $a < b < c$. If there are multiple valid configurations, you must output the one that is lexicographically earliest (smallest $a$; in case of a tie, smallest $b$; in case of a further tie, smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
