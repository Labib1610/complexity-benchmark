# Orbital Reflection Synchrony

Time limit: 1 s   Memory limit: 256 MB

A satellite network consists of $n$ orbital modules, numbered $1$ through $n$. You must assign each module an operating mode, represented by the integer $1$ or $2$.

The network's synchronization is governed by $m$ telemetry channels. Each channel connects a specific pair of modules. For a telemetry channel connecting module $u$ and module $v$ to function correctly, their assigned modes $p_u$ and $p_v$ must satisfy the following stability equation:

$2p_u^2 - 5p_u p_v + 2p_v^2 = 0$

Your task is to assign an operating mode ($1$ or $2$) to each of the $n$ modules so that every telemetry channel functions correctly. If multiple valid assignments are possible, you must output the lexicographically smallest valid sequence of modes (comparing sequences from index $1$ to $n$). If no such assignment is possible, you must output a specific failure message.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), representing the indices of a pair of modules connected by a telemetry channel.

## Output
If it is impossible to configure the modules to satisfy all channels, output a single line containing `NO`.
If it is possible, output `YES` on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1,2\}$) giving the lexicographically smallest valid sequence of modes.

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