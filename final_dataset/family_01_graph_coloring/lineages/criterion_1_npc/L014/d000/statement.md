# Problem A — Technician Roster

Time limit: 2 s
Memory limit: 256 MB

A continuous-operation facility divides its daily schedule into three distinct 8-hour blocks, designated 1, 2, and 3. The facility employs $n$ technicians, numbered 1 through $n$, each of whom must be allocated to exactly one of these blocks. To prevent workplace friction, HR mandates that certain pairs of technicians cannot be present during the same block. You are given the total number of technicians and the specific pairs that have documented conflicts. Produce a complete schedule assigning each technician to block 1, 2, or 3 without violating any HR mandates, or indicate that no such arrangement exists.

## Input
The first line contains two integers $n$ and $m$ — the number of technicians and the number of documented HR conflicts ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of technicians who cannot be assigned to the same block.

## Output
If no valid schedule can be created, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the block assigned to technician $i$. Any valid schedule will be accepted.

## Example 1
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

## Example 2
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
