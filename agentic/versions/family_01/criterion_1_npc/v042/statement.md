# Problem A — Network Licensing

Time limit: 2 s   Memory limit: 256 MB

A regional communication network consists of $n$ broadcast towers. The regulatory authority has licensed exactly three frequency channels for use, designated as channel 1, channel 2, and channel 3. 

Due to overlapping coverage areas, certain pairs of towers will experience critical signal interference if they are configured to operate on the exact same channel. You must assign every tower to exactly one of the three available channels such that no two interfering towers share a channel. If no such configuration is possible, you must report this.

## Input
The first line contains two integers $n$ and $m$ — the number of broadcast towers and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
The towers are numbered from 1 to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of towers that interfere.

## Output
If there is no valid channel configuration, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (each in $\{1, 2, 3\}$), where $c_i$ is the channel assigned to tower $i$. Among all valid configurations, output the lexicographically smallest sequence (compare $c_1$ first, then $c_2$, and so on).

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
