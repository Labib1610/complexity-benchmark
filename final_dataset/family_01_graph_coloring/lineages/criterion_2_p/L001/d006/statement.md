# Problem B — Network Transceivers

Time limit: 1 s   Memory limit: 256 MB

You are configuring a communication network consisting of $n$ servers and $m$ communication links. Each link connects a specific pair of servers.

To make the network operational, you must assign a single direction to each link. When a link between two servers is directed, one server becomes its origin and the other becomes its destination. Once all links are directed, you must assign an operating mode to each server according to these rules:
- **Mode 1**: The server is the origin for every link connected to it.
- **Mode 2**: The server is the destination for every link connected to it.

A configuration is valid if it is possible to direct the links such that every server qualifies for an operating mode. If a server has no links connected to it, it qualifies for both modes, but you must still assign it exactly one.

You must determine if there is a valid configuration. If there are multiple valid mode assignments, you must choose the assignment that yields the lexicographically smallest sequence of modes when listed in order from server $1$ to server $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a communication link between server $u$ and server $v$.

## Output
If there is no valid configuration, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the mode ($1$ or $2$) assigned to the $i$-th server, representing the lexicographically smallest valid assignment.

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