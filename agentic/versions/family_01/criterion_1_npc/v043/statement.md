# Problem A — Storage Cluster Allocation

Time limit: 2 s   Memory limit: 256 MB

You are migrating a system consisting of $n$ databases. The new architecture provides three independent storage clusters, identified by the numbers 1, 2, and 3. Every database must be hosted on exactly one of these three clusters.

Due to heavy cross-querying, certain pairs of databases will create an I/O bottleneck if they are hosted on the exact same cluster. You have a comprehensive list of these high-traffic database pairs. To ensure optimal performance, no two databases in any given pair may be assigned to the same storage cluster.

Find an allocation of each database to a storage cluster that satisfies all performance constraints, or report that no such allocation is possible.

## Input
The first line contains two integers $n$ and $m$ — the number of databases and the number of high-traffic pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of databases that cannot share a storage cluster.

## Output
If there is no valid cluster allocation, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$, where $c_i \in \{1, 2, 3\}$ represents the storage cluster assigned to database $i$. Any valid allocation will be accepted.

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
