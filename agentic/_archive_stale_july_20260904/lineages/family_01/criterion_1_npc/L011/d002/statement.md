# Problem A — Operational Modes

Time limit: 2 s   Memory limit: 256 MB

You are configuring a wireless network consisting of $n$ access points. There are three available operational modes, denoted by the integers 1, 2, and 3. Every access point must be assigned exactly one of these modes.

Due to physical proximity, certain pairs of access points are in interfering range. If two access points that are in interfering range are assigned the identical mode, they will disrupt each other's signals. A valid network configuration is one where no two such access points share the same mode.

Your task is to find a valid configuration for the entire network. If there are multiple valid configurations, you must choose the one that is lexicographically smallest. (To compare two configurations, compare the mode assigned to access point 1, then access point 2, and so on up to $n$. The first position where they differ determines which configuration is smaller.) If no valid configuration exists, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). Here, $n$ is the total number of access points and $m$ is the number of interfering pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that access point $u$ and access point $v$ are in interfering range and thus cannot operate on the same mode.

## Output
If it is impossible to configure the network without disruption, output a single line containing `NO`.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \ldots, c_n$, where each $c_i \in \{1, 2, 3\}$ represents the mode assigned to access point $i$. Remember to output the lexicographically smallest sequence if multiple exist.

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