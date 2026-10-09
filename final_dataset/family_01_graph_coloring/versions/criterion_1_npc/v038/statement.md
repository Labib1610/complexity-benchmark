# Problem A — Factory Schedule Codes

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant employs $n$ workers. Each worker $i$ (for $1 \le i \le n$) must be assigned a schedule code $s_i$. A valid schedule code is a positive integer $s_i$ such that $s_i^2 \le 9$.

There are $m$ incompatibility conditions. Each condition specifies two workers $u$ and $v$ who cannot be assigned the same schedule code. You must assign a valid schedule code to every worker such that all incompatibility conditions are satisfied, or determine if it is impossible.

It is guaranteed that for every incompatibility condition between $u$ and $v$, the sum $u + v$ is strictly less than $2n + 1$, and that the total number of conditions $m$ satisfies $2m < n^2$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ representing an incompatibility condition between the two workers.

## Output
If no valid assignment of schedule codes exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each satisfying $s_i \in \mathbb{Z}^+$ and $s_i^2 \le 9$), where $s_i$ is the schedule code of worker $i$. Any valid assignment is accepted.

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
