# Problem A — Access Level Allocation

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant must assign an access level to each of its $n$ employees. Every employee $i$ must receive an access level $s_i$ chosen from the integer range $1 \le s_i \le 3$.

Due to a limited inventory of specialized tools, certain pairs of employees are required to share a specific tool. Whenever two employees share a tool, their assigned access levels must strictly differ to prevent conflicting access requests.

Determine an access level assignment for all $n$ employees that satisfies all tool-sharing constraints, or determine if no such assignment is possible.

## Input
The first line contains two integers $n$ and $m$ — the number of employees and the number of tool-sharing constraints ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — denoting that employee $u$ and employee $v$ share a tool.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where $1 \le s_i \le 3$), representing the access level of each employee. If there are multiple valid assignments, any of them will be accepted.

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
