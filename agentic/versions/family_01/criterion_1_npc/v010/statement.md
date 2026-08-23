# Problem A — Operational Blocks

Time limit: 2 s   Memory limit: 256 MB

A factory employs $n$ workers. The daily schedule consists of multiple operational blocks. Every worker must be assigned to exactly one operational block, which is designated by an integer from 1 to 3.

Certain workers have documented grievances with one another. To prevent workplace disruptions, management requires that if two workers have a documented grievance, they must not be assigned to the same operational block.

Determine if there is a valid schedule for all $n$ workers. If a valid schedule exists, find the one that produces the lexicographically smallest sequence of block assignments (comparing worker 1's assignment first, then worker 2's, and so forth).

## Input
The first line contains two integers $n$ and $m$ — the number of workers and the total number of documented grievances ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of workers who have a grievance.

## Output
If no valid schedule can be formed, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each an integer from 1 to 3), where $s_i$ is the operational block assigned to worker $i$. Among all valid schedules, output the lexicographically smallest sequence.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
1 4
2 4
```
**Output:**
```
YES
1 2 3 3
```

## Example 2
**Input:**
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
**Output:**
```
NO
```
