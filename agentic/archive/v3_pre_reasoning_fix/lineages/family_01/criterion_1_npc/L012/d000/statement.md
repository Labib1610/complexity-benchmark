# Problem A — Tier Allocation

Time limit: 2 s   Memory limit: 256 MB

A facility employs $n$ workers. Each worker must be allocated a work tier, represented by an integer from 1 to 3 inclusive. Certain pairs of workers have incompatible roles and must not be allocated the same work tier. Allocate every worker to exactly one work tier so that no incompatible pair shares a tier, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair.

## Output
If no valid allocation exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $t_1, t_2, \dots, t_n$ (each in $\{1,2,3\}$), where $t_i$ is the tier of worker $i$. Among all valid allocations output the lexicographically smallest sequence (compare $t_1$ first, then $t_2$, and so on).

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
