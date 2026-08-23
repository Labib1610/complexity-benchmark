# Maintenance Handoffs

Time limit: 1 s
Memory limit: 256 MB

You are managing the maintenance schedule for a network of $n$ servers, numbered 1 to $n$. There are two available maintenance windows to choose from:
- Window 1: from hour 0 to hour 2.
- Window 2: from hour 1 to hour 3.

You must assign exactly one of these two windows to each server.

The network requires $m$ critical data handoff protocols to be executed. Each protocol operates between a specific pair of servers. For a handoff to be successful, the intersection of the scheduled maintenance windows of the two linked servers must have a duration of exactly 1 hour. If the overlap is greater than 1 hour, the servers interfere with each other's diagnostic tests. If the overlap is less than 1 hour, there is not enough time to complete the handoff.

Determine if it is possible to assign a maintenance window (1 or 2) to each of the $n$ servers so that all $m$ handoff protocols are successful simultaneously. If a valid schedule exists, you must provide the lexicographically smallest sequence of window assignments. A sequence of assignments $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if $s_i < t_i$ at the first index $i$ where the two sequences differ.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), denoting the total number of servers and the number of handoff protocols.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), specifying a protocol between server $u$ and server $v$.

## Output
If no valid assignment of windows (1 and 2) can make all $m$ handoff overlaps exactly 1 hour, output a single line with the word `NO`.
If a valid schedule is possible, print `YES` on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of maintenance windows.

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