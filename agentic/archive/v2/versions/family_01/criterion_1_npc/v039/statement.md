# Problem A — Frequency Channel Allocation

Time limit: 2 s   Memory limit: 256 MB

A telecommunications firm must assign one of three available frequency channels, labeled 1, 2, and 3, to each of $n$ radio transmitters. Certain pairs of transmitters are positioned close enough that operating on the same frequency channel causes mutual signal interference, so they must be assigned distinct channels.

Determine whether every transmitter can be assigned a channel from {1, 2, 3} such that no interfering pair shares a channel. If a valid configuration exists, find the lexicographically smallest channel sequence $s_1\ s_2\ \dots\ s_n$ (where $s_i$ is the channel allocated to transmitter $i$). Otherwise, report that no valid configuration is possible.

## Input
The first line contains two integers $n$ and $m$ — the number of transmitters and the number of interfering transmitter pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of interfering transmitters.

## Output
If no valid channel assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$ (each in $\{1, 2, 3\}$), where $s_i$ denotes the assigned channel of transmitter $i$. If there are multiple valid assignments, output the lexicographically smallest sequence (comparing $s_1$ first, then $s_2$, and so on).

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
