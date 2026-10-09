# Problem A — Distributed Shard Routing

Time limit: 2 s   Memory limit: 256 MB

You are configuring a distributed database with $n$ storage nodes. To ensure stable load distribution, each node must be assigned to exactly one of 3 available data shards. The shards are identified by the integer IDs 1, 2, and 3.

You are given a list of $m$ high-frequency query patterns. Each pattern involves a specific pair of nodes $(u, v)$ that are frequently accessed together.

To prevent routing bottlenecks, the hash-based router evaluates these pairs using an asymmetric checksum. For any given high-frequency pair of nodes $(u, v)$ from the list, let $c_u$ and $c_v$ be their assigned shard IDs. The router computes the checksum as $(7 \times c_u + 13 \times c_v) \bmod 20$. A routing collision occurs if this checksum evaluates to exactly 0. 

To maintain system stability, you must assign a shard ID (1, 2, or 3) to each of the $n$ nodes such that strictly zero collisions occur among all $m$ given query patterns. 

## Input
The first line contains two integers $n$ and $m$ — the number of storage nodes and the number of high-frequency query patterns ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of nodes involved in a high-frequency query pattern. Nodes are indexed from 1 to $n$.

## Output
If no such assignment is possible, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $c_1 \ c_2 \dots c_n$ (each being 1, 2, or 3), where $c_i$ is the shard ID assigned to node $i$. If multiple valid assignments exist, you may output any of them.

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