# Sensor Frequency Allocation

Time limit: 2 s   Memory limit: 256 MB

An atmospheric observatory operates $n$ observational units labeled $1$ through $n$. Each unit must be configured to transmit on one of three available channel frequencies, identified by integer labels $1$, $2$, or $3$.

Due to physical proximity, certain pairs of units will cause mutual electromagnetic interference if they operate on the same channel frequency. Consequently, no two interfering units may share the same channel label.

To ensure operational compliance, a valid configuration must satisfy all of the following requirements:
1. Each unit $i$ ($1 \le i \le n$) is assigned a single channel label $s_i \in \{1, 2, 3\}$.
2. For every pair of interfering units $(u, v)$, $s_u \neq s_v$.
3. The total sum of assigned channel labels $\sum_{i=1}^n s_i$ does not exceed $3n$.
4. The numerical difference between the highest channel label assigned and the lowest channel label assigned across all units does not exceed $2$.

Determine whether a valid channel assignment exists. If one exists, find the configuration that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of units and the number of interfering pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) indicating that unit $u$ and unit $v$ interfere with each other.

## Output
If no valid channel assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ is the channel assigned to unit $i$. If multiple valid assignments exist, output the lexicographically smallest sequence (comparing $s_1$ first, then $s_2$, and so on).

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
