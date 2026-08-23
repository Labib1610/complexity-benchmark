# Maintenance Handoffs

Time limit: 1 s
Memory limit: 256 MB

You are managing the maintenance schedule for a network of $n$ servers, numbered 1 to $n$. Every server requires a maintenance operation that lasts exactly 2 hours. You must assign each server to exactly one of two scheduling windows:
- Window 1: maintenance starts at hour 0.
- Window 2: maintenance starts at hour 1.

The network requires $m$ critical data handoff protocols to be executed. Each protocol operates between a specific pair of servers. For a handoff to be successful, the system must perform a sync check. The sync check is active during any time when exactly one of the two linked servers is undergoing maintenance (while the other is not). The total accumulated time during which the sync check is active for that pair must be exactly 2 hours. If this accumulated time is not exactly 2 hours, the protocol fails.

Determine if it is possible to assign a maintenance window (1 or 2) to each of the $n$ servers so that all $m$ handoff protocols are successful simultaneously. If a valid schedule exists, you must provide the lexicographically smallest sequence of window assignments. A sequence of assignments $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if $s_i < t_i$ at the first index $i$ where the two sequences differ.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), denoting the total number of servers and the number of handoff protocols.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), specifying a protocol between server $u$ and server $v$.

## Output
If no valid assignment of windows (1 and 2) can make all $m$ protocol sync checks last exactly 2 hours, output a single line with the word `NO`.
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