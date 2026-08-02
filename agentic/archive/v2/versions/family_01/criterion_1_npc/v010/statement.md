# Channel Partitioning Problem

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ technicians, indexed $1$ through $n$. Each technician must be assigned to work on exactly one of three available communication channels, identified by the numbers $1$, $2$, and $3$.

Due to physical proximity, certain pairs of technicians create mutual signal interference if placed on the same channel. Therefore, any two technicians who interfere with each other must be assigned to different channels.

Your task is to determine whether it is possible to assign every technician to a channel without any interference, and if so, to find the assignment vector $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$) that is lexicographically as small as possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of technicians and the number of interfering pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of technicians who interfere with each other. No pair is listed more than once.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 s_2 \dots s_n$, where $s_i$ denotes the channel assigned to technician $i$. If there are multiple valid assignments, output the one that is lexicographically smallest.

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
