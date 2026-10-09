# Problem B — Sensor Frequency Allocation

Time limit: 1 s   Memory limit: 256 MB

A smart factory has $n$ wireless sensors. Each sensor must be configured to broadcast on one of two available frequency bands, labeled 1 and 2. 

Due to hardware proximity, there are $m$ pairs of sensors that cause signal interference if configured incorrectly. To prevent data collision, for each such interfering pair of sensors $u$ and $v$, they must not broadcast on the same frequency. Instead, one sensor in the pair must be assigned to band 1, and the other must be assigned to band 2.

Determine if there is a valid configuration for all $n$ sensors. If there are multiple valid configurations, you must output the one where the sequence of band assignments $s_1 \dots s_n$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of sensors that interfere with each other.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid configuration.

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