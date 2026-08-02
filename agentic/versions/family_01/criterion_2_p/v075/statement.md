# Shift Assignment Coordination

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates two non-overlapping work shifts, labeled $1$ and $2$. There are $n$ technicians, identified by IDs from $1$ to $n$. Due to safety regulations, $m$ operational conflict rules are enforced between pairs of technicians. An operational conflict rule between two technicians specifies that they cannot work during the same shift.

You must assign a shift $s_i \in \{1, 2\}$ to each technician $i$ ($1 \le i \le n$) such that:
- Every technician receives exactly one shift assignment.
- For every operational conflict rule between two technicians, they are assigned different shifts.

If one or more valid shift assignments exist, choose the sequence $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest. (That is, $s_1$ is minimized first; if there are multiple assignments with the same $s_1$, $s_2$ is minimized next, and so on.) If no assignment can satisfy all rules simultaneously, report that no valid schedule exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of technicians and the number of conflict rules.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — indicating that technician $u$ and technician $v$ cannot be in the same shift.

## Output
If no valid shift assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of shift assignments.

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
