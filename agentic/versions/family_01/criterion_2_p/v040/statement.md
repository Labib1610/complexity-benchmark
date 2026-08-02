# Facility Pipeline: Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

The facility automation engine processes daily throughput across three distinct stages: pre-sorting, channel assignment, and queue dispatching. In the pre-sorting stage, $n$ distinct operational units (numbered $1$ through $n$) are identified alongside $m$ mutual-interference rules.

You are implementing the second stage: channel assignment. Every unit must be assigned to one of two operational channels, denoted by the values $1$ and $2$. If two units are specified in an interference rule, they cannot be assigned to the same channel. Once this assignment is completed, it will be forwarded to the queue dispatching stage.

If no valid assignment exists that satisfies all interference rules, report that the assignment is impossible. Otherwise, find the valid assignment that produces the lexicographically smallest sequence $(s_1, s_2, \dots, s_n)$, where $s_i \in \{1, 2\}$ is the channel assigned to unit $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interference rule indicating that unit $u$ and unit $v$ cannot share the same channel.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES`, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment.

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
