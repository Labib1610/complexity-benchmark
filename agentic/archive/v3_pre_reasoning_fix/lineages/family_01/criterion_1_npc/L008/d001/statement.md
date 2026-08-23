# Problem A — Data Redundancy Zones

Time limit: 2 s   Memory limit: 256 MB

A distributed database consists of $n$ data shards, numbered 1 through $n$. The infrastructure provides exactly three geographical hosting zones, identified as Zone 1, Zone 2, and Zone 3. 

To maintain high availability during regional outages, the system enforces a strict separation policy. You are given a list of mutually critical shard pairs. If a disaster affects a single zone, we cannot afford to lose both shards in a critical pair. Therefore, two shards that form a critical pair must never be hosted in the same zone.

Your task is to assign each of the $n$ shards to exactly one of the three zones such that no critical pair is hosted in the same zone. If there are multiple valid configurations, you must output the one that is lexicographically smallest (i.e., comparing the zone of shard 1 first, then shard 2, and so on). If no such configuration is possible, report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ — the number of data shards and the number of critical pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a critical pair of shards that must be separated.

## Output
If it is impossible to satisfy the separation policy, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \ldots, c_n$ (where each $c_i \in \{1, 2, 3\}$), representing the zone assigned to shard $i$. If there are multiple valid sequences, output the lexicographically smallest one.

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