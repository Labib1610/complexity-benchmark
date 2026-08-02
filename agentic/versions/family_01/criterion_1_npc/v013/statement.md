# Factory Shift Allocation

**Time limit:** 2 s   **Memory limit:** 256 MB

## Description
A manufacturing facility operates across three distinct daily shifts, numbered 1, 2, and 3. There are $n$ personnel, identified by integer IDs from 1 to $n$. Due to operational constraints, certain pairs of workers have mutual interference conflicts and must never be scheduled on the same shift.

To establish an orderly schedule, the facility follows a strict priority protocol: workers are evaluated in ascending order of their IDs (worker 1, then worker 2, up to worker $n$), with each worker assigned to the lowest numbered shift (1, then 2, then 3) that produces a globally valid schedule. This policy ensures that among all feasible conflict-free assignments, the chosen shift sequence $s_1, s_2, \dots, s_n$ is lexicographically as small as possible.

Determine whether a complete, valid shift assignment exists for all $n$ workers. If one exists, produce the prioritized shift schedule.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of workers and the number of pairwise conflict constraints, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that worker $u$ and worker $v$ cannot share the same shift. No conflict pair is listed more than once.

## Output
If no valid shift assignment can be made, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned shift for each worker from 1 to $n$. If multiple valid schedules exist, output the one that is lexicographically smallest.

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
