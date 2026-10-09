# Problem A — Protocol Allocation

Time limit: 2 s   Memory limit: 256 MB

A secure facility is evaluating $n$ encrypted data shards. To successfully process the data, each shard must be assigned exactly one processing protocol from the set $\{1, 2, 3\}$.

During preliminary analysis, the facility identified $m$ pairs of shards that contain cross-contaminating metadata. If any two shards from such a pair are assigned the identical processing protocol, the system will trigger a security fault and halt.

Your task is to determine whether it is possible to assign a protocol to each of the $n$ shards such that no security faults are triggered. If it is possible, provide a valid protocol assignment for all shards.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of data shards and the number of cross-contaminating pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing that shard $u$ and shard $v$ contain cross-contaminating metadata.

## Output
If there is no way to assign protocols without triggering a security fault, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$, where each $p_i \in \{1, 2, 3\}$ is the processing protocol assigned to shard $i$. If multiple valid assignments exist, you may output any of them.

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