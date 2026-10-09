# Problem B — Drone Elevation Protocols

Time limit: 1 s   Memory limit: 256 MB

## Description

A logistics company operates $n$ autonomous drones. For the upcoming shift, each drone must be assigned to exactly one of two elevations: the upper corridor (denoted by 1) or the lower corridor (denoted by 0).

To ensure safe operation, the routing system provides $m$ safety protocols. Each protocol lists exactly two elevation requirements. A protocol is strictly upheld if at least one of its two elevation requirements is adopted in the final assignment. 

Determine if there is a global flight plan for all $n$ drones that upholds all $m$ safety protocols at the same time. If such a plan is possible, output one valid assignment. Otherwise, report that no such plan exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$). The absolute value of each integer represents a drone ID (from $1$ to $n$). A positive value $x$ represents a requirement that drone $|x|$ uses the upper corridor. A negative value $x$ represents a requirement that drone $|x|$ uses the lower corridor. For each protocol, at least one of the two given requirements must be met by the flight plan.

## Output
If there is no valid flight plan, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$), indicating the elevation assigned to each drone from $1$ to $n$ in any valid flight plan.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid flight plans may exist; any one is accepted. The same elevation requirement may appear in multiple protocols.
