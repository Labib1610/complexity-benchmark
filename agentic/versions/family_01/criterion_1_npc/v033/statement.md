# Task Channel Allocation

**Time limit:** 2 s  
**Memory limit:** 256 MB

## Description
A computing cluster manages $n$ processes numbered $1$ through $n$. Each process must be assigned to one of three available execution channels, labeled $1$, $2$, and $3$.

Certain pairs of processes contend for exclusive resources and cannot be assigned to the same execution channel. You are given a list of all contending process pairs.

Determine whether it is possible to assign an execution channel to every process such that no pair of contending processes shares a channel. If a valid assignment exists, find the one that yields the lexicographically smallest sequence of channel assignments $(s_1, s_2, \dots, s_n)$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of processes and the number of pairwise contention constraints, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$) representing a contending pair of processes.

## Output
If no valid channel assignment exists, print `NO` on a single line.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ denotes the execution channel assigned to process $i$. Among all valid assignments, output the one that is lexicographically smallest.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
