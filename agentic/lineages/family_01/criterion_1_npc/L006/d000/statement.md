# Problem A — Shift Scheduling

Time limit: 2 s   Memory limit: 256 MB

A factory requires each of its $n$ workers to be assigned a shift identifier from the set $\{1, 2, 3\}$. However, certain workers are incompatible with each other and must not be assigned the same shift identifier. Determine an assignment for every worker such that no two incompatible workers share the same shift identifier, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating that worker $u$ and worker $v$ are incompatible.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the shift identifier of worker $i$. Any valid assignment is accepted.

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
