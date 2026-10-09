# Problem B — Network Transceivers

Time limit: 1 s   Memory limit: 256 MB

You are configuring a communication network consisting of $n$ servers and $m$ communication links. Each link connects a specific pair of servers.

To make the network operational, each communication link must be assigned a transmission polarity. For any link connecting a server $u$ and a server $v$, its polarity evaluated from $u$ to $v$, denoted $D_{u,v}$, must be chosen from $\{1, -1\}$. Evaluated in the reverse direction, the polarity of that same link is $D_{v,u} = -D_{u,v}$.

Once all links have been assigned a polarity, each server must be assigned a hardware type $T \in \{1, 2\}$.

A configuration is valid if it is possible to assign the link polarities such that for every server $i$, its assigned type $T_i$ satisfies the following equation for every link connecting server $i$ to a server $j$:
$$T_i = \frac{3 + D_{i,j}}{2}$$
where $D_{i,j}$ is the polarity of that specific link evaluated from $i$ to $j$.

If a server has no links connected to it, the equation is vacuously satisfied for both types, but you must still assign it exactly one type.

You must determine if there is a valid configuration. If there are multiple valid type assignments, you must choose the assignment that yields the lexicographically smallest sequence of types when listed in order from server $1$ to server $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a communication link between server $u$ and server $v$.

## Output
If there is no valid configuration, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the type ($1$ or $2$) assigned to the $i$-th server, representing the lexicographically smallest valid assignment.

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