# Problem B — System Equilibrium

Time limit: 1 s   Memory limit: 256 MB

A fluid control facility contains $n$ automated valves, labeled 1 through $n$. The system's protocol dictates that every valve must be assigned an operational state of either 1 or 2.

The network is supervised by $m$ pressure monitors. Each monitor is linked to a specific pair of valves. For the network to achieve equilibrium, every monitor must verify that the operational state of one of its two linked valves is exactly twice the operational state of the other.

You must determine whether a configuration exists that satisfies all monitors. If there are several valid configurations for the $n$ valves, you must output the sequence of states $s_1 \dots s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ — the labels of the two valves linked to a single monitor.

## Output
If no such configuration is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$) representing the lexicographically smallest valid configuration.

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