# Server Synchronization States

Time limit: 1 s   Memory limit: 256 MB

You are configuring a network of $n$ server nodes. Each node $i$ must be assigned an operational state $x_i$, which must be a positive integer ($x_i \ge 1$).

The nodes are connected by a set of $m$ bidirectional sync channels. To prevent data corruption during synchronization, every channel imposes a strict balance requirement on its endpoints: if a channel connects node $u$ and node $v$, their operational states must satisfy the equation $3x_u + 3x_v - 2x_u x_v = 5$.

Your task is to determine a valid state assignment for all $n$ nodes. If there are multiple valid ways to assign the states, you must output the assignment that is lexicographically smallest when written as the sequence $x_1, x_2, \dots, x_n$. If it is impossible to satisfy all channel requirements simultaneously, you must report that no such assignment exists.

## Input
The first line contains two integers $n$ and $m$. The number of nodes $n$ is at least 1 and bounded by a network maximum of $2\cdot 10^5$. The number of channels $m$ is at least 0 and at most $2\cdot 10^5$.
Each of the following $m$ lines contains two integers $u$ and $v$ (valid node IDs ranging from 1 to $n$), indicating that a channel exists between node $u$ and node $v$.

## Output
If there is no valid state assignment, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $x_1, x_2, \dots, x_n$, representing the lexicographically smallest valid assignment.

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