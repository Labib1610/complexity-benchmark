# Server Synchronization States

Time limit: 1 s   Memory limit: 256 MB

You are configuring a network of $n$ server nodes. Each node $i$ must be assigned an operational state $x_i$. The hardware restricts each node's state such that $x_i \in \{1, 2\}$.

The nodes are connected by a set of $m$ bidirectional sync channels. To prevent data collisions during synchronization, every channel imposes a routing balance requirement on its endpoints. Specifically, if a channel connects node $u$ and node $v$, consider a token that must travel on a 2D grid from the origin $(0,0)$ to the destination coordinates $(x_u, x_v)$. The token can only move in steps of $(+1, 0)$ and $(0, +1)$. The channel is considered balanced if and only if the number of distinct valid paths for the token is exactly 3.

Your task is to determine a valid state assignment for all $n$ nodes such that every channel is balanced. If there are multiple valid ways, you must output the assignment that produces the lexicographically smallest sequence of operational states $x_1, x_2, \dots, x_n$. If it is impossible to satisfy all channel requirements simultaneously, report that no such assignment exists.

## Input
The first line contains two integers $n$ and $m$. The number of nodes $n$ is at least 1 and bounded by a network maximum of $2\cdot 10^5$. The number of channels $m$ is at least 0 and at most $2\cdot 10^5$.
Each of the following $m$ lines contains two integers $u$ and $v$ (valid node IDs ranging from 1 to $n$), indicating that a channel exists between node $u$ and node $v$.

## Output
If there is no valid state assignment, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $x_1, x_2, \dots, x_n$, representing the lexicographically smallest valid sequence of operational states.

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