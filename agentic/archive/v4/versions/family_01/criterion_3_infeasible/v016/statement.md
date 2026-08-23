# Mutual Incompatibility Certificate

Time limit: 2 s   Memory limit: 256 MB

An industrial plant keeps a log of severe interpersonal conflicts between pairs of employees. Management is attempting to organize the staff into two separate working shifts such that no two conflicting employees are placed on the same shift. However, if there exist three employees who all mutually conflict with one another (that is, every pair among the three has a logged conflict), it is impossible to divide them across only two shifts without placing at least two conflicting individuals on the same shift.

You are given the list of all pairwise conflicts in the plant. It is guaranteed that at least one set of three mutually conflicting employees exists. Your task is to identify the lexicographically smallest such triple. Specifically, among all triples of employee IDs $(a, b, c)$ satisfying $1 \le a < b < c \le n$ where conflicts exist between $a$ and $b$, between $a$ and $c$, and between $b$ and $c$, output the one that minimizes $a$, breaking ties by minimizing $b$, and further ties by minimizing $c$.

## Input
The first line contains two integers $n$ and $m$, representing the total workforce size and the total number of conflict entries, respectively. The workforce headcount $n$ ranges from a minimum shift unit of 3 up to a maximum plant capacity of 2000 ($3 \le n \le 2000$). The number of conflicts $m$ is at least 3 and cannot exceed the logging system upper bound of 200,000 or the total possible distinct pairings of $n$ employees, whichever is smaller ($3 \le m \le \min(n(n-1)/2, 200000)$).

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a conflict between employee $u$ and employee $v$. No pair of employees appears more than once in the list.

It is guaranteed that at least one valid triple of mutually conflicting employees exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line with $a < b < c$, representing the lexicographically smallest triple of mutually conflicting employees.

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
