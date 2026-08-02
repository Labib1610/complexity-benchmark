# Dual Frequency Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

A communications network consists of $n$ transmitter nodes, numbered from $1$ to $n$. There are $m$ pairs of nodes that interfere with each other if they operate on the same channel.

There are exactly two available channels, labeled $1$ and $2$. You must assign every node to one of these two channels such that no two interfering nodes share the same channel.

If multiple valid channel assignments exist, you must select the assignment that produces the lexicographically smallest sequence of channels $(s_1, s_2, \dots, s_n)$. That is, at the first index $i$ where two valid sequences differ, the chosen sequence must have $s_i = 1$ and the other $s_i = 2$.

If it is impossible to assign channels without interference, report that no valid assignment exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5, 0 \le m \le 2\cdot 10^5$), representing the number of nodes and the number of interfering pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), specifying an interference pair between node $u$ and node $v$.

## Output
If no valid channel assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment.

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
