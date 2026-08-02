# Signal Channel Allocation

Time limit: 1 s   Memory limit: 256 MB

A wireless network consists of $n$ transceivers, numbered $1$ through $n$, and $m$ interference links. Each transceiver must be assigned to operate on one of two frequency channels, labeled 1 and 2. To prevent crosstalk, any pair of transceivers connected by an interference link must be assigned different channels.

Determine whether it is possible to assign a channel to every transceiver satisfying all non-interference conditions. If a valid configuration exists, report the lexicographically smallest sequence of channel assignments $s_1, s_2, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of transceivers and interference links, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating an interference link between transceiver $u$ and transceiver $v$.

## Output
If no valid channel assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment.

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
