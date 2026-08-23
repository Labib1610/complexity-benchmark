# Problem A — Telemetry Configuration

Time limit: 2 s   Memory limit: 256 MB

A facility's monitoring system consists of $n$ telemetry stations. Each station must be configured to use a specific radio band. The hardware allows each station to be set to band 1, band 2, or band 3.

Due to physical proximity, certain pairs of stations have overlapping broadcast ranges. If two stations with overlapping ranges are configured to the identical band, they will jam one another. 

Typically, engineers attempt to configure the system using only bands 1 and 2 by flipping back and forth between them across overlapping stations. Band 3 is provided solely as a patch for situations where a chain of overlapping stations wraps around asymmetrically, making it impossible to use just the first two bands. Since the facility's layout is intended to be well-structured, the assumption is that finding a stable configuration should not be complicated.

Given $n$ telemetry stations and $m$ pairs with overlapping ranges, you must assign every station to exactly one of the supported bands such that no jamming occurs. If a stable configuration is possible, you must output the lexicographically smallest sequence of band assignments.

## Input
The first line contains two integers $n$ and $m$ — the number of stations and the number of overlapping pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that station $u$ and station $v$ have overlapping ranges and cannot share a band.

## Output
If no stable configuration is possible, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $b_1, b_2, \dots, b_n$ (each in $\{1, 2, 3\}$), where $b_i$ is the band assigned to station $i$. Among all stable configurations, output the lexicographically smallest sequence (compare $b_1$ first, then $b_2$, and so on).

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
