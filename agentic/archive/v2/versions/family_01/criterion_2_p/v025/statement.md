# Problem B — Frequency Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

A telecommunications network consists of $n$ relay stations, identified by integer labels from $1$ to $n$. Each station must be configured to operate on one of two available frequency channels, labeled $1$ and $2$.

There are $m$ interference constraints between pairs of stations. Two stations in an interference constraint cannot use the same frequency channel. Additionally, to ensure system stability, within every group of stations that are connected to one another through direct or indirect interference links, the station with the smallest identifier must be assigned channel $1$.

Determine whether a valid channel assignment exists for all stations under these conditions. If no valid assignment exists, report impossibility. If multiple valid assignments exist, output the one that produces the lexicographically smallest sequence $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), specifying an interference constraint between station $u$ and station $v$.

## Output
If no valid channel assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

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
