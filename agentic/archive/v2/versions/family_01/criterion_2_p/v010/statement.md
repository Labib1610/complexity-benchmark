# Shift Partitioning

Time limit: 1 s   Memory limit: 256 MB

A facility operates under a two-team system. There are $n$ personnel, labeled $1$ through $n$, each of whom must be placed into either Team 1 or Team 2. Certain pairs of personnel cannot be placed into the same team due to operational constraints.

Determine whether it is possible to assign every person to Team 1 or Team 2 such that no constrained pair shares the same team. If it is possible, output the assignment sequence that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of personnel and the number of operational constraints, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that person $u$ and person $v$ cannot belong to the same team.

## Output
If no valid team assignment exists, print `NO` on a single line.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the team assigned to person $i$ in the lexicographically smallest valid assignment.

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
