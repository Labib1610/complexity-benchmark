# Problem A — Maintenance Scheduling

Time limit: 2 s
Memory limit: 256 MB

A transit agency is coordinating maintenance for $n$ vehicles. The maintenance work must be performed during one of the daily operational blocks: morning, afternoon, or night. For data entry, these blocks are designated by the codes 1, 2, and 3, respectively.

Certain pairs of vehicles require the same specialized diagnostic tool. Because the agency only owns one tool of each specialized type, these specific pairs cannot undergo maintenance during the same time block. The agency needs to assign exactly one operational block to every vehicle such that no two vehicles requiring the same tool are scheduled at the same time.

If multiple valid schedules exist, the system requires the one that prioritizes the numerically smallest block code for vehicle 1; in case of ties, the smallest block code for vehicle 2, and so on.

### Input
The first line provides two integers $n$ and $m$ — the total number of vehicles and the number of tool-sharing pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, representing a pair of vehicles that require the same specialized tool. Vehicles are numbered from 1 to $n$.

### Output
If no valid schedule can be formed, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 1, 2, or 3), where $s_i$ is the block assigned to vehicle $i$. Among all valid schedules, output the sequence that is smallest when compared element by element from left to right (comparing $s_1$ first, then $s_2$, and so on).

### Example 1
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

### Example 2
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
