# Server Synchronization States

Time limit: 1 s   Memory limit: 256 MB

You are configuring a network of $n$ server nodes. Each node $i$ must be assigned a signal transformation function $f_i$ mapping the set $\{1, 2\}$ to itself. 

There are exactly two valid transformation functions available:
- The pass-through function: $f(1)=1$ and $f(2)=2$.
- The inversion function: $f(1)=2$ and $f(2)=1$.

Let $x_i$ be the operational state of node $i$, defined as the result of evaluating $f_i(1)$. Thus, $x_i$ is securely restricted to either 1 or 2.

The nodes are connected by a set of $m$ bidirectional sync channels. To prevent data corruption during synchronization, every channel imposes a strict balance requirement on its endpoints: if a channel connects node $u$ and node $v$, a signal of 1 passed sequentially through both nodes' transformation functions must emerge as a 2. Mathematically, this requires $f_u(f_v(1)) = 2$. (Note that these two specific functions commute, so $f_u(f_v(1)) = f_v(f_u(1))$, meaning the order of the endpoints does not matter.)

Your task is to determine a valid transformation assignment for all $n$ nodes. If there are multiple valid ways, you must output the assignment that produces the lexicographically smallest sequence of operational states $x_1, x_2, \dots, x_n$. If it is impossible to satisfy all channel requirements simultaneously, report that no such assignment exists.

## Input
The first line contains two integers $n$ and $m$. The number of nodes $n$ is at least 1 and bounded by a network maximum of $2\cdot 10^5$. The number of channels $m$ is at least 0 and at most $2\cdot 10^5$.
Each of the following $m$ lines contains two integers $u$ and $v$ (valid node IDs ranging from 1 to $n$), indicating that a channel exists between node $u$ and node $v$.

## Output
If there is no valid function assignment, print a single line containing `NO`.
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