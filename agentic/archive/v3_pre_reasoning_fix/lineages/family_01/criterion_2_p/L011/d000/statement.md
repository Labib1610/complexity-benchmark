# Channel Allocation

Time limit: 1 s
Memory limit: 256 MB

A fleet of $n$ autonomous surveying vessels must each be assigned to one of two communication channels, designated as channel 1 and channel 2. During the survey, certain pairs of vessels will operate in close proximity. If two vessels in close proximity broadcast on the same channel, their signals will interfere. You are given $m$ records of such vessel pairs.

Your task is to assign a channel to every vessel such that no two vessels in close proximity share the same channel, or determine that this is impossible. If there are multiple valid ways to assign the channels, you must output the configuration that produces the lexicographically smallest sequence of channel assignments for vessels 1 through $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of vessels and the number of proximity records.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that vessel $u$ and vessel $v$ will operate in close proximity.

## Output
If no assignment can prevent all interference, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \ldots, s_n$ (each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment.

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
