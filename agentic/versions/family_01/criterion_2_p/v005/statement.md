# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A facility operates two non-overlapping work shifts, designated as shift 1 and shift 2. The facility currently employs $n$ workers, identified by unique IDs from $1$ to $n$. Due to operational constraints, certain pairs of workers have documented incompatibilities; $m$ such mutual conflict pairs exist.

Your task is to assign every worker to either shift 1 or shift 2 such that no two conflicting workers are assigned to the same shift. If multiple valid shift assignments exist, output the one that is lexicographically smallest (that is, minimizing the shift number of worker 1, then worker 2, and so on). If no valid assignment can satisfy all conditions, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$, representing the number of workers and the number of conflict pairs, respectively. The worker count $n$ is at least 1 and does not exceed the facility's maximum capacity of $200,000$. The number of conflicts $m$ is non-negative and does not exceed $200,000$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that worker $u$ and worker $v$ are in conflict.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
