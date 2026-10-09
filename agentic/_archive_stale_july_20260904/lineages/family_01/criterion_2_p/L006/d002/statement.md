# Calibration Valves

Time limit: 1 s   Memory limit: 256 MB

A fluid transport network contains $n$ calibration valves, numbered $1$ to $n$. Each valve must be configured to an operating pressure level of either $1$ or $2$.

The network is monitored by $m$ differential sensors. Each sensor bridges a specific pair of valves. When a sensor bridges two valves configured to pressure levels $x$ and $y$, it yields a valid reading if and only if the combination is authorized by the hardware calibration lookup table. The table defines the validity for each possible pair of assigned pressure levels $(x, y)$ as follows:
- $(1, 1)$ : Invalid
- $(1, 2)$ : Valid
- $(2, 1)$ : Valid
- $(2, 2)$ : Invalid

You must determine a pressure level for each of the $n$ valves such that every sensor in the network yields a valid reading. If there are multiple valid configurations, you must output the one that is lexicographically smallest (assigning pressure level $1$ to lower-numbered valves whenever possible). If no valid configuration exists, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of a pair of valves bridged by a sensor.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $p_1 \dots p_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid configuration.

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