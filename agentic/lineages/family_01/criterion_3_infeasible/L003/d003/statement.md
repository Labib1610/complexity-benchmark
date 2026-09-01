# Problem C — Grievance Audit

Time limit: 2 s   Memory limit: 256 MB

The factory's human resources department is auditing past worker schedules to understand why a complete operational halt occurred. You are provided with a historical archive of filed grievances. Each grievance establishes a mutual incompatibility between two specific employees. Your goal is to process these archives to isolate a trilateral impasse. A trilateral impasse is formed by a group of exactly three unique employees where every individual in the group has a filed grievance against both of the other two individuals in that same group.

We know that during this time, it was strictly impossible to divide the employees into two shifts without internal grievances. By the nature of this scheduling failure, the archive is guaranteed to hold at least one valid trilateral impasse. You must find such a group.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), which are the total number of employees and the total number of filed grievances, respectively.
The next $m$ lines each contain two integers $u$ and $v$, indicating that employee $u$ and employee $v$ have a mutual grievance.
It is guaranteed that there exists at least one trilateral impasse (a set of three distinct employees who all have mutual grievances with one another) in the dataset.

## Output
Print a single line containing three space-separated integers $a$, $b$, and $c$, arranged in strictly increasing order ($a < b < c$). These three integers must be the identifiers of the employees who make up a trilateral impasse. If the archive contains multiple valid impasses, you must output the one that is lexicographically smallest (i.e., among all valid impasses, output the one with the minimum possible value for $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$).

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