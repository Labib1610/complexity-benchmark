# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory operates exactly two production schedules, designated as Schedule 1 and Schedule 2. There are $n$ technicians and $m$ incompatibility records. Each record contains two technician IDs, indicating that these two individuals cannot be assigned to the same schedule. 

To assist with load balancing, the planning department guarantees the following structural properties for every set of records:
- If you calculate the frequency of each technician's ID across all $m$ records, the sum of these frequencies over all $n$ technicians is exactly $2m$.
- The maximum frequency of any single technician's ID across all records is at most $2m$.

Your task is to assign each technician to either Schedule 1 or Schedule 2 such that no two technicians in any incompatibility record share the same schedule. If it is impossible to satisfy all records, you must report this.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing an incompatibility record between technician $u$ and technician $v$.

## Output
If there is no valid schedule assignment, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \ldots, s_n$ (where each $s_i \in \{1, 2\}$) representing the schedule assigned to each technician. If there are multiple valid assignments, you must output the one that is lexicographically smallest.

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
