# Spectrum Allocation for Transmitter Networks

Time limit: 1 s   Memory limit: 256 MB

A telecommunications authority needs to assign operating channels to $n$ wireless transmitters, numbered $1$ through $n$. Due to hardware restrictions, only two channel frequencies are available, designated as Channel $1$ and Channel $2$.

There are $m$ interference conditions. Each condition specifies a pair of transmitters that are geographically adjacent; if both transmitters in a pair operate on the same channel, severe crosstalk occurs. Therefore, any two transmitters linked by an interference condition must be assigned different channels.

You must determine whether it is possible to assign a channel $s_i \in \{1, 2\}$ to every transmitter $i \in \{1, \dots, n\}$ such that no interference condition is violated. If at least one valid assignment exists, find the lexicographically smallest channel sequence $(s_1, s_2, \dots, s_n)$.

A sequence $(s_1, \dots, s_n)$ is lexicographically smaller than $(t_1, \dots, t_n)$ if at the first position $k$ where $s_k \neq t_k$, we have $s_k < t_k$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of transmitters and the number of interference conditions.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) representing an interference condition between transmitter $u$ and transmitter $v$.

## Output
If no valid channel assignment exists without interference, print a single line containing `NO`.

Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
