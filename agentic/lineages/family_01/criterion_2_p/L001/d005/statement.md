# Problem B — Network Transceivers

Time limit: 1 s   Memory limit: 256 MB

You are configuring a communication network consisting of $n$ servers and $m$ communication links. Each link connects a specific pair of servers.

To make the network operational, you must assign an operating mode to each server and a single direction to each link. There are exactly two available operating modes:
- **Transmitter** (represented by the value $1$): A server in this mode can only send data. If a server is configured as a transmitter, every link connected to it must be directed away from it.
- **Receiver** (represented by the value $2$): A server in this mode can only receive data. If a server is configured as a receiver, every link connected to it must be directed towards it.

You must determine if there is a valid way to assign an operating mode to every server and a direction to every link such that these rules are satisfied. Isolated servers (those with no links) can be configured in either mode.

If there are multiple valid mode assignments for the servers, you must choose the assignment that yields the lexicographically smallest sequence of values when listed in order from server $1$ to server $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a communication link between server $u$ and server $v$.

## Output
If there is no way to assign the operating modes and link directions without violating the rules, output a single line containing `NO`.
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