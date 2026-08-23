# Problem A — Channel Allocation

Time limit: 2 s   Memory limit: 256 MB

A network administrator is configuring a wireless network that uses three frequency channels labeled 1, 2, 3. There are $n$ access points to configure. Some pairs of access points have overlapping coverage areas and must not be assigned the same channel to avoid signal interference. Assign every access point to exactly one of the three channels so that no overlapping pair shares a channel, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of access points and the number of overlapping pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of access points with overlapping coverage.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $c_1, c_2, \ldots, c_n$ (each in $\{1,2,3\}$), where $c_i$ is the channel of access point $i$. Among all valid assignments output the lexicographically smallest sequence (compare $c_1$ first, then $c_2$, and so on).

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
