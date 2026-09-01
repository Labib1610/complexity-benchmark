# Problem A — Concurrent Task Profiling

Time limit: 2 s   Memory limit: 256 MB

You are configuring a concurrent system with $n$ tasks, indexed from $1$ to $n$. Each task $i$ must be assigned an execution profile, chosen from exactly one of three available profiles. Each profile dictates the sequence of resources a task will access over three distinct execution steps:
- Profile 1 accesses resources: `(1, 2, 3)`
- Profile 2 accesses resources: `(2, 3, 1)`
- Profile 3 accesses resources: `(3, 1, 2)`

The system is subject to $m$ concurrency constraints. Each constraint specifies a pair of tasks $u$ and $v$ that run simultaneously. To prevent resource conflicts, any two simultaneous tasks must not access the same resource during the same execution step. That is, if task $u$ and task $v$ are constrained to run simultaneously, their assigned profiles $P_u$ and $P_v$ must satisfy $P_u[k] \neq P_v[k]$ for all steps $k \in \{1, 2, 3\}$.

For deployment, the complete configuration is represented by a sequence of $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ is the Profile ID assigned to task $i$. 

To ensure deterministic deployment, the system strongly prioritizes assigning lower Profile IDs to tasks with smaller index numbers. If there are multiple valid configurations, you must select the one whose configuration sequence $c_1, c_2, \ldots, c_n$ is lexicographically smallest. That is, when comparing two valid configuration sequences, the one with the smaller Profile ID at the first task index where they differ is strictly preferred.

Determine if a valid configuration exists, and if so, output the optimal configuration sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of tasks and the number of concurrency constraints.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that task $u$ and task $v$ execute simultaneously and their assigned profiles must not conflict at any step.

## Output
If no valid configuration is possible, print a single line containing `NO`.
If a valid configuration is possible, print `YES` on the first line. On the second line, print exactly $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ is the Profile ID assigned to task $i$. Among all valid configurations, you must output the lexicographically smallest sequence $c_1, c_2, \ldots, c_n$ (compare $c_1$ first, then $c_2$, etc.).

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