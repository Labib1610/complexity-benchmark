# Signal Channel Partitioning Stage

Time limit: 1 s   Memory limit: 256 MB

As part of an automated network deployment pipeline, a system must configure $n$ transmission units (labeled $1$ through $n$). The pipeline consists of three sequential phases:

1. **Topology Analysis:** Identifies $m$ operational constraints where pairs of units interfere with each other if active on the same frequency band.
2. **Channel Assignment (Current Stage):** Assign each of the $n$ units to operate on either Channel 1 or Channel 2. To avoid interference, two units with an operational constraint must be assigned to different channels. If multiple valid channel assignments exist, the system requires the assignment $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest (comparing values at unit 1, then unit 2, and so on).
3. **Data Broadcast:** Commences only if a valid channel configuration is established in Stage 2.

Your task is to implement the Channel Assignment stage. Given the $n$ units and $m$ interference constraints, determine whether a valid channel assignment exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of units and the number of interference constraints, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating an interference constraint between unit $u$ and unit $v$.

## Output
If it is impossible to assign channels without violating any constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line, and print a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid channel assignment vector.

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
