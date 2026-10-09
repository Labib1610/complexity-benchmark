# Problem B — Alternating Cycles

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant operates $n$ robotic assembly arms. The arms must be connected to one of two distinct power grids, labeled 1 and 2. 

There are $m$ pairs of arms that have overlapping physical motion ranges. To prevent collisions, any pair of arms with overlapping ranges must be connected to different power grids so they operate on alternating cycles. 

Assign each assembly arm to a power grid such that no two arms with overlapping ranges share the same grid, or report that this is impossible. 

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of assembly arms and the number of overlapping pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of arms with overlapping motion ranges.

## Output
If no valid grid assignment exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$), representing the grid assigned to each arm. If multiple valid assignments exist, output the one that is lexicographically smallest.

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
