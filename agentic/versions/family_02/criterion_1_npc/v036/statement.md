# Problem A — Network Stabilization

Time limit: 2 s   Memory limit: 256 MB

## Description

A city water network contains $n$ treatment stations. Each station must operate in exactly one of two modes: alkaline (represented as `1`) or acidic (represented as `0`). 

The network is monitored across $m$ sensor zones. To prevent corrosion, each zone mandates a safety property. A zone's safety property lists exactly three acceptable station behaviors. The zone remains stable provided the current network configuration matches one, two, or all three of the behaviors listed for that zone.

A behavior is provided as a non-zero integer $x$. If $x$ is positive, it requires station $x$ to be in alkaline mode. If $x$ is negative, it requires station $|x|$ to be in acidic mode. The same station might be referenced multiple times within a single zone's property.

Determine if there is a network-wide configuration of all $n$ stations that stabilizes all $m$ sensor zones simultaneously. 

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero integers $l_1, l_2, l_3$, with $|l_i| \le n$. These represent the three acceptable behaviors for a zone.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each `0` or `1`), where $s_i$ is the mode of station $i$. Any valid configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```
