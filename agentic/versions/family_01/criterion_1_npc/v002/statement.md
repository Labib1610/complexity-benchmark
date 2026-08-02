# Radio Channel Allocation

Time limit: 2 s   Memory limit: 256 MB

A telecom network consists of $n$ radio transmitters numbered $1$ to $n$. Exactly three broadcast channels, labeled $1$, $2$, and $3$, are available for assignment. Certain pairs of transmitters cause signal interference if operated on the same channel; each such pair must be assigned to different channels.

Assign every transmitter to exactly one of the three channels so that no interfering pair shares a channel, or report that it is impossible. If multiple valid channel assignments exist, find the one that produces the lexicographically smallest sequence of assigned channels $c_1, c_2, \dots, c_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of transmitters and the number of interfering pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of interfering transmitters.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $c_1, c_2, \dots, c_n$ (each in $\{1, 2, 3\}$), where $c_i$ is the channel assigned to transmitter $i$. Output the lexicographically smallest valid assignment (comparing $c_1$ first, then $c_2$, and so on).

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
