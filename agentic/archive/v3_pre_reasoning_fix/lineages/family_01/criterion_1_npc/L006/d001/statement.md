# Problem A — Distributed Storage Allocation

Time limit: 2 s   Memory limit: 256 MB

You are managing a distributed database consisting of $n$ data shards, numbered 1 through $n$. You have exactly three separate physical drives available to store these shards, identified by the integers 1, 2, and 3. Each shard must be saved on exactly one of these drives.

Due to heavy concurrent querying, specific pairs of shards are highly correlated in their access patterns. If both shards in such a pair are saved on the exact same drive, it creates a read bottleneck that degrades overall performance. To maintain optimal throughput, any such pair of shards must be allocated to different drives.

You need to find a valid drive assignment for all $n$ shards. If there are multiple valid assignments, you must prioritize placing shard 1 on the lowest possible drive number. If ties remain, you resolve them by minimizing the drive number for shard 2, and so on sequentially up to shard $n$. If no valid assignment exists, you must output a failure message.

## Input
The first line contains two integers $n$ and $m$ — the number of data shards and the number of correlated pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The next $m$ lines each contain two integers $u$ and $v$, meaning that shard $u$ and shard $v$ are accessed concurrently and cannot be placed on the same drive.

## Output
If it is impossible to distribute the shards without creating a bottleneck, print NO on a single line.
Otherwise, print YES on the first line. On the second line, output $n$ integers separated by spaces, representing the drive numbers (1, 2, or 3) assigned to shards 1 through $n$ respectively, following the tie-breaking rules.

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