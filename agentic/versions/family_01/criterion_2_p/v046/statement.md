# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A factory administration is scheduling its $n$ workers into two shifts, labeled 1 and 2. HR has identified specific pairs of workers who have personality conflicts. To maintain a productive environment, any two workers in a conflicting pair must be assigned to different shifts. Because Shift 1 includes a preferred pay differential, the final assignment must prioritize placing workers with lower ID numbers into Shift 1, meaning the overall sequence of shift assignments must be lexicographically smallest. If no valid schedule is possible under these conflict constraints, the system must report this.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of workers and the number of conflicting pairs, respectively. Workers are identified by integers from $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a conflicting pair of workers.

## Output
If it is impossible to assign the workers to the two shifts without violating the conflict constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of workers to shifts.

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
