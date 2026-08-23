# Production Line Diagnostics

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility manages its workload by routing tasks through exactly two independent processing streams. Certain pairs of tasks require exclusive access to a shared calibration instrument. If two such tasks are assigned to the same processing stream, it causes a workflow collision. Therefore, these pairs are marked as mutually restrictive and must always be assigned to different streams.

Your objective is to identify a "critical cluster" within the workflow. A critical cluster is a group of exactly three tasks where every possible pair within the group is mutually restrictive.

To guarantee deterministic output, if multiple critical clusters are present, your software must report the one whose task identifiers are sequentially lowest.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of tasks and the number of mutually restrictive pairs. Tasks are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that task $u$ and task $v$ are mutually restrictive.
It is guaranteed that at least one critical cluster exists in the provided data.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the identifiers of the three tasks in the critical cluster. Output the combination that is sequentially lowest (the smallest possible value for $a$; in case of a tie, the smallest possible value for $b$; and finally the smallest possible value for $c$).

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
