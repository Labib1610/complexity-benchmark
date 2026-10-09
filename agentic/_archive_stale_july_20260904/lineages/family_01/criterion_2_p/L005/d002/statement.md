# Problem B — Resource Allocation

Time limit: 1 s   Memory limit: 256 MB

You are configuring a network of $n$ nodes. Each node must be assigned a tier of either $1$ or $2$. 

The network has $m$ communication channels, each connecting a pair of nodes. Each channel has exactly 3 units of bandwidth available. To fully utilize the network without overloading it, the two nodes connected by any channel must together consume exactly the available bandwidth of that channel. A node assigned to tier $s$ consumes exactly $s$ units of bandwidth on each of its connected channels.

You must assign a tier to every node. If it is impossible to configure the network to satisfy the bandwidth requirement for all channels, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 200000$, $0 \le m \le 200000$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of nodes connected by a communication channel.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$, each equal to 1 or 2, representing the tiers of the nodes. If multiple valid configurations exist, output the lexicographically smallest one.

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