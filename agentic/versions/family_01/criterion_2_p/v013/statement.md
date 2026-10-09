# Problem B — Shift Configuration Search

Time limit: 1 s   Memory limit: 256 MB

A factory requires a master schedule for $n$ workers. Each worker must be assigned a shift identifier from the domain $\{1, 2\}$. A complete schedule is a sequence of $n$ such identifiers, meaning there are $2^n$ potential configurations to consider.

The assignment is subject to a set of $m$ strict binary constraints. Each constraint specifies a pair of workers who are incompatible and absolutely must not be assigned the same shift identifier. 

Your objective is to determine if the state space of $2^n$ possible schedules contains at least one configuration that satisfies all $m$ constraints simultaneously. If multiple valid configurations exist, you must identify the one that is lexicographically smallest. If the constraints are mutually exclusive such that no valid configuration exists in the entire state space, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of workers and the number of binary constraints.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of workers who cannot be assigned the same shift.

## Output
If there is no valid schedule among the $2^n$ possibilities, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid schedule.

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
