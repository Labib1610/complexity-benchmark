# Protocol Synchronization

Time limit: 2 s   Memory limit: 256 MB

You are configuring the synchronization protocols for a distributed network of $n$ server nodes.
Each node $i$ must be assigned a protocol version $b_i$, which must be an integer chosen from the set $\{1, 2, 3\}$.

You are given a list of $m$ communication links between pairs of nodes. For each link $(u, v)$, the two nodes exchange data. To ensure the entire network operates without packet loss, the protocol assignment must satisfy a specific global stability condition. A configuration is considered stable if and only if the network's total synchronization energy equals exactly $4m$. 
The total synchronization energy is calculated as the sum over all $m$ communication links $(u, v)$ of the quantity $5(b_u - b_v)^2 - (b_u - b_v)^4$.

Your objective is to determine if there exists a stable protocol assignment for all $n$ nodes. If a stable assignment exists, output it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of server nodes and the number of communication links.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a communication link between node $u$ and node $v$.

## Output
If there is no stable protocol assignment, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $b_1, b_2, \dots, b_n$ (each in $\{1, 2, 3\}$), where $b_i$ is the protocol version assigned to node $i$. If there are multiple valid assignments, any valid assignment is accepted.

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