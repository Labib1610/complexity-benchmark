# Shift Allocation

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility employs $n$ staff members and maintains a list of $m$ operational incompatibilities. The facility runs two distinct operational periods, designated as period 1 and period 2.

Your task is to allocate each staff member to exactly one of the two periods. To maintain safety standards, the allocation must satisfy all of the following conditions:
- For every incompatibility between staff member $u$ and staff member $v$, $u$ and $v$ cannot be allocated to the same period.
- Let $c_i$ denote the total number of incompatibilities involving staff member $i$. If $P_1$ and $P_2$ are the sets of staff members allocated to period 1 and period 2 respectively, the allocation must guarantee that $\sum_{x \in P_1} c_x + \sum_{y \in P_2} c_y = 2m$.
- Let $k$ be the number of incompatibilities where the two involved staff members are allocated to different periods. The allocation must ensure $k = m$.

If there are multiple safe allocations, you must provide the one that is lexicographically smallest when represented as a sequence of period designations (1 or 2) for staff members 1 through $n$. If no safe allocation is possible, you must report this.

## Input
The first line provides $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The subsequent $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), indicating an incompatibility between staff member $u$ and staff member $v$.

## Output
If a safe allocation cannot be found, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers, each being either 1 or 2, representing the lexicographically smallest safe allocation.

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
