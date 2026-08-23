# Dual-Channel Frequency Allocation for Distributed Units

Time limit: 1 s   Memory limit: 256 MB

A network consists of $n$ processing nodes, numbered $1$ through $n$. Every node must be configured to operate on one of two available channels, labeled $1$ or $2$.

There are $m$ operational restrictions. Each restriction links two distinct nodes, requiring that they must not be assigned to the same channel.

Your task is to determine whether a valid channel assignment exists for all nodes. If one or more valid configurations exist, choose the configuration $s_1, s_2, \dots, s_n$ that is lexicographically smallest. Otherwise, indicate that no valid assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of nodes and the number of restrictions, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that node $u$ and node $v$ cannot share the same channel setting.

## Output
If no valid channel assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line, and print $n$ space-separated integers $s_1, s_2, \dots, s_n$ on the second line (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
