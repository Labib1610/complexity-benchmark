# Signal Frequency Allocation for Laboratory Modules

Time limit: 2 s   Memory limit: 256 MB

A high-energy physics facility is setting up $n$ independent diagnostic units, numbered $1$ through $n$. Each unit must operate continuously on one of three available telemetry channels, indexed $1$, $2$, and $3$.

Due to physical proximity and mutual electromagnetic distortion, specific pairs of diagnostic units cannot be assigned to the same telemetry channel. A complete list of all conflicting pairs is provided.

Determine whether a conflict-free channel allocation exists for all $n$ units. If valid channel assignments exist, select the one that yields the lexicographically smallest sequence of channel numbers $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2, 3\}$ denotes the channel assigned to unit $i$. If no valid allocation can satisfy all interference constraints, report that it is impossible.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of diagnostic units and the number of interference constraints, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that diagnostic unit $u$ and diagnostic unit $v$ cannot be assigned the same telemetry channel.

## Output
If no valid channel allocation exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$, representing the channel assigned to each unit from $1$ to $n$. If there are multiple valid configurations, output the one that is lexicographically smallest.

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
