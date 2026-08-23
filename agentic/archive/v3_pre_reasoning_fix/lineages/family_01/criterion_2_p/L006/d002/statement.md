# Problem B — Signal Separation

Time limit: 1 s   Memory limit: 256 MB

A wildlife tracking project uses $n$ automated monitoring stations, numbered 1 to $n$. Each station must be configured to transmit its data on one of two available radio frequencies, designated as Band 1 and Band 2.

Because of the terrain and the high transmission power used, certain pairs of stations are at risk of causing signal interference with each other. The engineers have identified $m$ such pairs. To prevent data loss, any two stations that are at risk of interfering with each other must be assigned to different transmission bands.

Your task is to determine if it is possible to assign a frequency band to each of the $n$ stations such that no two interfering stations use the same band. If multiple valid configurations exist, the central controller requires the configuration whose sequence of band assignments is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of monitoring stations and the number of interfering pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ indicating that station $u$ and station $v$ are at risk of interfering with each other.

## Output
If no valid band assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of band assignments.

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