# Problem B — Factory Protocol

Time limit: 1 s
Memory limit: 256 MB

A factory employs $n$ workers, numbered 1 through $n$. Management is implementing a new operational protocol where every worker must be assigned a schedule code. Each schedule code must be chosen from the set $\{1, 2\}$.

The factory floor has strict safety regulations regarding shared workstations. You are given a log of $m$ pairs of workers who operate the same workstation. To maintain the required operational balance, any two workers in a logged pair must have schedule codes that sum to exactly 3.

Determine if it is possible to assign a schedule code to all $n$ workers in accordance with the safety regulations. If it is impossible, report it. If there are multiple valid assignments, you must output the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of workers who share a workstation.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1, 2\}$), representing the lexicographically smallest valid assignment.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```
