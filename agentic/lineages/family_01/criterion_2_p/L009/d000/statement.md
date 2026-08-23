# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant is organizing its $n$ staff members into two operational teams, identified as team 1 and team 2. 

There are $m$ pairs of staff members who share a specialized tool. Because a tool cannot be used by two people on the same team, the two members of any such pair must be assigned to different teams. 

You must determine an assignment of each staff member to either team 1 or team 2 that satisfies all tool-sharing constraints, or report that no such arrangement is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of staff members who share a tool.

## Output
If no valid team arrangement exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $s_1, \dots, s_n$ (each $s_i \in \{1, 2\}$), where $s_i$ is the team assigned to staff member $i$. If there are multiple valid arrangements, output the one that is lexicographically smallest.

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
