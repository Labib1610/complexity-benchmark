# Shift Allocation Optimization

Time limit: 1 s   Memory limit: 256 MB

A facility employs $n$ workers, indexed from $1$ to $n$. The facility operates across two distinct operational windows, designated as Schedule 1 and Schedule 2.

There are $m$ pairwise incompatibility constraints between specific pairs of workers. An incompatibility constraint between worker $u$ and worker $v$ dictates that worker $u$ and worker $v$ cannot be assigned to the same operational window.

Evaluating all $2^n$ possible schedule configurations to find one where no two incompatible workers share an operational window is a major operational challenge. Your task is to determine whether there exists any valid schedule assignment of every worker to either Schedule 1 or Schedule 2 such that all $m$ incompatibility constraints are simultaneously satisfied.

If one or more valid assignments exist, you must output the one that is lexicographically smallest. That is, comparing two valid schedule sequences $(s_1, s_2, \dots, s_n)$ and $(t_1, t_2, \dots, t_n)$, the sequence $s$ is smaller if at the first index $i$ where $s_i \neq t_i$, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of workers and the number of pairwise incompatibility constraints, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$), indicating that worker $u$ and worker $v$ cannot share the same schedule.

## Output
If no valid schedule configuration exists that satisfies all constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid schedule configuration.

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
