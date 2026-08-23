# Multi-Zone Deployment Orchestration

Time limit: 1 s   Memory limit: 256 MB

A cloud architect is deploying $n$ software modules, numbered 1 through $n$, across two isolated availability zones: Zone 1 and Zone 2.

Certain pairs of modules rely on the same legacy hardware dependencies. If deployed in the same zone, they will create a resource deadlock. The architect has identified $m$ such conflicting pairs. To ensure system stability, any two modules in a conflicting pair must be hosted in different zones.

Your task is to determine whether all $n$ modules can be successfully deployed without any resource deadlocks.

If a valid deployment exists, you must provide the specific zone assignment for each module. The deployment engine is configured to favor Zone 1, breaking ties by prioritizing lower-numbered modules for Zone 1. Formally, you must output the lexicographically smallest valid sequence of zone assignments. A sequence of assignments $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first module index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of modules and the number of conflicting pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of modules that cannot be deployed in the same zone.

## Output
If it is impossible to deploy all modules without deadlocks, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid zone assignment.

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