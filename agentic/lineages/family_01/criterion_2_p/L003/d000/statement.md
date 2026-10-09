# Problem B — Maintenance Windows

Time limit: 1 s   Memory limit: 256 MB

A cloud provider must schedule maintenance updates for $n$ database instances. The update process requires assigning each instance to one of two maintenance windows, designated 1 and 2.

Certain pairs of instances share a dedicated backup storage array. To prevent storage overload, these pairs cannot undergo maintenance during the same window. 

You must assign a window to each instance to satisfy all storage constraints, or determine that no such schedule exists. If multiple valid schedules exist, the automated deployment system requires the schedule whose sequence of window assignments $s_1 \dots s_n$ (where $s_i$ is the window assigned to instance $i$) is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of database instances and the number of shared backup arrays.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that instances $u$ and $v$ share a backup array.

## Output
If no valid schedule exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid schedule.

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
