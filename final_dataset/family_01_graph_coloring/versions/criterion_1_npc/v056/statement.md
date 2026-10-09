# Distributed Database Sharding

Time limit: 2 s
Memory limit: 256 MB

You are deploying a distributed database across three distinct storage zones, identified as zone 1, zone 2, and zone 3. The database is composed of $n$ unique data shards.

Your task is to partition the $n$ shards into the three zones while adhering to a strict set of deployment policies:
1. **Uniqueness**: Every shard must be mapped to exactly one zone.
2. **Global Conservation**: The sum of the number of shards mapped to zone 1, zone 2, and zone 3 must equal exactly $n$.
3. **Zone Capacity**: No single zone may be mapped to more than $n$ shards.
4. **Thrashing Prevention**: You are given a log of $m$ concurrent query overlaps. Each overlap specifies two shards. If both shards in an overlap are mapped to the same zone, the zone will experience I/O thrashing. Therefore, the two shards in any given overlap must be mapped to different zones.
5. **Log Integrity**: It is guaranteed that the total number of shard identifiers listed in the overlap log is exactly $2m$.

Determine if a valid deployment plan exists for all $n$ shards across the three zones.

## Input
The first line contains two integers $n$ and $m$ — the total number of shards and the number of concurrent query overlaps ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$, representing an overlap between shard $u$ and shard $v$. Shards are indexed from 1 to $n$.

## Output
If a deployment plan satisfying all policies is impossible, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $z_1, z_2, \dots, z_n$ (where each $z_i \in \{1, 2, 3\}$), representing the zone assigned to shard $i$. If multiple valid plans exist, any of them will be accepted.

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
