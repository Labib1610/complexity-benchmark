# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant is organizing its $n$ staff members into two operational shifts, identified as shift 1 and shift 2. 

There are $m$ specialized tools, each assigned to a specific pair of staff members. To guarantee round-the-clock operation, every tool must be active during both shifts. A tool is considered active during a particular shift if and only if at least one of its assigned staff members is scheduled to work that shift. 

You must determine an assignment of each staff member to exactly one shift (either shift 1 or shift 2) such that all tools remain active during both shifts, or report that no such arrangement is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two staff members assigned to a single tool.

## Output
If no valid shift arrangement exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $s_1, \dots, s_n$ (each $s_i \in \{1, 2\}$), where $s_i$ is the shift assigned to staff member $i$. If there are multiple valid arrangements, output the one that is lexicographically smallest.

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