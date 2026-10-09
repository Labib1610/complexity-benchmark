# Database Maintenance

Time limit: 1 s   Memory limit: 256 MB

A network of $n$ databases requires scheduled maintenance during one of two available time windows, designated 1 and 2. Certain pairs of databases share a continuous replication link. To prevent data corruption, any two databases connected by a replication link must undergo maintenance in different time windows.

Determine a valid maintenance schedule for all $n$ databases, or determine if no such schedule can be formed. When multiple valid schedules exist, the automated planner selects the one that assigns window 1 as early as possible: comparing two schedules from database 1 upwards, it prefers the one that assigns window 1 at the first database where they differ.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of databases and the number of replication links, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ — indicating that a replication link exists between database $u$ and database $v$.

## Output
If no valid schedule can be formed without corrupting data, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the maintenance window assigned to each database in the selected schedule.

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
