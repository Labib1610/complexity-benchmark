# Task Execution Scheduling

Time limit: 2 s   Memory limit: 256 MB

A high-performance computing system must assign each of $n$ distinct background tasks (numbered 1 through $n$) to one of 3 available processing cores, labeled 1, 2, and 3.

Due to hardware resource lock contention, certain pairs of tasks are mutually exclusive and cannot be assigned to the same processing core.

Determine whether it is possible to assign every task a core such that no mutually exclusive pair of tasks is placed on the same core. If valid core assignments exist, output the assignment that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of tasks and the number of mutually exclusive pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of tasks that cannot share a core.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the core assigned to task $i$. Among all valid assignments, output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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