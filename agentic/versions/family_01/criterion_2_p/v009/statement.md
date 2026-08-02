# Day and Night

Time limit: 1 s   Memory limit: 256 MB

In a facility with $n$ workers, there are $m$ specified conflict pairs $(u, v)$ where worker $u$ and worker $v$ cannot share the same work shift. Every worker must be assigned to either shift $1$ or shift $2$. A shift assignment is valid if every conflicting pair consists of two workers assigned to different shifts.

Determine whether a valid assignment exists, and if so, produce the lexicographically smallest valid assignment $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a conflicting pair.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ space-separated integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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
