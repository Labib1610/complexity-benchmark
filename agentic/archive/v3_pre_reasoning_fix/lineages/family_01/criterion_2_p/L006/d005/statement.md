# Problem B — Memory Routing

Time limit: 1 s   Memory limit: 256 MB

You are configuring a dual-channel memory controller for a high-performance computing cluster. The system contains $n$ memory banks, numbered 1 to $n$. Every memory bank must be routed to exactly one of the two available data channels: channel 1 or channel 2.

The dense physical layout of the motherboard creates $m$ interference zones. Each zone strictly bounds a specific pair of memory banks. To achieve signal integrity through destructive interference, the routing must be perfectly asymmetric across each zone: for every flagged pair of banks, exactly one bank must be assigned to channel 1, and the other must be assigned to channel 2.

Your task is to determine if there is a valid channel assignment for all $n$ memory banks that stabilizes all interference zones. If multiple valid assignments are possible, the initialization firmware requires the configuration whose sequence of channel assignments is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of memory banks and the number of interference zones, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ indicating that memory bank $u$ and memory bank $v$ share an interference zone.

## Output
If no valid routing exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of channel assignments.

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