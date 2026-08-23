# Problem B — Frequency Allocation

Time limit: 1 s   Memory limit: 256 MB

A wildlife tracking system consists of $n$ field sensors, consecutively labeled from 1 to $n$. The system uses exactly two transmission channels, Channel 1 and Channel 2, to relay data. Because of signal overlap, certain pairs of sensors are prone to mutual interference. If two such sensors are configured to transmit on the same channel, their signals become corrupted.

You are given a list of $m$ interfering sensor pairs. You must decide whether it is possible to configure each sensor to use either Channel 1 or Channel 2 so that no two interfering sensors share a channel.
When multiple valid configurations exist, the firmware requires the configuration sequence to be as small as possible in lexicographical order.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 2·10⁵, 0 ≤ $m$ ≤ 2·10⁵), which denote the number of sensors and the number of interfering pairs.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$), meaning that sensor $u$ and sensor $v$ must be assigned to different channels.

## Output
If there is no way to allocate the channels without causing interference, print a single line containing `NO`.
If a safe allocation is possible, print `YES` on the first line. On the second line, print $n$ integers $c_1, \dots, c_n$ (where each $c_i \in \{1, 2\}$), representing the channel assignment for sensors 1 through $n$. This sequence must be the lexicographically smallest valid configuration.

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
