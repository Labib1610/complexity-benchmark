# Task Block Assignment

**Time limit:** 2 s   **Memory limit:** 256 MB

## Description
An automated logistics terminal manages $n$ processing tasks, identified by integer IDs from $1$ to $n$. Every task must be assigned to exactly one of three available operational time blocks, labeled 1, 2, and 3.

Certain pairs of tasks are mutually incompatible and must never share the same time block. 

To establish a deterministic allocation, the system follows a strict priority protocol: tasks are evaluated in ascending order of their IDs ($1, 2, \dots, n$). The terminal selects a valid block sequence $s_1, s_2, \dots, s_n$ (where $s_i \in \{1, 2, 3\}$) that satisfies all incompatibility constraints while being lexicographically as small as possible. That is, among all conflict-free assignments, it prioritizes minimizing $s_1$, then $s_2$, and so on.

Determine whether a valid assignment exists for all $n$ tasks. If one exists, output the lexicographically smallest block sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of tasks and the number of pairwise incompatibility constraints, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that task $u$ and task $v$ cannot be assigned to the same time block. No constraint pair is listed more than once.

## Output
If no valid assignment can be made, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned time block for each task from $1$ to $n$. If multiple valid assignments exist, output the one that is lexicographically smallest.

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
