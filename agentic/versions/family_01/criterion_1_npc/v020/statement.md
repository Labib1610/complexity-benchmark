# Problem A — Storage Sharding

Time limit: 2 s   Memory limit: 256 MB

You are configuring a distributed database that spans exactly three independent storage drives, labeled 1, 2, and 3. The database consists of $n$ distinct tables. Every table must be allocated to exactly one of these three drives.

To prevent I/O bottlenecks during complex queries, certain pairs of tables that are frequently joined must reside on completely different drives. If they are placed on the same drive, concurrent read operations will cause hardware thrashing. You are provided with a list of all such high-traffic table pairs. 

Determine whether it is possible to distribute all $n$ tables across the three drives such that for every high-traffic pair, the two tables in the pair are assigned to different drives.

## Input
The first line contains two integers $n$ and $m$ — the number of tables and the number of high-traffic pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ $v$ — a high-traffic pair of tables that must be separated. Tables are numbered from 1 to $n$.

## Output
If no valid allocation exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $d_1, d_2, \dots, d_n$ (each in {1, 2, 3}), where $d_i$ is the drive assigned to table $i$. Any valid allocation is accepted.

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
