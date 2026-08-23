# Resource Placement Protocol

**Time limit:** 2 s   **Memory limit:** 256 MB

## Description
A facility manages $n$ distinct processing tasks, indexed by integers from $1$ to $n$. Each task must be assigned to exactly one of three available operational channels, designated as channel $1$, channel $2$, or channel $3$.

Certain pairs of tasks are mutually exclusive due to shared hardware interference and cannot run on the same channel. You are provided with a complete list of these pair constraints.

To establish a deterministic assignment, the system enforces a strict priority rule: between any two complete configurations that satisfy all interference constraints, the system prefers the configuration that assigns a lower channel number to the lowest-indexed task where the two configurations differ. In other words, the sequence of assigned channel numbers $(s_1, s_2, \dots, s_n)$ must be lexicographically as small as possible.

Determine whether a valid channel assignment exists for all $n$ tasks. If one exists, produce the prioritized assignment sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of tasks and the number of pairwise exclusion constraints, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that task $u$ and task $v$ cannot share the same channel. No pair of tasks is listed more than once.

## Output
If no valid assignment can be made, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned channel for each task from $1$ to $n$. If multiple valid configurations exist, output the one that is lexicographically smallest.

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
