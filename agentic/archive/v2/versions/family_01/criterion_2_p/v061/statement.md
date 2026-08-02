# Network Subnet Partitioning

Time limit: 1 s   Memory limit: 256 MB

An infrastructure manager controls $n$ network devices numbered $1$ to $n$. Certain pairs of devices are linked by high-traffic hardware channels. Due to bandwidth constraints, two linked devices cannot be assigned to the same network segment. Exactly two network segments are available, labeled $1$ and $2$.

Each device $i$ ($1 \le i \le n$) must be assigned to segment $s_i \in \{1, 2\}$ such that for every hardware link connecting device $u$ and device $v$, $s_u \neq s_v$.

Determine whether a valid segment assignment exists for all $n$ devices. If multiple valid assignments exist, select the assignment sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest. A sequence $A = (a_1, \dots, a_n)$ is lexicographically smaller than $B = (b_1, \dots, b_n)$ if at the first index $i$ where $a_i \neq b_i$, $a_i < b_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of devices and the number of hardware links.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a hardware link between device $u$ and device $v$.

## Output
If no valid segment assignment exists, print `NO` on a single line.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ representing the lexicographically smallest valid segment assignment.

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
