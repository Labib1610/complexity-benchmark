# Problem A — Transmission Channels

Time limit: 2 s   Memory limit: 256 MB

A set of $n$ sensors is deployed to monitor a facility. Each sensor must be assigned one of three transmission channels: 1, 2, or 3. Certain pairs of sensors are positioned too close to each other; if they broadcast on the same channel, their signals will interfere.

In most standard deployments, the physical layout of the facility is highly regular. Engineers typically configure the network by simply alternating adjacent sensors between channel 1 and channel 2. Channel 3 is provided merely as a fallback to resolve situations where a sequence of interferences wraps around unevenly and prevents perfect alternation. Because the network design is intended to be well-behaved, the expectation is that resolving conflicts is straightforward.

Given a list of $n$ sensors and $m$ interfering pairs, you must assign every sensor to exactly one of the three channels such that no interfering pair shares a channel. If a collision-free assignment is possible, you must output the lexicographically smallest sequence of channels.

## Input
The first line contains two integers $n$ and $m$ — the number of sensors and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that sensor $u$ and sensor $v$ will interfere if they share a channel.

## Output
If no valid channel assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (each in $\{1, 2, 3\}$), where $c_i$ is the channel assigned to sensor $i$. Among all valid assignments, output the lexicographically smallest sequence (compare $c_1$ first, then $c_2$, and so on).

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
