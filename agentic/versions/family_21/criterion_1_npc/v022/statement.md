# Subnet Isolation for Root Servers

Time limit: 5 s
Memory limit: 256 MB

## Description
A data centre network consists of $n$ routers connected by $m$ bidirectional fibre links. Each link has a deactivation cost based on its bandwidth. Within this network, $k$ routers are designated as Root Servers. Due to a new security protocol, these Root Servers must be completely isolated from one another. You are tasked with deactivating a set of links so that no two Root Servers can communicate, even indirectly.

In typical deployments, the network is well-behaved, with routers naturally clustering around the nearest Root Server. Because of this apparent regularity, one might be tempted to isolate pairs of Root Servers by evaluating their bottleneck capacities, or by repeatedly tracing the shortest connections between them to sever the cheapest links. However, your solution must find a globally valid set of links for the exact network provided, regardless of its topology.

Your total budget for deactivating links is $B$. You must select a set of links whose total deactivation cost does not exceed $B$, such that after their removal, no two Root Servers are connected by any path of remaining links. The remaining non-root routers can end up in whichever connected component the deactivations produce—their placement is unconstrained. If the budget is sufficient, output the exact links to remove; otherwise, determine that it is impossible.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$.
The second line contains $k$ integers, the IDs of the Root Servers.
The next $m$ lines each contain three integers $u$, $v$, and $w$, representing a bidirectional link between router $u$ and router $v$ with a deactivation cost of $w$.

## Output
If it is possible to isolate all Root Servers within the budget, output `YES`. On the next line, output the number $c$ of deactivated links. Then, output $c$ lines, each containing `u v` (the endpoints of a deactivated link). If it is impossible, output `NO`.

## Example

**Input**
```text
5 5 3 10
1 2 3
1 4 5
2 4 5
3 4 5
4 5 12
1 5 4
```

**Output**
```text
YES
2
2 4
3 4
```
