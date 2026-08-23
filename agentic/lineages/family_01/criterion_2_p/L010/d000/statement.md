# Frequency Interference

Time limit: 1 s   Memory limit: 256 MB

A city is deploying a network of $n$ wireless sensors. To operate correctly, each sensor must be configured to transmit on either channel 1 or channel 2. However, certain pairs of sensors are installed physically close to each other. If a close pair transmits on the exact same channel, their signals will interfere and data will be lost.

You are given a list of $m$ pairs of sensors that are at risk of interfering. Your task is to determine whether it is possible to configure every sensor with a channel such that no two interfering sensors share the same channel. 

If a valid configuration exists, you must provide it. Because there may be multiple ways to configure the network without interference, the engineering team requires the lexicographically smallest sequence of channel assignments. A sequence of channel assignments $s_1, \dots, s_n$ is lexicographically smaller than another valid sequence $t_1, \dots, t_n$ if, at the first sensor index $i$ where they differ, $s_i < t_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of sensors and the number of interfering pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of sensors that will interfere if assigned the same channel.

## Output
If there is no way to assign channels 1 and 2 to all sensors without causing interference, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid channel assignment.

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
