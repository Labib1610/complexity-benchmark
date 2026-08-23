# Phase II: Triad Isolation

Time limit: 2 s
Memory limit: 256 MB

A large-scale compute cluster executes $n$ concurrent tasks. The cluster's resource manager operates in three distinct phases to prevent system halts.

In Phase I, the manager runs a continuous background trace, recording instances where two tasks attempt to lock the same resource. Over a given period, it compiles a list of $m$ such mutual contention events.

Your program is responsible for Phase II. The system relies on a heuristic that severe cluster degradation is always triggered by a "contention triad"—a set of exactly three distinct tasks such that all three possible pairs formed by these tasks appear in the Phase I logs as having a mutual contention event. To initiate recovery, you must parse the Phase I logs and isolate one such triad. Because the cluster is currently experiencing degradation, the logs are guaranteed to contain at least one contention triad. 

In Phase III, the cluster's recovery module will terminate the three tasks you identified. To ensure deterministic recovery, if the logs contain multiple contention triads, Phase III requires the triad whose smallest task ID is as small as possible. If there are still multiple options, it prefers the one whose second-smallest task ID is as small as possible, and finally the third-smallest task ID.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of tasks and the number of contention events logged in Phase I.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that a mutual contention event was recorded between task $u$ and task $v$. Each pair of tasks is logged at most once.

It is guaranteed that at least one contention triad exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$, separated by spaces, representing the task IDs of the isolated contention triad. The IDs must be printed in ascending order ($a < b < c$). The output must satisfy the deterministic recovery conditions for Phase III.

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
